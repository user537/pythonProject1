# capitalize - первая заглавная буква
x = "aaabbb"
print(x.capitalize())

# title - capitalize all first letters
y = "row, row, row your boat\n\
Gently down the stream\n\
Merrily merrily, merrily, merrily\n\
Life is but a dream"
print(y.title())

# casefold - str to lower case
z = "Row, Row, Row Your Boat\n\
Gently Down The Stream\n\
Merrily Merrily, Merrily, Merrily\n\
Life Is But A Dream"
print(z.casefold())

# длина строки
print(len(z))

# отцентровать
print(x.center(20, "!"))

# кол-во символов
print(x.count("a"))

#найти позицию первого вхождения символа
print(x.find("a"))

# split - Splits the string at the specified separator, and returns a list
# splitlines - splits the string at line breaks and returns a list
fruits = "Apple Orange Banana"
print(fruits.split())
print(fruits.splitlines())

# состоит ли строка только лижь из цифр?
a = "12"
b = "12ab"
print(a.isdigit())
print(b.isdigit())