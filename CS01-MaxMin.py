Num = int(input("Enter your loop "))
Numtotal = []

for i in range(Num):
    data = int(input('Enter your data: '))
    Numtotal += [data]
Numtotal.sort()


print(Numtotal[0]) 
print(Numtotal[-1])