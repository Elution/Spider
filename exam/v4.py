for k in range (0,4):
    if k==0 or k==3:
        print ("* "*5,end="")
    if k == 1 or k == 2:
        for j in range (5):
            if j==0 or j==4:
                print("* ", end="")
            else:
                print("  ", end="")
    print ()