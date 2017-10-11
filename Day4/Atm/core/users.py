import sys
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from database import dbapi
from conf import settings

un_dir = os.path.join(settings.DB_DIR,'userlist.db')


class user():
    user_list = dbapi.load_data_from_db(un_dir)

    def update_db(self):
        dbapi.write_data_to_db(un_dir,self.user_list)

    def login(self):
        time = 0
        while time < 3:
            name = input("请输入用户名：")
            time += 1

            for i in self.user_list:
                # print(self.user_list[i]['pw'])
                if time == 3:
                    sys.exit('用户不存在，退出！')
                if  i== name:
                    if self.user_list[i]['islocked']== 1:
                        sys.exit('用户已锁定！')
                    passtime = 0
                    while passtime < 3:
                        password = input("请输入密码：")
                        if password == self.user_list[i]['pw']:
                            print('Welcome!')
                            break
                        passtime += 1
                    if passtime == 3:
                        self.user_list[i]['islocked'] = 1
                        print("用户已锁定")
                        self.update_db()
                        break

            else:
                print('该用户名不存在')





u = user()
u.login()

