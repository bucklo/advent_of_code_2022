
# Read file
elf_file = open("elves.txt", "r")

# Read file into list, delimiter is empty newline
content = elf_file.read().splitlines()

# Close file
elf_file.close()

elves = []
sum = 0

for x in content:
  if x == '':
    elves.append(sum)
    sum = 0

  else:
    sum += int(x)

first = (max(elves))
print("First star: " + str(first))

second = elves.remove(first)
print(second)

third = elves.remove([first, second])

print(first, second, third)