"""
上午7:15早读，7:40伪下课，7:45上课，每节40分钟*4，11:10训练课，11:35下课
12:35-13:40
下午13:50预备，14:00上课，每节45分钟*4
"""
from turtle import *
from datetime import datetime
from win32com import client as c
import os

com=c.Dispatch("SAPI.SpVoice.1")
def begin():
    com.Speak("Class begin.")
def end():
    com.Speak("Class is over.")
def rest():
    com.Speak("Rest.")
def go():
    com.Speak()
plans=[
    ['语文','数学','信息','历史','地理','语文','数学','英语','英语'],
    ['语文','数学','英语','地理','信息','语文','道法','数学','英语'],
    ['语文','数学','英语','地理','信息','语文','道法','数学','英语'],
    ['语文','数学','英语','地理','信息','语文','道法','数学','英语'],
    ['语文','数学','英语','地理','信息','语文','道法','数学','英语'],
    ['语文','数学','英语','地理','信息','语文','道法','数学','英语'],
    ['语文','数学','英语','地理','信息','道法','语文','数学','历史']
]

FFFF=True

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

def make_hand_shape(name, laenge, spitze):
    reset()
    jump(-laenge*0.055)
    begin_poly()
    hand(laenge, spitze)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)

def clockface(radius):
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global second_hand, minute_hand, hour_hand, writer
    mode("logo")
    make_hand_shape("second_hand", 125, 25)
    make_hand_shape("minute_hand",  130, 25)
    make_hand_shape("hour_hand", 90, 25)
    clockface(160)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("gray20", "gray80")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("blue1", "red1")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("blue3", "red3")
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()
    writer = Turtle()
    #writer.mode("logo")
    writer.ht()
    writer.pu()
    writer.bk(85)

