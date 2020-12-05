import time
t = time.time()

# Read input
with open("day3.txt", "r") as file:
    query = file.readlines()

for index, s in enumerate(query):
    query[index] = s.strip()

print(query)

##################################################


def solution_a():
    x = 0
    tree_count = 0
    for s in query:
        if s[x] == '#':
            tree_count += 1
        x = (x+3) % len(s)
    return tree_count


print(str(solution_a()))


def descend_with(x: int, y: int) -> int:
    moving_x = 0
    tree_count = 0
    iteration = 0
    for s in query:
        if y == 1 or iteration % 2 != 1:
            if s[moving_x] == '#':
                tree_count += 1
            moving_x = (moving_x + x) % len(s)
        iteration += 1
    return tree_count


def solution_b() -> int:
    return descend_with(1, 1)*descend_with(3, 1)*descend_with(5, 1)*descend_with(7, 1)*descend_with(1, 2)


print(str(solution_b()))
