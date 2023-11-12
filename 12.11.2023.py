# №1

# class Snow:
#
#     def __init__(self, count):
#         self.count = count
#
#     def __add__(self, n):
#         self.count += n
#         return self
#
#     def __sub__(self, n):
#         self.count -= n
#         return self
#
#     def __mul__(self, n):
#         self.count *= n
#         return self
#
#     def __truediv__(self, n):
#         self.count /= n
#         return self
#
#     def makeSnow(self, row_count):
#         snowflakes_per_row = self.count // row_count
#         rows = "*" * snowflakes_per_row + "\n"
#         result = rows * row_count
#         return result
#
#
# snow = Snow(15)
# print(snow.makeSnow(3))
# snow += 5
# print(snow.makeSnow(4))
# snow -= 7
# print(snow.makeSnow(2))


# №2

# class SnowFlake:
#
#     def __init__(self, side):
#         self.side = side
#         self.matrix = [['-'] * side for _ in range(side)]
#
#     def thaw(self, steps):
#         for _ in range(steps):
#             for i in range(self.side):
#                 self.matrix[i][0] = '-'
#                 self.matrix[i][-1] = '-'
#                 self.matrix[0][i] = '-'
#                 self.matrix[-1][i] = '-'
#
#     def freeze(self, n):
#         new_side = self.side + 2 * n
#         new_matrix = [['-'] * new_side for _ in range(new_side)]
#         for i in range(self.side):
#             for j in range(self.side):
#                 new_matrix[i + n][j + n] = self.matrix[i][j]
#         self.side = new_side
#         self.matrix = new_matrix
#
#     def thicken(self):
#         new_side = self.side
#         new_matrix = [['-'] * new_side for _ in range(new_side)]
#         for i in range(self.side):
#             for j in range(self.side):
#                 if self.matrix[i][j] == '*':
#                     new_matrix[i - 1][j] = self.matrix[i][j]
#                     new_matrix[i + 1][j] = self.matrix[i][j]
#                     new_matrix[i][j - 1] = self.matrix[i][j]
#                     new_matrix[i][j + 1] = self.matrix[i][j]
#                 else:
#                     new_matrix[i][j] = self.matrix[i][j]
#         self.matrix = new_matrix
#
#     def show(self):
#         for row in self.matrix:
#             print(' '.join(row))
#
#
# snowflake = SnowFlake(3)
# snowflake.show()
# snowflake.freeze(2)
# snowflake.thaw(1)
# snowflake.thicken()
# snowflake.show()

# №3

# class Robot:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.path_coordinates = [(x, y)]
#
#     def move(self, commands):
#         for command in commands:
#             if command == "N" and self.y < 100:
#                 self.y += 1
#             elif command == "S" and self.y > 0:
#                 self.y -= 1
#             elif command == "E" and self.x < 100:
#                 self.x += 1
#             elif command == "W" and self.x > 0:
#                 self.x -= 1
#
#             self.path_coordinates.append((self.x, self.y))
#
#         return (self.x, self.y)
#
#     def path(self):
#         return self.path_coordinates
#
#
# robot = Robot(50, 50)
# robot.move("NE")
# print(robot.path())

# №4

class Talking:
    def __init__(self, name):
        self.name = name
        self.yes_count = 0
        self.no_count = 0
        self.yes_no_toggle = True

    def to_answer(self):
        if self.yes_no_toggle:
            self.yes_no_toggle = False
            self.yes_count += 1
            return "moore-moore"
        else:
            self.yes_no_toggle = True
            self.no_count += 1
            return "meow-meow"

    def number_yes(self):
        return self.yes_count

    def number_no(self):
        return self.no_count