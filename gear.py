def gear():
    import math
    p1=input("上级输入功率（kW）：")
    p1=eval(p1)
    n1=input("输入转速（rpm）：")
    n1=eval(n1)
    u=input("传动比：")
    u=eval(u)
    hour=input("总工作时长（h）：")
    hour=eval(hour)
    z1=input("选择小齿轮齿数：")
    z1=eval(z1)
    z2=z1*u
    print("计算大齿轮齿数为"+str(z2))
    z2=input("根据需求圆整为：")
    z2=eval(z2)
    u=z2/z1
    bb=input("选择螺旋角（度）：")
    bb=eval(bb)
    print("估计小齿轮直径（推荐"+str(z1*3)+"mm至"+str(z1*6)+"mm之间）")
    d11=input("单位（mm）：")
    d11=eval(d11)
    v1=math.pi*d11*n1/60000
    N1=60*n1*hour
    N2=N1/u

    print("根据Page177 图7-18寻找N1="+str(N1)+"与N2="+str(N2)+"对应系数")
    ynt1=input("Ynt1=：")
    ynt2=input("Ynt2=：")
    ynt1=eval(ynt1)
    ynt2=eval(ynt2)
    print("根据Page173-Page177 材料硬度与材料种类选择弯曲疲劳寿命极限")
    xgf1=input("齿轮1弯曲疲劳寿命极限（MPa）：")
    xgf2=input("齿轮1弯曲疲劳寿命极限（MPa）：")
    xgf1=eval(xgf1)
    xgf2=eval(xgf2)
    kkk=input("是否有正反转需求（是为1，否为0）：")
    kkk=eval(kkk)
    s=input("安全系数：")
    s=eval(s)
    x1=(1-kkk*0.3)*xgf1*ynt1*2/s
    x2=(1-kkk*0.3)*xgf2*ynt2*2/s

    t1=9550*1000*p1/n1
    ffd=input("查询Page167 表7-8选择齿宽系数：")
    ffd=eval(ffd)
    print("根据预估速度"+str(v1)+"m/s")
    kv=input("查询Page160 图7-9 选择Kv：")
    kv=eval(kv)
    ka=input("查询Page158 图7-2 选择KA：")
    ka=eval(ka)
    kha=input("查询Page160 图7-3 选择KFa：")
    kha=eval(kha)
    print("查询Page162 图7-4 选择KFb中a1-4的值：")
    aa1=input("a1：")
    aa1=eval(aa1)
    aa2=input("a2：")
    aa2=eval(aa2)
    aa3=input("a3：")
    aa3=eval(aa3)
    aa4=input("a4：")
    aa4=eval(aa4)
    khb=aa1+aa2*(1+aa3*ffd**2)*ffd**2+aa4*ffd*d11
    k=kv*ka*kha*khb

    bbr=bb*math.pi/180
    zv1=z1/(math.cos(bbr))**3
    zv2=z2/(math.cos(bbr))**3
    print("查询Page172 表7-9" )
    print("根据当量齿数Zv1="+str(zv1)+"与Zv2="+str(zv2)+"选择：")
    yfa1=input("齿轮1齿形系数YFa1：")
    yfa2=input("齿轮2齿形系数YFa2：")
    ysa1=input("齿轮1应力修正系数YSa1：")
    ysa2=input("齿轮2应力修正系数YSa2：")
    yfa1=eval(yfa1)
    yfa2=eval(yfa2)
    ysa1=eval(ysa1)
    ysa2=eval(ysa2)
    epaa=math.cos(bbr)*(1.88-3.2*(1/z1+1/z2))
    aan=20*math.pi/180
    aat=math.atan(math.tan(aan)/math.cos(bbr))
    bbb=math.atan(math.tan(bbr)*math.cos(aat))
    epaan=epaa/math.cos(bbb)**2
    yep=0.25+0.75/epaan
    epbb=0.318*ffd*z1*math.tan(bbr)
    if epbb>1:
        epbb=1
    ybb=1-epbb*bb/120
    if ybb<1:
        ybb=0.75
    xx1=yfa1*ysa1/x1
    xx2=yfa2*ysa2/x2
    if xx1>=xx2:
        xx=xx1
    else:
        xx=xx2
    m=math.pow((2*k*t1*math.cos(bbr)*yep*ybb*xx)/(ffd*z1**2),1.0/3)
    print("求得的模数为"+str(m)+"mm（推荐选择模数值不小于"+str(math.ceil(m))+"mm且传递动力齿轮的模数应不小于2mm）")
    m=input("选择的模数值为（mm）：")
    m=eval(m)
    a=m*(z1+z2)/(2*math.cos(bbr))
    print("计算中心距为"+str(a)+"mm")
    a=input("根据需求圆整为（mm）：")
    a=eval(a)
    rbb=math.acos(m*(z1+z2)/2/a)
    print("计算螺旋角为"+str(rbb/math.pi*180)+"度")
    rbb=input("根据需求圆整为（度）：")
    rbb=math.pi*eval(rbb)/180
    d1=m*z1/math.cos(rbb)
    d2=m*z2/math.cos(rbb)
    b=d1*ffd
    print("计算齿宽为"+str(b)+"mm")
    b=input("根据需求圆整为（mm）：")
    b=eval(b)

    print("根据Page170 图7-14寻找N1="+str(N1)+"与N2="+str(N2)+"对应系数")
    znt1=input("Znt1=：")
    znt2=input("Znt2=：")
    znt1=eval(znt1)
    znt2=eval(znt2)
    print("根据Page167-Page169 材料硬度与材料种类选择接触疲劳寿命极限")
    xgh1=input("齿轮1接触疲劳极限（MPa）：")
    xgh2=input("齿轮1接触疲劳极限（MPa）：")
    xgh1=eval(xgh1)
    xgh2=eval(xgh2)
    sh=input("安全系数：")
    sh=eval(sh)
    xh1=znt1*xgh1/sh
    xh2=znt2*xgh2/sh
    if xh1<xh2:
        xh=xh1
    else:
        xh=xh2
    aat=math.atan(math.tan(aan)/math.cos(rbb))

    ffd=b/d1
    aat=math.atan(math.tan(aan)/math.cos(rbb))
    cosbb=math.pow((1-(math.sin(rbb)*math.cos(aan))**2),1.0/2)
    zh=math.pow(2*cosbb/(math.sin(aat)*math.cos(aat)),1.0/2)
    print("根据Page165 表7-5")
    ze=input("查询弹性影响系数ZE（MPa^1/2）：")
    ze=eval(ze)
    epaa=math.cos(rbb)*(1.88-3.2*(1/z1+1/z2))
    epbb=0.318*ffd*z1*math.tan(rbb)
    if epaa<1:
        zep=math.pow((4-epaa)*(1-epbb)/3+epbb/epaa,1.0/2)
    else:
        zep=math.pow(1/epaa,1.0/2)
    zbb=math.pow(math.cos(rbb),1.0/2)
    xxh=zbb*ze*zep*zh*math.pow((2*k*t1*(u+1))/(u*b*d1**2),1.0/2)
    if xxh<xh:
        print("校核通过\n")
        print("设计成功\n")
        print("设计结果：\n")
        print("传动比="+str(u)+"\n")
        print("齿轮1直径d1="+str(d1)+"mm\n")
        print("齿轮2直径d2="+str(d2)+"mm\n")
        print("模数m="+str(m)+"mm\n")
        print("中心距="+str(a)+"mm\n")
        print("螺旋角="+str(rbb/math.pi*180)+"度\n")
        print("齿厚="+str(b)+"mm\n")
        flag=1
    else:
        print("校核未通过\n")
        print("设计失败")
        flag=0
    print("*****FINISH*****")
    return flag