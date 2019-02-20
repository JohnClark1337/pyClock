import tkinter
import time
import threading
from tkinter import messagebox
from functools import partial

"""
Created by Jonathon Scofield

Creating a simple gui clock application.
"""




"""
clockChange()
Arguments: none

To be run in its own separate thread. It changes the clock label to be the current time.
It looks at the AMPMvar in the main thread to determine if the clock should be displayed
as AM/PM or 24 hour time. 


"""
def setAlarmClock(setting = 0, updown = 0):
    hours = int(lblAlarmH["text"][0:2])
    minutes = int(lblAlarmM["text"][0:2])
    seconds = int(lblAlarmS["text"][0:2])
    if setting == 1:
        if ((hours + updown) >= 0) and ((hours + updown) < 24):
            hours += updown
        if hours <= 9:
            lblAlarmH["text"] = "0" + str(hours) + " :"
        else:
            lblAlarmH["text"] = str(hours) + " :"
    elif setting == 2:
        if ((minutes + updown) >= 0) and ((minutes + updown) < 60):
            minutes += updown
        if minutes <= 9:
            lblAlarmM["text"] ="0" + str(minutes) + " :"
        else:
            lblAlarmM["text"] = str(minutes) + " :"
    elif setting == 3:
        if ((seconds + updown) >= 0) and ((seconds + updown) < 60):
            seconds += updown
        if seconds <= 9:
            lblAlarmS["text"] = "0" + str(seconds)
        else:
            lblAlarmS["text"] = str(seconds)
    elif setting == 0:
        at = [hours, minutes, seconds]
        alarmTimes.append(at)
    alarmClock()


def alarmClock():
    htime = int(time.strftime("%H"))
    mtime = int(time.strftime("%M"))
    stime = int(time.strftime("%S"))
    global alarmTimes
    for times in alarmTimes:
        if times[0] == htime and times[1] == mtime and times[2] == stime:
            messagebox.showinfo("ALARM!", "BEEP BEEP BEEP!")
   


def clockChange():
    while True:
        global AMPMvar
        if AMPMvar.get() == 0:
            lblclock.config(font=fontClock)
            currentTime = time.strftime("%H:%M:%S")
        else:
            lblclock.config(font=fontClockAP)
            currentTime = time.strftime("%I:%M:%S %p")
        lblclock.config(text=currentTime)
        alarmClock()
        time.sleep(.5)


def acAlarm():
    while True:
        global alarmTimes
        if len(alarmTimes) > 0:
            lstAlarms.delete(0, tkinter.END)
            for item in alarmTimes:
                lstAlarms.insert(tkinter.END, item)
        time.sleep(1)


