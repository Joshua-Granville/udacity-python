import webbrowser
import time

count = 0

while (count < 3):
    time.sleep(10)
    webbrowser.open("http://www.linkedin.com")
    count = count + 1

print ('done loop')
