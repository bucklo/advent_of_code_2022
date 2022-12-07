input_file = open("input.txt", "r")
content = input_file.readlines()
input_file.close()

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
  return total_size


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

print(file_system)
#print(cf)






root_size = sum_func(file_system)

print(part1_size)