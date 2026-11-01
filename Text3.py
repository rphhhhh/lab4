def parse_weather(raw_data):
    return [(d.strip(), int(t)) for d, t in (s.split("|") for s in raw_data)]  # "Пн | 15" -> ("Пн", 15)
def calculate_average_temp(weather):
    return sum(t for _, t in weather) / len(weather)  # сумма / число дней
def find_hottest_day(weather):
    return max(weather, key=lambda x: x[1])  # день с макс. температурой
def find_coldest_day(weather):
    return min(weather, key=lambda x: x[1])  # день с мин. температурой
def count_warm_cold_days(weather, threshold):
    warm = sum(t >= threshold for _, t in weather)  # True = 1, считаем тёплые
    return warm, len(weather) - warm  # остальные холодные

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
raw_data = [f"{d} | {input(f'{d}: ')}" for d in days]  # вводим температуру по каждому дню
weather = parse_weather(raw_data)

print(f"\nСредняя: {calculate_average_temp(weather):.1f}°C")
print("Самый тёплый:", find_hottest_day(weather))
print("Самый холодный:", find_coldest_day(weather))
print("Тёплых/холодных:", count_warm_cold_days(weather, calculate_average_temp(weather)))  # порог = средняя