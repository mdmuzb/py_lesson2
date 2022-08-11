list_ex4 = input("Введите строку разделяя пробелами").split(" ")
n=1
for elem in list_ex4:
   # if len(elem)>10:
    print(f"№ {n}. {elem[:10]}" )
    #else: print(f"№ {n}. {elem}" )
    n+=1
