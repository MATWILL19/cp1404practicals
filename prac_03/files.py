# a.

FILENAME = "name.txt"
out_file = open(FILENAME, 'w')
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# b.

out_file = open(FILENAME, 'r')
print(f"Hi {out_file.read().strip()}!", end="")
out_file.close()

c.

FILENAME = "numbers.txt"
with open(FILENAME, "r") as in_file:
    total_amount = int(in_file.readline()) + int(in_file.readline())
print(total_amount)

# d.

FILENAME = "numbers.txt"
total_amount = 0
with open(FILENAME, "r") as in_file:
    for line in in_file:
        total_amount += int(line)
print(total_amount)
