# 生物學參考意義審計

本文件回答一個核心問題：這個模擬器目前是否有科學生物學參考意義？

結論：目前有「定性研究輔助」價值，但沒有「定量生物預測」價值。它可以用來探索螞蟻行為模型的假說、檢查規則是否能產生某些群體現象、產生可重現的 ABM 資料；但不能直接聲稱能預測真實蟻群的覓食率、死亡率、產卵率或費洛蒙濃度。

## 1. 目前有生物學參考意義的部分

### 1.1 費洛蒙路徑與局部感知

目前模型具有：

- 離散費洛蒙場。
- 擴散與蒸發。
- 前/左/右方向取樣。
- 最小可感知閾值。
- 食物、水、回巢、警戒、死亡、避開訊號。

參考意義：可以研究「局部化學訊號 + 隨機探索」是否足以形成路徑、路徑是否會因蒸發與降雨衰退、閾值如何影響路徑追隨。

限制：目前濃度不是實際化學濃度，擴散/蒸發參數也不是從半衰期或實測擴散係數校準。

可驗證輸出：

- 首次穩定路徑形成時間。
- 食物發現後 food_pheromone 上升曲線。
- 食物移除或降雨後 food_pheromone 衰退曲線。
- 不同 `senseThreshold` 下的採集成功率。

### 1.2 Response-threshold 任務分工

目前模型具有：

- 個體任務閾值。
- 育幼、食物、水、屍體、威脅刺激。
- 個體依刺激與內部狀態切換 task。

參考意義：可以研究簡化 response-threshold 是否能產生工蟻分工，例如育幼壓力提高時 nurse/brood task 上升，資源短缺時 foraging task 上升。

限制：閾值數值是模型假設，尚未用個體追蹤實驗校準。

可驗證輸出：

- broodDemand 上升時 brood task 比例。
- hunger 上升時 food/water task 比例。
- 屍體數量上升時 corpse cleanup 行為比例。

### 1.3 Necrophoresis / 屍體清除

目前模型具有：

- 死亡個體轉為 corpse。
- death chemical field。
- 工蟻依 death cue 搜尋、搬運、放置到 refuse area。
- 大量死亡後清除負荷增加。

參考意義：可以研究「死亡化學線索 + 局部清除規則」是否能產生屍體搬離巢區與 refuse pile。

限制：真實螞蟻的死亡辨識涉及屍體化學輪廓與時間延遲；目前模型把它簡化成一個 death field，尚未模擬脂肪酸釋放曲線、活體抑制訊號或病原感染狀態。

可驗證輸出：

- corpse 出現到首次搬運的延遲。
- corpseMoves/day。
- 巢區內 corpse 數量隨時間下降曲線。
- 大量死亡後清除是否延遲或飽和。

### 1.4 巢內育幼與微氣候

目前模型具有：

- brood chamber temperature/humidity。
- 溫濕度偏離造成 brood stress。
- nurse/brood task 影響微氣候回復。
- 食物與水影響幼蟲到蛹、蛹到成蟻。

參考意義：可以定性探索「育幼照護、儲水、溫濕度」與 brood development 的關係。

限制：發育時間、死亡率、產卵率尚未按物種文獻校準；目前不能用來預測真實發育天數。

可驗證輸出：

- brood_stress 與 larvae/pupae/new worker 的關係。
- 熱乾、冷乾、穩定濕度下的 brood survival proxy。

## 2. 目前生物學參考意義弱或不可用的部分

### 2.1 物種差異

目前 `Lasius niger` 與 `Eciton burchellii` 只有行為參數差異，例如速度、兵蟻比例、費洛蒙持久性、死亡漩渦敏感度。這可用於展示「species profile」概念，但不能當作兩個物種的真實模型。

正式研究前需要：

- 每個參數都有來源、單位與可信度。
- species-specific brood duration、foraging range、worker lifespan、colony size、caste distribution。
- 不同物種的行為模組差異，而不是只調倍率。

### 2.2 能量與代謝

目前 energy/hydration 是行為控制變數，不是實際代謝模型。它能讓螞蟻在資源壓力下回巢或死亡，但不能換算成熱量、水分流失或真實生理狀態。

正式研究前需要：

- 依行為拆分成本：探索、搬運、戰鬥、育幼、休息。
- 對應到速度、距離、時間或體重的成本函式。
- 不同 caste 的消耗率。

### 2.3 天敵與戰鬥

目前 enemy 是局部威脅源，可觸發 alarm/defense，但不是任何特定天敵或種間戰鬥模型。

正式研究前需要：

- 天敵類型。
- 接觸機率、受傷率、死亡率。
- 招募兵蟻與撤退的實測行為門檻。

## 3. 最小生物學驗證案例

若要讓本專案具備真正研究輔助價值，建議先完成三個可量化 validation case。

### Case A: 食物路徑形成與消退

目的：驗證費洛蒙路徑模型是否能再現「發現食物後路徑增強，食物消失或降雨後路徑衰退」。

實驗設計：

1. 成熟蟻群。
2. 固定 seed 組：至少 30 個 seed。
3. 單一食物源固定距離。
4. 記錄每 0.25 天的 food_pheromone、food_trips、food_store、carrying_food。
5. 第 N 天移除食物或觸發 rain。

合格標準：

- food_pheromone 在食物可用時上升。
- food_trips 在路徑形成後上升。
- 移除食物或 rain 後 food_pheromone 顯著下降。

目前狀態：已能測，尚未與真實數據比對。

### Case D: 雙橋路徑選擇

目的：對照 Deneubourg/Beckers 類型雙橋實驗：兩條等價路徑初期都被使用，但正回饋可能造成單一路徑被放大；若預先給其中一條橋較強 trail，模型應提高該橋被選中的機率。

實驗設計：

1. 成熟蟻群，固定巢穴與單一食物源。
2. 在巢穴與食物間建立中央障礙，留下上下兩條路徑。
3. 每次 crossing 通過 gate 時記錄 upper/lower。
4. 用多 seed 比較 `dominance = abs(upper-lower)/(upper+lower)`。
5. 可加入 `--bias-branch upper/lower` 與 `--bias-strength` 測試初始費洛蒙偏差。

