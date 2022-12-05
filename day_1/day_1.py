
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

print(f"Biggest load: {max(elves)}")

sorted_elves = sorted(elves)

top_three = 0
for x in sorted_elves[-3:]:
  print(x)
  top_three += x

print(f"Top three: {top_three}")