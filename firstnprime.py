i=1 
x = int(input("Enter the number:")) 
counter = 0 
while True: 
    factor=0; 
    for j in range (1, (i+1), 1): 
        a = i%j 
        if (a==0): 
            factor =factor +1 
    if (factor==2): 
        print (i) 
        counter = counter + 1 
        if counter >= x: 
            break 
    i=i+1 
