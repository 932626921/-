#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：杨涛诚
日期：2019.11.20
"""

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
print('--------------')
choice_name=input()
def ball(choice_name):
    if choice_name!='石头' and choice_name!='史波克' and choice_name!='纸' and choice_name!='蜥蜴' and choice_name!='剪刀':
      print('Error:No Correct Name')
    else:
     print('您的选择为:%s'%choice_name)
ball(choice_name)
import random
number=random.randint(0,4)
def number_to_name(number):
     if number==0:
        return('石头')              
     if number==1:
       return('史波克')
     if number==2:
       return('纸')
     if number==3:
       return('蜥蜴')
     if number==4:
       return('剪刀')                        
comp_choice=number_to_name(number)
print('电脑的选择为:%s'%comp_choice)
def rpsls(choice_name,comp_choice):
    if choice_name=="石头" and (comp_choice=="蜥蜴" or comp_choice=='剪刀'):
	    print('你赢了')
    elif choice_name=='石头' and (comp_choice=='纸' or comp_choice=='史波克'):
        print('电脑赢了')
    elif choice_name=='石头' and comp_choice=='石头':
        print('平局')
    elif choice_name=='史波克' and comp_choice=='史波克':
	    print('平局')
    elif choice_name=='史波克' and (comp_choice=='剪刀' or comp_choice=='石头'):
	    print('你赢了')			
    elif choice_name=='史波克' and (comp_choice=='蜥蜴' or comp_choice=='布'):
	    print('电脑赢了')
    elif choice_name=='纸' and (comp_choice=='史波克' or comp_choice=='石头'):
	    print('你赢了')
    elif choice_name=='纸' and (comp_choice=='剪刀' or comp_choice=='蜥蜴'):
	    print('电脑赢了')
    elif choice_name=="纸" and comp_choice=="纸":
	    print('平手')
    elif choice_name=='剪刀' and comp_choice=='纸' or comp_choice=='蜥蜴':
	    print('你赢了')
    elif choice_name=='剪刀' and comp_choice=='石头' or comp_choice=='史波克':
	    print('电脑赢了')
    elif choice_name=='剪刀' and comp_choice=='剪刀':
	    print('平手')
    elif choice_name=='蜥蜴' and comp_choice=='蜥蜴':
        print('平手')
    elif choice_name=='蜥蜴' and comp_choice=='史波克' or comp_choice=='纸':
	    print('你赢了')
    elif choice_name=='蜥蜴' and comp_choice=='剪刀' or comp_choice=='石头':
        print('电脑赢了')
rpsls(choice_name,comp_choice)

