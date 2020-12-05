import time
t = time.time()

# Read input
with open("day1.txt", "r") as file:
    query = file.readlines()

# Remove line breaks and convert input to integers
for index, s in enumerate(query):
    query[index] = s.strip()
    query[index] = int(s)

found = False
# Find 3 numbers that add up to 2020
for i in query:
    for j in query:
        if not i+j > 2020:  # Massively reduces runtime
            for k in query:
                if i+j+k == 2020:
                    print(i*j*k)
                    found = True
                    break
        if found:
            break
    if found:
        break

time_total = time.time() - t
print("Seconds: " + str(time_total))  #0.0261s