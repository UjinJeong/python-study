# 4강. 파일 읽기와 예외 처리

코드: [`lesson4_csv.py`](../lesson4_csv.py), [`robot_analysis.py`](../robot_analysis.py) 의 `load_log`

## 핵심

```
파일에서 데이터 가져오기
├─ with open() (위드 오픈) ── 파일 열고 자동으로 닫기       ≈ C# using
├─ csv (씨에스브이) 모듈 ── 한 줄을 dict 하나로 바꿔 줌
├─ 형 변환 ── 파일에서 읽은 값은 전부 문자열
└─ try / except (트라이 / 익셉트) ── 에러가 나도 멈추지 않기   ≈ C# try / catch
```

## CSV 파일

쉼표로 값을 나눈 평범한 텍스트 파일. 확장자만 `.csv`.

- VS Code: 새 파일 → 이름 `robot_log.csv` → 붙여 넣고 저장 (가장 간단)
- 메모장: 저장할 때 형식을 "모든 파일"로 (아니면 `.csv.txt`가 됨)
- 엑셀: "CSV UTF-8(쉼표로 분리)"로 저장 (한글 깨짐 방지)

## with open()

```python
with open("robot_log.csv", encoding="utf-8") as file:
    text = file.read()
```

```
with open("파일이름", encoding="utf-8") as file:
│    │                 │                  └─ 열린 파일의 이름표
│    │                 └─ 한글 안 깨지게
│    └─ 파일 열기 (기본은 읽기, 쓰기는 "w")
└─ 블록이 끝나면 자동으로 닫음
```

## csv.DictReader (딕트 리더)

```
robot_log.csv               DictReader 결과
time,angle,temp      →     (첫 줄은 키 이름)
0,10.0,58            →     {'time': '0', 'angle': '10.0', 'temp': '58'}
```

값이 전부 문자열이라 `int()`, `float()`로 바꿔야 계산 가능.

## try / except

```
try 블록 실행
├─ 에러 없음 → except 건너뜀
└─ 에러 발생 → 그 줄에서 멈추고 except로 이동
              → except가 끝나면 그 아래 코드 계속
```

| 에러 | 언제 | C#에서 비슷한 것 |
|---|---|---|
| `FileNotFoundError` (파일 낫 파운드 에러) | 파일 없음 | `FileNotFoundException` |
| `ValueError` (밸류 에러) | `float("abc")` 변환 불가 | `FormatException` |
| `KeyError` (키 에러) | dict에 없는 키를 `[]`로 | `KeyNotFoundException` |
| `IndexError` (인덱스 에러) | list 범위 밖 | `ArgumentOutOfRangeException` |

## 데이터에서 일어난 일

5초 줄은 온도가 비어 있어서 `float('')`에서 ValueError → 그 줄 전체를 건너뜀.
(6강의 pandas는 줄을 살리고 빈 칸만 NaN으로 표시)

## 확인 문제와 결과

```python
try:
    x = int("12a")
    print("A")
except ValueError:
    print("B")
print("C")

def safe_float(text):
    try:
        return float(text)
    except ValueError:
        return None

print(safe_float("45.5"))
print(safe_float(""))
print(safe_float("7") + 1)
```

정답: `B` / `C` / `45.5` / `None` / `8.0` — 결과: 5줄 중 4줄 정답

| 줄 | 적은 답 | 정답 | 틀린 이유 |
|---|---|---|---|
| 마지막 | 8 | 8.0 | `float("7")`은 7.0, 실수 + 정수 = 실수. C#은 8.0을 `8`로 출력하지만 파이썬은 `8.0` |
