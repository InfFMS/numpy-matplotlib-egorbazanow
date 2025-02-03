# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import numpy as np
import matplotlib.pyplot as plt
num_rolls = 1000
rolls = np.random.randint(1, 7, num_rolls)
counts = np.zeros(6, dtype=int)
for roll in rolls:
    counts[roll - 1] += 1
probabilities = counts / num_rolls

max_streak = 0
current_streak = 0
prev_roll = None
for roll in rolls:
    if roll == prev_roll:
        current_streak += 1
    else:
        max_streak = max(max_streak, current_streak)
        current_streak = 1
    prev_roll = roll
max_streak = max(max_streak, current_streak)
plt.figure(figsize=(8, 6))
plt.bar(range(1, 7), counts, tick_label=range(1, 7))
plt.xlabel("Значение кубика")
plt.ylabel("Количество выпадений")
plt.title("Распределение результатов 1000 бросков игрального кубика")
plt.grid(axis='y', alpha=0.75)
plt.show()
print("Количество выпадений каждого значения:")
for i, count in enumerate(counts):
    print(f"Значение {i + 1}: {count} раз")

print("\nВероятности выпадения каждого значения:")
for i, prob in enumerate(probabilities):
    print(f"Значение {i + 1}: {prob:.3f}")

print(f"\nМаксимальное количество подряд выпавших одинаковых значений: {max_streak}")
