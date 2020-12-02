
puzzle_file = open('puzzle.txt', 'r')
lines1 = puzzle_file.read().split()
puzzle_file.close()
puzzle_file2 = open('puzzle.txt', 'r')
lines2 = puzzle_file2.read().split()
puzzle_file2.close()
number_seen = set()

for i in lines1:
    for j in lines2:
        if (int(i)+int(j)) == 2020:
            if i not in number_seen:
                number_seen.add(i)
                number_seen.add(j)
                print(i,j)
                print(int(i)*int(j))

