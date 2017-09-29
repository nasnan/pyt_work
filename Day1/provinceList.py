import sys

a = {'ZheJiang':{'Hangzhou':['LinAn','YuHang'],'ShaoXing':['YueCheng','KeQiao']}}


print('Welcome!')

# 省列表
while 1:
    print(a)
    choose1 = input('请输入输入省份名字进入该省，q退出\n')
    if choose1 == 'q':
        sys.exit(0)

    for province in a :
        if province == choose1:
            # print(a[province])

            # 市列表
            while 1 :
                print(a[province])
                choose2 = input('请输入市名进入该市，b返回上级列表，q退出\n')
                if choose2 == 'q':
                    sys.exit(0)
                if choose2 == 'b':
                    break
                for city in a[province]:
                    if city == choose2:

                        # 区列表
                        while 1:
                            print(a[province][city])
                            choose3 = input('请输入：b返回上级列表，q退出\n')
                            if choose3 == 'q':
                                sys.exit(0)
                            if choose3 == 'b':
                                break
                            else :
                                print('没有该选项！')
                                continue
                else:
                    print('没有该选项！')
                    continue
    else :
        print('没有该选项！')
        continue

