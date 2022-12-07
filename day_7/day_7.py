input_file = open("input.txt", "r")
content = input_file.readlines()
input_file.close()

part1 = 0
dir_sizes = []

def sum_func(file_sys):
  global part1
  total_size = 0

  for x in file_sys.values():
    if isinstance(x, int):
      total_size += x
    else:
      total_size += sum_func(x)

  if total_size <= 100000:
    part1 = part1 + total_size
#    dir_sizes.append(total_size)

  else:
    dir_sizes.append(total_size)

  return total_size

def find_small_dir(file_sys, required_size):
  global dir_sizes
  for x in file_sys.values():
    if isinstance(x, int):
      if x >= required_size:
        dir_sizes.append(x)
    else:
      find_small_dir(x, required_size)

  return dir_sizes

file_system = {}
cf = [file_system]

for cmd in content:
  cmd = cmd.split()
  if cmd[1] == "ls":
    continue

  elif cmd[1] == "cd":
    if cmd[2] == "/":
      cf = [file_system]
    elif cmd[2] == "..":
      cf.pop()
    else:
      cf.append(cf[-1][cmd[2]])

  elif cmd[0] == "dir":
    dir_name = cmd[1]
    cf[-1][dir_name] = {}

  else:
    size = cmd[0]
    name = cmd[1]
    cf[-1][name] = int(size)

root_size = sum_func(file_system)
required_space = 30000000 - (70000000 - root_size)

#print(part1)

print(f"Root size: {root_size}")
print(f"Required space: {required_space}")


dir_sizes.sort()

for size in dir_sizes:
  if size >= required_space:
    print(f"Smallest directory: {size}")
    break