# 진도표

마지막 업데이트: 2026-11-27

## 현재 위치

**6강 확인 문제 풀기** → 실시간 그래프 실행 확인 → 다음 단계(A 또는 B) 고르기

## 강의별 진행

| 강 | 주제 | 상태 | 확인 문제 | 노트 |
|---|---|---|---|---|
| 1 | 변수와 자료형 | 완료 | 1/4 | [notes/lesson1.md](notes/lesson1.md) |
| 2 | list, dict, 반복문 | 완료 | 3/5 | [notes/lesson2.md](notes/lesson2.md) |
| 3 | 함수와 모듈 | 완료 | 2/4 (+1 절반) | [notes/lesson3.md](notes/lesson3.md) |
| 4 | 파일과 예외 처리 | 완료 | 4/5 | [notes/lesson4.md](notes/lesson4.md) |
| 5 | 클래스 | 완료 | 0/4 → 재확인 2/2 | [notes/lesson5.md](notes/lesson5.md) |
| 6 | pandas, matplotlib | 진행 중 | 미응시 | [notes/lesson6.md](notes/lesson6.md) |
| 실습 | 실시간 시각화 1단계 | 코드 완성, 실행 확인 전 | - | [notes/live-practice.md](notes/live-practice.md) |
| 7 | 3D 시각화 | 예정 | - | - |

## 다음에 할 일

- [ ] 6강 확인 문제: 예상 답 적기 → `quiz.py`로 실행해서 비교
- [ ] 실시간 그래프 실행 (`live_graph.py` 먼저, 그다음 `fake_robot.py`)
- [ ] 다음 단계 고르기
  - A. 스마트폰 센서 (phyphox 앱)로 진짜 데이터 받기
  - B. 7강: Unity로 3D 시각화 (파이썬 → UDP → Unity 로봇 팔)

## 자주 틀린 부분 (복습용)

- `/`는 항상 실수, 정수 몫은 `//` (1강)
- 겹친 함수는 안쪽부터 계산: `len(nums[2:])` (2강)
- `return`이 없으면 `None` (3강)
- `float`가 섞이면 결과도 실수, 파이썬은 `8.0`으로 출력 (4강)
- `self.필드`는 객체마다 따로, `c = a`는 같은 객체 (5강)

## 환경

- Windows, VS Code + Python 확장 (Microsoft)
- Python 3.15 (Python install manager로 설치)
- pandas 3.1.1, matplotlib 3.11.2