def wochentag(t):
    global FFFF

    wochentag = ["周一", "周二", "周三",
        "周四", "周五", "周六", "周日"]
    wkd=t.weekday()
    today=wochentag[wkd]
    sekunde = int(t.second + t.microsecond*0.000001)
    minute = int(t.minute + sekunde/60.0)
    stunde = int(t.hour + minute/60.0)
    #print(sekunde,minute,stunde)
    if(stunde==7 and minute==15 and sekunde < 0.05 and FFFF):
        begin()
        FFFF=False
    if(stunde==7 and minute==15 and sekunde > 30):
        FFFF=True

    if(stunde==7 and minute==45 and sekunde < 0.05 and FFFF):
        begin()
        FFFF=False
    if(stunde==7 and minute==45 and sekunde > 30):
        FFFF=True

    if(stunde==8 and minute==35 and sekunde < 0.05 and FFFF):
        begin()
        FFFF=False
    if(stunde==8 and minute==35 and sekunde > 30):
        FFFF=True

    if(stunde==9 and minute==15 and sekunde < 0.05 and FFFF):
        go()
        FFFF=False
    if(stunde==9 and minute==15 and sekunde > 30):
        FFFF=True

    if(stunde==9 and minute==40 and sekunde < 0.05 and FFFF):
        begin()
        FFFF=False
    if(stunde==9 and minute==40 and sekunde > 30):
        FFFF=True

    if(stunde==10 and minute==30 and sekunde < 0.05 and FFFF):
        begin()
        FFFF=False
    if(stunde==10 and minute==30 and sekunde > 30):
        FFFF=True

    if(stunde==14 and minute==0 and sekunde < 0.05 and FFFF):
        begin()
        FFFF=False
    if(stunde==14 and minute==0 and sekunde > 30):
        FFFF=True

    if(stunde==14 and minute==55 and sekunde < 0.05 and FFFF):
        begin()
        FFFF=False
    if(stunde==14 and minute==55 and sekunde > 30):
        FFFF=True

    if(stunde==15 and minute==50 and sekunde < 0.05 and FFFF):
        begin()
        FFFF=False
    if(stunde==15 and minute==50 and sekunde > 30):
        FFFF=True

    if(stunde==16 and minute==45 and sekunde < 0.05 and FFFF):
        begin()
        FFFF=False
    if(stunde==16 and minute==45 and sekunde > 30):
        FFFF=True

    if(stunde==12 and minute==35 and sekunde < 0.05 and FFFF):
        os.system("start 革命不是请客吃饭.exe")
        rest()
        FFFF=False
    if(stunde==12 and minute==35 and sekunde > 30):
        FFFF=True

    if(stunde==13 and minute==40 and sekunde < 0.05 and FFFF):
        os.system("start 希望寄托在你们身上.exe")
        FFFF=False
    if(stunde==13 and minute==40 and sekunde > 30):
        FFFF=True

    if(stunde==8 and minute==25 and sekunde < 0.05 and FFFF):
        end()
        FFFF=False
    if(stunde==8 and minute==25 and sekunde > 30):
        FFFF=True

    if(stunde==9 and minute==15 and sekunde < 0.05 and FFFF):
        end()
        FFFF=False
    if(stunde==9 and minute==15 and sekunde > 30):
        FFFF=True

    if(stunde==10 and minute==20 and sekunde < 0.05 and FFFF):
        end()
        FFFF=False
    if(stunde==10 and minute==20 and sekunde > 30):
        FFFF=True

    if(stunde==11 and minute==10 and sekunde < 0.05 and FFFF):
        end()
        FFFF=False
    if(stunde==11 and minute==10 and sekunde > 30):
        FFFF=True

    if(stunde==11 and minute==35 and sekunde < 0.05 and FFFF):
        end()
        FFFF=False
    if(stunde==11 and minute==35 and sekunde > 30):
        FFFF=True

    if(stunde==14 and minute==45 and sekunde < 0.05 and FFFF):
        end()
        FFFF=False
    if(stunde==14 and minute==45 and sekunde > 30):
        FFFF=True

    if(stunde==15 and minute==40 and sekunde < 0.05 and FFFF):
        end()
        FFFF=False
    if(stunde==15 and minute==40 and sekunde > 30):
        FFFF=True

    if(stunde==16 and minute==35 and sekunde < 0.05 and FFFF):
        end()
        FFFF=False
    if(stunde==16 and minute==35 and sekunde > 30):
        FFFF=True

    if(stunde==17 and minute==30 and sekunde < 0.05 and FFFF):
        end()
        FFFF=False
    if(stunde==17 and minute==30 and sekunde > 30):
        FFFF=True

    if(stunde==7 and minute>=15 and minute<40):
        title('当前：早读')
    if(stunde==7 and minute>=40 and minute<45):
        title('当前：早读下课')
    if((stunde==7 and minute>=45)or(stunde==8 and minute<25)):
        title('当前：1'+plans[wkd][0])
    if(stunde==8 and minute>=25 and minute<35):
        title('当前：1'+plans[wkd][0]+'下课')
    if((stunde==8 and minute>=35)or(stunde==9 and minute<15)):
        title('当前：2'+plans[wkd][1])
    if(stunde==9 and minute>=15 and minute<40):
        title('当前：跑操')
    if((stunde==9 and minute>=40)or(stunde==10 and minute<20)):
        title('当前：3'+plans[wkd][2])
    if(stunde==10 and minute>=20 and minute<30):
        title('当前：3'+plans[wkd][2]+'下课')
    if((stunde==10 and minute>=30)or(stunde==11 and minute<10)):
        title('当前：4'+plans[wkd][3])
    if(stunde==11 and minute>=10 and minute<35):
        title('当前：5'+plans[wkd][4])
    if((stunde==11 and minute>=35)or(stunde==12 and minute<35)):
        title('当前：午饭')
    if((stunde==12 and minute>=35)or(stunde==13 and minute<40)):
        title('当前：午读')
    if(stunde==13 and minute>=40 and minute<50):
        title('当前：入校')
    if(stunde==13 and minute>=50):
        title('当前：预备')
    if(stunde==14 and minute>=0 and minute<45):
        title('当前：6'+plans[wkd][5])
    if(stunde==14 and minute>=45 and minute<55):
        title('当前：6'+plans[wkd][5]+'下课')
    if((stunde==14 and minute>=55)or(stunde==15 and minute<40)):
        title('当前：7'+plans[wkd][6])
    if(stunde==15 and minute>=40 and minute<50):
        title('当前：7'+plans[wkd][6]+'下课')
    if((stunde==15 and minute>=50)or(stunde==16 and minute<35)):
        title('当前：8'+plans[wkd][7])
    if(stunde==16 and minute>=35 and minute<45):
        title('当前：8'+plans[wkd][7]+'下课')
    if((stunde==16 and minute>=45)or(stunde==17 and minute<30)):
        title('当前：9'+plans[wkd][8])
    if((stunde==17 and minute>=30) or stunde>17):
        title('当前：晚自修')

    return today

def datum(z):
    monat = ["一月", "二月", "三月", "四月", "五月", "六月",
            "七月", "八月", "九月", "十月", "十一月", "十二月"]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "%d %s %d" % (j, m, t)

def tick():
    t = datetime.today()
    sekunde = t.second + t.microsecond*0.000001
    minute = t.minute + sekunde/60.0
    stunde = t.hour + minute/60.0
    try:
        tracer(False)  # Terminator can occur here
        writer.clear()
        writer.home()
        writer.forward(65)
        writer.write(wochentag(t),
                    align="center", font=("Courier", 14, "bold"))
        writer.back(150)
        writer.write(datum(t),
                    align="center", font=("Courier", 14, "bold"))
        writer.forward(85)
        tracer(True)
        second_hand.setheading(6*sekunde)  # or here
        minute_hand.setheading(6*minute)
        hour_hand.setheading(30*stunde)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"

if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
