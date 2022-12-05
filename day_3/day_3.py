def getPriority(item):
  """Returns the priority of an item.
  Lowercase item types `a` through `z` have priorities 1 through 26, respectively.
  Uppercase items have priorities 27 through 52, respectively. Items with other types have priority 0.
  """

  priority = 0
  if item.islower():
    priority = ord(item) - 96
  elif item.isupper():
    priority = ord(item) - 64 + 26

  return priority

rucksack_file = open("rucksack.txt", "r")
rucksacks = rucksack_file.read().splitlines()
rucksack_file.close()



def part_one(rucksacks):
  priority_sum = 0

  for content in rucksacks:
    # Split each line in to two parts. compartment_a and compartment_b.
    length = len(content)
    compartment_a = content[:length // 2]
    compartment_b = content[length // 2:]

    print(f"Compartment A: {compartment_a}")
    print(f"Compartment B: {compartment_b}")

    # Check if items in compartment also exist in the other compartment.
    for item in compartment_a:
      if item in compartment_b:
        print(f"item {item} is in both compartments")
        print(f"priority of {item} is {getPriority(item)}")
        priority_sum += getPriority(item)
        break

    print("\n")
  print(priority_sum)

def part_two(rucksacks):
  i = 0
  priority_sum = 0

  while i < len(rucksacks):
    elf_a = rucksacks[i]
    elf_b = rucksacks[i + 1]
    elf_c = rucksacks[i + 2]

    for x in elf_a:
      if x in elf_b and x in elf_c:
        print(f"item {x} is in all three compartments")
        print(f"priority of {x} is {getPriority(x)}")
        priority_sum += getPriority(x)
        break

    i += 3

  print(priority_sum)

part_two(rucksacks)