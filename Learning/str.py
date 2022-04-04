print("Same")
print('thing')

# not_works = "this "shit" wrong"
print("Look like \"its\" 'worked' for me")

# табуляция, перенос строки
print("I'm not \tshure what is \ngoing on")

# Логическая строка != 2 физические
verse = "Oh tell me where your freedom lies\n\
The streets are fields that never die"
print(verse)

# запостить строку, содержащей путь и не обьебаться?
# для этого нужно объявить "сырую" строку

# тут будет все плохо
path = "C:\d\new.txt"
path_raw = r"C:\d\new.txt"

print(path)
print(path_raw)

# это конкатенация строк
s1 = "Пайтон"
s2 = " - "
s3 = "изян"
print(s1+s2+s3)