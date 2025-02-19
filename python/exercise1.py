
import time

current_time = time.localtime().tm_hour
print(current_time)

if current_time < 12:
    print("Good morning!")
elif current_time < 17:
    print("Good afternoon!")
else:
    print("Good evening!")
