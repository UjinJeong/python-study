"""로봇 로그 분석 도구 모음 (3강 함수, 4강 파일 읽기, 5강 클래스)"""
import csv


# ---------- 3강. 함수 ----------

def get_values(log, key):
    """로그에서 원하는 항목만 뽑아 list로 돌려준다."""
    values = []
    for row in log:
        values.append(row[key])
    return values


def average(values):
    return sum(values) / len(values)


def summary(values):
    """최소, 최대, 평균을 한 번에 돌려준다."""
    return min(values), max(values), average(values)


def find_over(log, key, limit=62):
    """기준을 넘은 시간(초) 목록을 돌려준다."""
    times = []
    for row in log:
        if row[key] > limit:
            times.append(row["time"])
    return times


# ---------- 4강. 파일 읽기와 예외 처리 ----------

def load_log(path):
    """CSV 파일을 읽어 숫자로 변환한 log(list of dict)를 돌려준다."""
    log = []
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                log.append({
                    "time": int(row["time"]),
                    "angle": float(row["angle"]),
                    "temp": float(row["temp"]),
                })
            except ValueError:
                print(f"건너뜀: {row}")
    return log


# ---------- 5강. 클래스 ----------

class RobotLog:
    """로봇 한 대의 로그 데이터와 분석 기능을 묶은 클래스"""

    def __init__(self, name, rows):
        self.name = name
        self.rows = rows

    def values(self, key):
        return get_values(self.rows, key)

    def stats(self, key):
        return summary(self.values(key))

    def times_over(self, key, limit):
        return find_over(self.rows, key, limit)

    def __str__(self):
        return f"RobotLog({self.name}, {len(self.rows)}줄)"