目前狀態：

- 無 bias 8-seed test：上下路徑各被選中 4 次，平均 dominance 約 0.173。這表示模型已能產生隨機早期差異驅動的對稱破缺，但鎖定強度仍低於經典雙橋實驗常見的強單一路徑選擇。
- 強 connected upper bias：3/3 seeds 選上橋，平均 dominance 約 0.525。表示模型能對連續且接上巢穴/食物的 trail 偏差產生明顯反應。
- `double_bridge_calibration_v1`：以 Deneubourg/Le Goff reinforced-random-walk 參考 target 做 8 組 grid search，最佳參數為 `pheromoneStrength=120`、`senseThreshold=10`、`evaporationRate=80`，loss 約 1.49。此組已設為目前 UI/headless 預設。

解讀：目前能說「分岔路徑、初始 trail 偏差、正回饋方向相符」；仍未達到經典雙橋實驗的定量吻合。正式校準需 digitize 文獻曲線，並以多 seed 估計 branch choice probability。

### Case E: 個體隨機性分布與環境改變後適應

目的：對照 Shiraishi et al. 的 diverse stochasticity 模型：不同程度的 trail-following 隨機性可能在不同食物環境下提高群體效率。

實驗設計：

1. 成熟蟻群，固定 seed 組。
2. 四組 turn-noise profile：low、medium、high、diverse。
3. 前半段固定食物；後半段保留舊費洛蒙並把食物移到另一側位置。
4. 比較每組 `phase_food_trips`、`phase_food_collected`、`avg_turn_noise`。
5. 分開看 raw trips 與 normalized adaptation ratio，避免把「穩定環境 exploitation」和「環境改變後彈性」混為同一件事。

目前狀態：

- `stochasticity_probe_v1` 已完成 8 seeds。
- relocated food 階段結果：low 311.75 trips、medium 236.38、high 175.38、diverse 207.63。
- 這與 Shiraishi et al.「多樣化隨機性可提升某些環境下效率」的方向不一致。
- `stochasticity_probe_v2` 改為分窗輸出：`relocated_early`、`relocated_late`、`relocated_total`，並加入 `trips_vs_initial` / `collected_vs_initial`。
- v2 8-seed 結果：
  - raw `relocated_early` trips：low 49.25、medium 25.50、high 4.38、diverse 18.88。
  - normalized `relocated_early trips_vs_initial`：low 0.375、medium 0.671、high 0.250、diverse 0.689。
  - raw `relocated_total` trips：low 200.38、medium 81.88、high 47.75、diverse 86.88。
- `stochasticity_probe_v3` 加入交通/擁擠成本與食物記憶衰退：
  - raw `relocated_early` trips：low 32.88、medium 15.75、high 2.88、diverse 13.50。
  - normalized `relocated_early trips_vs_initial`：low 0.426、medium 0.502、high 0.170、diverse 0.532。
  - raw `relocated_total` trips：low 129.88、medium 101.63、high 48.38、diverse 89.38。
  - `relocated_total avg_traffic_load`：low 0.343、medium 0.138、high 0.003、diverse 0.129。
- `stochasticity_probe_v4` 加入狀態依賴 stochasticity：
  - 個體保留 `baseTurnNoise`，同時依擁擠、舊食物記憶、資源壓力調整 `explorationDrive` 與有效 `turnNoise`。
  - normalized `relocated_early trips_vs_initial`：low 0.368、medium 0.372、high 0.249、diverse 0.522。
  - raw `relocated_total` trips：low 113.38、medium 36.38、high 49.13、diverse 79.75。
  - `relocated_total avg_traffic_load`：low 0.324、medium 0.136、high 0.004、diverse 0.098。
  - 自動報告：`outputs/biological_validation_report_v4.md`。

解讀：v4 是目前較完整的行為層版本。diverse 在食物搬移早期的相對適應率高於 low，支持「個體隨機性分布會影響群體適應彈性」的定性研究用途；但 medium 與 low 沒有清楚分離，raw total exploitation 仍由 low 勝出。因此仍不能聲稱完整重現 Shiraishi et al. 的最佳分布曲線。下一步應用 digitized paper curve 或實驗追蹤資料校準個體路徑記憶半衰期、發現者招募差異與路徑幾何成本。

### Case B: 資源壓力下的任務分配

目的：驗證 response-threshold 任務分工是否會隨 hunger/broodDemand 改變。

實驗設計：

1. 三組：低 hunger、高 hunger、高 broodDemand。
2. 每組至少 30 seeds。
3. 比較 food/water/brood/corpse task 比例。

合格標準：

- 高 hunger 組 food/water task 顯著高於低 hunger 組。
- 高 broodDemand 組 brood task 顯著高於資源壓力組。

目前狀態：自動探針已做定性檢查，尚未做統計顯著性。

### Case C: 屍體清除

目的：驗證死亡化學線索是否能產生巢區屍體移除。

實驗設計：

1. 成熟蟻群。
2. 在巢內放置固定數量 corpse 或觸發 mass death。
3. 記錄 corpses、corpseMoves、death_pheromone、carrying_corpse。
4. 比較不同 corpse 數量與 colony size。

合格標準：

- corpseMoves 隨 corpse 數量上升。
- 巢內 corpse 逐步移出到 refuse area。
- 大量死亡時清除速度出現飽和。

目前狀態：已具備機制，尚未分離「巢內 corpse」與「refuse corpse」統計欄位。

## 4. 參數可信度分級

