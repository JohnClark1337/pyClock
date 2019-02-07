import tkinter
import time
import threading

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



#Main thread, creation and implementation of gui elements
if __name__ == '__main__':
    mainWindow = tkinter.Tk()
    mainWindow.title("PyClock")
    mainWindow.geometry("400x260")
    timeType = 0

    mainWindow.columnconfigure(0, weight=5)
    mainWindow.columnconfigure(1, weight=5)
    mainWindow.columnconfigure(2, weight=10)
    mainWindow.rowconfigure(0, weight=5)
    mainWindow.rowconfigure(1, weight=10)

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

    fontClock = ('times', 50, 'bold')
    fontClockAP = ('times', 35, 'bold')

    #Create labels and buttons

    lblclock = tkinter.Label(clockFrame, text="00:00:00", background="black", foreground="white", font=fontClock)
    lblsb = tkinter.Label(sideButtons, text="Side Buttons here")
    lblbb = tkinter.Label(bottomButtons, text="Bottom Buttons here")
    btnExit = tkinter.Button(bottomButtons, text="Exit", command =mainWindow.destroy)
    lblAlarm = tkinter.Label()
    chkAMPM = tkinter.Checkbutton(sideButtons, text = "AM/PM", variable = AMPMvar)
    #lblAlarm = tkinter.Label(alarmFrame, text="00:00:00", background="white", foreground="red", font=fontClock)
    lblAlarmH = tkinter.Label(alarmFrame, text="00 :", background="white", foreground="red", font=fontClockAP, pady=10, padx=5)
    lblAlarmM = tkinter.Label(alarmFrame, text="00 :", background="white", foreground="red", font=fontClockAP, pady=10, padx=5)
    lblAlarmS = tkinter.Label(alarmFrame, text="00", background="white", foreground="red", font=fontClockAP, pady=10, padx=5)
    btnHUPAlarm = tkinter.Button(alarmBtnUpper, text = "\u2227", padx="30", padx=5)
    btnMUPAlarm = tkinter.Button(alarmBtnUpper, text = "\u2227", padx="30", padx=5)
    btnSUPAlarm = tkinter.Button(alarmBtnUpper, text = "\u2227", padx="30", padx=5)
    btnHDownAlarm = tkinter.Button(alarmBtnLower, text = "\u2228", padx="30", padx=5)
    btnMDownAlarm = tkinter.Button(alarmBtnLower, text = "\u2228", padx="30", padx=5)
    btnSDownAlarm = tkinter.Button(alarmBtnLower, text = "\u2228", padx="30", padx=5)

    #Add Labels and buttons to grid

    lblclock.grid()
    lblsb.grid(row=0, column=0)
    lblbb.grid(row=0, columnspan=3)
    btnExit.grid(row=1, column=3)
    chkAMPM.grid(row=1, column=0)
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
    mainWindow.mainloop()
