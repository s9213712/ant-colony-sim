from playwright.sync_api import sync_playwright


URL = "http://127.0.0.1:8876/"


SCENARIOS = {
    "founding_stable_40d": """
        setupFoundingColony();
        ui.temperature.value = 26; ui.humidity.value = 58;
        runDays(40);
    """,
    "founding_supplied_80d": """
        setupFoundingColony();
        ui.temperature.value = 26; ui.humidity.value = 58;
        addFood(700, 390, 350); addWater(760, 390, 350);
        runDays(80);
    """,
    "mature_no_resources_20d": """
        setupMatureColony();
        world.food = []; world.water = [];
        runDays(20);
    """,
    "mature_supplied_stable_40d": """
        setupMatureColony();
        world.food = []; world.water = [];
        ui.temperature.value = 26; ui.humidity.value = 58;
        addFood(250, 180, 1600); addWater(320, 180, 1600);
        runDays(40);
    """,
    "mature_supplied_hot_dry_40d": """
        setupMatureColony();
        world.food = []; world.water = [];
        ui.temperature.value = 40; ui.humidity.value = 20;
        addFood(250, 180, 1600); addWater(320, 180, 1600);
        runDays(40);
    """,
    "mature_supplied_cool_humid_40d": """
        setupMatureColony();
        world.food = []; world.water = [];
        ui.temperature.value = 18; ui.humidity.value = 80;
        addFood(250, 180, 1600); addWater(320, 180, 1600);
        runDays(40);
    """,
    "predator_response_3d": """
        setupMatureColony();
        world.food = []; world.water = [];
        addFood(250, 180, 1000); addWater(320, 180, 1000);
        addEnemy(world.nest.x + 170, world.nest.y);
        runDays(3);
    """,
    "rain_washes_pheromone": """
        setupMatureColony();
        world.food = []; world.water = [];
        addFood(250, 180, 1000); addWater(320, 180, 1000);
        runDays(3);
        const beforeRainFoodPhero = Math.round(world.pheromones.food.data.reduce((s, v) => s + v, 0));
        triggerRain();
        window.__beforeRainFoodPhero = beforeRainFoodPhero;
        runDays(1);
    """,
    "pheromone_high_evaporation_1d": """
        setupFoundingColony();
        world.ants = []; world.food = []; world.water = [];
        ui.evaporationRate.value = 180;
        ui.diffusionRate.value = 100;
        clearPheromones();
        world.pheromones.food.add(600, 380, 220);
        runDays(1);
    """,
    "pheromone_low_evaporation_1d": """
        setupFoundingColony();
        world.ants = []; world.food = []; world.water = [];
        ui.evaporationRate.value = 40;
        ui.diffusionRate.value = 100;
        clearPheromones();
        world.pheromones.food.add(600, 380, 220);
        runDays(1);
    """,
    "human_disturbance_1d": """
        setupMatureColony();
        triggerHumanDisturbance();
        runDays(1);
    """,
    "flood_event_2d": """
        setupMatureColony();
        triggerFlood();
        runDays(2);
    """,
    "mass_death_cleanup_5d": """
        setupMatureColony();
        triggerMassDeath();
        runDays(5);
    """,
    "heatwave_dry_10d": """
        setupMatureColony();
        addWater(320, 180, 1000);
        triggerHeatwave();
        runDays(10);
    """,
    "fake_food_pheromone_2d": """
        setupMatureColony();
        world.food = []; world.water = [];
        ui.fakePheromone.value = 'food';
        paintPheromone(260, 250);
        runDays(2);
    """,
    "death_spiral_8d": """
        setupMatureColony();
        createAntMill();
        runDays(8);
    """,
    "brood_pressure_tasks_2d": """
        setupMatureColony();
        world.food = []; world.water = [];
        world.foodStore = 420; world.waterStore = 420;
        world.eggs = 80; world.larvae = 140; world.pupae = 40;
        ui.broodDemand.value = 100;
        ui.hunger.value = 10;
        runDays(2);
    """,
    "resource_pressure_tasks_2d": """
        setupMatureColony();
        world.food = []; world.water = [];
        world.foodStore = 0; world.waterStore = 0;
        world.eggs = 0; world.larvae = 0; world.pupae = 0;
        ui.broodDemand.value = 10;
        ui.hunger.value = 90;
        addFood(250, 180, 800); addWater(320, 180, 800);
        runDays(2);
    """,
    "eciton_mature_baseline_5d": """
        ui.species.value = 'eciton';
        setupMatureColony();
        world.food = []; world.water = [];
        addFood(250, 180, 1200); addWater(320, 180, 1200);
        runDays(5);
    """,
    "eciton_death_spiral_5d": """
        ui.species.value = 'eciton';
        setupMatureColony();
        createAntMill();
        runDays(5);
    """,
    "brood_climate_extreme_8d": """
        setupMatureColony();
        world.food = []; world.water = [];
        world.foodStore = 420; world.waterStore = 0;
        world.eggs = 90; world.larvae = 120; world.pupae = 25;
        window.__startAnts = world.ants.length;
        ui.temperature.value = 12; ui.humidity.value = 18;
        ui.broodDemand.value = 100;
        runDays(8);
    """,
    "brood_climate_supported_8d": """
        setupMatureColony();
        world.food = []; world.water = [];
        world.foodStore = 420; world.waterStore = 420;
        world.eggs = 90; world.larvae = 120; world.pupae = 25;
        window.__startAnts = world.ants.length;
        ui.temperature.value = 26; ui.humidity.value = 70;
        ui.broodDemand.value = 100;
        runDays(8);
    """,
}