| 參數/機制 | 目前狀態 | 可信度 | 原因 |
|---|---|---:|---|
| 費洛蒙擴散/蒸發 | 有機制、可調 | 中低 | 方向正確，但未校準半衰期 |
| 費洛蒙梯度感知 | 有前/左/右採樣 | 中 | 可對應 tropotaxis/局部梯度追隨，但感知距離未校準 |
| 隨機探索 | 有 | 中 | ABM 常用，需和真實轉角分布比對 |
| 任務分工 | response-threshold 近似 | 中低 | 理論方向合理，閾值是假設 |
| 能量/水分 | 有行為控制 | 低 | 不是生理代謝模型 |
| 產卵/育幼 | 有生命階段 | 低 | 發育天數與產卵率未校準 |
| Necrophoresis | 有死亡場與搬運 | 中低 | 現象方向正確，化學細節簡化 |
| 天敵/戰鬥 | 有警戒與兵蟻反應 | 低 | 未對應特定天敵 |
| 物種差異 | 有 preset | 低 | 參數尚非文獻表 |

## 5. 下一步開發應優先做什麼

如果目標是科學生物學參考意義，優先順序應改為：

1. 加入 validation metrics：路徑形成時間、採集率、任務比例、屍體清除半衰期。
2. batch runner 支援多 seed、多參數輸出與彙總統計。
3. 建立 `PARAMETER_PROVENANCE`，每個參數標註 source、unit、confidence。
4. 選一個物種先做校準，不要同時追求多物種真實性。
5. 對照至少一個文獻實驗，而不是只看 UI 行為像不像。

## 6. 目前可以怎麼正確使用

可以：

- 用來測試某個行為規則是否能產生預期的群體現象。
- 比較同一模型內不同參數的相對趨勢。
- 做教學與方法展示。
- 做後續文獻校準前的 ABM 原型。

不可以：

- 宣稱它預測真實 Lasius niger 或 Eciton burchellii 的數值。
- 把目前的 day、distance、pheromone value 當成真實單位。
- 用單次 seed 的結果做生物學結論。
- 在沒有文獻校準前比較不同物種的絕對差異。

## 7. 已補上的研究支援能力

- 固定 seed：`antSim.setSeed(seed)`。
- 參數快照：CSV 每列包含 seed、random_state、溫濕度、壓力、費洛蒙控制參數、模型版本與 provisional 單位假設。
- 批次實驗：`experiments/batch_runner.py` 可跑多 seed、多參數組。
- 彙總統計：`experiments/summarize_batch.py` 可輸出每個時間點的 mean/sd/n。
- 個體層級 snapshot：`antSim.collectIndividualSnapshot(limit)` 可輸出個體位置、任務、狀態、能量、水分、健康。
- 生物學 validation metrics：一般 snapshot 已包含 task/state counts、trip rates、brood_total、nest_corpses、disposed_corpses。
- 文獻現象探針：`experiments/literature_alignment_probe.py` 檢查 food/nest trail、rain washout、evaporation sensitivity、death spiral。
- 雙橋探針：`experiments/double_bridge_probe.py` 檢查分岔路徑選擇與初始 trail bias。
- 雙橋校準：`experiments/calibrate_double_bridge.py` 對 Deneubourg-style choice reference target 做 grid search，輸出 loss-ranked CSV/JSON。
- 隨機性探針：`experiments/stochasticity_probe.py` 比較 low/medium/high/diverse turn-noise profile 在食物 relocation 後的覓食效率。

## 8. 文獻對照方向

目前最適合對照的文獻方向：

- 蟻類覓食路徑與局部費洛蒙追蹤模型。
- 雙費洛蒙或吸引/排斥費洛蒙模型。
- Necrophoresis 與 oleic/linoleic acid 等死亡線索。
- ODD protocol / individual-based model 描述規範。

## 9. 已執行的文獻現象對照

### Perna et al. 2012 / Weber-like local pheromone response

目前 `steerByField()` 使用左右感知對比；低濃度時近似 Weber contrast，高濃度時加入輕度非線性，以支援 Deneubourg 型雙橋正回饋。`literature_alignment_probe.py` 顯示 food/nest pheromone trail 可形成，且降雨/蒸發會消退。

限制：尚未輸出每隻螞蟻的左右感知濃度與轉角資料，因此還不能擬合論文中的 turning-angle response function。

### Malickova/Yates/Bodova 2015 / two-pheromone trail following

目前模型有 food 與 nest 兩個方向性訊號；文獻對照探針顯示它們能在食物源與巢穴間形成可量測 trail，且外部擾動會降低 trail。

限制：該論文是 off-lattice stochastic model，正式對照應比較 food discovery time、path persistence、環境改變後重新適應時間。

### Ryan 2015 / ant raid collective dynamics

目前模型已有 foraging/returning 狀態與食物搬運，但尚未量測 lane formation/order parameter，也未測食物耗盡後從 collective trail 回到 dispersed individual state。

下一步：新增 food depletion probe，量測食物耗盡前後的 `food_pheromone`、crossing flow、trail-following state count。

### Das 2017 / ant mill

Eciton preset + `createAntMill()` 能產生 death-spiral-like mortality；文獻現象探針已通過。

限制：目前 death spiral 是可觸發事件，不是從一般 trail 交叉自發形成；死亡速率、半徑、持續時間未校準。

### Dussutour et al. 2004 / crowded trail traffic

Nature 2004 的擁擠雙路徑實驗顯示：低密度時 pheromone attraction 形成單一路徑；高擁擠時會建立另一條路徑，以維持食物返回流量。這指出模型需要「擁擠造成的抑制互動」或容量限制。

目前狀態：尚未實作。現有模型缺少 ant-ant collision / density inhibition，因此不能直接驗證這篇論文。

下一步：新增 traffic probe，量測不同 ant density 下的 route split、flow、velocity proxy；再加入局部密度造成的轉向/速度抑制。

### John et al. 2009 / absence of jammed phase

PRL 2009 的螞蟻交通實驗指出，ant trail 的平均速度幾乎不隨密度下降，因此沒有典型車流 jammed phase。

目前狀態：尚未實作。若只用目前模型測試，很可能「沒有堵塞」只是因為缺少個體間排斥或接觸規則，不能算生物學相符。

下一步：在加入局部密度互動後，再量測 velocity-density curve，確認是否仍無 jammed phase。

### Shiraishi et al. 2018 / diverse stochasticity

該模型研究不同 trail-following 隨機性分布與覓食效率；結果指出最佳 stochasticity distribution 會依食物環境改變。

