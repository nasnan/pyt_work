import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from database import dbapi
from conf import settings

db_dir = os.path.join(settings.DB_DIR,'shoopinglist.db')

class shop:
    shop_list = dbapi.load_data_from_db(db_dir)
    cart_list = []

    # 商品加入购物车
    def add_to_cart(self,good):
        self.cart_list.append(good)
        print(good['name'],"已加入购物车")

    # 查看购物车
    def show_cart(self):
        for i in self.cart_list:
            print(i)
        input('输入任意键继续，返回上一级菜单')

    def show_good(self):
        while 1:
            num = 0
            for i in sorted(self.shop_list):
                print(i,self.shop_list[i])
                num += 1
            choose1 = input('请输入你要购买的商品的编号,c查看购物车,q结算并退出：\n')
            if choose1.isdigit():
                choose1 = int(choose1)
                if choose1 <= num and choose1 > 0:
                    buygood = self.shop_list[str(choose1)]
                    self.add_to_cart(buygood)
                else:
                    print('没有该商品')

            elif choose1 == 'c':
                self.show_cart()

            elif choose1 == 'q':

                pass

                sys.exit(0)
            else:
                print('输入错误')
                continue




test=shop()
test.show_good()

