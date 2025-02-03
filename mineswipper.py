# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
#
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import ListedColormap
size = 10
num_mines = 15
field = np.zeros((size, size), dtype=int)
mine_indices = np.random.choice(size * size, num_mines, replace=False)
mine_rows = mine_indices // size
mine_cols = mine_indices % size
field[mine_rows, mine_cols] = -1
for row in range(size):
    for col in range(size):
        if field[row, col] == -1:
            continue
        mine_count = 0
        for i in range(max(0, row - 1), min(size, row + 2)):
            for j in range(max(0, col - 1), min(size, col + 2)):
                if field[i, j] == -1:
                    mine_count += 1
        field[row, col] = mine_count
mine_color_map = ListedColormap(['white', 'red'])
plt.figure(figsize=(7, 7))
plt.imshow(field == -1, cmap=mine_color_map,
           extent=[0, size, 0, size])
plt.xticks(np.arange(size))
plt.yticks(np.arange(size))
plt.title("Игровое поле (мины красным)")
plt.grid(color='black', linewidth=0.5)
plt.show()
plt.figure(figsize=(7, 7))
plt.imshow(field, cmap='viridis', extent=[0, size, 0, size])
plt.xticks(np.arange(size))
plt.yticks(np.arange(size))
for i in range(size):
    for j in range(size):
        plt.text(j + 0.5, i + 0.5, str(field[i, j]), ha='center', va='center',
                 color='white' if field[i, j] > 4 else 'black')
plt.title("Игровое поле с количеством мин вокруг")
plt.grid(color='black', linewidth=0.5)
plt.show()

print("Поле в виде матрицы:")
print(field)