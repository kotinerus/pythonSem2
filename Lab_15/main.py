typesofCoffe = ['Black','Latte','Cappuccino','Americano','Espresso','Doppio']

for i in range(len(typesofCoffe)):
    if i==0:
        print("- - - - - - - - - - - -\n| " + typesofCoffe[i]+ "\n- - - - - - - - - - - -")
    elif i==len(typesofCoffe)-1:
        print("| " + typesofCoffe[i] + "\n- - - - - - - - - - - -")
    else:
        print("| "+typesofCoffe[i]+ "\n- - - - - - - - - - - -")