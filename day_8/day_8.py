input_file = open("input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

columns = {}
visible_trees = 0

for line in input:
    print(line)
    for i in range(0, len(line)):
        columns[i] = columns.get(i, "") + line[i]

print(columns)

def reverse_slicing(s):
    return s[::-1]

def is_visible(tree, trees):
    for x in trees:
        if int(x) >= int(tree):
          return False
    return True

def get_view_distance(tree, trees):
    view_distance = 0
    for x in trees:
        if int(x) < int(tree):
          view_distance += 1
        elif int(x) == int(tree):
          view_distance += 1
          break
        else:
          view_distance += 1
          break
    return view_distance

max_view_distance = 0

for row, line in enumerate(input):
    reversed_line = line[::-1]

    for tree in range(0, len(line)):
        if tree == 0 or tree == len(line) - 1:
          visible_trees += 1

        else:
          left_trees = line[:tree]
          right_trees = reversed_line[:len(line) - tree - 1]
          above_trees = columns[tree][:row]
          below_trees = columns[tree][row + 1:]

          if is_visible(line[tree], left_trees) == True:
            visible_trees += 1
            #print(f"{line[tree]} is visible from the left")

          elif is_visible(line[tree], right_trees) == True:
            visible_trees += 1
            #print(f"{line[tree]} is visible from the right")

          elif is_visible(line[tree], above_trees) == True:
            visible_trees += 1
            #print(f"{line[tree]} is visible from above")

          elif is_visible(line[tree], below_trees) == True:
            visible_trees += 1
            #print(f"{line[tree]} is visible from below")

    for column, tree in enumerate(range(0, len(line))):
        left_trees = reverse_slicing(line[:tree])
        right_trees = line[tree + 1:]
        above_trees = reverse_slicing(columns[tree][:row])
        below_trees = columns[tree][row + 1:]

        view_distance_left = get_view_distance(line[tree], left_trees)
        view_distance_right = get_view_distance(line[tree], right_trees)
        view_distance_above = get_view_distance(line[tree], above_trees)
        view_distance_below = get_view_distance(line[tree], below_trees)

        view_score = view_distance_left * view_distance_right * view_distance_above * view_distance_below

        print(f"Left: {left_trees}")
        print(f"Right: {right_trees}")
        print(f"Above: {above_trees}")
        print(f"Column: {column} Row: {row} Tree: {tree} {line[tree]}")
        print(f"{line[tree]}: {view_distance_left} {view_distance_right} {view_distance_above} {view_distance_below}")
        print(f"View score: {view_score}")
        print("-----------------")

        if view_score > max_view_distance:
          max_view_distance = view_score


print(visible_trees)

print(f"Max view distance: {max_view_distance}")