目前狀態：`stochasticity_probe_v1` 顯示不相符。low-noise profile 在 relocated food 階段表現最好，diverse profile 沒有優勢。

下一步：把隨機性從單一 turnNoise 改成 role/state dependent exploration strategy，例如 scouts 維持高探索、carriers 維持低噪音、trail followers 依路徑成功率動態調整。

### Amorim 2014 / PDE foraging model and Ramirez et al. 2018 / tropotaxis

這兩類模型把螞蟻與費洛蒙場形式化為 PDE 或 active walker/tropotaxis。它們適合用來校準 `steerByField()` 的梯度反應、擴散係數、trail formation threshold。

目前狀態：已定性相容。模型有 food/nest fields、diffusion/evaporation、左右/前方感知，並已輸出 aggregate gradient-turn alignment、局部左右濃度差、轉角反應與 trail segment flow/density。

目前已可輸出 bounded per-step individual trajectory/sensing series。下一步不是再加特例規則，而是用 digitized paper curves 擬合 tropotaxis response function，並檢查不同物種/幾何條件下的參數穩定性。

## 10. Paper-condition validation matrix

`experiments/paper_conditions_probe.py` 把多篇文獻轉成可重跑的 condition check。這不是「證明模型等於真實蟻群」，而是檢查目前規則是否能在指定條件下重現文獻中的定性方向，並標出還不能量化比對的缺口。

執行：

```bash
python3 experiments/paper_conditions_probe.py \
  --seeds 1-3 \
  --output outputs/paper_conditions_v5.csv \
  --json-output outputs/paper_conditions_v5.json \
  --report-output outputs/paper_conditions_report_v5.md
```

目前 `v5` 結果：17 個 exact/near-exact biological conditions 全部為 `pass`。`pass` 只表示 shared general rules 在該條件下重現文獻定性方向，不表示已完成物種專屬數值擬合。

| 文獻 / 條件 | 狀態 | 觀測摘要 | 仍缺什麼 |
| --- | --- | --- | --- |
| Perna et al. 2012 / local pheromone trail | pass | 平均 `food_trips=131.667`、trajectory rows `16000.0`、trajectory sensing rows `7479.333`、trajectory alignment `0.955`，且 trail segment flow `160.9912` | 已有 per-step trajectory/sensing 與 segment metrics；仍缺 digitized curve fitting |
| Ramirez et al. 2018 / tropotaxis | pass | 與 Perna 條件共享 per-step trajectory/sensing、gradient-turn 與 segment-flow metrics | 缺文獻 trajectory/方程式曲線 digitization 與數值擬合 |
| Amorim 2014 / trail formation and washout | pass | rain + food removal 後 `food_pheromone_ratio=0.0` | 仍是 ABM heuristic field，不是 PDE 參數單位 |
| Deneubourg/Goss/Beckers double bridge | pass | seeded selected fraction `0.667`、seeded return selected fraction `0.667`、return-traffic lift `0.0964`、branch curve error `0.2623` | 已輸出 branch-choice timecourse、return-traffic choice 與 curve error；仍需 digitized probability/time-course curve 做數值擬合 |
| Dussutour et al. 2004 / crowded traffic | pass | 高密度 crossings 較高，segment density/flow 上升，segment speed 未崩潰 | 缺 explicit antennal contacts、lane discipline、collision avoidance |
| John et al. 2009 / no jammed phase | pass | 高/低密度位移比 `0.6719`，segment flow `396.9503` > `154.181` | 已有 flow-density proxy；仍缺 digitized no-jam curve |
| Shiraishi et al. 2018 / diverse stochasticity | pass | diverse relocation ratio `2.2357` > low `0.7085` | 尚未重建文獻中的 environment-dependent optimum distribution |
| Malickova/Yates/Bodova 2015 / two-cue adaptation proxy | pass | relocation 有適應，washout 能清除 food pheromone | 不是該文 exact two-pheromone stochastic model，缺 synchronization metric |
| Kang & Theraulaz 2015 / task organization | pass | brood demand 下 `task_brood=249.667`；resource shortage 下 food/water tasks `132.333`；已輸出 task-switch rate | 缺可校準的 worker-worker contact matrix |
| Afek/Kecher/Sulamy 2015 / fail-stop foraging | pass | 大量死亡後 food trips 降低但非零，resilience ratio `0.5873` | 仍缺 algorithmic lower-bound 對照，不能作 proof-level validation |
| Jimenez-Romero et al. 2015 / negative pheromone | pass | avoid field 將 hazard occupancy ratio 降到 `0.8231`，且不永久阻斷覓食 | 仍不是該文 spiking-neural-controller implementation |
| Aswale et al. 2022 / misleading pheromone attack | pass | sustained fake trail 與 caution/avoid signal 產生可測 disruption/mitigation | 缺主動 attacker agents 與定量 effect-size 校準 |
| Jackson & Chaline 2007 / food quality recruitment | pass | counterbalanced 條件下平均採集品質 `1.334`，high-quality source pheromone `156.167` > low-quality `96.333` | 缺物種專屬蔗糖濃度校準與直接 trail-laying event counts |
| Avanzi, Lisart & Detrain 2024 / necrophoresis cleanup | pass | 巢區屍體由 `36.0` 降到 `0.333`，平均 disposed corpses `34.333` | 缺病原狀態、屍體年齡化學曲線與 colony interaction network 驗證 |
| Baudier et al. 2019 / brood microclimate | pass | heat-dry stress `1.8` > stable `0.0`；cold pupal brood chamber 比 cold larval 高 `1.5°C` | 缺 fitted metabolic heat budget、巢址幾何與物種專屬 brood survival curve |
| Army-ant trail-following / death spiral | pass | 平均 start ants `420.0`、final ants `104.0`、corpse fraction `0.7595`、death pheromone `15032.667` | 仍是定性 death-spiral/closed-loop trail failure；缺 raid fronts、living bridges、prey geometry 與 species energetics |
| Pratt et al. 2002 / nest relocation quorum | pass | high-quality site visits `73.973` > low-quality `0.0`，quorum/redeployment 完成 | 缺 tandem running、搬運軌跡、巢容積與 quorum threshold 實測校準 |

