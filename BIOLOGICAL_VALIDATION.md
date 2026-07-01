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

目前狀態：已部分相容，因為模型有 food/nest fields、diffusion/evaporation、左右/前方感知；但尚未輸出梯度感知與轉角資料。

下一步：新增 per-step sensing log，記錄 left/right/forward signal、turn angle、state，用於擬合 tropotaxis response function。

## 10. Paper-condition validation matrix

`experiments/paper_conditions_probe.py` 把多篇文獻轉成可重跑的 condition check。這不是「證明模型等於真實蟻群」，而是檢查目前規則是否能在指定條件下重現文獻中的定性方向，並標出還不能量化比對的缺口。

執行：

```bash
python3 experiments/paper_conditions_probe.py \
  --seeds 1-3 \
  --output outputs/paper_conditions_v3.csv \
  --json-output outputs/paper_conditions_v3.json \
  --report-output outputs/paper_conditions_report_v3.md
```

目前 `v3` 結果：

| 文獻 / 條件 | 狀態 | 觀測摘要 | 仍缺什麼 |
| --- | --- | --- | --- |
| Perna et al. 2012 / local pheromone trail | partial | 平均 `food_trips=44.333`、`food_pheromone=48872.333`，可形成 food trail | 尚未輸出左右感知濃度與轉角，不能擬合 Weber-law turning response |
| Ramirez et al. 2018 / tropotaxis | partial | 與 Perna 條件共享 trail formation metrics | 缺 local gradient vectors 與 per-step orientation change log |
| Amorim 2014 / trail formation and washout | pass | rain + food removal 後 `food_pheromone_ratio=0.0` | 仍是 ABM heuristic field，不是 PDE 參數單位 |
| Deneubourg/Goss/Beckers double bridge | partial | upper bias 只在 `0.333` runs 被選中，平均 dominance `0.0746` | 正回饋/橋幾何尚未貼近經典 branch-choice probability curve |
| Dussutour et al. 2004 / crowded traffic | pass | 高密度 crossings 較高，dominance 低於低密度 | 缺 explicit antennal contacts、lane discipline、collision avoidance |
| John et al. 2009 / no jammed phase | pass | 高/低密度位移比 `0.6531`，未硬性停滯 | 目前只是 displacement proxy，尚未量 flow-density/velocity curve |
| Shiraishi et al. 2018 / diverse stochasticity | pass | diverse `trips_vs_initial=0.4655` 高於 low `0.362` | 尚未重建文獻中的 environment-dependent optimum distribution |
| Malickova/Yates/Bodova 2015 / two-cue adaptation proxy | pass | relocation + washout 均能維持方向性適應 | 不是該文 exact two-pheromone stochastic model，缺 synchronization metric |
| Kang & Theraulaz 2015 / task organization | pass | brood demand 下 `task_brood=243.0`；resource shortage 下 food/water tasks `241.667` | 缺 worker-worker contact matrix 與 explicit task-switching rates |
| Afek/Kecher/Sulamy 2015 / fail-stop foraging | partial | 大量死亡後 food trips 仍非零，但 resilience ratio 只有 `0.1471` | 缺韌性搜尋策略、存活 forager reallocation、algorithmic lower-bound 對照 |
| Jimenez-Romero et al. 2015 / negative pheromone | partial | avoid field 將 hazard occupancy ratio 降到 `0.8897`，但效果弱 | 缺個體學習、短/長效雙費洛蒙分工、明確 forbidden-path 記憶 |
| Aswale et al. 2022 / misleading pheromone attack | partial | fake trail 沒有降低 food trips；caution 只讓 fake-path occupancy 小幅下降 | 缺主動 detractor agents；目前 static fake trail 不是文獻攻擊模型 |

整體解讀：

