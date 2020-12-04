
def tree_count(step_right,step_down,filename):
    with open(filename, 'r') as file:
        lines = [line.strip('\n') for line in file]
    X_count = 0
    O_count = 0
    position_X = 0
    position_Y = 0
    while True:
        position_X += step_right
        position_Y += step_down

        if position_X > len(lines[0])-1:
            position_X -= len(lines[0])
        if position_Y >= len(lines):
            break

        if lines[position_Y][position_X] == '#':
            X_count += 1
        else:
            O_count += 1

    return X_count


filename = "puzzle.txt"
#part1
print("part 1")
print(tree_count(3,1,filename))

#part2
steps =[(1,1),(3,1),(5,1),(7,1),(1,2)]
result = 1
for step1, step2 in steps:
    result *= tree_count(step1,step2,filename)

print(result)