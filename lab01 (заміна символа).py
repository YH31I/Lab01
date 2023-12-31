"""
Задача №4: Напишіть програму, щоб у введеному користувачем рядку виконати обмін місцями першого та останнього символів.
Умова задачі: Напишіть програму для друку літери Ж висотою 5 рядків за допомогою введеного користувачем символу.
Автор: Гладкович Ярослав 31І

"""

 # Запит користувача на введення рядка
user_input = input("Введіть рядок: ")

# Перевірка, чи рядок має більше одного символу
if len(user_input) > 1:  
    # Обмін першого та останнього символу у рядку
    swapped_string = user_input[-1] + user_input[1:-1] + user_input[0]  

     # Виведення обміненого рядка
    print(swapped_string) 
     # Виведення введеного рядка, якщо він складається з одного символу
else:
    print(user_input)  
