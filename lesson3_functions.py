"""3강. 함수와 모듈 - 분석 기능을 robot_analysis.py 로 분리"""
import robot_analysis as ra

log = [
    {"time": 0, "angle": 10.0, "temp": 58},
    {"time": 1, "angle": 25.5, "temp": 60},
    {"time": 2, "angle": 40.0, "temp": 63},
    {"time": 3, "angle": 55.5, "temp": 65},
    {"time": 4, "angle": 45.0, "temp": 61},
]

temps = ra.get_values(log, "temp")
low, high, avg = ra.summary(temps)   # 값 여러 개 나눠 받기
print(f"온도  최저 {low}  최고 {high}  평균 {avg}")

print("과열 시간:", ra.find_over(log, "temp"))
print("각도 50도 초과:", ra.find_over(log, "angle", limit=50))
