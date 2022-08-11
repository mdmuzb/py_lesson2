list_ex2 = input("Введите числа разделяя символом ""'/'"":").split('/')
i,j = 0,1
while len(list_ex2)>j:
    tmp = list_ex2[i]
    list_ex2[i]=list_ex2[j]
    list_ex2[j]=tmp
    i+=2
    j+=2
print(list_ex2)




