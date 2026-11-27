# python-study

Unity C# 개발자의 파이썬 학습 기록입니다.
로봇 데이터를 읽고, 분석하고, 시각화하는 프로그램을 강의 단위로 조금씩 키워 갑니다.

## 강의 목록

| 강 | 주제 | 파일 | 핵심 |
|---|---|---|---|
| 1 | 변수와 자료형 | `lesson1_variables.py` | 동적 타입, f-string, `/` `//` `%` |
| 2 | list, dict, 반복문 | `lesson2_list_dict.py` | 인덱싱, 슬라이싱, `dict.get`, `for` |
| 3 | 함수와 모듈 | `lesson3_functions.py` | `def`, 기본값 인자, 여러 값 반환, `import` |
| 4 | 파일과 예외 처리 | `lesson4_csv.py` | `with open`, `csv.DictReader`, `try / except` |
| 5 | 클래스 | `lesson5_class.py` | `__init__`, `self`, `__str__` |
| 6 | pandas, matplotlib | `lesson6_graph.py` | DataFrame, 조건 필터, NaN, 그래프 |
| 실습 | 실시간 시각화 | `fake_robot.py`, `live_graph.py` | UDP 소켓, JSON, 실시간 그래프 |

3~5강에서 만든 분석 함수와 클래스는 `robot_analysis.py`에 모여 있습니다.

## 실행 환경

- Python 3.15
- VS Code + Python 확장 (Microsoft)

```
python -m pip install pandas matplotlib
```

## 실행 방법

이 폴더를 VS Code에서 연 다음, 각 파일을 열고 `Ctrl + F5`로 실행합니다.

실시간 시각화 실습은 터미널 두 개가 필요합니다.

```
# 터미널 1 (받는 쪽 먼저)
python live_graph.py

# 터미널 2 (보내는 쪽)
python fake_robot.py
```

## 데이터

`robot_log.csv`는 로봇 한 대의 7초 동안의 로그입니다(시간, 관절 각도, 모터 온도).
5초 줄은 센서 값 누락을 흉내 내려고 온도 칸을 일부러 비워 두었습니다.

## C#과 다른 점 메모

- 블록은 중괄호 대신 들여쓰기, 문장 끝에 `;` 없음
- `/`는 항상 실수 나눗셈, 정수 몫은 `//`
- `return`이 없는 함수는 `None`을 돌려줌
- 메서드 첫 매개변수 `self`는 생략할 수 없음 (C#의 `this`)
- 변수는 값에 붙이는 이름표: `b = a`는 복사가 아니라 같은 객체를 가리킴
- `private`이 없고, `_이름`으로 내부용임을 표시하는 관례만 있음
