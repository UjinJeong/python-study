import pandas as pd
import matplotlib.pyplot as plt

# 한글 깨짐 방지 (Windows)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 1. 읽기
df = pd.read_csv("robot_log.csv")
print(df)

# 2. 분석
print(f"평균 온도: {df['temp'].mean()}")
print(f"최고 온도: {df['temp'].max()}")
print(f"온도 빈 칸: {df['temp'].isna().sum()}개")
print("과열 구간:")
print(df[df["temp"] > 62])

# 3. 그래프 (위: 각도, 아래: 온도)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(df["time"], df["angle"], marker="o")
ax1.set_ylabel("각도 (도)")
ax1.set_title("ARM-01 로그")

ax2.plot(df["time"], df["temp"], marker="o", color="tab:red")
ax2.axhline(62, linestyle="--", color="gray")
ax2.set_ylabel("온도 (도)")
ax2.set_xlabel("시간 (초)")

plt.tight_layout()
plt.show()
