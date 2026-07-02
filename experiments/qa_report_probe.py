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
              const sumPhero = (name) =>
                Math.round(antSim.world.pheromones[name].data.reduce((sum, value) => sum + value, 0));
              const out = {};

              out.api = {
                globalTick: typeof window.tick,
                namespacedTick: typeof antSim.tick,
                globalResetWorld: typeof window.resetWorld,
                globalTriggerAlert: typeof window.triggerAlert,
                syncUi: typeof antSim.syncUi,
                startTrajectoryLog: typeof antSim.startTrajectoryLog,
                collectTrajectoryLog: typeof antSim.collectTrajectoryLog,
                collectSegmentMetrics: typeof antSim.collectSegmentMetrics
              };

              antSim.resetWorld();
              antSim.syncUi();
              out.founding = {
                queens: antSim.world.queens.length,
                ants: antSim.world.ants.length,
                foodObjects: antSim.world.food.length,
                waterObjects: antSim.world.water.length,
                antsLabel: antSim.ui.antsLabel.textContent,
                sliderValue: Number(antSim.ui.antCount.value)
              };

              antSim.resetWorld();
              antSim.world.food = [];
              antSim.world.water = [];
              const mover = antSim.addAntAt(100, 150, 'worker');
              mover.energy = 100;
              mover.hydration = 100;
              mover.health = 100;
              mover.state = 'exploring';
              const start = { x: mover.x, y: mover.y };
              antSim.addFood(760, 390, 400);
              antSim.addWater(820, 390, 400);
              antSim.runSteps(80, 9);
              antSim.startTrajectoryLog({ sampleEverySteps: 1, antLimit: 5, maxRows: 200 });
              antSim.runSteps(20, 9);
              const trajectoryRows = antSim.stopTrajectoryLog();
              const segment = antSim.collectSegmentMetrics(100, 150, 760, 390, 120);
              out.movement = {
                start,
                end: { x: Number(mover.x.toFixed(2)), y: Number(mover.y.toFixed(2)) },
                moved: Number(Math.hypot(mover.x - start.x, mover.y - start.y).toFixed(2)),
                state: mover.state,
                trajectoryRows: trajectoryRows.length,
                trajectoryHasPosition: trajectoryRows.some(row => Number.isFinite(row.x) && Number.isFinite(row.y)),
                trajectoryHasSensingColumns: trajectoryRows.some(row => 'sensing_left' in row && 'sensing_turn' in row),
                segmentCount: segment.count,
                segmentMeanSpeed: segment.mean_speed
              };

              antSim.setupMatureColony();
              const matureWaterObjects = antSim.world.water.length;
              antSim.runSteps(200, 9);
              out.matureWater = {
                waterObjects: matureWaterObjects,
                waterCollected: Math.round(antSim.world.stats.waterCollected),
                waterTrips: antSim.world.stats.waterTrips
              };

              antSim.setupMatureColony();
              const beforeAlertAnts = antSim.world.ants.length;
              const alertReturn = antSim.triggerAlert();
              antSim.runSteps(200, 9);
              out.alert = {
                beforeAnts: beforeAlertAnts,
                afterAnts: antSim.world.ants.length,
                enemies: antSim.world.enemies.length,
                returnedEnemies: alertReturn.enemies,
                returnedAnts: alertReturn.ants,
                alarmPheromone: sumPhero('alarm')
              };

              antSim.resetWorld();
              for (let i = 0; i < 3; i++) antSim.addAntAt(240 + i * 8, 220, 'worker');
              antSim.syncUi();
              out.uiSync = {
                ants: antSim.world.ants.length,
                label: antSim.ui.antsLabel.textContent,
                sliderValue: Number(antSim.ui.antCount.value)
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

        check(
            "script API exposes stable entry points",
            results["api"]["globalTick"] == "function"
            and results["api"]["namespacedTick"] == "function"
            and results["api"]["globalResetWorld"] == "function"
            and results["api"]["globalTriggerAlert"] == "function"
            and results["api"]["syncUi"] == "function"
            and results["api"]["startTrajectoryLog"] == "function"
            and results["api"]["collectTrajectoryLog"] == "function"
            and results["api"]["collectSegmentMetrics"] == "function",
            results["api"],
        )
        check(
            "founding reset starts with queen-only founding colony",
            results["founding"]["queens"] == 1
            and results["founding"]["ants"] == 0
            and results["founding"]["waterObjects"] == 0,
            results["founding"],
        )
        check(
            "manual worker moves under tick/runSteps",
            results["movement"]["moved"] > 5
            and results["movement"]["trajectoryRows"] > 0
            and results["movement"]["trajectoryHasPosition"]
            and results["movement"]["trajectoryHasSensingColumns"],
            results["movement"],
        )
        check(
            "mature colony intentionally seeds a water source",
            results["matureWater"]["waterObjects"] >= 1,
            results["matureWater"],
        )
        check(
            "triggerAlert creates alarm/enemy without clearing ants",
            results["alert"]["beforeAnts"] > 0
            and results["alert"]["afterAnts"] > 0
            and results["alert"]["returnedAnts"] == results["alert"]["beforeAnts"]
            and results["alert"]["returnedEnemies"] >= 1
            and results["alert"]["alarmPheromone"] > 0,
            results["alert"],
        )
        check(
            "scripted ant insertion synchronizes visible count controls",
            results["uiSync"]["ants"] == 3
            and results["uiSync"]["label"] == "3"
            and results["uiSync"]["sliderValue"] == 3,
            results["uiSync"],
        )

        if errors:
            failures.extend(errors)
            print(f"PAGE_ERRORS: {errors}")
        print(f"summary: {len(failures)} failed checks")
        browser.close()

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
