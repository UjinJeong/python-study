"""5강. 클래스 - 로봇 로그를 객체로 묶기"""
import robot_analysis as ra

try:
    rows = ra.load_log("robot_log.csv")
    arm = ra.RobotLog("ARM-01", rows)   # 객체 생성 -> __init__ 자동 호출

    print(arm)                           # __str__ 자동 호출
    low, high, avg = arm.stats("temp")
    print(f"온도  최저 {low}  최고 {high}  평균 {avg}")
    print("과열 시간:", arm.times_over("temp", 62))
    print("각도 50도 초과:", arm.times_over("angle", 50))

except FileNotFoundError:
    print("robot_log.csv 파일을 찾을 수 없습니다.")
