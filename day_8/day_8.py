input_file = open("test_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

columns = {}
visible_trees = 0

for line in input:
    print(line)
    for i in range(0, len(line)):
        columns[i] = columns.get(i, "") + line[i]

print(columns)



for line in input:
    reversed_line = line[::-1]

    for i in range(0, len(line)):
        if i == 0 or i == len(line) - 1:
          print(len(line))
          visible_trees += 1

        else:
          for i in range(0 + 1, len(line) - 1):
            for x in range(0, i):
              if line[x] < line[i]:
                visible_trees += 1
                print(f"{line[i]} is visible from the left")
                break

              for y in range(i +1, len(line)):
                if line[y] < line[i]:
                  visible_trees += 1
                  print(f"{line[i]} is visible from the right")
                  break

    print("-----------------")

print(visible_trees)