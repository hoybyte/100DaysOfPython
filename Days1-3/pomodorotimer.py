from datetime import datetime
from datetime import timedelta
import os
import sys
import tkinter as tk

timer_length = sys.argv[0]

def set_timer(timer_length):
    print(type(timer_length))
    timer_length = timer_length.second
    now = datetime.now()
    alert = timedelta(minutes= timer_length)
    new_time =  (now + alert)
    set_alert(new_time)
    pass

def set_alert(new_time):
    print("test")
    print(new_time)
    milliseconds = new_time.microsecond
    print(milliseconds)


set_timer(timer_length)