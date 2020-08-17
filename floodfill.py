import time
from os import system
image = [
    list("...#######........."),
    list("...#.***.#........."),
    list("...#****##$$$......"),
    list("...#..#....#......."),
    list("...####.....#######"),
    list("...#######........."),
    list("...########........"),
    list("..................."),
]
image2 = [list("...#######........"),
         list("...#.....#........"),
         list("...#.....#........"),
         list("...#..######......"),
         list("...#..#....#......"),
         list("...####....######."),
         list("....#...........#."),
         list("....#############."),
         list("..................")]

def print_image():
    for line in image2:
        print("".join(line))
depth = 0
def floodfill(row, col, c):
    global depth
    depth += 1

    system('clear')
    print_image()
    print(">" * depth)
    time.sleep(0.25)

    if row < 0 or row > len(image2) - 1 or col < 0 or col > len(image2[0]) - 1:
        depth -= 1
        return
    if image2[row][col] != '.':
        depth -= 1
        return

    image2[row][col] = c

    system('clear')
    print_image()
    time.sleep(0.25)

    floodfill(row-1, col, c)
    floodfill(row+1, col, c)
    floodfill(row, col+1, c)
    floodfill(row, col-1, c)

    depth -= 1

floodfill(2, 5, "*")
floodfill(5, 8, "$")
floodfill(1, 1, "&")
# print_image()
# time.sleep(0.25)
