# 2강. list, dict, 반복문

코드: [`lesson2_list_dict.py`](../lesson2_list_dict.py)

## 핵심

```
데이터 묶음
├─ list (리스트) ── 순서대로 줄 세우기   [58, 60, 63]     ≈ C# List<T>
├─ dict (딕트) ─── 이름으로 찾기         {"temp": 62}     ≈ C# Dictionary<K,V>
└─ for (포) ───── 하나씩 꺼내 보기       for t in temps:  ≈ C# foreach
```

## list (리스트)

```python
temps = [58, 60, 63, 65, 61]

temps[0]      # 58   첫 번째 (0부터)
temps[-1]     # 61   맨 뒤 ← C#에 없던 기능
temps[1:3]    # [60, 63]  1번부터 3번 "직전"까지 (슬라이싱)
len(temps)    # 5    개수 (C#의 .Count)
temps.append(59)   # 추가 (C#의 .Add)
```

## dict (딕트)

```python
robot = {"name": "ARM-01", "angle": 45.5, "temp": 62}

robot["name"]          # ARM-01
robot["temp"] = 64     # 값 바꾸기
robot["speed"] = 1.2   # 없는 키에 대입하면 새로 추가
```

### `[]` 와 `.get()` 의 차이

```
d.get("temp", 0)
├─ ① "temp" 칸이 있나?
│   ├─ 있으면 → 그 값
│   └─ 없으면 → ②
└─ ② 기본값 0
```

| 방법 | 키가 있을 때 | 키가 없을 때 |
|---|---|---|
| `d["temp"]` | 값 | KeyError (키 에러)로 멈춤 |
| `d.get("temp", 0)` | 값 | 기본값 0 |
| `d.get("temp")` | 값 | None |

- C#의 `GetValueOrDefault("temp", 0)`와 같음
- 센서 값이 빠질 수 있는 데이터에 유용
- 빈 값을 0으로 채우면 평균이 낮아지므로, 실무에서는 `None`으로 받고 `if temp is not None:`으로 거름
- `None` 비교는 `==` 대신 `is` (C#의 `!= null` → `is not None`)

## for (포) 반복문

```python
for t in temps:              # foreach (var t in temps)
    print(t)

for i in range(3):           # for (int i = 0; i < 3; i++)
    print(i)                 # 0, 1, 2

for i, t in enumerate(temps):    # 번호와 값을 같이
    print(f"{i}초: {t}도")
```

## 로그 데이터의 모양

로봇 로그는 "시간마다 dict 하나"를 list에 담은 모양.

```
log (list)
├─ [0] {"time": 0, "angle": 10.0, "temp": 58}
├─ [1] {"time": 1, "angle": 25.5, "temp": 60}
└─ ...
```

f-string 안에서 dict를 꺼낼 때는 `row['time']`처럼 작은따옴표 (바깥이 큰따옴표라서).

## 확인 문제와 결과

```python
nums = [10, 20, 30, 40, 50]
print(nums[-2])
print(nums[1:3])
print(len(nums[2:]))

d = {"angle": 30}
print(d.get("temp", 0))

count = 0
for n in nums:
    if n % 20 == 0:
        count += 1
print(count)
```

정답: `40` / `[20, 30]` / `3` / `0` / `2` — 결과: 5문제 중 3개 정답

| 줄 | 적은 답 | 정답 | 틀린 이유 |
|---|---|---|---|
| `len(nums[2:])` | 30 40 50 | 3 | 겹친 함수는 안쪽부터: 잘라낸 뒤 `len`이 개수를 셈 |
| `count` | 3 | 2 | `n % 20 == 0`은 20의 배수인지. 20, 40만 해당 |