整體解讀：

- 目前可以作為「行為生態學概念模型」與「假說篩選工具」：費洛蒙路徑、雨水沖刷、擁擠下替代路徑、無硬堵塞、異質隨機性適應、任務重分配、食物品質招募、屍體移除、brood microclimate 與 nest relocation 都有初步定性支撐。
- 還不能作為「定量預測工具」：雙橋分支機率、個體轉角反應、交通速度-密度曲線、PDE 單位參數、文獻曲線 digitization 都未完成。
- 下一個最重要的科學改進不是增加更多 UI，而是用現有可校準資料做數值校準：branch choice probability curve fitting、body-contact/lane-discipline calibration、物種專屬參數範圍。
- v2 新增文獻指出兩個模型缺口：大量死亡後的覓食韌性偏弱；negative pheromone 目前只是局部排斥場，還不像雙費洛蒙模型中的可學習「禁止路徑」記憶。
- v3 新增文獻指出兩個模型缺口：tropotaxis 需要逐步感知/轉向 log；misleading pheromone 應改成 active detractor agents，而不是一次性靜態 fake trail。
- v4 新增食物品質模型與 necrophoresis cleanup 條件，讓 food quality / concentration 與 corpse-disposal 類文獻從 `not_covered` 轉為可測；但前者仍是品質倍率，不是特定物種的實測蔗糖濃度曲線，後者也還不是病原風險與互動網路的定量模型。
- v5 新增 brood microclimate、nest relocation/quorum、per-step trajectory/sensing log、segment flow-density、branch-choice timecourse、task-switch/contact metrics 與 misleading-trail avoid learning 的通用規則/量測。實驗腳本只能改參數、初始條件與環境狀態；個體決策、task/state transition、費洛蒙規則必須由同一套基礎模型產生，不能為單篇文獻注入例外行為。

## 11. Actual behavior-level biological simulation

`experiments/actual_biology_simulation.py` 是目前第一個「實際生物情境模擬」套件。它不是逐篇文獻審查，也不是為單篇論文寫特殊規則，而是在同一套通用螞蟻行為規則下，固定 seed 並改變初始資源與環境條件，輸出可重跑的時間序列。

執行方式：

```bash
python3 experiments/actual_biology_simulation.py \
  --output outputs/actual_biology_simulation.csv \
  --json-output outputs/actual_biology_simulation.json \
  --report-output outputs/actual_biology_simulation.md
```

目前 `v1` 條件：

| scenario | 生物問題 | 改變的條件 |
| --- | --- | --- |
| `stable_mature` | 成熟蟻群在穩定補給下是否能正常覓食並維持存活 | 中等巢內庫存、明確食物/水源、穩定溫濕度 |
| `resource_stress` | 低庫存與遠端有限資源是否造成覓食/能量壓力 | 低 food/water stores、遠端有限資源 |
| `heat_dry_stress` | 熱乾條件是否造成水分或 brood climate 壓力 | 40°C、20% humidity、有限巢內水分 |
| `founding_colony` | 創群階段是否以蟻后與 brood 為核心，而非一開始生成成熟工蟻群 | 只有蟻后與早期 brood，無初始 workers |

目前正式輸出：

- `outputs/actual_biology_simulation.csv`
- `outputs/actual_biology_simulation.json`
- `outputs/actual_biology_simulation.md`

`v1` 使用 seeds `101-105`、8 個模型日、每 0.25 日取樣。摘要如下：

| scenario | final ants | food trips | water trips | avg energy | avg hydration | brood stress | brood delta | queen health |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `stable_mature` | 430.2 | 68.4 | 43.6 | 88.2 | 92.0 | 0.10 | -7.0 | 100.0 |
| `resource_stress` | 428.8 | 41.6 | 35.2 | 86.2 | 87.2 | 0.14 | -7.4 | 100.0 |
| `heat_dry_stress` | 430.0 | 51.0 | 78.8 | 89.0 | 90.2 | 0.60 | -7.0 | 100.0 |
| `founding_colony` | 0.4 | 0.0 | 0.0 | 90.0 | 93.5 | 0.27 | 3.6 | 100.0 |

定性檢查結果：

- `stable_mature_foraging`: pass，成熟穩定組有 food/water trips。
- `stable_mature_survival`: pass，短期穩定環境沒有 worker collapse。
- `resource_pressure_response`: pass，資源壓力組的平均能量與水分低於穩定組。
- `heat_dry_hydration_stress`: pass，熱乾組 brood stress 明顯高於穩定組。
- `founding_queen_viability`: pass，創群組仍是 queen-centered，蟻后健康維持。

科學解讀：

- 這一套已經能產生「實際模擬實驗」的資料，而不只是 UI 展示或文獻分類。
- 它支持目前模型作為 behavior-level ABM 的研究輔助：可用於比較條件、產生時間序列、篩選假說。
- 它仍不能宣稱物種級定量預測：模型日尚未對應真實日齡，能量/水分是模型單位，brood development 與 queen fecundity 尚未用 Lasius niger 實測曲線校準。
- `founding_colony` 的 8 模型日結果只能看作 queen/brood viability smoke test；真正創群研究需要校準卵到幼蟲、蛹到工蟻的發育時間。

後續若要提高科學生物學參考價值，應把這個 suite 擴充為：

1. species-specific parameter set：先聚焦 Lasius niger，加入文獻範圍與單位。
2. digitized target curves：把 food trips、brood survival、trail decay、founding worker emergence 對照實驗曲線。
3. parameter sweep：只改參數與環境條件，檢查模型能否在同一規則下同時符合多個情境。
4. individual-level validation：抽樣輸出 worker trajectory、task switching、energy/hydration 分布，對照追蹤實驗。

## 12. Advanced parameter-sensitivity screen

`experiments/actual_biology_sensitivity.py` 是 actual biology suite 的進階版。它不是另寫行為規則，而是用 `antSim.setParam()` 對公開參數做 treatment，並在同一組生物情境下比較相對 baseline 的效應。

