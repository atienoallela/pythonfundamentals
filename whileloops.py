# A while loop will continute to execute a set of statements until the condition is no longer true

j = 1

while j < 10:
    print(j)
    if j == 5:
        break
    j += 1

# continue statemet

k = 8
while k < 24:
    k += 1
    if k == 13:
        continue
    print(k)
