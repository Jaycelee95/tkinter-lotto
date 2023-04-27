import tkinter
import tkinter.font
import random # 기능 연결(random, tkinter)

lotto_num = range(1,46) # 1~46까지의 랜덤한 숫자를 lotto_num변수에 넣음.

def buttonClick(): # 함수 생성
    label = tkinter.Label(window, text=str(random.sample(lotto_num,6))) # 변수에서 6개의 랜덤한 숫자를 윈도우에 출력 (타입 리스트를 스트링으로 변환)
    label.pack()

window=tkinter.Tk() # TKinter 생성
window.title("lotto") # 윈도우의 이름 설정
window.geometry("400x200") # 윈도우 창 크기 설정
window.resizable(False, False) # 창 크기 고정

button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
# 버튼 생성(외곽선/텍스트/크기/커맨드 클릭으로 지정/딜레이=1000/딜레이=100)
button.pack()

window.mainloop() # 반복 / 명령 끝나도 꺼지지 않게 루프