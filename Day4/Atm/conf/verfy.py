import time

# 数字输入
def isint():
    while 1:
        num = input()
        if num.isdigit():
            num = int(num)
            return num
            break
        else:
            print('输入仅限数字，请重新输入!')




def gettime():
    time_now = time.time()
    time_local = time.localtime(time_now)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt


