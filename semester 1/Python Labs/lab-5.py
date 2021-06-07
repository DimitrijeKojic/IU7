import sys

while True:
    x,eps,i,inter = map(float,input("Введите аргумент, точность, шаг печати, максмальное значение интераций: ").split())
    if inter > 0 and i > 0:
        break
    elif i <= 0 or inter <= 0:
        print("Ошибка ввода")
        print("Шаг печати больше нуля.")
        print("Максимальное значение интераций больше нуля.")
    else:
        print("Ошибка ввода")
n = 0 # значение n для 
b = 1 # использую для вычисления шага печати
t = 1 # член ряда
S = 0 # sum
num = 1 # номер интерации
print("\n"+"-"*68)
print("|{:^20}|{:^20}|{:^24}|".format("Номер итерации","Текущий член ряда","Текущее значение суммы"))
print("-"*68)
while abs(t) > eps:
    if num <= int(inter): 
        if (num%2 == 0):
            t = -(n+1)*(n+2)*x**n/2
        else:
            t = (n+1)*(n+2)*x**n/2
        S += t # Текущее значение суммы
        if num == b:
            print("|{:^20}|{:^20}|{:^24}|".format(f'{num:.10g}', f'{t:.10g}', f'{S:.10g}'))

            b += i
        num += 1 
        n += 1   
    else:
        print("-"*68)
        print('\nРяд не сошелся (не достигнута заданная точность) за максимальное количество итераций')
        sys.exit()
else:
    print("-"*68)
    print("Сумма ряда: {:.10g}".format(S), 'и количество интераций:', num-1)
    

