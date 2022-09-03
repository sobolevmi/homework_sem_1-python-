# Программа, рассчитывающая расстояние между двумя точками на плоскости

coordinate_x_1 = int(input("Введите значение координаты X точки А: "))
coordinate_y_1 = int(input("Введите значениe координаты Y точки А: "))
coordinate_x_2 = int(input ("Введите значение координаты X точки B: "))
coordinate_y_2 = int(input("Введите значение координаты Y точки B: "))

from math import hypot
result = hypot((coordinate_x_2 - coordinate_x_1), (coordinate_y_2 - coordinate_y_1))
print(f"- А ({coordinate_x_1},{coordinate_y_1}); B ({coordinate_x_2},{coordinate_y_2}) -> {round(result, 3)}")
