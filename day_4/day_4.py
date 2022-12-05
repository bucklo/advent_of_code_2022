input_file = open("input.txt", "r")
content = input_file.readlines()
input_file.close()

def getSequence(elf):
  start = int(elf.split("-")[0])
  end = int(elf.split("-")[1]) + 1
  elf_sequence = list(range(start, end))
  return elf_sequence

overlaps = 0
subset_overlaps = 0

for pair in content:
  elf_a = pair.split(",")[0]
  elf_b = pair.split(",")[1]

  elf_a_sequence = getSequence(elf_a)
  elf_b_sequence = getSequence(elf_b)

  # Check if one of the sequences is a subset of the other
  if set(elf_a_sequence).issubset(elf_b_sequence) or set(elf_b_sequence).issubset(elf_a_sequence):
    subset_overlaps += 1
    print(f"Subset overlap: {elf_a} and {elf_b}")

  # Check if the sequences overlap
  if set(elf_a_sequence).intersection(elf_b_sequence):
    overlaps += 1
    print(f"Intersection: {elf_a} and {elf_b}")

print(f"Subset overlaps: {subset_overlaps}")
print(f"Intersection: {overlaps}")