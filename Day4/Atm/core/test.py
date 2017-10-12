import time


time_now = time.time()
time_local = time.localtime(time_now)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

print(dt)
