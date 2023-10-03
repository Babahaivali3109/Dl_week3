r1=int(input("Enter number of Rows of Matrix A:"))
c1=int(input("Enter nu,mber of Columns of matrix A:"))
r2=int(input("Enter number of Rows of Matrix B:"))
c2=int(input("Enter nu,mber of Columns of matrix B:"))
if(r1==r2 and c1==c2):
    A=[]
    print("Enter the element::>")
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(int(input()))
        A.append(row)
    print(A)
    print("Display Array in matrix form")
    for i in range(r1):
        for j in range(c1):
            print(A[i][j],end=" ")
        print()
    B=[]
    B=[] 
    print("Enter the element ::>") 
    for i in range (r2): 
        row=[] 
        for j in range(c2): 
            row.append(int(input()))
        B.append(row)
    print(B)
    print("Display Array In Matrix Form") 
    for i in range(r2): 
        for j in range(c2): 
            print(B[i][j], end=" ") 
        print()
    S=[[0 for i in range(c2)] for j in range(r2)] 
    for i in range(len(A)): 
        for j in range(len(B)):
            S[i][j]=A[i][j]+B[i][j]
    print("Product of Matrices A and B: ") 
    for i in range(r1): 
        for j in range(c2): 
            print(S[i][j],end=" ") 
        print() 
    else: 
        print("Matrix Addition is not possible.") 







 
