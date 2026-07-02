# Parameter Provenance

本表追蹤目前模型參數的來源等級。正式研究使用前，每個低可信度參數都應替換為文獻值、實驗估計值或明確的 sensitivity-analysis 範圍。

## Confidence Scale

- `A`: 直接文獻量測值，含單位與物種。
- `B`: 文獻推導或同屬/近似物種估計。
- `C`: 行為級合理假設，已做 sensitivity analysis。
- `D`: 原型 placeholder，尚未校準。

## Current Parameters

| Parameter | Meaning | Current Unit | Current Source | Confidence | Needed Upgrade |
|---|---|---|---|---:|---|
| `diffusionRate` | 費洛蒙擴散倍率 | UI percent | sensitivity range + qualitative literature constraints | C/D | 對應半衰期/擴散係數與 digitized trail curves |
| `evaporationRate` | 費洛蒙蒸發倍率 | UI percent | sensitivity range + qualitative literature constraints | C/D | 對應 trail decay data |
| `senseThreshold` | 最小可感知費洛蒙總量 | grid value | sensitivity range + qualitative literature constraints | C/D | 對應行為反應閾值 |
| `pheromoneStrength` | 個體沉積費洛蒙強度 | model value | 模型假設 | D | 對應成功覓食後沉積強度 |
| `ant.speed` | 個體移動速度 | model unit / dt | species multiplier + random | D | 對應 mm/s 或 cm/s |
| `energy` | 內部能量狀態 | percent-like | 行為控制變數 | D | 建立行為成本函式 |
| `hydration` | 內部水分狀態 | percent-like | 行為控制變數 | D | 建立溫濕度水分流失模型 |
| `eggInterval` | 蟻后產卵間隔 | model dt | 模型調校 | D | 對應物種產卵率 |
| `broodRate` | 卵/幼蟲/蛹發育倍率 | multiplier | 模型假設 | D | 對應發育天數 |
| `broodTemp` | 育幼室偏好溫度 | Celsius | species profile assumption | C/D | 文獻或實驗來源 |
| `broodHumidity` | 育幼室偏好濕度 | percent RH | species profile assumption | C/D | 文獻或實驗來源 |
| `soldierRatioDefault` | 兵蟻比例 | percent | species profile assumption | D | species-specific caste ratio |
| `millSusceptibility` | 死亡漩渦敏感度 | multiplier | 行為展示假設 | D | 軍蟻/行軍蟻實驗或移除 |
| `death chemical` | 屍體化學線索 | model value | necrophoresis 現象抽象 | C/D | 加入 time-since-death chemical profile |

## Interpretation Rules

1. `D` 級參數不得用來做絕對生物結論。
2. `C/D` 可用於探索相對趨勢，但必須報告 sensitivity range。
3. 發表前至少核心 validation case 的主要參數應提升到 `B` 或 `C`。
4. 多物種比較只有在 species profile 主要參數達 `B` 以上時才有生物學意義。

## Current Calibration Notes

- `diffusionRate`、`evaporationRate`、`senseThreshold` 已從純 placeholder 提升到 `C/D`：`actual_biology_sensitivity.py` 會做多情境 sensitivity screen，`literature_calibration_cycle.py` 會檢查 literature-guided qualitative constraints。
- 目前合格的 persistent-trail candidate 是 `evaporationRate=70`、`senseThreshold=8`；更極端的 `evaporationRate=55`、`senseThreshold=7` 仍保留為壓力測試，不列為合理校準範圍。
- `C/D` 的意思是：方向性與穩健性已有自動檢查，但仍沒有真實物理單位、半衰期或 species-specific concentration threshold。
