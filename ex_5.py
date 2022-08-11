list_ex5 = [7,5,3,3,2]
while True:
    new_rate = input("Укажите новый рейтинг или q для выхода:")
    if new_rate!='q':
        list_ex5.append(int(new_rate))
        list_ex5.sort(reverse=True)
        print(list_ex5)
    else:break

