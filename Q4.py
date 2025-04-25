names = set()

n = int(input("How many names will you enter? "))
for i in range(n):
    name = input(f"Enter name {i+1}: ")
    names.add(name)

a_names = {name for name in names if name.startswith('A')}
b_names = {name for name in names if name.startswith('B')}

print("Names starting with A:", a_names)
print("Names starting with B:", b_names)