執行方式：

```bash
python3 experiments/actual_biology_sensitivity.py \
  --output outputs/actual_biology_sensitivity.csv \
  --effects-output outputs/actual_biology_sensitivity_effects.csv \
  --json-output outputs/actual_biology_sensitivity.json \
  --report-output outputs/actual_biology_sensitivity.md
```

目前正式輸出：

- `outputs/actual_biology_sensitivity.csv`
- `outputs/actual_biology_sensitivity_effects.csv`
- `outputs/actual_biology_sensitivity.json`
- `outputs/actual_biology_sensitivity.md`

`v1` 使用 seeds `101-103`、4 個模型日、每 0.25 日取樣，情境為 `stable_mature`、`resource_stress`、`heat_dry_stress`。

| treatment | 參數改變 | 生物學問題 |
| --- | --- | --- |
| `baseline` | 無 | 目前 behavior-level 預設 |
| `fast_pheromone_loss` | `evaporationRate=130`, `senseThreshold=16` | 較快氣味消退與較高感知門檻是否破壞路徑 |
| `persistent_pheromone` | `evaporationRate=55`, `senseThreshold=7` | 較持久/易感知氣味是否造成過度路徑承諾 |
| `calibrated_persistent_pheromone` | `evaporationRate=70`, `senseThreshold=8` | 第一輪文獻約束後的較溫和持久氣味候選 |
| `high_diffusion` | `diffusionRate=170` | 擴散較高是否改變梯度精度與採集 |
| `brood_demand_high` | `broodDemand=85` | 育幼需求是否改變覓食/育幼 tradeoff |

最大相對效應：

| treatment | scenario | food trips effect | hydration effect | brood stress effect | peak food pheromone effect |
| --- | --- | ---: | ---: | ---: | ---: |
| `persistent_pheromone` | `heat_dry_stress` | -0.221 | -0.026 | +0.175 | +0.686 |
| `persistent_pheromone` | `resource_stress` | -0.259 | -0.011 | +0.056 | +0.012 |
| `calibrated_persistent_pheromone` | `heat_dry_stress` | +0.151 | -0.015 | +0.062 | +0.599 |
| `calibrated_persistent_pheromone` | `resource_stress` | -0.027 | +0.034 | -0.065 | -0.230 |
| `high_diffusion` | `heat_dry_stress` | +0.244 | +0.004 | -0.048 | +0.140 |
| `brood_demand_high` | `heat_dry_stress` | -0.058 | 0.000 | -0.072 | -0.345 |

科學解讀：

- 目前模型對極端 `persistent_pheromone` 最敏感，尤其在熱乾與資源壓力下會降低 food trips，並提高或改變 brood stress / food pheromone peak。這暗示費洛蒙半衰期、感知閾值、氣味持久性是下一個最需要文獻校準的參數群。
- 第一輪文獻約束後的 `calibrated_persistent_pheromone` 把 P0 fail 清除：熱乾 food trips effect `+0.151`、brood stress effect `+0.062`；資源壓力 food trips effect `-0.027`。因此 `evaporationRate=70`、`senseThreshold=8` 暫列為較合理的模型單位候選範圍。
- `high_diffusion` 在熱乾條件下提高 food trips，表示擴散不只是視覺效果，會影響行為輸出；後續應把 diffusion/evaporation 從任意 UI 參數改成可報告的模型單位與合理範圍。
- `brood_demand_high` 的效應較小但方向可測，適合作為 nurse/forager tradeoff 的後續校準入口。
- 此 screen 只回答「模型對哪些參數敏感」，不回答「哪個參數是真實值」。下一步要用 digitized trail decay、food recruitment、brood survival 曲線做 parameter fitting。

## 13. Literature calibration cycle

`experiments/literature_calibration_cycle.py` 會讀取 `targets/literature_pheromone_constraints.json` 與 `outputs/actual_biology_sensitivity_effects.csv`，把文獻導向的 qualitative constraints 轉成自動 backlog。

目前使用的文獻依據：

| source | 用途 | URL |
| --- | --- | --- |
| Perna et al. 2012 | 個體對局部費洛蒙梯度的反應應是穩健規則，不應靠極端場參數才形成路徑 | https://arxiv.org/abs/1201.5827 |
| Malickova/Yates/Bodova 2015 | diffusion properties 會改變群體運動，因此 diffusion sensitivity 必須被記錄並設邊界 | https://arxiv.org/abs/1508.06816 |
| Amorim 2014 | 路徑形成與資源移除/採集效率耦合，持久費洛蒙不能阻止適應 | https://arxiv.org/abs/1402.5611 |

目前輸出：

- `outputs/literature_calibration_cycle.csv`
- `outputs/literature_calibration_cycle.json`
- `outputs/literature_calibration_cycle.md`

目前結果：

| 指標 | 數量 |
| --- | ---: |
| total constraints | 6 |
| pass | 6 |
| fail | 0 |
| missing | 0 |

解讀：目前第一層 qualitative literature constraints 已無剩餘 fail。下一層問題不是再調同一組 qualitative band，而是把文獻圖表 digitize 成數值曲線，建立真實的 `trail_decay_curve`、`recruitment_curve`、`branch_choice_curve`、`brood_survival_curve`。

## 14. Quantitative readiness for Level 4-5

`experiments/quantitative_readiness_audit.py` 會讀取 `targets/quantitative_curve_targets.json`，檢查目前是否有足夠的 digitized biological curves 進入 Level 4-5。

執行方式：

```bash
python3 experiments/quantitative_readiness_audit.py \
  --targets targets/quantitative_curve_targets.json \
  --csv-output outputs/quantitative_readiness_audit.csv \
  --json-output outputs/quantitative_readiness_audit.json \
  --report-output outputs/quantitative_readiness_audit.md
```

目前結果：

| 指標 | 數量 |
| --- | ---: |
| estimated current level | 3.0 |
| target curves | 6 |
| ready_for_fit | 0 |
| model_reference_only | 1 |
| qualitative_proxy_only | 1 |
| missing_digitized_data | 4 |
| open P0 targets | 4 |

