import time

count = int(input("Type how many seconds that you want on the timer: "))
timestep = 0

while timestep < count:
    timestep += 1
    time.sleep(1)
    print(timestep)