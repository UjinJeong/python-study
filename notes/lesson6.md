# 6강. pandas (판다스) 와 matplotlib (맷플롯립)

코드: [`lesson6_graph.py`](../lesson6_graph.py)

## 핵심

```
6강
├─ pip (핍) ─────────── 라이브러리 설치          ≈ NuGet, Unity Package Manager
├─ pandas (판다스) ───── 표 데이터 다루기
│   ├─ DataFrame (데이터프레임) ── 표 전체
│   ├─ df["temp"] ──── 열 꺼내기
│   ├─ mean (민), max (맥스) ── 계산
│   └─ df[조건] ────── 줄 거르기
└─ matplotlib (맷플롯립) ── 그래프 그리기
```

## 설치

```
python -m pip install pandas matplotlib
```

또는 `python -m pip install -r requirements.txt`

## DataFrame

```python
import pandas as pd
df = pd.read_csv("robot_log.csv")
```

```
   time  angle  temp
0     0   10.0  58.0
...
5     5   30.0   NaN     ← NaN (난): Not a Number, 값 없음
6     6   20.0  59.0
```

- 숫자 변환을 알아서 함
- 빈 칸은 NaN으로 두고 줄은 살림 (4강은 줄을 통째로 버렸음)

## 열 꺼내기와 계산

```
df["temp"]
├─ .mean()  (민) ──── 평균, NaN은 빼고 계산 → 61.0
├─ .max()   (맥스) ── 최대 → 65.0
├─ .min()   (민) ──── 최소 → 58.0
└─ .isna()  (이즈 엔에이) ── 칸마다 비었나 True/False
   └─ .sum() (섬) ── True=1 로 세서 빈 칸 개수
```

`mean`(평균)과 `min`(최소)은 읽는 소리가 같음.

## 조건으로 줄 거르기

```
df[ df["temp"] > 62 ]
    └─ ① 줄마다 62보다 큰지 True/False (NaN은 False)
└─ ② True인 줄만 남긴 새 표
```

## matplotlib

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"   # 한글 깨짐 방지
plt.rcParams["axes.unicode_minus"] = False

plt.plot(df["time"], df["temp"])   # 가로 값들, 세로 값들
plt.show()
```

```
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
│     │                       │  │   └─ sharex (셰어 엑스): 가로축 공유
│     │                       │  └─ 가로 1칸
│     │                       └─ 세로 2칸
│     └─ 나뉜 칸 두 개
└─ fig (피그): 창 전체

ax.plot(..., marker="o")      marker (마커): 점 모양
ax.axhline(62, linestyle="--")  axhline (액스 에이치 라인): 가로 기준선
ax.set_title / set_xlabel / set_ylabel   제목, 축 이름
plt.tight_layout()            tight layout (타이트 레이아웃): 간격 정리
```

- 그래프에서 5초 자리 선이 끊기면 정상 (NaN을 억지로 잇지 않음)
- 그래프 창을 닫아야 프로그램이 끝남

## 직접 만든 것 vs pandas

| 하는 일 | 1~5강 | pandas |
|---|---|---|
| CSV 읽기 | `load_log` | `pd.read_csv(...)` |
| 열 꺼내기 | `get_values` | `df["temp"]` |
| 평균, 최대 | `summary` | `.mean()`, `.max()` |
| 기준 넘은 줄 | `find_over` | `df[df["temp"] > 62]` |
| 빈 값 | 줄 통째로 버림 | NaN 표시, 줄 유지 |

## 확인 문제 (아직 안 풂)

```python
import pandas as pd
df = pd.read_csv("robot_log.csv")

print(len(df))
print(df["angle"].max())
print(len(df[df["angle"] > 30]))
print(df["temp"].isna().sum())
```

1. 먼저 실행하지 말고 예상해서 적기
2. `quiz.py`로 실행해서 맞춰 보기
3. 예상과 결과를 같이 기록하기
