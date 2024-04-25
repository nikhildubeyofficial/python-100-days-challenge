# Exercise 2 

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hr = int(time.strftime("%H"))
min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))
if(hr < 12 and hr > 6):
    print("Good Morning")
elif(hr < 17 and hr > 12):
    print("Good Afternoon")
elif(hr < 22 and hr > 17):
    print("Good Evening")
else:
    print("Good Night")