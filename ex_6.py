list_ex6 = []
while True:
        list_ex6.append((input("Номер товара: "),
                       {"Название": input("Название: "),
                        "Цена": input("Цена: "),
                        "Количество": input("Количество: "),
                        "ед.": input("Единицы учёта: ")}))
        q = input("Закончить ввод позиций? Да, Нет: ")
        if q == "Да":
            break

    # my_lst = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    #          (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    #         (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]

names_lst = []
prices_lst = []
counts_lst = []
units_lst = []
new_dict = {}
for i in range(len(list_ex6)):
       names_lst.append(list_ex6[i][1]['Название'])
       prices_lst.append(list_ex6[i][1]['Цена'])
       counts_lst.append(list_ex6[i][1]['Количество'])
       units_lst.append(list_ex6[i][1]['ед.'])

new_dict.update({'Название': names_lst, 'Цена': prices_lst, 'Количество': counts_lst, 'ед.': units_lst})
print(new_dict)