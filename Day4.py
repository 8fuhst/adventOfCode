import time
import re
t = time.time()

query = []
entry = ''

# Read input
with open("day4.txt", "r") as file:
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


def solve_a() -> int:
    counter = 0
    for q in query:
        if 'byr' in q and 'iyr' in q and 'eyr' in q and 'hgt' in q and 'hcl' in q and 'ecl' in q and 'pid' in q:
            counter += 1
    return counter


print(str(solve_a()))


def strip_into_kategories(s: str) -> list:
    lst = s.split()
    for a in lst:
        a = a.strip()
    return lst


def check_allowed(s: str) -> bool:
    ecl_allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    category = s[:s.index(':')]
    value = s[s.index(':')+1:]

    if category == 'byr':
        if len(value) == 4 and value.isnumeric():
            if 1920 <= int(value) <= 2002:
                return True
    elif category == 'iyr':
        if len(value) == 4 and value.isnumeric():
            if 2010 <= int(value) <= 2020:
                return True
    elif category == 'eyr':
        if len(value) == 4 and value.isnumeric():
            if 2020 <= int(value) <= 2030:
                return True
    elif category == 'hgt':
        if ('cm' in s and 150 <= int(s[s.index(':') + 1:len(s)-2]) <= 193) \
                or ('in' in s and 59 <= int(s[s.index(':') + 1:len(s)-2]) <= 76):
            return True
    elif category == 'ecl':
        if any(ecl in value for ecl in ecl_allowed):
            return True
    elif category == 'hcl':
        if re.match(r"#[a-f0-9]{6}", value):
            return True
    elif category == 'pid':
        if len(value) == 9 and value.isnumeric():
            return True
    elif category == 'cid':
        return True
    return False


def solve_b() -> int:
    categories = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    counter = 0
    valid_counter = 0
    new_query = []

    for q in query:
        if all(cat in q for cat in categories):
            new_query.append(q)

    print(new_query)

    for index, q in enumerate(new_query):
        new_query[index] = strip_into_kategories(q)

    for q in new_query:
        valid_counter = 0
        valid = True
        for l in q:
            if not check_allowed(l):
                valid = False
            else:
                valid_counter += 1
            if not valid:
                break
        if valid and (valid_counter == 7 or valid_counter == 8):
            counter += 1
    return counter

print(str(solve_b()))