#Main thread, creation and implementation of gui elements
if __name__ == '__main__':
    mainWindow = tkinter.Tk()
    mainWindow.title("PyClock")
    mainWindow.geometry("600x415")
    timeType = 0
    alarmTimes = list(())
    mainWindow.columnconfigure(0, weight=5)
    mainWindow.columnconfigure(1, weight=5)
    mainWindow.columnconfigure(2, weight=10)
    mainWindow.rowconfigure(0, weight=5)
    mainWindow.rowconfigure(1, weight=10)
    mainWindow.rowconfigure(2, weight=10)
    mainWindow.rowconfigure(3, weight=10)
    mainWindow.rowconfigure(4, weight=10)

    clockFrame= tkinter.Frame(mainWindow)
    sideButtons = tkinter.Frame(mainWindow)
    bottomButtons=tkinter.Frame(mainWindow)
    alarmBtnUpper = tkinter.Frame(mainWindow)
    alarmFrame = tkinter.Frame(mainWindow)
    alarmBtnLower = tkinter.Frame(mainWindow)

    clockFrame.grid(columnspan=2)
    sideButtons.grid(row=0, column=2)
    alarmBtnUpper.grid(row=1, columnspan=2)
    alarmFrame.grid(row=2, columnspan=2)
    alarmBtnLower.grid(row=3, columnspan=2)
    bottomButtons.grid(row=4, columnspan=3)

    #Store variable for AM/PM checkbox, also used with clockChanger()

    AMPMvar = tkinter.IntVar()
    AMPMvar.set(0)

    #Store clock fonts

    fontClock = ('times', 35, 'bold')
    fontClockAP = ('times', 35, 'bold')

    #Create labels and buttons

    lblclock = tkinter.Label(clockFrame, text="00:00:00", background="black", foreground="white", font=fontClock, pady=10, padx=5)
    lblsb = tkinter.Label(sideButtons, text="Time Format:")
    lblbb = tkinter.Label(bottomButtons, text="")
    btnExit = tkinter.Button(bottomButtons, text="Exit", command =mainWindow.destroy)
    lblAlarm = tkinter.Label()
    chkAMPM = tkinter.Checkbutton(sideButtons, text = "AM/PM", variable = AMPMvar)
    lstAlarms = tkinter.Listbox(sideButtons)
    btnsetAlarm = tkinter.Button(bottomButtons, text="Set Alarm", command=setAlarmClock)
    #lblAlarm = tkinter.Label(alarmFrame, text="00:00:00", background="white", foreground="red", font=fontClock)
    lblAlarmH = tkinter.Label(alarmFrame, text="00 :", background="white", foreground="red", font=fontClockAP, pady=10, padx=12)
    lblAlarmM = tkinter.Label(alarmFrame, text="00 :", background="white", foreground="red", font=fontClockAP, pady=10, padx=12)
    lblAlarmS = tkinter.Label(alarmFrame, text="00", background="white", foreground="red", font=fontClockAP, pady=10, padx=12)
    btnHUPAlarm = tkinter.Button(alarmBtnUpper, text = "\u2227", padx=40, pady=5, command=partial(setAlarmClock, 1, 1))
    btnMUPAlarm = tkinter.Button(alarmBtnUpper, text = "\u2227", padx=40, pady=5, command=partial(setAlarmClock, 2, 1))
    btnSUPAlarm = tkinter.Button(alarmBtnUpper, text = "\u2227", padx=40, pady=5, command=partial(setAlarmClock, 3, 1))
    btnHDownAlarm = tkinter.Button(alarmBtnLower, text = "\u2228", padx=40, pady=5, command=partial(setAlarmClock, 1, -1))
    btnMDownAlarm = tkinter.Button(alarmBtnLower, text = "\u2228", padx=40, pady=5, command=partial(setAlarmClock, 2, -1))
    btnSDownAlarm = tkinter.Button(alarmBtnLower, text = "\u2228", padx=40, pady=5, command=partial(setAlarmClock, 3, -1))

    #Add Labels and buttons to grid

    lblclock.grid()
    lblsb.grid(row=0, column=0)
    lblbb.grid(row=0, columnspan=3)
    btnsetAlarm.grid(row=1, column=2)
    btnExit.grid(row=1, column=3)
    chkAMPM.grid(row=1, column=0)
    lstAlarms.grid(row=1, column=2)
    lblAlarmH.grid(row=0, column=0, sticky = 'NEWS')
    lblAlarmM.grid(row=0, column=1, sticky = 'NEWS')
    lblAlarmS.grid(row=0, column=2, sticky = 'NEWS')
    btnHUPAlarm.grid(row=0, column=0)
    btnMUPAlarm.grid(row=0, column=1)
    btnSUPAlarm.grid(row=0, column=2)
    btnHDownAlarm.grid(row=0, column=0)
    btnMDownAlarm.grid(row=0, column=1)
    btnSDownAlarm.grid(row=0, column=2)

    #Begin thread for ongoing clock

    timer1 = threading.Thread(target=clockChange)
    timer1.daemon = True
    timer1.start()

    timer2 = threading.Thread(target=acAlarm)
    timer2.daemon = True
    timer2.start()
    mainWindow.mainloop()
