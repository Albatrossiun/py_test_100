'=============================================================================='
'题目：输入三个整数x,y,z，请把这三个数由小到大输出。'
'''arr = []
for i in range(3):
    x = int(input('integer:\n'))
    arr.append(x)
arr.sort(reverse=True) '降序-True   升序-False'
print (arr)
'''


'=============================================================================='
'题目：输入某年某月某日，判断这一天是这一年的第几天？'
'''arr=[31,28,31,30,31,30,31,31,30,31,30,31]
while(1):
    mouth=int(input("请输入月份："))
    if((mouth>=1)and(mouth<=12)):
        break
days=0
i=0
while(i<=(mouth-1)):
    days+=arr[i]
    i=i+1
print(days)
'''



'=============================================================================='
'题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？'
'''for i in range(1,3000):
    for j in range(1,1000):
        if((i+100)==(j*j)):
            for k in range(1,1000):
                if((i+100+168)==(k*k)):
                    print(i)
                    break
'''



'=============================================================================='
'''
题目：企业发放的奖金根据利润提成。
程序分析：请利用数轴来分界，定位。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，
高于20万元的部分，可提成5%；
40万到60万之间时,
高于40万元的部分，可提成3%；
60万到100万之间时，
高于60万元的部分，可提成1.5%，
高于100万元时，
超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
'''i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)
'''



'==============================================================================='
'题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'
'程序分析：可填在百位、十位、个位的数字都是1、2、3、4。'
'程序分析：组成所有的排列后再去掉不满足条件的排列。'
'''for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print i,j,k
'''
