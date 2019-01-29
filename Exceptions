text = input()
text_list = text.split()
try:
    len(text_list) != 3
    sign = text_list[0]
    num1 = text_list[1]
    num2 = text_list[2]
    assert sign in ['+', '-', '*', '/'], 'Такой операции нет в списке доступных'
    try:
       num1 = int(text_list[1])
       num2 = int(text_list[2])
       if "+" in sign:
          print("Результат сложения:", (num1 + num2))
       elif "-" in sign:
          print("Результат вычитания:", (num1 - num2))
       elif '*' in sign:
          print("Результат умножения:", (num1 * num2))
       elif '/' in sign:
          if num2 == 0:
             try:
                print(num1 / num2)
             except ZeroDivisionError:
                print('На ноль делить нельзя')
          else:
             print("Результат деления:", (num1 / num2))
    except Exception:
       print('Введены не числа. Строки делить нельзя')
except Exception:
    print('Введено неверное количество аргументов')

print('Конец выполнения Задачи1 и Задачи2')
print('Начало выполнения Задачи3')

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

try:
    def people_names():
       for people_names in documents:
           print(people_names["name"])
    people_names()
except KeyError:
    print('Поле "name" нет в документе')