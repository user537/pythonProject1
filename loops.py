"""
i = 0
while i < 11:
  print(i)
  i += 1

for i in range(10):
  print(i)
  if i == 5:
    break
  else:
    continue

for i in range(10):
  if i < 5:
    continue
  print(i)

lis = [1,2,3,4,5]
for i in lis:
    print(i)
else:
    print("zalupa")

while True:
    print("a")
"""

fac = 1
number = int(input("Введите число"))
while fac != number:
    number = number * (fac + 1)
    print(number)