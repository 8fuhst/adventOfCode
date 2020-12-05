import time
t = time.time()

# Read input
with open("day2.txt", "r") as file:
    query = file.readlines()

for index, s in enumerate(query):
    query[index] = s.strip()

print(query)


def extract_min_max_letter(working_string: str):
    min = 0
    max = 0
    letter = ''

    cut_string = working_string[:working_string.index(':')]
    min = int(cut_string[0:cut_string.index('-')])
    max = int(cut_string[cut_string.index('-') + 1:cut_string.index(' ')])
    letter = cut_string[len(cut_string)-1]

    return min, max, letter


count_valids = 0

for q in query:
    mi, ma, let = extract_min_max_letter(q)
    q = q[q.index(':')+2:]
    # count = 0
    new_query = q[mi-1]+q[ma-1]
    if new_query.count(let) == 1:
        count_valids += 1
    # for c in q[q.index(':')+2:]:
    #    if c == let:
    #        count += 1
    # if mi <= count <= ma:
    #    count_valids = count_valids + 1

print(count_valids)
