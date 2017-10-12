import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from database import dbapi
from conf import settings,verfy

db_dir = os.path.join(settings.DB_DIR,'cardlist.db')
rep_dir = os.path.join(settings.RP_DIR,'rep.db')
bill_dir = os.path.join(settings.RP_DIR,'bill.db')


class bank:
    all_db_list = dbapi.load_data_from_db(db_dir)
    db_list = []

    def __init__(self,name):
        self.name = name
        for i in self.all_db_list:
            if i['owner'] == name:
                self.db_list.append(i)


    # 查看银行卡
    def show_card(self):
        for i in self.db_list:
            print(i)

    # 查看账单
    def show_bill(self,user):
        f = open(bill_dir)
        for i in f:
            i = eval(i.strip('\n'))
            if i['user'] == str(user):
                # print(i)
                print('%s 卡号:%s  %s  %s元' % (i['time'], i['card'], i['use'], i['amount']))
        f.close()


    # 将记录存入账单
    def write_bill(self, num, use, card,user):
        time = verfy.gettime()
        bill = {}
        bill['time'] = time
        bill['amount'] = num
        bill['use'] = use
        bill['card'] = card
        bill['user'] = user
        f = open(bill_dir, 'a')
        f.write(str(bill) + '\n')
        f.close()

    # 查看购物清单
    def show_shop_report(self,user):
        f = open(rep_dir)
        for i in f :
            i = eval(i.strip('\n'))
            if i['user'] == str(user):
                print('%s  %s  %s元' %(i['time'],i['good'],i['amount']))
        f.close()

    # 将记录存入购物清单
    def write_shop_report(self, name, num, card, user):
        time = verfy.gettime()
        rep = {}
        rep['time'] = time
        rep['good'] = name
        rep['card'] = card
        rep['amount'] = num
        rep['user'] = user
        f = open(rep_dir, 'a')
        f.write(str(rep)+'\n')
        f.close()

    # 选择银行卡 返回字典
    def choose_card(self):
        while 1:
            choose = verfy.isint()
            for i in self.db_list:
                if str(choose) == i['id']:
                    return i
            else:
                print('无此卡号！')


    # 提现
    def withdraw(self):
        # 手续费没算
        self.show_card()
        print('请输入提现卡号：')
        choose = self.choose_card()
        print('请输入提现金额：')
        num = verfy.isint()
        if num <= choose['balance']:
            choose['balance'] -= num
            print('已提现%s元' %num)
        else:
            print('余额不足，提现失败！')

    # 还款
    def repay(self):
        self.show_card()
        print('请输入要还款的卡号：')
        choose = self.choose_card()

        if choose['balance'] >= 0:
            print('不需要还款！')
        else :
            print('请输入要还的金额：')
            num = verfy.isint()
            choose['balance'] += int(num)
            print('已还款%s元' %num)



    # 查看余额
    def show_balance(self):
        for i in self.db_list:
            print('id：%s , 余额：%s' %(i['id'],i['balance']))

    # 转账
    def transfer(self):
        self.show_card()
        print('请输入转出的卡号：')
        fromid = self.choose_card()
        print('请输入要转入的卡号：')
        toid = self.choose_card()
        print('请输入转账金额：')
        num = verfy.isint()
        if fromid['balance'] >= num:
            fromid['balance'] -= num
            toid['balance'] += num
            print('已成功转账！')
        else:
            print('金额不足，转账失败！')


    # 付款
    def pay(self,num):
        self.show_card()
        print('请选择付款卡号：')
        choose = self.choose_card()
        if choose['balance'] + choose['line'] >= num:
            choose['balance'] -= num

            '''
            加到账单、购物清单
            '''

            print('已成功付款')
            input('输入任意键返回')
        else:
            print('扣款失败，余额/额度不足！')
            input('输入任意键返回')




test = bank("Du")
test.show_bill('Du')