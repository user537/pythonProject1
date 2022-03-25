import json
from itertools import count

#Вроде этот кусок кода бесполезен
#Нужно написать парсер для Json и потом уже сделать так, чтобы id добавлялся +1
student_id_gen = count()
teacher_id_gen = count()
classroom_id_gen = count()

students = []
teachers = []
classroom = []

with open("storage.json") as fp:
    data = json.load(fp)
    students = data["students"]

template_students = "Добавлен учащийся. Имя: {}. Возраст: {}. Пол: {}. Характеристика: {}"
template_teachers = "Добавлен преподаватель. ФИО: {}. Предмет: {}. Рейтинг: {}."
template_classroom = "Добавлен предмет. Кол-во учеников: {}. Буква: {}. Список предметов: {}"

# print("введите команду(добавить ученика, добавить учителя, добавить класс)")
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
    students.append(dict(name=name, age=age, gender=gender, description=description, id=next(student_id_gen)))
    with open('students.json', 'a') as f:
        f.write(f"{name},{age},{gender},{description},{student_id_gen}\n")

    print(template_students.format(students[-1]["name"], students[-1]["age"], students[-1]["gender"],
                                   students[-1]["description"]))

    # Добавить преподавателя
elif command == "2":
    print(" введите ФИО")
    name = input()
    print(" введите предмет")
    subject = input()
    print(" введите рейтинг")
    rating = input()
    teachers.append(dict(name=name, subject=subject, rating=rating, id=next(teacher_id_gen)))
    with open('teachers.csv', 'a') as f:
        f.write(f"{name},{subject},{rating},{teacher_id_gen}\n")
    print(template_teachers.format(teachers[-1]["name"], teachers[-1]["subject"], teachers[-1]["rating"]))

    # Добавить предмет
elif command == "3":
    print(" введите кол-во учеников")
    students_count = input()
    print(" введите буква(имя класса)")
    letter = input()
    print(" введите список предметов")
    subject_list = input()
    classroom.append(
        dict(students_count=students_count, letter=letter, subject_list=subject_list, id=next(classroom_id_gen)))
    print(template_classroom.format(classroom[-1]["students_count"], classroom[-1]["letter"],
                                    classroom[-1]["subject_list"]))
else: print("Нет такой темы")

# command = input()
with open("winter_storage.json", "w") as fp:
    json.dump(dict(students=students, teachers=teachers), fp)

print(students)