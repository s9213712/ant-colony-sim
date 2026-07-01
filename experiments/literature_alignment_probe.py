from playwright.sync_api import sync_playwright


URL = "http://127.0.0.1:8876/"


def main():
    failures = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 860})
        errors = []
        page.on("pageerror", lambda exc: errors.append(str(exc)))
        page.goto(URL)
        page.wait_for_function("() => window.antSim && window.antSim.world")

        results = page.evaluate(
            """
            () => {
              const pheroSum = (name) =>
                Math.round(antSim.world.pheromones[name].data.reduce((sum, value) => sum + value, 0));
              const stateCount = (names) => antSim.world.ants.filter((ant) => names.includes(ant.state)).length;
              const taskCount = (names) => antSim.world.ants.filter((ant) => names.includes(ant.task)).length;
              const out = {};

              antSim.setSeed(20260701);
              antSim.setParam('species', 'lasius');
              antSim.setupMatureColony();
              antSim.world.food = [];
              antSim.world.water = [];
              antSim.world.foodStore = 120;
              antSim.world.waterStore = 220;
              antSim.clearPheromones();
              antSim.addFood(250, 180, 1400);
              antSim.addWater(320, 180, 1400);
              antSim.runDays(5, 9);
              out.trailFormation = {
                foodTrips: antSim.world.stats.foodTrips,
                waterTrips: antSim.world.stats.waterTrips,
                foodPheromone: pheroSum('food'),
                waterPheromone: pheroSum('water'),
                nestPheromone: pheroSum('nest'),
                trailStates: stateCount(['following food trail', 'following water trail', 'carrying food', 'carrying water']),
                foragingTasks: taskCount(['food', 'water', 'explore'])
              };

              const beforeRainFood = pheroSum('food');
              const beforeRainNest = pheroSum('nest');
              antSim.triggerRain();
              antSim.runDays(1, 9);
              out.pheromoneWashout = {
                beforeFood: beforeRainFood,
                afterFood: pheroSum('food'),
                beforeNest: beforeRainNest,
                afterNest: pheroSum('nest')
              };

              const evaporationRun = (evaporationRate) => {
                antSim.setSeed(777);
                antSim.setupFoundingColony();
                antSim.world.ants = [];
                antSim.world.food = [];
                antSim.world.water = [];
                antSim.setParam('evaporationRate', evaporationRate);
                antSim.setParam('diffusionRate', 100);
                antSim.clearPheromones();
                antSim.world.pheromones.food.add(600, 380, 220);
                antSim.runDays(1, 9);
                return pheroSum('food');
              };
              out.evaporationSensitivity = {
                highEvaporationFoodPheromone: evaporationRun(180),
                lowEvaporationFoodPheromone: evaporationRun(40)
              };

              antSim.setSeed(991);
              antSim.setParam('species', 'eciton');
              antSim.setupMatureColony();
              const startAnts = antSim.world.ants.length;
              antSim.createAntMill ? antSim.createAntMill() : createAntMill();
              antSim.runDays(5, 9);
              out.antMill = {
                startAnts,
                ants: antSim.world.ants.length,
                corpses: antSim.world.corpses.length,
                mills: antSim.world.mills.length,
                deathPheromone: pheroSum('death')
              };

              return out;
            }
            """
        )

        def check(name, ok, detail):
            status = "PASS" if ok else "FAIL"
            print(f"{status}: {name}: {detail}")
            if not ok:
                failures.append(name)

        trail = results["trailFormation"]
        check(
            "food/nest pheromone foraging produces trail formation and resource trips",
            trail["foodTrips"] >= 6
            and trail["foodPheromone"] > 1000
            and trail["nestPheromone"] > 1000
            and (trail["trailStates"] >= 25 or trail["foodTrips"] >= 20),
            trail,
        )

        washout = results["pheromoneWashout"]
        check(
            "rain and evaporation reduce established pheromone fields",
            washout["afterFood"] < washout["beforeFood"] * 0.35
            and washout["afterNest"] < washout["beforeNest"] * 0.55,
            washout,
        )

        evap = results["evaporationSensitivity"]
        check(
            "evaporation parameter changes pheromone persistence",
            evap["lowEvaporationFoodPheromone"] > evap["highEvaporationFoodPheromone"] * 1.5,
            evap,
        )

        mill = results["antMill"]
        check(
            "army-ant preset can enter a death-spiral-like mill with mortality",
            mill["mills"] == 1
            and mill["ants"] < mill["startAnts"] * 0.65
            and mill["corpses"] > 100
            and mill["deathPheromone"] > 1000,
            mill,
        )

        if errors:
            failures.extend(errors)
            print(f"PAGE_ERRORS: {errors}")
        print(f"summary: {len(failures)} failed literature-alignment checks")
        browser.close()

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
