# 모듈 불러오기 (python pypi 프로그램 "keyboard", "threading", "time", "random" 다운로드 후 가져오기)
import keyboard
import threading
import time
import random

#파일 가져오기
file = open('./sentence.txt', 'r', encoding="utf8")
line = file.readlines()
txt = []
for i in line:
    txt.append(i)
typing = False


def program():
    global typing
    while typing:
        rd = random.randint(0, (len(txt) - 1))
        keyboard.write(txt[rd])
        keyboard.press_and_release('enter')
        time.sleep(0.1)



def on_backtick(e):
    global typing
    if e.name == '`':
        if typing:
            print("매크로 정지")
            typing = False
        else:
            # 반복 시작
            print("Starting typing...")
            typing = True
            # 별도의 스레드에서 반복 작업 수행
            typing_thread = threading.Thread(target=program)
            typing_thread.start()


def main():
    print(" '`'키를 누르면 프로그램이 시작됩니다. (한번 더 누르면 종료.) ")
    keyboard.on_press(on_backtick)
    try:
        # 프로그램이 종료되지 않도록 유지
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nProgram terminated.")
        keyboard.unhook_all()  # 모든 이벤트 훅 해제

if __name__ == "__main__":
    main()

#made by @bitik_jam with OpenAI
