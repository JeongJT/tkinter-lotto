import tkinter                          # tkinter모듈 가져오기
import tkinter.font                     # tkinter.font모듈 가져오기
import random                           # random모듈 가져오기

lotto_num = range(1, 46)                # lotto_num변수에 범위를 1~45까지 지정

def buttonClick():                      # 버튼 클릭 함수생성
    print(random.sample(lotto_num, 6))  # 버튼을 클릭하면 random모듈의 sample클래스를 사용하여 lotto_num변수에 6개 무작위수 print

window = tkinter.Tk()                   # window변수에 tkinter.TK()클래스를 대입하여 창띄우기
window.title("lotto")                   # window창의 이름을 lotto로 지정
window.geometry("400x200")              # window창의 크기를 400x200으로 지정
window.resizable(False, False)          # window창의 가로 세로 크기를 False로 하여 크기조절 방지

# button변수에 tkinter모듈 button클래스를 사용하여 window창에 solid형태, 번호확인, 넓이는 15, 동작은 buttonClick함수, 누르면 1초후에 동작, 계속누르고있으면0.1초동작을 하도록 대입
button = tkinter.Button(window, overrelief="solid", text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)  
button.pack()                           # pack클래스를 이용하여 버튼생성

window.mainloop()                       # window창이 동작이 끝나도 자동으로 종료되지 않도록 mainloop를 사용하여 무한반복하게 명령