- 目前可以作為「行為生態學概念模型」與「假說篩選工具」：費洛蒙路徑、雨水沖刷、擁擠下替代路徑、無硬堵塞、異質隨機性適應都有初步定性支撐。
- 還不能作為「定量預測工具」：雙橋分支機率、個體轉角反應、交通速度-密度曲線、PDE 單位參數、文獻曲線 digitization 都未完成。
- 下一個最重要的科學改進不是增加更多 UI，而是增加可校準資料輸出：per-step sensing/turning log、trail-segment crossing log、flow-density log、branch choice probability curve fitting。
- v2 新增文獻指出兩個模型缺口：大量死亡後的覓食韌性偏弱；negative pheromone 目前只是局部排斥場，還不像雙費洛蒙模型中的可學習「禁止路徑」記憶。
- v3 新增文獻指出兩個模型缺口：tropotaxis 需要逐步感知/轉向 log；misleading pheromone 應改成 active detractor agents，而不是一次性靜態 fake trail。

## 11. 100+ paper triage corpus

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
- 下一批最值得轉成自動測試的主題：food quality vs. trail strength、nest relocation quorum、brood microclimate、corpse cleanup latency、active misleading pheromone detractor agents。

## 12. 120-paper sequential evaluation

`experiments/evaluate_literature_corpus.py` 逐篇讀取 `outputs/literature_corpus_100.json`，並把每一篇對應到目前 `outputs/paper_conditions_v3.json` 的 simulation evidence。輸出：

- `outputs/literature_corpus_120_evaluation.csv`
- `outputs/literature_corpus_120_evaluation.json`
- `outputs/literature_corpus_120_evaluation.md`

目前逐篇結果：

| 狀態 | 數量 | 解讀 |
| --- | ---: | --- |
| pass | 7 | 有 exact paper-condition，且目前定性方向符合 |
| partial | 56 | 有 exact condition 或 category proxy，但缺 paper-specific 數據/機制 |
| not_covered | 25 | 目前驗證套件或模型缺必要條件 |
| not_biological_target | 32 | 主要是 robotics / ACO / 工程類比，不應作為直接生物學驗證 |

範圍統計：

| scope | 數量 |
| --- | ---: |
| category_proxy | 74 |
| algorithmic_or_robotics_analogy | 32 |
| exact_paper_condition | 12 |
| unmapped | 2 |

直接結論：目前不能說 120 篇都能正確模擬。較嚴格地說，只有少數 exact condition 達到定性通過；大多數仍需轉成更精確的 simulation condition，或先補模型機制。下一輪優先順序應是：

1. `food_quality_needed`：加入食物品質/濃度/距離收益，測 food quality vs. trail strength。
2. `brood_microclimate_needed`：建立育幼微氣候 condition，測溫濕度與 brood survival proxy。
3. `corpse_cleanup_needed`：建立 necrophoresis latency / corpse disposal curve。
4. `nest_relocation_needed`：建立 nest-site quorum / relocation condition。
5. `active_misleading_pheromone`：把 static fake trail 改成 active detractor agents。

## 13. Gap backlog for later work

`experiments/generate_literature_gap_backlog.py` 會把逐篇評估中所有非 `pass` 文獻記錄成待辦清單。輸出：

- `outputs/literature_gap_backlog.csv`
- `outputs/literature_gap_backlog.json`
- `outputs/literature_gap_backlog.md`

目前 backlog：

| 優先級 | 數量 | 用途 |
| --- | ---: | --- |
| P0_missing_biology_condition | 25 | 生物學相關，但目前模型/測試條件不足，優先補 |
| P1_exact_condition_partial | 5 | 已有 exact paper condition，但仍缺關鍵量測或機制 |
| P2_proxy_only | 51 | 只有泛化 proxy，需逐篇轉成專用 condition |
| P3_algorithmic_reference_only | 32 | robotics / ACO / 工程類比，只作靈感或演算法參考 |
| total | 113 | 所有尚未 fully simulated 的文獻 |

目前 P0 的主要工作群：

- food quality / concentration / distance reward model。
- brood microclimate validation。
- necrophoresis latency and corpse disposal curves。
- nest relocation / quorum decision conditions。
- active misleading pheromone detractor agents。

後續改模型時，應先從 P0 做起；每補一個 condition，就重跑 `paper_conditions_probe.py`、`evaluate_literature_corpus.py`、`generate_literature_gap_backlog.py`，讓 backlog 數量逐步下降。
