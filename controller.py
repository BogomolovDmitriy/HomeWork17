import os

# определяем путь к файлу
def path(name_file): 
    path = os.path.abspath(name_file) 
    return path

# считываем данные с базы данных
def get_base(file): 
    data = open(file, "r")
    line = list(i for i in data)
    data.close()
    return line

data_base = "base.txt" # файл базы данных txt
data_base_csv = "base_csv.csv" # файл базы данных csv
data_base_json = "base_json.json" # файл базы данных json


