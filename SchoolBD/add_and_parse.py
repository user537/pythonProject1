import json

students = []

template_students = "Добавлен учащийся. Имя: {}. Возраст: {}. Пол: {}. Характеристика: {}"

command = input("введите команду(1 - Добавить ученика, 2 - Добавить учителя, 3 - Добавить класс)")
if command == "1":
    print(" введите ФИО")
    name = input()
    print(" введите возраст")
    age = input()
    print(" введите пол")
    gender = input()
    print(" введите краткую характеристику")
    description = input()

dictionary ={
    "Name": name,
    "Age": age,
    "Gender": gender,
    "Description": description
}
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)