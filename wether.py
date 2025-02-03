# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import numpy as np
import matplotlib.pyplot as plt
num_days = 365
temperatures = np.random.uniform(-10, 35, num_days)
average_temp = np.mean(temperatures)
hot_days = np.sum(temperatures > 25)
max_cold_streak = 0
current_cold_streak = 0
for temp in temperatures:
    if temp < 0:
        current_cold_streak += 1
    else:
        max_cold_streak = max(max_cold_streak, current_cold_streak)
        current_cold_streak = 0
max_cold_streak = max(max_cold_streak, current_cold_streak)
plt.figure(figsize=(12, 6))
cold_days_indices = np.where(temperatures < 0)[0]
plt.scatter(cold_days_indices, temperatures[cold_days_indices], color='blue', s=20, label='Холодные дни')
hot_days_indices = np.where(temperatures > 25)[0]
plt.scatter(hot_days_indices, temperatures[hot_days_indices], color='red', s=20, label='Жаркие дни')
plt.plot(range(num_days), temperatures, color='gray', linestyle='-', label='Температура')
plt.xlabel("День")
plt.ylabel("Температура (°C)")
plt.title("Годовой график температуры")
plt.grid(axis='y', alpha=0.75)
plt.legend()
plt.show()
plt.figure(figsize=(8, 6))
plt.hist(temperatures, bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Температура (°C)")
plt.ylabel("Количество дней")
plt.title("Распределение температур за год")
plt.grid(axis='y', alpha=0.75)
plt.show()
print(f"Средняя температура за год: {average_temp:.2f}°C")
print(f"Количество дней с температурой выше 25°C: {hot_days}")
print(f"Самая длинная последовательность дней с температурой ниже 0°C: {max_cold_streak}")