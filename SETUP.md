# 새 PC에서 이어서 하기

```
① 파이썬 설치 → ② VS Code 확장 → ③ 저장소 받기 → ④ 라이브러리 설치 → ⑤ 실행 확인
```

## ① 파이썬 설치

1. https://www.python.org/downloads/windows/ 에서 설치
2. 일반 설치 파일(Windows installer)을 쓰면 첫 화면에서 **Add python.exe to PATH** 체크 후 Install Now
3. VS Code를 껐다 켜고 터미널에서 확인

```
python --version
```

`Python was not found`가 나오면: Windows 설정 > 앱 > 고급 앱 설정 > 앱 실행 별칭 에서
`python.exe`, `python3.exe` 두 개를 끄고 VS Code를 다시 켠다.

## ② VS Code 확장

확장 탭(Ctrl + Shift + X)에서 `Python` 검색 → Microsoft 제작 설치
(Pylance, Python Debugger가 같이 설치됨)

## ③ 저장소 받기

Fork 사용 시: File > Clone → `https://github.com/UjinJeong/python-study.git`

터미널 사용 시:

```
git clone https://github.com/UjinJeong/python-study.git
```

VS Code에서 **파일 > 폴더 열기**로 받은 `python-study` 폴더를 연다.

## ④ 라이브러리 설치

VS Code 터미널(터미널 > 새 터미널)에서:

```
python -m pip install -r requirements.txt
```

마지막에 `Successfully installed`가 나오면 완료. 노란 WARNING, `[notice]`는 무시해도 된다.

## ⑤ 실행 확인

`lesson6_graph.py`를 열고 Ctrl + F5 → 처음이면 Python Debugger → Python File 선택.
그래프 창이 뜨면 준비 완료.

| 메시지 | 해결 |
|---|---|
| 디버거 선택에 Python이 없음 | ② 확장 설치 |
| `ModuleNotFoundError: No module named 'pandas'` | Ctrl+Shift+P → `Python: Select Interpreter` → 설치한 버전 선택 |
| `FileNotFoundError` | 폴더 열기로 `python-study` 폴더를 열었는지 확인 |
| 그래프 한글이 네모 | 코드 맨 위 `rcParams` 두 줄 확인 |

## 이어서 공부하기

1. [PROGRESS.md](PROGRESS.md) 에서 현재 위치 확인
2. 해당 강의의 `notes/` 노트로 복습
3. Claude와 이어서 할 때는 "python-study 저장소의 PROGRESS.md 보고 이어서 수업해 줘"라고 요청
   (Claude Code에서 이 폴더를 열면 `CLAUDE.md`의 수업 방식을 자동으로 따른다)
