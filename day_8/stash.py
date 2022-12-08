          for mt in range(0 + 1, len(line) - 1):
            for x in range(0, mt):
              print(f"Checking {line[mt]}")
              if line[x] < line[mt]:
                visible_trees += 1
                print(f"{line[mt]} is visible from the left")
                break

              else:
                print(f"{line[mt]} is not visible from the left")


              for y in range(mt, len(line)):
                if line[y] < line[mt]:
                  visible_trees += 1
                  print(f"{line[mt]} is visible from the right")
                  break
                else:
                  print(f"{line[mt]} is not visible from the right")