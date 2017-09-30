import sys

goodList = [['Book1',10],['Book2',22],['Book3',124]]

boughtList = []

print('Welcome!')

salary = input('please input your salary!\n')
if salary.isdigit():
    salary = int(salary)
pay = 0

while 1:
    num = 1

    # 输出商品列表
    for good in goodList:
        print(num,',',good[0],good[1])
        num += 1

    choose1 = int(input('请输入你要购买的商品的编号,0退出：\n'))
    if choose1 == 0:
            if len(boughtList) > 0 :
                print('您已购买:')
                i = 0
                while i < len(boughtList):
                    print(boughtList[i][0],':',boughtList[i][1],'元')
                    i += 1
                print('共计',pay,'元')
            sys.exit(0)


    elif choose1 <= len(goodList) :
        if salary >= goodList[choose1-1][1]:
            salary -= goodList[choose1-1][1]
            pay += goodList[choose1-1][1]
            boughtList.append([goodList[choose1-1][0],goodList[choose1-1][1]])
            print('您已购买',goodList[choose1-1][0],',共花费',goodList[choose1-1][1],'元')
            print('您的可用余额为',salary,'元')
        else :
            print('余额不足！')
            print('您要买的商品金额为',goodList[choose1-1][1],'元,您的余额为',salary,'元')

    else :
        print('输入错误')
        continue