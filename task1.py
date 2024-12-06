import math
import matplotlib.pyplot as plt # type: ignore

class Point_17:
    # Лічильник для кількості екземплярів
    point_count = 0
    
    def __init__(self, x=0, y=0):
        # Ініціалізація координат точки
        self.__x = x
        self.__y = y
        Point_17.point_count += 1  # Збільшуємо лічильник при створенні нового екземпляра

    def __del__(self):
        # Деструктор: зменшуємо лічильник при видаленні екземпляра
        Point_17.point_count -= 1
        print(f"Object with coordinates ({self.__x}, {self.__y}) destroyed!")
    
    @property
    def x(self):
        # Геттер для координати x
        return self.__x

    @x.setter
    def x(self, value):
        # Сеттер для координати x з перевіркою меж
        self.__x = value if -100 <= value <= 100 else 0

    @property
    def y(self):
        # Геттер для координати y
        return self.__y

    @y.setter
    def y(self, value):
        # Сеттер для координати y з перевіркою меж
        self.__y = value if -100 <= value <= 100 else 0
    
    @classmethod
    def get_point_count(cls):
        # Метод класу для отримання кількості точок
        return cls.point_count
    
    def move(self, dx, dy):
        # Метод для зсуву точки на dx по осі x та dy по осі y
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        # Метод для розрахунку відстані між поточною точкою та іншою
        return math.sqrt((self.__x - other.x) ** 2 + (self.__y - other.y) ** 2)

    def __str__(self):
        # Строкове представлення точки
        return f"Point({self.__x}, {self.__y})"

# Створюємо список з трьох точок
point1 = Point_17(10, 20)
point2 = Point_17(30, 40)
point3 = Point_17(50, 60)

# Виводимо кількість створених точок
print(f"Total points created: {Point_17.get_point_count()}")

# Порахувати відстань між другою та третьою точками
distance = point2.distance_to(point3)
print(f"Distance between point2 and point3: {distance}")

# Переміщаємо першу точку на 50 одиниць вгору
point1.move(0, 50)
print(f"After moving, point1 is at: {point1}")

# Виведемо кількість точок після змін
print(f"Total points after moving: {Point_17.get_point_count()}")

# Створюємо графік до змін
plt.figure(figsize=(5,5))
plt.scatter([point1.x, point2.x, point3.x], [point1.y, point2.y, point3.y], color='blue')
plt.text(point1.x, point1.y, 'Point1', fontsize=12, ha='right')
plt.text(point2.x, point2.y, 'Point2', fontsize=12, ha='right')
plt.text(point3.x, point3.y, 'Point3', fontsize=12, ha='right')
plt.title('Points before moving')
plt.grid(True)
plt.show()

# Створюємо графік після змін
plt.figure(figsize=(5,5))
plt.scatter([point1.x, point2.x, point3.x], [point1.y, point2.y, point3.y], color='red')
plt.text(point1.x, point1.y, 'Point1', fontsize=12, ha='right')
plt.text(point2.x, point2.y, 'Point2', fontsize=12, ha='right')
plt.text(point3.x, point3.y, 'Point3', fontsize=12, ha='right')
plt.title('Points after moving')
plt.grid(True)
plt.show()

# Зберігаємо координати точок у файл
with open("points.txt", "w") as f:
    if Point_17.get_point_count() % 2 != 0:  # Для непарних варіантів
        f.write(f"1: {point1.x}; {point1.y}\n")
        f.write(f"2: {point2.x}; {point2.y}\n")
        f.write(f"3: {point3.x}; {point3.y}\n")
    else:  # Для парних варіантів
        f.write(f"1: {point1.x}:{point1.y}\n")
        f.write(f"2: {point2.x}:{point2.y}\n")
        f.write(f"3: {point3.x}:{point3.y}\n")

print("Coordinates saved to 'points.txt'.")

