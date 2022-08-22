
print("Entre ton nom > ")
name = input()

print([*name])


def printNode(node, neighbour_at_right, neighbour_at_bottom):
    print(node[0] + " " + node[1]
          + " " + neighbour_at_right[0] + " " + neighbour_at_right[1]
          + " " + neighbour_at_bottom[0] + " " + neighbour_at_bottom[1])
