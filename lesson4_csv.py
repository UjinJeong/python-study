"""4강. 파일 읽기와 예외 처리 - CSV 로그 파일 분석"""
import robot_analysis as ra

try:
    log = ra.load_log("robot_log.csv")

    temps = ra.get_values(log, "temp")
    low, high, avg = ra.summary(temps)
    print(f"읽은 줄: {len(log)}개")
    print(f"온도  최저 {low}  최고 {high}  평균 {avg}")
    print("과열 시간:", ra.find_over(log, "temp"))

except FileNotFoundError:
    print("robot_log.csv 파일을 찾을 수 없습니다.")
