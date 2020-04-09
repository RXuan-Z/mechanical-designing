import belt
import gear
def main():
    print("选择需要的设计内容")
    print("*******************")
    print("\t0.带轮（V带）")
    print("\t1.斜齿轮（硬)")
    print("*******************")
    select=input("输入数字：")
    if(eval(select)==0):
        flag=belt.belt()
    elif(eval(select)==1):
        flag=gear.gear()
    else:
        print("输入有误")
try:
    main()
except ValueError:
    print("可能因数值问题程序意外终止，尝试重新选择参数")
except:
    print("程序意外终止")