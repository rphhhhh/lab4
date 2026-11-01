def is_pal(n):
    return str(n) == str(n)[::-1]  # палиндром

def mirror_universe(n, step, max_steps, path):
    path.append(n)
    if is_pal(n) or step >= max_steps:  # нашли палиндром или кончился лимит
        return is_pal(n), step
    return mirror_universe(n + int(str(n)[::-1]), step + 1, max_steps, path)  # число + реверс

def mirror_loop(n, max_steps):
    path, step = [n], 0 # путь начинается с исходного числа, шагов пока 0
    while not is_pal(n) and step < max_steps:
        n += int(str(n)[::-1])
        step += 1
        path.append(n)
    return is_pal(n), step, path

n = int(input("Начальное число: "))
max_steps = int(input("Лимит шагов (50-100): "))

path = [] #карта шагов для рекурсии
found, steps = mirror_universe(n, 0, max_steps, path) # запуск рекурсивной версии
found2, steps2, path2 = mirror_loop(n, max_steps) # запуск версии с циклом

if found:
    print(f"Путь к Палиндрому! Шагов: {steps}\n" + " -> ".join(map(str, path)))
else:
    print(f"ВНИМАНИЕ: Обнаружен Парадокс Лихрела (число {n}-типа)")
print("Рекурсия и цикл совпадают:", (found, steps, path) == (found2, steps2, path2))