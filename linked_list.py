from main import *

### Linked List Poor Function ### TITLES

start = time.perf_counter()

linked_list_hash_table_1 = [[] for i in range(len(movies))]
linked_list_hash_table_1_collision_counter = 0

for i in range(len(movies)):
    hash = title_hash1(titles[i], len(movies))

    collision = True
    counter = 0
    while collision:
        if linked_list_hash_table_1[hash] == None:
                collision = False
        
        else: # linked probing, if space is full, go to previous until empty
            if hash == 0:
                hash = len(linked_list_hash_table_1)
            hash -= 1

            counter += 1

    if counter > 0:
        linked_list_hash_table_1_collision_counter += 1

    linked_list_hash_table_1[hash] = movies[i]

end = time.perf_counter()

filled_counter = 0
for i in linked_list_hash_table_1:
    if i != None:
        filled_counter += 1

print("Linear Probing Hash Table Method 1 Titles")
print(f"Number of collisions: {linked_list_hash_table_1_collision_counter}")
print(f"Total space filled: {filled_counter}")
print(f"Wasted space: {len(linked_list_hash_table_1)-filled_counter}")
print(f"Construction time: {end-start}")