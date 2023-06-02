
# 1. Составить алгоритм: если введенное число больше 7, то вывести “Привет”
# Решение:

number = int(input("Ввдите число: "))
if (number > 7):
   print("Привет")

# 2.Составить алгоритм: если введенное имя совпадает с Вячеслав,
# то вывести “Привет, Вячеслав”, если нет, то вывести "Нет такого имени"
# Решение:

name = input("Введите ваше имя: ")
if (name=="Вячеслав"):
   print("Привет,Вячеслав!")
else:
   print("Нет такого имени.")

# 3.Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3.
# Решение:

count_elements = int(input("Введите кол-во элементов массива: "))
array = [int(input("Введите число: "))for i in range(count_elements)]
print(array)
for i in array:
   if (i % 3 == 0):
      print("Элемент массива кратный 3: ", i)

# 4.Дана скобочная последовательность: [((())()(())]]
# - Можно ли считать эту последовательность правильной?
# - Если ответ на предыдущий вопрос “нет” - то что необходимо в ней изменить, чтоб она стала правильной?
#
#    Ответ: Последовательность не правильная т.к. нет одной открывающей скобки "["
#    и нет одной закрывающей скобки ")"
#    Можно либо добавить отсутствуюшие элементы ,либо удалить не парные элементы.
