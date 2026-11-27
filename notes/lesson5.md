# 5강. 클래스

코드: [`lesson5_class.py`](../lesson5_class.py), [`robot_analysis.py`](../robot_analysis.py) 의 `RobotLog`

## 핵심

```
클래스 (C#과 다른 점 위주)
├─ __init__ (던더 이닛) ── 생성자
├─ self (셀프) ──── 자기 자신, 반드시 적음        ≈ C# this
├─ 필드 ──── self.x = 값 으로 그 자리에서 생성 (따로 선언 안 함)
├─ 접근 제한 ─ private 없음, _이름 으로 표시만
└─ __str__ (던더 에스티알) ── 출력 모양 정하기   ≈ C# ToString()
```

던더 = double underscore (더블 언더스코어), 밑줄 두 개.

## 비유: 계수기 공장

```
class Counter  =  계수기 설계도 (종이 한 장, 기계는 아직 없음)
│
├─ Counter()     → 계수기 1대 생산 (숫자 0부터)
├─ Counter(10)   → 계수기 1대 더 생산 (숫자 10부터)
│                   두 기계는 완전히 별개
├─ a = ...       → 기계에 "a" 스티커 붙이기
├─ c = a         → 새 기계 X, a가 붙은 그 기계에 "c" 스티커 추가
├─ a.add(5)      → "a" 스티커 붙은 기계의 버튼을 누르기
└─ self          → 버튼이 눌린 "바로 그 기계"
```

## 꼭 기억할 세 가지

```
1. Counter( ) 를 부른 횟수 = 기계 대수, 숫자도 각자 따로 (static 아님)
2. 변수는 기계를 가리키는 스티커: c = a → 같은 기계에 스티커 2장
3. 화면에 안 나와도 메서드는 실행된 것: a.add() → 출력 없어도 숫자 올라감
```

## Robot("ARM-01") 한 줄 안에서 일어나는 일

```
Robot("ARM-01")
├─ ① 빈 Robot 객체 생성
├─ ② 파이썬이 자동으로 __init__ 호출
│      def __init__(self,  name):
│                   │      └─ 괄호 안에 넣은 "ARM-01"
│                   └─ ①의 빈 객체 (파이썬이 채움)
├─ ③ self.name = name 등 실행 → 필드 생김
└─ ④ 다 채워진 객체를 돌려줌
```

| 하는 일 | C# | 파이썬 |
|---|---|---|
| 객체 만들기 | `new Robot("ARM-01")` | `Robot("ARM-01")` |
| 자동으로 불리는 것 | 생성자 | `__init__` |
| 만들어진 객체 | `this` (숨어 있음) | `self` (매개변수로 드러남) |

## self 를 매번 적는 이유

```
arm.rotate(30)
  │        └──────▶ amount = 30
  └───────────────▶ self = arm   (자동으로 넣어 줌)

def rotate(self, amount):
```

메서드 안에서 필드는 반드시 `self.angle`. `self.`을 빼면 지역 변수가 됨.

## print(객체) 와 __str__

```
print(b)
├─ b는 객체라서 글자가 아님
├─ 파이썬이 자동으로 b.__str__() 호출
└─ 돌려받은 글자를 출력 → Counter=10
```

- `print(b.count)` → 숫자만 `10`
- `print(b)` → `__str__`이 정한 모양 `Counter=10`
- `__str__`이 없으면 `<__main__.Counter object at 0x...>`

## 상속

```python
class ArmRobot(Robot):              # C#의 class ArmRobot : Robot
    def __init__(self, name, joints):
        super().__init__(name)      # C#의 : base(name)
        self.joints = joints
```

## 확인 문제와 결과

### 1차: Counter

```python
class Counter:
    def __init__(self, start=0):
        self.count = start
    def add(self, n=1):
        self.count += n
        return self.count
    def __str__(self):
        return f"Counter={self.count}"

a = Counter()
b = Counter(10)
a.add()
print(a.add(5))
print(b.count)
c = a
c.add()
print(a.count)
print(b)
```

정답: `6` / `10` / `7` / `Counter=10` — 결과: 4줄 모두 오답 (적은 답: 15, 11, 15, 12)

원인: a와 b가 count 하나를 같이 쓴다고 생각함 (static처럼). `self.count`는 객체마다 따로.

| 코드 | 객체 A | 객체 B | 출력 |
|---|---|---|---|
| `a = Counter()` | 0 | - | |
| `b = Counter(10)` | 0 | 10 | |
| `a.add()` | 1 | 10 | (없음) |
| `print(a.add(5))` | 6 | 10 | 6 |
| `print(b.count)` | 6 | 10 | 10 |
| `c = a` | 6 | 10 | (c도 A를 가리킴) |
| `c.add()` | 7 | 10 | (없음) |
| `print(a.count)` | 7 | 10 | 7 |
| `print(b)` | 7 | 10 | Counter=10 |

### 2차: Box (다시 확인)

```python
x = Box(1)
y = Box(2)
z = x
z.v = 100
print(x.v, y.v)
print(y)
```

정답: `100 2` / `Box=2` — 결과: 2줄 모두 정답 (이해 완료)
