# 3강. 함수와 모듈

코드: [`lesson3_functions.py`](../lesson3_functions.py), [`robot_analysis.py`](../robot_analysis.py)

## 핵심

```
코드 정리하기
├─ 함수 def (데프) ── 작업 하나에 이름 붙이기      ≈ C# 메서드
│   ├─ 기본값 인자 ── 오버로딩 대신 씀
│   └─ 여러 값 반환 ── out 대신 씀
├─ 내장 함수 ── sum (섬), max (맥스), min (민), len (렌)
└─ 모듈 import (임포트) ── 다른 파일의 함수 가져오기
```

## def (데프)

`def`는 define (디파인, 정의하다)의 줄임. C#에서 반환 타입(`int`, `void`)이 있던 자리에 `def`를 씀.

```
def add(a, b):
│    │    │   └─ 콜론: 여기부터 함수 내용 (C#의 { )
│    │    └─ 매개변수, 타입 안 적음
│    └─ 함수 이름
└─ "함수를 만든다"는 표시

    return a + b      ← 들여쓰기된 줄이 함수 내용
```

```
함수
├─ 만들기 (정의) ── def add(a, b):   ← 레시피를 적어 두기만 함
└─ 쓰기 (호출) ──── add(2, 3)        ← 이때 실제로 실행
```

| C# | 파이썬 |
|---|---|
| `static double Average(List<int> v)` | `def average(v):` |
| 반환 타입을 적음 | 적지 않음 |
| `return` 없으면 `void` | `return` 없으면 `None`을 돌려줌 |
| 메서드는 반드시 클래스 안 | 파일 어디에나 단독으로 |

## 기본값 인자, 이름 붙여 넘기기

```python
def find_over(values, limit=62): ...

find_over(temps)             # limit = 62
find_over(temps, 70)
find_over(temps, limit=70)   # 이름 붙여 넘기기
```

C#의 선택적 매개변수, 명명된 인수와 같음. 파이썬에는 오버로딩이 없음.

## 여러 값 반환

```python
def summary(values):
    return min(values), max(values), average(values)

low, high, avg = summary(temps)   # 나눠 받기
```

쉼표로 묶어 돌려준 값은 실제로는 tuple (튜플) 하나.

```
├─ x, y = f(...)  나눠 받으면 → 각각 변수에
└─ print(f(...))  통째로 출력 → (2, 2) 처럼 괄호가 붙음
```

## 모듈

`.py` 파일 하나가 곧 모듈.

```python
import math
import robot_analysis as ra          # 별명 ra
from robot_analysis import average   # 함수 하나만
```

함수 바로 아래 `"""설명"""`은 docstring (독스트링). C#의 `/// <summary>`와 같은 역할.

## 확인 문제와 결과

```python
def f(a, b=10):
    return a * 2, a + b

x, y = f(3)
print(x, y)
print(f(1, b=1))

def g(n):
    n = n + 1

print(g(5))

nums = [3, 9, 4]
print(max(nums) - min(nums))
```

정답: `6 13` / `(2, 2)` / `None` / `6` — 결과: 4줄 중 2줄 정답, 1줄 절반

| 줄 | 적은 답 | 정답 | 틀린 이유 |
|---|---|---|---|
| `print(f(1, b=1))` | 2 2 | (2, 2) | 나눠 받지 않고 통째로 출력하면 tuple 모양 |
| `print(g(5))` | 6 | None | `return`이 없어서 안에서 만든 6은 사라지고 None 반환 |

"계산했는데 결과가 None이에요" 버그는 대부분 `return`을 빠뜨린 경우.
