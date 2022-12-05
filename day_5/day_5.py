input_file = open("input.txt", "r")
content = input_file.read().splitlines()

def move_crate(stacks, crates, from_stack, to_stack):
  crates_to_move = stacks[from_stack][:crates]

  print(f"Moving {crates_to_move} from {from_stack} to {to_stack}")

  print("Before:")
  print(f"From stack: {stacks[from_stack]}")
  print(f"To stack: {stacks[to_stack]}\n")

  # Delete the crates from the from_stack
  stacks[from_stack] = stacks[from_stack][crates:]

  # Add the crates to the beginning of the to_stack using insert
  for x in reversed(crates_to_move):
    stacks[to_stack].insert(0, x)



  print(f"After:")
  print(f"From stack: {stacks[from_stack]}")
  print(f"To stack: {stacks[to_stack]}")
  print("--------------------\n")

  return stacks

stacks = {
  1: ["R", "W", "F", "H", "T", "S"],
  2: ["W", "Q", "D", "G", "S"],
  3: ["W", "T", "B"],
  4: ["J","Z","Q","N","T","W","R","D"],
  5: ["Z","T","V","L","G","H","B","F"],
  6: ["G","S","B","V","C","T","P","L"],
  7: ["P","G","W","T","R","B","Z"],
  8: ["R","J","C","T","M","G","N"],
  9: ["W","B","G","L"],
}


for x in range (10, len(content)):
  crates = int(content[x].split(" ")[1])
  from_stack = int(content[x].split(" ")[3])
  to_stack = int(content[x].split(" ")[5])

  print(f"Moving {crates} from {from_stack} to {to_stack}")
  stacks = move_crate(stacks, crates, from_stack, to_stack)

for stack in stacks:
  # Print value of stack
  print(f"Stack {stack} contains {stacks[stack][0]}")