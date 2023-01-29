import json
import controller as contr
import view

def start():
    pos = [find_worker, selection_post, selection_salary,  add_worker, del_worker,
    udate_worker, import_json, import_csv, exit]
    return pos[view.show_menu() - 1]()


# поиск сотрудника
def find_worker():
    base = contr.get_base(contr.data_base)
    name = input("Введите фамилию сотрудника: ")
    data = list(i for i in base if name in i)
    if len(data) > 0:
        print(data)
    else:
        print("Такого сотрудника нет.")
    return data

# выборка сотрудников по должности
def selection_post():
    base = contr.get_base(contr.data_base)
    post = input("Введите должность: ")
    data = list(i for i in base if post in i)
    if len(data) > 0:
        print(data)
    else:
        print("Такой должности нет.")
    return data

# выборка сотрудников по зарплате
def selection_salary():
    base = contr.get_base(contr.data_base)
    post = input("Введите оклад: ")
    data = list(i for i in base if post in i)
    if len(data) > 0:
        print(data)
    else:
        print("Такого оклада нет.")
    return data


# создать сотрудника
def add_worker():
    file = contr.data_base
    name = input("Введите фамилию сотрудника: ")
    post = input("Введите должность сотрудника: ")
    salary = input("Введие оклад сотрудника: ")
    with open(file, "a") as data:
        data.write('{} {} {}\n'.format(name, post, salary))

# удаление сотрудника
def del_worker():
    base = contr.get_base(contr.data_base)
    name = input("Введите фамилию сотрудника: ")
    temp = list(i for i in base if name in i)
    base.remove(temp[0])
    with open(contr.data_base, "w") as data:
        for i in base:
            data.write(i)
    return base
    

# обновление данных сотрудника
def udate_worker():
    base = contr.get_base(contr.data_base)
    name = input("Введите фамилию сотрудника, данные которого хотите изменить: ")
    temp = str(list(i for i in base if name in i)).split()
    temp1 = list(i for i in base if name in i)
    base.remove(temp1[0])
    with open(contr.data_base, "w") as data:
        for i in base:
            data.write(i)
    print(temp[0])
    file = contr.data_base
    temp[0] = input(f"Введите фамилию сотрудника: {temp[0]} ")
    temp[1] = input(f"Введите должность сотрудника: {temp[1]} ")
    temp[2] = input(f"Введие оклад сотрудника: {temp[2]} ")
    with open(file, "a") as data:
        data.write('{} {} {}\n'.format(temp[0], temp[1], temp[2]))
    return base

# импотр в формате json
def import_json():
    filename = contr.data_base
    dict1 = {}
    fields = ['name', 'post', 'salary']
    with open (filename) as fn:
        l = 1
        for line in fn:
            description = list(line.strip().split( None , 3))
            sno = 'emp' + str(l)
            i = 0
            dict2 = {}
            while i < len(fields):
                dict2[fields[i]] = description[i]
                i = i + 1
            dict1[sno] = dict2
            l += 1
    out_file = open ("base_json.json" , "w" )
    json.dump(dict1, out_file, indent = 3 )
    out_file.close()


# импорт в формате csv
def import_csv():
    filename = contr.data_base_csv
    data = contr.get_base(contr.data_base)
    with open(filename, "w", encoding="utf-8") as fout:
        for i in data:
            fout.write(i)

