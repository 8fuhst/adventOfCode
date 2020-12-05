import time
t = time.time()

# Read input
with open("day5.txt", "r") as file:
    query = file.readlines()

for index, s in enumerate(query):
    query[index] = s.strip()

print(query)

##################################################


seat_rows = [i for i in range(0, 128)]
seat_columns = [i for i in range(0, 8)]


def identify_seat_row(rows: list, seat: str, lower, higher):
    if lower > higher:
        return -1

    mid = int((lower + higher)/2)
    if 'R' in seat[0] or 'L' in seat[0]:
        return mid

    if 'F' in seat[0]:
        return identify_seat_row(rows, seat[1:], lower, mid)
    elif 'B' in seat[0]:
        return identify_seat_row(rows, seat[1:], mid + 1, higher)


def identify_seat_column(columns: list, seat: str, lower, higher):
    if lower > higher:
        return -1

    mid = int((lower + higher)/2)

    if seat == '':
        return mid

    if 'F' in seat[0] or 'B' in seat[0]:
        return identify_seat_column(columns, seat[1:], lower, higher)

    if 'L' in seat[0]:
        return identify_seat_column(columns, seat[1:], lower, mid)
    elif 'R' in seat[0]:
        return identify_seat_column(columns, seat[1:], mid + 1, higher)


def identify_seat(seat: str):
    return identify_seat_row(seat_rows, seat, 0, 127), identify_seat_column(seat_columns, seat, 0, 7)


def solution_a():
    max = 0
    for i in query:
        row, column = identify_seat(i)
        value = row * 8 + column
        if value > max:
            max = value

    return max


def solution_b():
    lst = []

    for i in query:
        row, column = identify_seat(i)
        value = row * 8 + column
        lst.append(value)

    lst.sort()
    print(lst)

    for i in lst:
        if i+2 in lst and i+1 not in lst:
            return i, i+2
        elif i-2 in lst and i-1 not in lst:
            return i-2, i
    return -1


print(solution_a())
print(solution_b())