目前 Level 4 blocker：

- `trail_decay_curve`: 缺 digitized trail decay / occupancy time series。
- `food_recruitment_strength_curve`: 缺食物品質/濃度對 recruitment 或 trail-laying 的數值曲線。
- `double_bridge_branch_choice_curve`: 目前只有 model reference，不是 raw biological counts。
- `brood_survival_microclimate_curve`: 缺溫濕度對 brood survival/development 的數值曲線。

結論：目前可稱為 Level 3 左右的定性/約束式研究輔助工具。往 Level 4 的下一個必要動作不是再增加 UI 或更多 qualitative probes，而是取得或 digitize 至少一條真實生物曲線，並保留另一條曲線作 independent validation。

## 15. 100+ paper triage corpus

`experiments/build_literature_corpus.py` 用 Crossref 查詢與既有 seed papers 建立 100+ 文獻候選池。輸出：

- `outputs/literature_corpus_100.json`
- `outputs/literature_corpus_100.csv`
- `outputs/literature_corpus_100.md`

目前 corpus 摘要：

| 指標 | 數量 |
| --- | ---: |
| deduplicated records | 120 |
| direct_or_near_term | 118 |
| needs_new_condition | 2 |
| pheromone_trail_foraging | 81 |
| computational_swarm_model | 70 |
| networks_interactions | 30 |
| task_allocation_division_labor | 25 |
| traffic_collective_motion | 22 |
| army_ant_raids_mills | 17 |
| food_quality_choice | 16 |
| nest_relocation_house_hunting | 8 |
| brood_nest_microclimate | 6 |
| misleading_negative_pheromone | 6 |
| necrophoresis_social_immunity | 2 |

解讀：

- 這是「測試候選池」，不是 120 篇都已經完成驗證。
- 文獻庫混合三類資料：真實螞蟻行為/生態實驗、ABM/PDE/數學模型、以及受螞蟻啟發的 swarm robotics / ACO 模型。後兩者可提供演算法與測試條件，但不能直接當作生物學真實度證據。
- 下一批最值得轉成自動測試的主題：nest relocation quorum、brood microclimate、corpse-age/pathogen necrophoresis calibration、active misleading pheromone detractor agents、逐步感知/轉向紀錄。

## 16. 120-paper sequential evaluation

`experiments/evaluate_literature_corpus.py` 逐篇讀取 `outputs/literature_corpus_100.json`，並把每一篇對應到目前 `outputs/paper_conditions_v5.json` 的 simulation evidence。輸出：

- `outputs/literature_corpus_120_evaluation.csv`
- `outputs/literature_corpus_120_evaluation.json`
- `outputs/literature_corpus_120_evaluation.md`

目前逐篇結果分成兩層解讀：`status` 是 simulator-condition 層級，`scientific_status` 是生物學驗證層級。

| 狀態 | 數量 | 解讀 |
| --- | ---: | --- |
| pass | 120 | 目前條件矩陣沒有失敗，但不代表 120 篇都已定量重現 |

範圍統計：

| scope | 數量 |
| --- | ---: |
| validated_family_condition | 69 |
| algorithmic_or_robotics_analogy | 34 |
| exact_paper_condition | 17 |

直接結論：目前 120 筆 corpus 全部通過「條件矩陣」，但不是「完美模擬」。新的嚴格欄位會把結果分成：exact qualitative、family qualitative proxy、model reference only、not biological target。只要缺 paper-specific digitized curve、物種參數或獨立 holdout validation，就會標成 `requires_followup=yes`。下一輪優先順序應是：

嚴格生物學分級：

| scientific_status | 數量 | 解讀 |
| --- | ---: | --- |
| family_qualitative_proxy | 69 | 通用規則覆蓋行為家族，但缺 paper-specific 數值 |
| not_biological_target | 34 | 工程/ACO/robotics 類比，不列入直接生物驗證 |
| model_reference_only | 9 | 數學/ABM/PDE 參考，缺原始生物曲線 |
| exact_qualitative_only | 8 | exact paper condition 定性通過，但缺數位化曲線 fit |

目前 `requires_followup=yes`: 86。

1. `branch_choice_curve_fitting`：digitize double-bridge branch-choice curves，校準 probability/time course。
2. `species_parameter_ranges`：把速度、感知半徑、費洛蒙半衰期、代謝/水分消耗轉成物種專屬範圍。
3. `body_contact_lane_discipline`：把現有 segment speed/flow/density 推進到可驗證的接觸與車道規則。
4. `necrophoresis_calibration`：在現有 corpse cleanup 基礎上加入 corpse-age chemistry、pathogen state、interaction network。
5. `brood_relocation_calibration`：把 brood microclimate 與 nest relocation 從定性 proxy 推進到物種專屬數值校準。

## 17. Gap backlog for later work

`experiments/generate_literature_gap_backlog.py` 會把逐篇評估中所有 `requires_followup=yes` 的文獻記錄成待辦清單。這比「非 pass」更嚴格，因為定性 family pass 與 exact qualitative pass 仍然不能宣稱完成 paper-level biological calibration。輸出：

- `outputs/literature_gap_backlog.csv`
- `outputs/literature_gap_backlog.json`
- `outputs/literature_gap_backlog.md`

目前 backlog 的解讀方式：

| 優先級 | 數量 | 用途 |
| --- | ---: | --- |
| P1_needs_quantitative_curve | 17 | exact/model reference 需要 digitized curve 或原始測量 |
| P2_family_proxy_needs_paper_data | 69 | 通用行為家族可對上，但缺 paper-specific data |
| total | 86 | 仍需後續處理的生物學/模型參考文獻 |

剩下工作不是讓矩陣 pass，而是把 exact qualitative / family qualitative proxy 逐步提高到 paper-specific quantitative calibration；演算法/機器人文獻則保留為靈感來源，不列入生物真實度。

後續改模型時，應先從 P0 做起；每補一個 condition，就重跑 `paper_conditions_probe.py`、`evaluate_literature_corpus.py`、`generate_literature_gap_backlog.py`，讓 backlog 數量逐步下降。

