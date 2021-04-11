'''
 1. 1~20
 2. 무작위 추첨, 중복 X
 3. random과 shuffle 활용
'''
from random import *
id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #= range(1,21)
shuffle(id)

#1

f=(sample(id,4))
chi1=f[0]
cof1=[f[1],f[2],f[3]]
print("-- 당첨자 발표 --")
print("치킨 당첨자 :",chi1) #print("치킨 당첨자 : {0}".format(f[0]))
print("커피 당첨자 :",cof1) #print("커피 당첨자 : {0}".format(f[1:]))
print("-- 축하합니다 --")

#2

chi2=sample(id,1)
id.remove(chi2[0])
cof2=sample(id,3)
print("-- 당첨자 발표 --")
print("치킨 당첨자 :",int(chi2[0]))
print("커피 당첨자 :",cof2)
print("-- 축하합니다 --")