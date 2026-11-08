#Бесконечный генератор Пифагоровых троек
#Легенда: Вы работаете в отделе криптографии, которому нужны
#уникальные геометрические константы. Вам нужно найти все Пифагоровы
#тройки (a,b,c), где a^2+b2=c^2
from itertools import count, islice

def pythagorean_triples():
    for c_limit in count(2):  # растём по m, чтобы перебор шёл в бесконечность
        m = c_limit
        for n in range(1, m):  # m > n > 0
            yield m*m - n*n, 2*m*n, m*m + n*n  # формула Евклида (a, b, c)

for a, b, c in islice(pythagorean_triples(), 10):  # берём первые 10 троек
    print(f"({a}, {b}, {c})  проверка: {a*a + b*b == c*c}")
