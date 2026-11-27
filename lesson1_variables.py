"""1강. 변수와 자료형 - 로봇 상태 값 하나 다루기"""

# 로봇 상태 값 (타입을 적지 않아도 값에 따라 정해짐)
robot_name = "ARM-01"   # str
joint_angle = 45.5      # float, 관절 각도 (도)
motor_temp = 62         # int, 모터 온도 (도)
is_running = True       # bool

# 출력 (C#의 $"..." 대신 f"...")
print(f"로봇: {robot_name}")
print(f"관절 각도: {joint_angle}도")
print(f"모터 온도: {motor_temp}도")
print(type(joint_angle))

# 판단
limit = 60
is_overheated = motor_temp > limit
print(f"과열 여부: {is_overheated}")

# 나눗셈 기호 정리
print(7 / 2)    # 3.5  항상 실수 나눗셈
print(7 // 2)   # 3    몫 (C#의 정수 나눗셈)
print(7 % 2)    # 1    나머지
