name = "Vasyan"
age = 30

# именные маркеры
#print("My name is %(name)s. I\'m %(age)s") %{"name" : name, "age" : age}

# позиционные маркеры
print("My name is {}. I\'m {}".format(name, age))