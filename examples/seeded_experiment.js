// Ant-Colony-Sim seeded experiment example.
// Paste into the browser console after opening index.html, or run through Playwright.

antSim.setSeed(777);
antSim.setParam('species', 'lasius');
antSim.setParam('temperature', 26);
antSim.setParam('humidity', 58);
antSim.setParam('diffusionRate', 100);
antSim.setParam('evaporationRate', 100);
antSim.setParam('senseThreshold', 18);

antSim.setupMatureColony();
antSim.world.food = [];
antSim.world.water = [];
antSim.addFood(250, 180, 800);
antSim.addWater(320, 180, 800);

const rows = [];
for (let day = 0; day < 10; day += 1) {
  rows.push(antSim.runDays(1));
}

console.table(rows);
console.log(antSim.getExperimentConfig());
antSim.exportCsv();
