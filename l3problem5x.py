# Problem 5A

for n in range(2, 12, 2):
    print n
print("Goodbye!")

# Problem 5B

print("Hello!")
for i in range(10, 0, -2):
    print i

# Problem 5C

acum = 0
end = int(raw_input("enter: "))
for n in range(1, (end + 1)):
    acum += n
print acum
