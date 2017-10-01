import sys

print('Welcome!')

logIn = input('请选择1.商家 2.用户:')

# 商家接口
if logIn == '1' :
    # 输出商品列表
    while 1:
        goodList = []
        openGood = open('goodlist')
        for goods in openGood.readlines():
            [good, val] = goods.split()
            goodList.append([good, int(val)])

        openGood.close()

        for index, good in enumerate(goodList):
            print(index, good)

        c = input('请选择1.增加商品，2.修改商品价格,q.退出:')

        # 增加商品
        if c == '1':
            addGoodName = input('请输入商品名称：')
            addGoodPrice = input('请输入商品价格：')
            openGood2 = open('goodList','a')
            openGood2.write(addGoodName+' '+addGoodPrice+'\n')
            openGood2.close()

        # 修改商品价格
        elif c =='2':
            upName = input('请输入要修改的商品名称：')
            for item in goodList:
                if item[0] == upName:
                    upPrice = input('请输入商品新价格：')
                    item[1] = int(upPrice)

                    openGood = open('goodlist','w')
                    for i in goodList:
                        openGood.write(i[0]+' ' +str(i[1])+'\n')


        elif c == 'q' :
            exit()
        else:
            print('无此选项！')
            pass


# 用户接口
elif logIn == '2' :
    goodList = []
    openGood = open('goodlist')

    for goods in openGood.readlines():
        [good, val] = goods.split()
        goodList.append([good, int(val)])

    openGood.close()

    boughtList = []
    openSalary = open('salary')
    salarytemp = openSalary.readline()
    openSalary.close()
    if salarytemp.isdigit():
        salary = int(salarytemp)
    else:
        salary = input('please input your salary!\n')
        if salary.isdigit():
            salary = int(salary)
        else:
            print('输入错误')
            exit()

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
            openSalary2 = open('salary','w+')
            openSalary2.write(str(salary))

            sys.exit(0)
        else:
            print('输入错误')
            continue

else:
    print('无此选项!')
    exit()
