from main import *

### Linked List Poor Function ### TITLES

start = time.perf_counter()

linked_list_hash_table_1 = [[] for i in range(len(movies))]
linked_list_hash_table_1_collision_counter = 0

for i in range(len(movies)):
    hash = title_hash1(titles[i], len(movies))

    if len(linked_list_hash_table_1[hash])>0:
        linked_list_hash_table_1_collision_counter += 1
    
    linked_list_hash_table_1[hash].append(movies[i])

end = time.perf_counter()

filled_counter = 0
for i in linked_list_hash_table_1:
    if len(i) > 0:
        filled_counter += 1

print("Linear Probing Hash Table Method 1 Titles")
print(f"Number of collisions: {linked_list_hash_table_1_collision_counter}")
print(f"Total space filled: {filled_counter}")
print(f"Wasted space: {len(linked_list_hash_table_1)-filled_counter}")
print(f"Construction time: {end-start}")
print("\n\n")



### Linked List Good Function ### TITLES

start = time.perf_counter()

linked_list_hash_table_2 = [[] for i in range(len(movies))]
linked_list_hash_table_2_collision_counter = 0

for i in range(len(movies)):
    hash = title_hash2(titles[i], len(movies))

    if len(linked_list_hash_table_2[hash])>0:
        linked_list_hash_table_2_collision_counter += 1
    
    linked_list_hash_table_2[hash].append(movies[i])

end = time.perf_counter()

filled_counter = 0
for i in linked_list_hash_table_2:
    if len(i) > 0:
        filled_counter += 1

print("Linear Probing Hash Table Method 2 Titles")
print(f"Number of collisions: {linked_list_hash_table_2_collision_counter}")
print(f"Total space filled: {filled_counter}")
print(f"Wasted space: {len(linked_list_hash_table_2)-filled_counter}")
print(f"Construction time: {end-start}")
print("\n\n")



### Linked List Poor Function ### Quotes

start = time.perf_counter()

linked_list_hash_table_3 = [[] for i in range(len(movies))]
linked_list_hash_table_3_collision_counter = 0

for i in range(len(movies)):
    hash = title_hash1(titles[i], len(movies))

    if len(linked_list_hash_table_3[hash])>0:
        linked_list_hash_table_3_collision_counter += 1
    
    linked_list_hash_table_3[hash].append(movies[i])

end = time.perf_counter()

filled_counter = 0
for i in linked_list_hash_table_3:
    if len(i) > 0:
        filled_counter += 1

print("Linear Probing Hash Table Method 1 Quotes")
print(f"Number of collisions: {linked_list_hash_table_3_collision_counter}")
print(f"Total space filled: {filled_counter}")
print(f"Wasted space: {len(linked_list_hash_table_3)-filled_counter}")
print(f"Construction time: {end-start}")
print("\n\n")



### Linked List Good Function ### Quotes

start = time.perf_counter()

linked_list_hash_table_4 = [[] for i in range(len(movies))]
linked_list_hash_table_4_collision_counter = 0

for i in range(len(movies)):
    hash = title_hash2(titles[i], len(movies))

    if len(linked_list_hash_table_4[hash])>0:
        linked_list_hash_table_4_collision_counter += 1
    
    linked_list_hash_table_4[hash].append(movies[i])

end = time.perf_counter()

filled_counter = 0
for i in linked_list_hash_table_4:
    if len(i) > 0:
        filled_counter += 1

print("Linear Probing Hash Table Method 2 Quotes")
print(f"Number of collisions: {linked_list_hash_table_4_collision_counter}")
print(f"Total space filled: {filled_counter}")
print(f"Wasted space: {len(linked_list_hash_table_4)-filled_counter}")
print(f"Construction time: {end-start}")
print("\n\n")