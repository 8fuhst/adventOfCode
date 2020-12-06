import time
import re
t = time.time()

query = []
entry = ''

# Read input
with open("day6.txt", "r") as file:
    for line in file:
        if line != "\n":
            entry += line
        elif entry != '\n':
            query.append(entry)
            entry = ''
    query.append(entry)


for index, s in enumerate(query):
    query[index] = s.strip()
    query[index] = query[index].replace('\n', ' ')

print(query)

##################################################


def convert_entry(answers: str):
    ret = set()
    for c in answers:
        if c != ' ':
            ret.add(c)
    return ret


def convert_query(lst: list):
    for index, l in enumerate(lst):
        lst[index] = convert_entry(l)
    return lst


def solution_a():
    new_query = convert_query(query)
    sum = 0
    for s in new_query:
        sum += len(s)
    return sum


def find_answer_everyone(answers: str):
    answers_list = answers.split()
    count = 0
    for s in answers_list[0]:
        internal_count = 1
        for a in range(1, len(answers_list)):
            if s in answers_list[a]:
                internal_count += 1
        if internal_count == len(answers_list):
            count += 1
    return count


def solution_b():
    count = 0
    for q in query:
        count += find_answer_everyone(q)
    return count


print(solution_b())
print(solution_a())
