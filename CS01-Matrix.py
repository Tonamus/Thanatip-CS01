import numpy as np


MatrixOne = []
MatrixTwo = []
loop = 1
MatrixColumns =  int(input("EnterYourColumn : "))
MatrixRows =  int(input("EnterYourRows : "))
while(loop <= 2):
    print("EnterYourMatrix", loop)
    for i in range(MatrixRows) :
        for j in range(MatrixColumns) :
            print("MatrixColumns [",i,",",j,"] :", end ="")
            if(loop ==1):
                MatrixOneInput = int(input(""))
                MatrixOne.append(MatrixOneInput)
            else:
                MatrixTwoInput = int(input(""))
                MatrixTwo.append(MatrixTwoInput)
    loop += 1 
NumpyMatrixOne = np.asarray(MatrixOne)
NumpyMatrixTwo = np.asarray(MatrixTwo)
NewMatrixOne=NumpyMatrixOne.reshape(MatrixRows,MatrixColumns)
NewMatrixTwo=NumpyMatrixTwo.reshape(MatrixRows,MatrixColumns)
print(NewMatrixOne,"\n=========================")
print(NewMatrixTwo,"\n=========================")
sum = np.add(NewMatrixTwo, NewMatrixTwo)
print(sum)














"""import numpy as np
arry=[]
array=[]
m=int (input("enter the height you want for ur matrix to be "))
n=int (input("enter the width you want for ur matrix to be "))
x=m*n
print ("enter number for your first array")
for i in range(x):
    arry+=[int(input(""))]
NewAray = np.asarray(arry)
print ("enter number for your second array")
for j in range(x):
    array+=[int(input(""))]
NewAray = np.asarray(array)
NewArray = np.asarray(arry)
NewArrayNumpy = NewArray.reshape(int(m),n)
print(NewArrayNumpy)
NewArryNumpy = NewAray.reshape(int(n),m)
print(NewArryNumpy)
y=np.add(NewArrayNumpy,NewArryNumpy)
print(y)"""