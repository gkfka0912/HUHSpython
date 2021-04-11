'''
운행소요시간 : 5~50
소요시간 5~15만 매칭
'''
from random import *

#while
i=1
customer_while=0
while i<=50:
    min=(randrange(5,51))
    if 5<= min <=15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,min))
        customer_while+=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,min))
    i=i+1
print("총 탑승 승객 : {0} 분".format(customer_while))

#for
customer_for=0
for customer in range(1,51):
    min=(randrange(5,51))
    if 5<= min <=15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer,min))
        customer_for+=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer,min))
print("총 탑승 승객 : {0} 분".format(customer_for))