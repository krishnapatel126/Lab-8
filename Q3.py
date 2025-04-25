name_set = set()

for i in range(5):
    name = input(f"Enter name {i+1} to add: ")
    name_set.add(name)
print("After adding names:", name_set)

old_name = input("Enter the name you want to modify: ")
if old_name in name_set:
    new_name = input("Enter the new name: ")
    name_set.remove(old_name)
    name_set.add(new_name)
    print("Name modified.")
else:
    print(f"{old_name} not found in the set.")

for i in range(2):
    name_to_delete = input(f"Enter name {i+1} to delete: ")
    name_set.discard(name_to_delete)
print("After modifications:", name_set)
