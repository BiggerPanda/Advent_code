file = open("puzzle.txt", "r")
line = file.read().split()
range_a, range_b = 0,0
important_letter = ""
right_passwords = 0
for i in range (0,len(line)):
    if i%3 == 0:
        range_a,range_b = line[i].split('-')
    if i%3 == 1:
        important_letter = line[i].split(':')[0]
    if i%3 == 2:
        count = 0
        buffor = line[i]
        for one_lett in buffor:
            if one_lett == important_letter:
                count += 1

        if int(range_a) <= count <= int(range_b):
            right_passwords += 1

print(right_passwords)

