"""
Задача №3
Умова задачі: Напишіть програму для друку літери Ж висотою 5 рядків за допомогою введеного користувачем символу.

Автор: Гладкович Ярослав 31І

"""

s = input ("Уведіть символ")
print (f' {s}{s}  {s}{s}  {s}{s} '.format(s,s,s,s,s,s,s,s))
print (f'     {s}{s}{s}{s}  '.format(s,s,s,s,s,s,s,s))
print (f'     {s}{s}{s}{s}   '.format(s,s,s,s,s,s,s,s))
print (f'   {s}  {s}{s}  {s}   '.format(s,s,s,s,s,s,s,s))
print (f' {s}    {s}{s}    {s}  '.format(s,s,s,s,s,s,s,s)) 