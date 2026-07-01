# Ant-Colony-Sim ODD 模型規格草案

本文件把目前版本定位為「行為級 agent-based model 研究輔助原型」，不是已完成定量校準的真實蟻群預測器。用途是支援假說探索、教學展示、自動化實驗流程與後續文獻校準。

## 1. Purpose

模型目標是模擬蟻群在有限環境中的行為級現象：

- 創群與成熟蟻群兩種初始狀態。
- 工蟻、兵蟻、護幼工蟻、蟻后、卵、幼蟲、蛹的簡化生命階段。
- 食物、水、天敵、障礙、人為干擾、降雨、熱浪、洪水、大量死亡。
- 食物、飲水、回巢、警戒、死亡、避開等化學場。
- 任務分工、覓食、取水、育幼、防衛、屍體清除、死亡漩渦。

目前可用於比較不同參數設定下的定性趨勢，例如費洛蒙蒸發率對路徑維持的影響、溫濕度對取水需求的影響、死亡化學場對屍體清除行為的影響。

## 2. Entities, State Variables, and Scales

### 2.1 Entities

- `ant`: 工蟻、兵蟻、護幼工蟻。
- `queen`: 蟻后。
- `corpse`: 死亡個體與死亡化學線索來源。
- `food`, `water`: 使用者放置或初始化的資源。
- `enemy`: 使用者放置的天敵/威脅源。
- `rock`: 障礙物。
- `pheromone field`: 離散網格上的化學濃度場。

### 2.2 Ant State Variables

- `role`: worker, soldier, nurse。
- `task`: explore, food, water, brood, corpse, patrol, defense 等。
- `state`: 當前可視化行為狀態。
- `x`, `y`, `angle`: 位置與移動方向。
- `energy`, `hydration`, `health`, `age`: 生理狀態。
- `carrying`, `carryingWater`, `carryingCorpse`: 搬運狀態。
- `thresholds`: response-threshold 任務分工參數。
- `memory`: 食物與敵人位置的短期記憶。

### 2.3 Spatial and Temporal Scale

- 空間目前是 1200 x 760 模擬單位，不等同真實公分或毫米。
- 費洛蒙網格大小目前是 22 模擬單位。
- `world.day += dt / 900`，也就是 900 個模擬 dt 單位代表 1 天。
- 目前時間與空間尚未用實驗資料校準成真實單位。

## 3. Process Overview and Scheduling

每個固定步長更新會依序執行：

1. 更新世界時間、雨水與干擾計時器。
2. 更新每隻螞蟻的代謝、感知、任務決策、移動與互動。
3. 死亡個體轉為 corpse。
4. 更新屍體化學場。
5. 更新蟻后能量、水分、健康、產卵。
6. 更新育幼室微氣候。
7. 更新卵、幼蟲、蛹發育。
8. 移除耗盡的食物、水、敵人。
9. 更新各類費洛蒙場的擴散與蒸發。
10. 每 0.25 模擬日記錄一次統計快照。

研究腳本應使用 `antSim.runSteps(steps, dt)` 或 `antSim.runDays(days, dt)`，這會暫停動畫並以固定步長推進，避免畫面渲染迴圈造成額外更新。

## 4. Design Concepts

### 4.1 Emergence

路徑形成、資源搬運、屍體清除、防衛聚集、死亡漩渦都不是單一全域命令，而是由個體感知局部費洛蒙、資源、威脅與內部狀態後產生。

### 4.2 Adaptation

個體會依能量、水分、群體儲存量、育幼需求、死亡化學場、警戒費洛蒙等因素切換任務。低能量或低水分個體會優先返回巢穴恢復。

### 4.3 Sensing

螞蟻會在前方、左方、右方取樣費洛蒙。使用者可調整：

- `diffusionRate`: 擴散速率。
- `evaporationRate`: 蒸發速率。
- `senseThreshold`: 最小可感知濃度。

### 4.4 Stochasticity

所有模擬隨機性應透過 seeded PRNG。使用：

```js
antSim.setSeed(777);
```

同一 seed、同一初始化、同一固定步長應得到相同輸出。

### 4.5 Observation

模型提供：

- UI 統計面板。
- CSV 匯出。
- `antSim.collectStatsSnapshot()`。
- `world.statsHistory`。

CSV 每列包含 seed、random_state、主要參數快照與群體統計。

## 5. Initialization

目前有兩個主要初始化流程：

- `setupFoundingColony()`: 創群模式，一開始只有蟻后、少量儲備與卵。
- `setupMatureColony()`: 成熟蟻群，含蟻后、工蟻、兵蟻、卵、幼蟲、蛹與少量資源。

物種 preset 目前有：

- `Lasius niger`
- `Eciton burchellii`

注意：物種參數目前是行為級近似，不是完整文獻校準參數集。

## 6. Input Data

目前不依賴外部實驗資料。所有參數來自 UI、species preset 與內建常數。

正式研究使用前，需要加入至少下列資料來源：

- 移動速度與覓食距離。
- 費洛蒙半衰期與擴散特性。
- 卵、幼蟲、蛹發育時間。
- 工蟻壽命與死亡率分布。
- 食物品質、距離與招募強度關係。
- 溫濕度對活動與育幼成功率的影響。

## 7. Submodels

### 7.1 Pheromone Field

目前為離散網格，使用 Gaussian-like 鄰域擴散與蒸發係數。每種化學場獨立更新。

限制：

- 尚未使用真實物理單位。
- 尚未校準半衰期。
- 尚未改成 sparse grid 或 GPU/worker 加速。

### 7.2 Metabolism

目前已有能量、水分、健康、年齡與低能量回巢。不同工作狀態的代謝差異仍偏簡化。

下一步應把代謝拆成角色與行為成本：

- exploration cost
- carrying cost
- combat cost
- brood care cost
- nest recovery gain

### 7.3 Reproduction and Brood

蟻后依健康、能量、水分、儲備與育幼壓力產卵。卵、幼蟲、蛹依照照護、食物、水與育幼室氣候發育。

限制：

- 發育時間尚未對應真實天數。
- 產卵率尚未依物種與文獻校準。

### 7.4 Task Allocation

使用 response-threshold 風格的任務分配。任務刺激包含育幼、食物、水、屍體、威脅。

限制：

- 閾值目前多為模型假設。
- 尚未與真實個體追蹤資料校準。

## 8. Current Validation Status

目前自動測試涵蓋：

- 創群 40/80 天。
- 成熟蟻群無資源、穩定供應、熱乾、冷濕。
- 天敵、防衛、降雨沖刷、人為干擾、洪水、大量死亡。
- 假費洛蒙、死亡漩渦、育幼壓力、資源壓力。
- 兩種物種 preset。
- 固定 seed 可重現性。

這些是行為回歸測試，不等同生物學定量驗證。

## 9. Research Acceptance Criteria

要從原型提升到正式研究輔助工具，最低應完成：

1. 固定 seed 與參數快照輸出。
2. Headless/batch experiment runner。
3. ODD 文件與參數手冊。
4. 至少一組文獻資料的定量比對。
5. 多 seed Monte Carlo 輸出平均值、變異與信賴區間。
6. 模擬核心與 UI 分離。
7. 效能可支援至少 1000 隻螞蟻的批量實驗。

## 10. Known Boundaries

- 目前不應宣稱可預測真實蟻群數量或精確覓食率。
- 不應把 `Eciton burchellii` 視為已校準軍蟻模型。
- 不應把費洛蒙濃度解讀為真實化學濃度。
- 不應在沒有校準資料時比較絕對數值，只應比較相同模型內的相對趨勢。

