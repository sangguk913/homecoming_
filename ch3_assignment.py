#1330
A, B = map(int, input().split(' '))
if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')

#9498
score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

#2753
Y = input()
Y = int(Y)
if Y%4==0:
    if Y%100!=0:
        print('1')
    elif Y%400==0:
        print('1')
    else:
        print('0')
else:
    print('0')

#14681
x=int(input())
y=int(input())
if x>0 and y>0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
else:
    print('4')
