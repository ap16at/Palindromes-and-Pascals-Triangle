# Andrew Perez-Napan
# ap16at
# Due Date: 1-20-21
# The program in this file is the individual work of Andrew Perez-Napan

def print_triangle(n):
    pascal = []
    for row in range(1, n + 1):
        node = 1
        pascal.append(0)
        for pos in range(1, row + 1):
            pascal.append(node)
            node = (node * (row - pos) / pos)
        for count in range(1, len(pascal)):
            print(int(pascal[count]), end=" ")
        pascal.clear()
        print("")


if __name__ == "__main__":
    rows = input("Enter the number of rows: ")
    print_triangle(int(rows))
