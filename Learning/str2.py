name = "Vasyan"
age = 26

# привести age к соответствующему типу, для возможности конкатенации
print("My name is" + name + "." + " I'm " + str(age))

print(name * 3)

# индексация последнего символа
print(name[-1])

# срезы позволяют получить последовательность символов
some_text = "ту-ту-туВЫСТРЕЛту-ту-ту"
print(some_text[8:15])

# если в диапазоне символов нет, то ошибку не получим
print(some_text[8:50])

# опустить каждый 2й символ
print(some_text[::2])

# строка наоборот
print(some_text[::-1])