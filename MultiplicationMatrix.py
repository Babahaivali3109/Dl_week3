r1=int(input("Enter number of Rows of Matrix A: ")) 
c1=int(input("Enter number of Columns of Matrix A: ")) 
r2=int(input("Enter number of Rows of Matrix B: ")) 
c2=int(input("Enter number of Columns of Matrix B: ")) 
if(c1==r2):
    A=[]
    print("Enter the element ::>")
    for i in range(r1): 
        row=[] 
        for j in range(c2): 
            row.append(int(input())) 
        A.append(row) 
    print(A) 
    print("Display Array In Matrix Form") 
    for i in range(r1): 
        for j in range(c1): 
            print(A[i][j], end=" ") 
        print() 
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
    P=[[0 for i in range(c2)] for j in range(r1)] 
    for i in range(len(A)): 
        for j in range(c2): 
            for k in range(len(B)): 
                P[i][j]=P[i][j]+(A[i][k]*B[k][j]) 
    print("Product of Matrices A and B: ") 
    for i in range(r1): 
        for j in range(c2): 
            print(P[i][j],end=" ") 
        print() 
    
