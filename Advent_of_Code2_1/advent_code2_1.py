file = open("puzzle.txt", "r")
line = file.read().split()
place_a, place_b = 0, 0
important_letter = ""
right_passwords = 0
for i in range (0,len(line)):
    if i % 3 == 0:
        place_a, place_b = line[i].split('-')
    if i % 3 == 1:
        important_letter = line[i].split(':')[0]
    if i % 3 == 2:
        count = 0
        buffor = line[i]

        if (buffor[int(place_a)-1] == important_letter) and (buffor[int(place_b)-1] != important_letter) or \
                (buffor[int(place_a)-1] != important_letter) and (buffor[int(place_b)-1] == important_letter) :
            right_passwords += 1

print(right_passwords)
