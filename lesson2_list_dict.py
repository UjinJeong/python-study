"""2강. list, dict, 반복문 - 5초 동안의 로봇 로그 분석"""

# 시간마다 dict 하나, 그것들을 list로 묶은 로그
log = [
    {"time": 0, "angle": 10.0, "temp": 58},
    {"time": 1, "angle": 25.5, "temp": 60},
    {"time": 2, "angle": 40.0, "temp": 63},
    {"time": 3, "angle": 55.5, "temp": 65},
    {"time": 4, "angle": 45.0, "temp": 61},
]

limit = 62
total = 0
max_temp = log[0]["temp"]

for row in log:
    total += row["temp"]

    if row["temp"] > max_temp:
        max_temp = row["temp"]

    if row["temp"] > limit:
        print(f"{row['time']}초: 과열 {row['temp']}도")

avg = total / len(log)
print(f"평균 온도: {avg}도")
print(f"최고 온도: {max_temp}도")

# dict에서 안전하게 꺼내기: 없는 키면 기본값
robot = {"name": "ARM-01", "angle": 45.5}
print(robot.get("temp", 0))   # 0
print(robot.get("temp"))      # None
