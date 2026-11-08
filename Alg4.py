#«Анализатор паролей безопасности» — Поиск самой длинной
#подстроки без повторений
#Легенда:
#Вы разрабатываете модуль оценки надёжности паролей для корпоративной
#системы безопасности. Один из критериев стойкости пароля - длина самой
#длинной последовательности уникальных символов (без повторений).
#Чем длиннее такая последовательность, тем выше энтропия пароля и тем
#сложнее его взломать.
#Ваша задача — написать функцию, которая находит длину самой длинной
#подстроки без повторяющихся символов в заданном пароле.
def longest_unique_naive(password):
    best_len, best_start = 0, 0
    n = len(password)
    for i in range(n):  # начало
        for j in range(i, n):  # конец
            sub = password[i:j + 1]
            if len(set(sub)) == len(sub) and len(sub) > best_len:  # уникальна и длиннее лучшей
                best_len, best_start = len(sub), i
    return best_len, password[best_start:best_start + best_len], best_start
def longest_unique_optimized(password):
    last_seen = {}  # символ -> последняя позиция
    left = best_len = best_start = 0
    for right, ch in enumerate(password):
        if ch in last_seen and last_seen[ch] >= left:  # повтор внутри окна
            left = last_seen[ch] + 1  # сдвигаем левую границу
        last_seen[ch] = right
        if right - left + 1 > best_len:  # окно длиннее лучшего
            best_len, best_start = right - left + 1, left
    return best_len, password[best_start:best_start + best_len], best_start
password = "abcabcbb"
for f in (longest_unique_naive, longest_unique_optimized):
    length, sub, pos = f(password)
    print(f"{f.__name__}: длина = {length}, подстрока = '{sub}', позиции {pos}-{pos + length - 1}")
