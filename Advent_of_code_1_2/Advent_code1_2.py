
puzzle_file = open('puzzle.txt', 'r')
lines1 = puzzle_file.read().split()
puzzle_file.close()
puzzle_file2 = open('puzzle.txt', 'r')
lines2 = puzzle_file2.read().split()
puzzle_file2.close()
puzzle_file3 = open('puzzle.txt', 'r')
lines3 = puzzle_file3.read().split()
puzzle_file3.close()
number_seen = set()

for i in lines1:
    for j in lines2:
        if (int(i)+int(j)) < 2020:
            for k in lines3:
                if (int(i)+int(j)+int(k)) == 2020:
                    if i not in number_seen:
                        print(int(i)*int(j)*int(k))
                        print(i, j, k)
                        number_seen.add(i)
                        number_seen.add(j)
                        number_seen.add(k)



