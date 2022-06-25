from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print("Current time:",now)
        if now == set_alarm_timer:
            print("Time to Wake up!")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Mehak's Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter the time in 24 hour format!", fg="yellow",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Minute   Second",font=("Helevetica",10)).place(x = 115)
setYourAlarm = Label(clock,text = "Set the time",fg="black",font=("Helevetica",10,"bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "white",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "white",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "white",width = 15).place(x=200,y=30)

submit = Button(clock,text = "Set Alarm",fg="black",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()