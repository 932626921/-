#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����γ�
���ڣ�2019.11.20
"""

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
print('--------------')
choice_name=input()
def ball(choice_name):
    if choice_name!='ʯͷ' and choice_name!='ʷ����' and choice_name!='ֽ' and choice_name!='����' and choice_name!='����':
      print('Error:No Correct Name')
    else:
     print('����ѡ��Ϊ:%s'%choice_name)
ball(choice_name)
import random
number=random.randint(0,4)
def number_to_name(number):
     if number==0:
        return('ʯͷ')              
     if number==1:
       return('ʷ����')
     if number==2:
       return('ֽ')
     if number==3:
       return('����')
     if number==4:
       return('����')                        
comp_choice=number_to_name(number)
print('���Ե�ѡ��Ϊ:%s'%comp_choice)
def rpsls(choice_name,comp_choice):
    if choice_name=="ʯͷ" and (comp_choice=="����" or comp_choice=='����'):
	    print('��Ӯ��')
    elif choice_name=='ʯͷ' and (comp_choice=='ֽ' or comp_choice=='ʷ����'):
        print('����Ӯ��')
    elif choice_name=='ʯͷ' and comp_choice=='ʯͷ':
        print('ƽ��')
    elif choice_name=='ʷ����' and comp_choice=='ʷ����':
	    print('ƽ��')
    elif choice_name=='ʷ����' and (comp_choice=='����' or comp_choice=='ʯͷ'):
	    print('��Ӯ��')			
    elif choice_name=='ʷ����' and (comp_choice=='����' or comp_choice=='��'):
	    print('����Ӯ��')
    elif choice_name=='ֽ' and (comp_choice=='ʷ����' or comp_choice=='ʯͷ'):
	    print('��Ӯ��')
    elif choice_name=='ֽ' and (comp_choice=='����' or comp_choice=='����'):
	    print('����Ӯ��')
    elif choice_name=="ֽ" and comp_choice=="ֽ":
	    print('ƽ��')
    elif choice_name=='����' and comp_choice=='ֽ' or comp_choice=='����':
	    print('��Ӯ��')
    elif choice_name=='����' and comp_choice=='ʯͷ' or comp_choice=='ʷ����':
	    print('����Ӯ��')
    elif choice_name=='����' and comp_choice=='����':
	    print('ƽ��')
    elif choice_name=='����' and comp_choice=='����':
        print('ƽ��')
    elif choice_name=='����' and comp_choice=='ʷ����' or comp_choice=='ֽ':
	    print('��Ӯ��')
    elif choice_name=='����' and comp_choice=='����' or comp_choice=='ʯͷ':
        print('����Ӯ��')
rpsls(choice_name,comp_choice)

