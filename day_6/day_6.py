input_file = open("input.txt", "r")
input_data = input_file.readlines()
input_file.close()

for line in input_data:
    total_len = len(line)

    i = 13

    while i < total_len:
      element_list = []
      print(line[i-14:i])

      for char in line[i-14:i]:
        element_list.append(char)

      i += 1

      if element_list == []:
        continue

      if len(set(element_list)) == len(element_list):
        print(f"Chars processed: {i-1}")
        break