## 18. Digitized curve inventory

Level 4 需要至少一條 primary-source digitized biological curve，且另有一條獨立 validation curve。現在已加入 Perna et al. 2012 的 `individual_pheromone_response_curve` 作為第一條 fit-ready 曲線，來源是 Figure 5 圖說中的六個斜率值，x 軸由原文 pheromone-bin 範圍的幾何中點重建。`experiments/digitized_curve_inventory.py` 會檢查 `targets/digitized_curves/*.csv` 是否符合欄位、數值與來源要求。輸出：

- `outputs/digitized_curve_inventory.csv`
- `outputs/digitized_curve_inventory.json`
- `outputs/digitized_curve_inventory.md`

`targets/digitized_curves/source_leads.json` 只記錄候選來源，不可直接用於 fitting。若只找到二手摘要，必須標為 lead，不能填入 target value。這避免為了配合文獻而製造例外規則或虛假數值。

## 19. Individual response curve fit

`experiments/fit_individual_response_curve.py` 會對 Perna 2012 的個體費洛蒙反應曲線做 power-law fit。輸出：

- `outputs/individual_response_curve_fit.csv`
- `outputs/individual_response_curve_fit.json`
- `outputs/individual_response_curve_fit.md`

目前結果：

| 指標 | 值 |
| --- | ---: |
| status | pass |
| strict CI status | needs_review |
| fitted A | 35.9277 |
| fitted beta | 1.0338 |
| log-space R2 | 0.99763 |

解讀：這是第一條可用於共享 response submodel calibration 的 primary-source quantitative target。strict Figure 6 CI reproduction 仍需要原始 x/y 資料，但 rounded/bin-reconstructed target 已可作為 Level 4 的 fit target。

## 20. Independent traffic holdout

`experiments/validate_traffic_holdout.py` 使用 John et al. 2009 的 Figure 4 速度-密度資料作為獨立 holdout。這條曲線沒有用來調參，只用來檢查高密度交通是否沒有 jam collapse。輸出：

- `outputs/traffic_holdout_validation.csv`
- `outputs/traffic_holdout_validation.json`
- `outputs/traffic_holdout_validation.md`

目前結果：

| 指標 | 值 |
| --- | ---: |
| status | pass |
| target high/low velocity retention | 0.748 |
| model high/low velocity retention | 0.672 |

這使 readiness 從 Level 3.5 推進到 Level 4.0：已有一條 fit-ready primary-source response curve，也有一條獨立 holdout curve。下一階段不是宣稱「完整生物真實」，而是朝 Level 5 補 uncertainty、更多物種曲線、物理單位映射與外部資料驗證。

## 21. Level 5 uncertainty audit

`experiments/level5_uncertainty_audit.py` 會檢查 Level 4 曲線是否具有足夠 uncertainty 資訊。輸出：

- `outputs/level5_uncertainty_audit.csv`
- `outputs/level5_uncertainty_audit.json`
- `outputs/level5_uncertainty_audit.md`

目前結果：

| 指標 | 值 |
| --- | --- |
| estimated level | 4.4 |
| fit curve bootstrap CI | true |
| holdout curve present | true |
| holdout variance values | true |
| paper-condition replicate CI | true |
| independent pushing redirect holdout | true |
| holdout formal CI available | false |

解讀：Perna response fit 已有 bootstrap 95% CI，paper-condition probes 已有跨 seed bootstrap CI，Dussutour pushing/redirect probability 已有獨立數值 holdout；John traffic holdout 有 Figure 4 報告的 SD，但沒有 density-bin sample size 或 raw tracking data，因此不能計算正式 holdout CI。這是從 Level 4 往 Level 5 的實質進展，但還不能宣稱 Level 5。

## 22. Level 5 replicate statistics

`experiments/level5_replicate_statistics.py` 讀取 `outputs/paper_conditions_v5.json` 裡的 `raw_rows`，對每個文獻條件的核心指標計算跨 seed 統計：

- `n`
- mean
- sample SD
- SEM
- bootstrap 95% CI

輸出：

- `outputs/level5_replicate_statistics.csv`
- `outputs/level5_replicate_statistics.json`
- `outputs/level5_replicate_statistics.md`

目前結果：

| 指標 | 值 |
| --- | ---: |
| condition count | 27 |
| summary pass fraction | 1.0 |
| core metrics with bootstrap CI | 50 / 50 |
| minimum replicate count | 3 |

解讀：這把 paper-condition matrix 從「單次/平均觀察」推進到「可報告 stochastic replicate uncertainty」。它沒有改變任何螞蟻規則，也不把 qualitative pass 升格成 quantitative reproduction；Level 5 仍需要更多 primary-source digitized curves、文獻端 sample size/raw data、獨立 holdout 與物種單位映射。

## 23. Dussutour pushing/redirect holdout

`experiments/validate_pushing_redirect.py` 使用 Dussutour et al. 2004 Figure 3d 的 pushing probability 斜率 `J = 0.571 ± 0.057 CI95%` 作為 crowded-traffic mechanism holdout。模型端使用通用交通壓力規則輸出的 `traffic_redirect_per_encounter`，不是為該文獻特別注入狀態或任務。

輸出：

- `outputs/pushing_redirect_validation.csv`
- `outputs/pushing_redirect_validation.json`
- `outputs/pushing_redirect_validation.md`

目前結果：

| 指標 | 值 |
| --- | ---: |
| status | pass |
| target J | 0.571 |
| target 95% CI low | 0.514 |
| target 95% CI high | 0.628 |
| model mean redirect per encounter | 0.6122 |
| model 95% CI low | 0.595 |
| model 95% CI high | 0.6234 |
| model encounters | 28800 |

解讀：這是目前第二條獨立 traffic/contact 類 holdout，且比 John speed-retention 更接近微觀機制層。它支持模型的通用 frontal-encounter redirect rule，但仍不等於完整重現 Dussutour 的橋寬轉換、雙向 lane discipline 或完整接觸網路。
