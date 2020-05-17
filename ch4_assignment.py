#2884
H, M = input().split()
H = int(H)
M = int(M)
if M >= 45:
    print(H, M-45)
else:
    if H is 0:
        print(23, (M+60)-45)
    else:
        print(H-1, (M+60)-45)

#1065
N_str = input()
N_str = int(N_str)

def f(a):
    if 100 <= a < 1000:
        if int(str(a)[2]) - int(str(a)[1]) == int(str(a)[1]) - int(str(a)[0]):
            return True
    if a < 100:
        return True

number_of_hansu = 0
for b in range(1, N_str + 1):
    if f(b) == True:
        number_of_hansu += 1

print(number_of_hansu)