def count_states(result, names):
    states = result["states"]
    return sum(states.get(name, 0) for name in names)


def evaluate_expectations(results):
    checks = []

    def add(name, ok, detail):
        checks.append((name, bool(ok), detail))

    founding = results["founding_stable_40d"]
    add(
        "founding colony keeps queen and produces first workers/brood",
        founding["queens"] == 1 and founding["ants"] > 0 and founding["corpses"] == 0 and (founding["larvae"] + founding["pupae"] + founding["eggs"]) > 0,
        founding,
    )

    supplied = results["founding_supplied_80d"]
    add(
        "supplied founding colony has better hydration and no die-off",
        supplied["queens"] == 1 and supplied["corpses"] == 0 and supplied["avgHydration"] >= 60 and supplied["ants"] >= founding["ants"],
        supplied,
    )

    starving = results["mature_no_resources_20d"]
    add(
        "mature colony without resources shows stress but not instant collapse",
        starving["ants"] > 300 and starving["avgEnergy"] < 55 and starving["avgHydration"] < 55 and starving["corpses"] == 0,
        starving,
    )

    stable = results["mature_supplied_stable_40d"]
    add(
        "stable supplied colony maintains adults and brood without deaths",
        stable["ants"] >= 420
        and stable["corpses"] == 0
        and stable["avgEnergy"] >= 60
        and stable["avgHydration"] >= 70
        and (stable["eggs"] + stable["larvae"] + stable["pupae"]) >= 20,
        stable,
    )

    hot = results["mature_supplied_hot_dry_40d"]
    cool = results["mature_supplied_cool_humid_40d"]
    add(
        "hot/dry environment increases water stress and water-foraging behavior",
        hot["avgHydration"] < cool["avgHydration"]
        and hot["waterTrips"] > cool["waterTrips"]
        and hot["waterCollected"] > cool["waterCollected"],
        {"hot": hot, "cool": cool},
    )

    predator = results["predator_response_3d"]
    add(
        "predator produces alarm/defense response without auto-spawned enemies",
        predator["alarmPhero"] > 0 and count_states(predator, ["recruited defense", "retreating", "patrolling"]) > 30,
        predator,
    )

    rain = results["rain_washes_pheromone"]
    add(
        "rain washes down established food pheromone",
        rain["beforeRainFoodPhero"] and rain["foodPhero"] < rain["beforeRainFoodPhero"] * 0.25,
        rain,
    )

    high_evap = results["pheromone_high_evaporation_1d"]
    low_evap = results["pheromone_low_evaporation_1d"]
    add(
        "pheromone evaporation control changes chemical persistence",
        low_evap["foodPhero"] > high_evap["foodPhero"] * 1.5,
        {"high_evaporation": high_evap, "low_evaporation": low_evap},
    )

    disturbance = results["human_disturbance_1d"]
    add(
        "human disturbance leaves avoid signal and disorganized colony state",
        disturbance["avoidPhero"] > 0 and count_states(disturbance, ["exploring", "sheltering from rain", "retreating"]) > 150,
        disturbance,
    )

    flood = results["flood_event_2d"]
    add(
        "flood damages brood/adults and triggers corpse cleanup",
        flood["corpses"] > 20
        and flood["corpseMoves"] + count_states(flood, ["corpse cleanup", "carrying corpse", "lifting corpse"]) > 50
        and flood["deathPhero"] > 1000,
        flood,
    )

    mass = results["mass_death_cleanup_5d"]
    add(
        "mass death creates necrophoresis-like cleanup behavior",
        mass["corpses"] > 50
        and mass["corpseMoves"] + count_states(mass, ["corpse cleanup", "carrying corpse", "lifting corpse"]) > 100
        and mass["deathPhero"] > 1000,
        mass,
    )

    spiral = results["death_spiral_8d"]
    add(
        "death spiral causes localized mortality and cleanup load",
        spiral["mills"] == 1
        and spiral["corpses"] > 50
        and spiral["corpseMoves"] + count_states(spiral, ["corpse cleanup", "carrying corpse", "lifting corpse"]) > 80,
        spiral,
    )

    fake = results["fake_food_pheromone_2d"]
    add(
        "fake food pheromone does not create food or enemies",
        fake["foodObjects"] == 0 and fake["enemies"] == 0 and fake["alarmPhero"] == 0,
        fake,
    )

    brood_tasks = results["brood_pressure_tasks_2d"]["tasks"]
    resource_tasks = results["resource_pressure_tasks_2d"]["tasks"]
    brood_care = brood_tasks.get("brood", 0)
    resource_care = resource_tasks.get("brood", 0)
    brood_foraging = brood_tasks.get("food", 0) + brood_tasks.get("water", 0)
    resource_foraging = resource_tasks.get("food", 0) + resource_tasks.get("water", 0)
    add(
        "response-threshold task allocation shifts with brood/resource stimuli",
        brood_care > resource_care and resource_foraging > brood_foraging,
        {"brood_pressure": brood_tasks, "resource_pressure": resource_tasks},
    )

    eciton = results["eciton_mature_baseline_5d"]
    add(
        "eciton preset applies higher soldier ratio and sustained raiding activity",
        eciton["soldiers"] > 65
        and eciton["foodTrips"] + eciton["waterTrips"] > 50
        and (eciton["tasks"].get("food", 0) + eciton["tasks"].get("water", 0) + eciton["tasks"].get("explore", 0)) > eciton["tasks"].get("brood", 0),
        eciton,
    )

    eciton_spiral = results["eciton_death_spiral_5d"]
    add(
        "eciton preset is more susceptible to army-ant-style death spiral",
        eciton_spiral["mills"] == 1
        and eciton_spiral["ants"] < 260
        and eciton_spiral["corpses"] > 150
        and eciton_spiral["deathPhero"] > 5000,
        eciton_spiral,
    )

    extreme_brood = results["brood_climate_extreme_8d"]
    supported_brood = results["brood_climate_supported_8d"]
    add(
        "brood microclimate stress suppresses development relative to supported brood chamber",
        extreme_brood["broodStress"] > supported_brood["broodStress"]
        and extreme_brood["pupae"] + extreme_brood["newWorkers"] < supported_brood["pupae"] + supported_brood["newWorkers"],
        {"extreme": extreme_brood, "supported": supported_brood},
    )

    reproducibility = results["seed_reproducibility"]
    add(
        "fixed seed reproduces identical scripted experiment output",
        reproducibility["same"] and reproducibility["first"]["seed"] == 777 and reproducibility["second"]["seed"] == 777,
        reproducibility,
    )

    return checks


