import webbrowser
import time

total_breaks = 4
break_count =  0

print ("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("http://www.linkedin.com")
    break_count = break_count + 1

print ('done loop')
