import sys
import os

time = 0

while time <3:
    name = input("请输入用户名：")
    time += 1
    openLocked = open("lockedname").readlines()

    # 判断用户是否被锁定
    for lockedname in openLocked:
        lockedname = lockedname.strip('\n')
        if name == lockedname:
            sys.exit('用户已锁定！')


    namepass = open("namepass").readlines()
    for namekey in namepass:
        namekey = namekey.strip('\n')
        [CorrectName,CorrectWord] = namekey.split()
        if name == CorrectName:
            passtime = 0
            while passtime < 3:
                password = input("请输入密码：")
                if password == CorrectWord:
                    print('Welcome!')
                    sys.exit(0)
                passtime += 1
            if passtime == 3:
                locked = open('lockedname','a')
                locked.write('\n'+name)
                sys.exit('错误次数太多，该用户已被锁定！')

    else:
        print('该用户名不存在')

    if time == 3:
        sys.exit('用户不存在，退出！')