SUMMARY_JS = """
() => {
  window.runDays = (days) => {
    return antSim.runDays(days, 9);
  };
  return true;
}
"""


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(URL)
        page.wait_for_timeout(500)
        page.evaluate(SUMMARY_JS)

        results = {}
        for name, script in SCENARIOS.items():
            result = page.evaluate(
                f"""
                () => {{
                  ui.temperature.value = 26;
                  ui.humidity.value = 58;
                  ui.foodSpawn.value = 45;
                  ui.threatPressure.value = 25;
                  ui.hunger.value = 35;
                  ui.broodDemand.value = 50;
                  ui.pheromoneStrength.value = 80;
                  ui.speed.value = 1.4;
                  ui.fakePheromone.value = 'food';
                  ui.diffusionRate.value = 100;
                  ui.evaporationRate.value = 100;
                  ui.senseThreshold.value = 18;
                  setSeed(12345);
                  ui.species.value = 'lasius';
                  applySpeciesDefaults();
                  window.__beforeRainFoodPhero = null;
                  window.__startAnts = null;
                  {script}
                  const states = world.ants.reduce((acc, ant) => {{
                    acc[ant.state] = (acc[ant.state] || 0) + 1;
                    return acc;
                  }}, {{}});
                  const tasks = world.ants.reduce((acc, ant) => {{
                    acc[ant.task || 'none'] = (acc[ant.task || 'none'] || 0) + 1;
                    return acc;
                  }}, {{}});
                  const avg = (field) => world.ants.length
                    ? Math.round(world.ants.reduce((sum, ant) => sum + ant[field], 0) / world.ants.length)
                    : null;
                  const pheroSum = (field) => Math.round(world.pheromones[field].data.reduce((sum, v) => sum + v, 0));
                  return {{
                    day: Number(world.day.toFixed(1)),
                    ants: world.ants.length,
                    queens: world.queens.length,
                    species: ui.species.value,
                    soldiers: world.ants.filter(ant => ant.role === 'soldier').length,
                    eggs: Math.round(world.eggs),
                    larvae: Math.round(world.larvae),
                    pupae: Math.round(world.pupae),
                    corpses: world.corpses.length,
                    foodStore: Math.round(world.foodStore),
                    waterStore: Math.round(world.waterStore),
                    foodObjects: world.food.length,
                    waterObjects: world.water.length,
                    enemies: world.enemies.length,
                    mills: world.mills.length,
                    avgEnergy: avg('energy'),
                    avgHydration: avg('hydration'),
                    broodTemp: Number(world.broodClimate.temp.toFixed(1)),
                    broodHumidity: Number(world.broodClimate.humidity.toFixed(1)),
                    broodStress: Number(world.broodClimate.stress.toFixed(2)),
                    newWorkers: window.__startAnts == null ? 0 : world.ants.length - window.__startAnts,
                    foodTrips: world.stats.foodTrips,
                    foodCollected: Math.round(world.stats.foodCollected),
                    waterTrips: world.stats.waterTrips,
                    waterCollected: Math.round(world.stats.waterCollected),
                    corpseMoves: world.stats.corpseMoves,
                    states,
                    tasks,
                    foodPhero: pheroSum('food'),
                    waterPhero: pheroSum('water'),
                    alarmPhero: pheroSum('alarm')
                    , deathPhero: pheroSum('death')
                    , avoidPhero: pheroSum('avoid')
                    , beforeRainFoodPhero: window.__beforeRainFoodPhero || null
                  }};
                }}
                """
            )
            results[name] = result
            print(f"{name}: {result}")

        reproducibility = page.evaluate(
            """
            () => {
              const run = () => {
                setSeed(777);
                ui.temperature.value = 26;
                ui.humidity.value = 58;
                ui.foodSpawn.value = 45;
                ui.threatPressure.value = 25;
                ui.hunger.value = 35;
                ui.broodDemand.value = 50;
                ui.pheromoneStrength.value = 80;
                ui.diffusionRate.value = 100;
                ui.evaporationRate.value = 100;
                ui.senseThreshold.value = 18;
                ui.species.value = 'lasius';
                applySpeciesDefaults();
                setupMatureColony();
                world.food = [];
                world.water = [];
                addFood(250, 180, 800);
                addWater(320, 180, 800);
                antSim.runDays(3, 9);
                return collectStatsSnapshot();
              };
              const first = run();
              const second = run();
              return {
                same: JSON.stringify(first) === JSON.stringify(second),
                first,
                second
              };
            }
            """
        )
        results["seed_reproducibility"] = reproducibility
        print(f"seed_reproducibility: {reproducibility}")

        print(f"errors: {errors}")
        print("\nchecks:")
        failed = 0
        for name, ok, detail in evaluate_expectations(results):
            status = "PASS" if ok else "FAIL"
            if not ok:
                failed += 1
            print(f"{status}: {name}")
            if not ok:
                print(f"  detail: {detail}")
        print(f"summary: {len(results)} scenarios, {failed} failed checks, {len(errors)} page errors")
        browser.close()


if __name__ == "__main__":
    main()
