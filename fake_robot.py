"""가짜 로봇: 실제 로봇 대신 0.1초마다 각도와 온도 값을 UDP로 보낸다."""
import socket
import json
import time
import math
import random

HOST = "127.0.0.1"   # 받는 쪽 주소 (127.0.0.1 = 내 PC 자신)
PORT = 5005          # 받는 쪽 번호 (받는 프로그램과 같아야 함)

# UDP 소켓 만들기 (데이터를 보내는 통로)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"가짜 로봇 시작: {HOST}:{PORT} 로 0.1초마다 전송 (멈추려면 Ctrl+C)")

t = 0.0
temp = 55.0
while True:
    # 각도: 0도 ~ 90도를 부드럽게 왕복 (로봇 팔이 흔들리는 흉내)
    angle = 45 + 45 * math.sin(t)

    # 온도: 조금씩 오르면서 살짝 흔들림, 70도를 넘으면 냉각됐다고 치고 55도로
    temp += 0.05 + random.uniform(-0.2, 0.25)
    if temp > 70:
        temp = 55.0

    data = {"time": round(t, 1), "angle": round(angle, 2), "temp": round(temp, 2)}

    # dict -> JSON 글자 -> 바이트로 바꿔서 전송
    sock.sendto(json.dumps(data).encode("utf-8"), (HOST, PORT))
    print(data)

    t += 0.1
    time.sleep(0.1)
