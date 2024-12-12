# Q :- Create a python program capable of greeting you with Good Morning, Good Evening, Good Afternoon and Good Night.
#         Your Program should use the time module to get the current time.

import time
timestamp = int(time.strftime('%H'))
print(timestamp)

if timestamp < 12 and timestamp > 0 :
    print("Good Morning, Raj")
elif timestamp > 12 and timestamp < 16 :
    print("Good Afternoon, Raj")
elif timestamp > 16 and timestamp < 20 :
    print("Good Evening Raj ")
else :
    print("Good Night Raj ")