r1=int(input("Enter number of Rows of Matrix A: ")) 
c1=int(input("Enter number of Columns of Matrix A: ")) 
A=[] 
print("Enter the element ::>") 
for i in range(r1): 
    row=[] 
    for j in range(c1): 
        row.append(int(input())) 
    A.append(row) 
print(A) 
print("Display Array In Matrix Form") 
for i in range(r1): 
    for j in range(c1): 
        print(A[i][j], end=" ") 
    print() 
transResult= [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))] 
print("The transpose of matrix A is: ") 
for res in transResult: 
    print(res) 
