def liczenie(clk,rst,q):
    wartost = q
    if (rst == 0):
        print("11110000")
    elif(clk>0 and clk==1):
        wartost+=1
    print(wartost)

liczenie(1,0,3)
liczenie(0,1,5)
liczenie(1,1,7)
liczenie(0,0,9)
