def belt():
    import math
    P=input("电动机额定功率（kW）：")
    hpd=input("每天运行时间（h）：")
    n1=input("小轮转速（rpm）：")
    n2=input("大轮转速（rpm）：")
    n1=eval(n1)
    n2=eval(n2)
    i=n1/n2
    print("根据每天运行时间"+hpd+"h")
    KA=input("查询Page357 表15-8选择系数KA：")
    Pca=eval(P)*eval(KA)
    print("根据计算功率"+str(Pca)+"kw")
    Tp=input("查询Page358 表15-11选择带类型（大写字母）：")
    print("根据采用"+Tp+"带")
    dd1=input("查询Page352 表15-2、Page358 表15-9选择主动轮直径（mm）：")
    dd1=eval(dd1)
    ep=input("运行滑动率，不考虑填0（%）：")
    dd2=i*(1-0.01*eval(ep))*dd1
    print("计算大轮直径"+str(dd2)+"mm：")
    dd2=input("选择大轮直径（mm）")
    dd2=eval(dd2)
    v=math.pi*dd1*n1/(60000)
    flag=1
    if v<=25:
        i1=dd2/((1-0.01*eval(ep))*dd1)
        di=(i1-i)/i
        if di<0.05:
            amax=0.7*(dd1+dd2)
            amin=2*(dd1+dd2)
            print("根据\n中心距上限"+str(amax)+"mm")
            print("中心距下限"+str(amin)+"mm")
            a0=input("初选中心距（mm）：")
            a0=eval(a0)
            Ld0=2*a0+math.pi*0.5*(dd1+dd2)+(dd2-dd1)**2/(a0*4)
            print("根据V带计算长度"+str(Ld0)+"mm")
            Ld=input("查询Page356 表15-7选取基准长度（mm）：")
            Ld=eval(Ld)
            KL=input("查询Page356 表15-7选取修正系数（若无填0）：")
            KL=eval(KL)
            if KL!=0:
                a=a0+0.5*(Ld-Ld0)
                aa=180-(dd2-dd1)*57.3/a
                if aa>120:
                    print("包角"+str(aa)+"度")
                    Kaa=input("查询Page356 表15-6选取包角系数：")
                    Kaa=eval(Kaa)
                    print("根据带类型 "+Tp+" 小带轮直径"+str(dd1)+"mm"+"小带轮转速"+str(n1)+"mm")
                    p0=input("查询Page354 表15-4选取基本额定功率（kW）：")
                    p0=eval(p0)
                    print("传动比"+str(i)+"")
                    dp0=input("查询Page355 表15-5选取增量（kW）：")
                    dp0=eval(dp0)
                    print("根据采用"+Tp+"带")
                    q=input("查询Page352 表15-3确定单位长度质量（kg/m）：")
                    q=eval(q)
                    z=math.ceil(Pca/((p0+dp0)*Kaa*KL))
                    F0=500*(2.5-Kaa)*Pca/(Kaa*z*v)+q*v**2
                    Fp=2*z*F0*math.sin(0.5*aa*2*math.pi/360)
                else:
                    print("参数选择不正确（包角过小）")
                    flag=0
            else:
                print("参数选择不正确（不能找到对应带）")
                flag=0
        else:
            print("参数选择不正确（传动比误差过大）")
            flag=0
    else:
        print("参数选择不正确（带速过高）")
        flag=0
    if flag==1:
        print("设计成功")
        print("设计结果：\n")
        print("带轮1直径dd1="+str(dd1)+"mm\n")
        print("带轮2直径dd2="+str(dd2)+"mm\n")
        print("带种类为"+Tp+"带\n")
        print("中心距="+str(a)+"mm\n")
        print("小轮包角="+str(aa)+"度\n")
        print("根数="+str(z)+"根\n")
        print("初拉力="+str(F0)+"N\n")
        print("压轴力="+str(Fp)+"N\n")
    else:
        print("设计失败")
    print("*****FINISH*****")
    return flag