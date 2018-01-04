#!/usr/bin/env python
#-*- coding: utf-8 -*-

import gtk


class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp,self).__init__()
        self.set_default_size(300,200)
        self.set_title("Maska Bahitowa")
        self.lbl = gtk.Label("Obsługa Maski Bahitova")

        self.btn1 = gtk.Button("OPEN")
        self.btn1.connect("button_press_event", self.open)

        self.btn2 = gtk.Button("CLOSE")
        self.btn2.connect("button_press_event", self.close)


        screen = gtk.Fixed()
        screen.put(self.lbl,60,30)
        screen.put(self.btn1,60,60)
        screen.put(self.btn2,140,60)

        self.add(screen)
        self.show_all()

    def open(self,widget,event):
        import RPi.GPIO as GPIO
        import time

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(12, GPIO.OUT) # PIN number

        p = GPIO.PWM(12, 50)

        p.start(2.5)
        p.ChangeDutyCycle(12.5)  # 180*
        time.sleep(1)
        p.stop()
        GPIO.cleanup()


    def close(self,widget,event):
        import RPi.GPIO as GPIO
        import time

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12, GPIO.OUT)
        p = GPIO.PWM(12, 50)
        p.start(12.5)
        p.ChangeDutyCycle(2.5)  # 180*

        time.sleep(1)
        p.stop()
        GPIO.cleanup()



PyApp()
gtk.main()
