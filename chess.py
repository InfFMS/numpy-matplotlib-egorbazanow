# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
size = 8
board = np.zeros((size, size), dtype=int)
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 1:
            board[i, j] = 1
while True:
    try:
        q_row = int(input(f"Введите строку ферзя (0-{size-1}): "))
        q_col = int(input(f"Введите столбец ферзя (0-{size-1}): "))
        if 0 <= q_row < size and 0 <= q_col < size:
            break
        else:
            print("Неверные координаты. Пожалуйста, введите координаты в диапазоне доски.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целые числа.")
queen_pos = [q_row, q_col]
attacks = np.zeros((size, size), dtype=int)
attacks[q_row, :] = 1
attacks[:, q_col] = 1
for i in range(1, size):
    if q_row - i >= 0 and q_col + i < size:
        attacks[q_row - i, q_col + i] = 1
    if q_row + i < size and q_col + i < size:
        attacks[q_row + i, q_col + i] = 1
    if q_row + i < size and q_col - i >= 0:
        attacks[q_row + i, q_col - i] = 1
    if q_row - i >= 0 and q_col - i >= 0:
         attacks[q_row - i, q_col - i] = 1
attacks[q_row, q_col] = 2
cmap = matplotlib.colors.ListedColormap(['white', 'black', 'red', 'orange'])
bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
plt.imshow(attacks, cmap=cmap, norm=norm, extent=[0, size, size, 0])
plt.grid(True, color='gray', linewidth=0.5)
plt.xticks(np.arange(0, size, 1))
plt.yticks(np.arange(0, size, 1))
plt.text(q_col + 0.3, q_row + 0.3, f"({q_row},{q_col})", color="white")
plt.title("Шахматная доска с ферзем и атаками")
plt.show()