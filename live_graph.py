"""받는 쪽: UDP로 들어오는 로봇 데이터를 받아 실시간 그래프로 그린다."""
import socket
import json
from collections import deque

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 한글 깨짐 방지 (Windows)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

PORT = 5005          # 보내는 쪽과 같은 번호
LIMIT = 62           # 과열 기준 온도
MAX_POINTS = 100     # 화면에 남길 점 개수 (0.1초 x 100 = 최근 10초)

# UDP 소켓: 5005번으로 들어오는 데이터를 받겠다고 등록
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", PORT))
sock.setblocking(False)   # 데이터가 없으면 기다리지 말고 바로 넘어가기

# 최근 값만 담는 list (꽉 차면 가장 오래된 값이 자동으로 빠짐)
times = deque(maxlen=MAX_POINTS)
angles = deque(maxlen=MAX_POINTS)
temps = deque(maxlen=MAX_POINTS)

# 그래프 틀 만들기 (위: 각도, 아래: 온도)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
line1, = ax1.plot([], [], marker=".")
line2, = ax2.plot([], [], marker=".", color="tab:red")
ax2.axhline(LIMIT, linestyle="--", color="gray")

ax1.set_ylabel("각도 (도)")
ax1.set_ylim(-5, 95)
ax2.set_ylabel("온도 (도)")
ax2.set_ylim(50, 75)
ax2.set_xlabel("시간 (초)")
title = ax1.set_title("데이터 기다리는 중...")


def update(frame):
    """0.1초마다 불린다: 새 데이터를 꺼내 그래프를 다시 그린다."""
    # 그사이 도착한 데이터를 전부 꺼냄
    while True:
        try:
            packet, _ = sock.recvfrom(1024)
        except BlockingIOError:
            break   # 더 꺼낼 데이터가 없음
        data = json.loads(packet.decode("utf-8"))
        times.append(data["time"])
        angles.append(data["angle"])
        temps.append(data["temp"])

    if times:
        line1.set_data(times, angles)
        line2.set_data(times, temps)
        ax1.set_xlim(times[0], times[0] + MAX_POINTS * 0.1)

        now = temps[-1]
        state = "과열!" if now > LIMIT else "정상"
        title.set_text(f"실시간 로봇 데이터  |  현재 온도 {now:.1f}도 ({state})")

    return line1, line2, title


ani = FuncAnimation(fig, update, interval=100, cache_frame_data=False)
plt.tight_layout()
plt.show()
