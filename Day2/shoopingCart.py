import sys

goodList = [['Book1',10],['Book2',22],['Book3',124]]

boughtList = []

print('Welcome!')

salary = input('please input your salary!\n')
if salary.isdigit():
    salary = int(salary)

    while 1:

        # 输出商品列表
        for index, good in enumerate(goodList):
            print(index, good)

        choose1 = input('请输入你要购买的商品的编号,q退出：\n')
        if choose1.isdigit():
            choose1 = int(choose1)
            if choose1 < len(goodList) and choose1 >= 0:
                buygood = goodList[choose1]
                if salary >= buygood[1]:
                    salary -= buygood[1]
                    boughtList.append(buygood)
                    print('您已购买', buygood[0], '，花费', buygood[1])
                    print('您的可用余额为', salary, '元')
                else:
                    print('余额不足！')
                    print('您要买的商品金额为', buygood[1], '元,您的余额为', salary, '元')
            else:
                print('没有该商品')
        elif choose1 == 'q':
            # if len(boughtList) > 0 :
            print('您已购买:')
            i = 0
            while i < len(boughtList):
                print(boughtList[i][0], ':', boughtList[i][1], '元')
                i += 1
            print('您的余额：', salary)

            sys.exit(0)
        else:
            print('输入错误')
            continue
else:
    print('输入错误')
