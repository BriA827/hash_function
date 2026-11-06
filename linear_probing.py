from main import *

### Linear Probing Poor Function ### TITLES

start = time.perf_counter()

linear_probing_hash_table_1 = [None for i in range(len(movies))]
linear_probing_hash_table_1_collision_counter = 0

for i in range(len(movies)):
    hash = title_hash1(titles[i], len(movies))

    collision = True
    while collision:
        if linear_probing_hash_table_1[hash] == None:
                collision = False
        
        else: # linear probing, if space is full, go to previous until empty
            if hash == 0:
                hash = len(linear_probing_hash_table_1)
            hash -= 1
            linear_probing_hash_table_1_collision_counter += 1

    linear_probing_hash_table_1[hash] = movies[i]

end = time.perf_counter()

filled_counter = 0
for i in linear_probing_hash_table_1:
    if i != None:
        filled_counter += 1

print("Linear Probing Hash Table Method 1 Titles")
print(f"Number of collisions: {linear_probing_hash_table_1_collision_counter}")
print(f"Total space filled: {filled_counter}")
print(f"Wasted space: {len(linear_probing_hash_table_1)-filled_counter}")
print(f"Construction time: {end-start}")
print("\n\n")



### Linear Probing Good Function ### TITLES

start = time.perf_counter()

linear_probing_hash_table_2 = [None for i in range(len(movies))]
linear_probing_hash_table_2_collision_counter = 0

for i in range(len(movies)):
    hash = title_hash2(titles[i], len(movies))

    collision = True
    while collision:
        if linear_probing_hash_table_2[hash] == None:
                collision = False
        
        else: # linear probing, if space is full, go to previous until empty
            if hash == 0:
                hash = len(linear_probing_hash_table_2)
            hash -= 1
            linear_probing_hash_table_2_collision_counter += 1

    linear_probing_hash_table_2[hash] = movies[i]

end = time.perf_counter()

filled_counter = 0
for i in linear_probing_hash_table_2:
    if i != None:
        filled_counter += 1

print("Linear Probing Hash Table Method 2 Titles")
print(f"Number of collisions: {linear_probing_hash_table_2_collision_counter}")
print(f"Total space filled: {filled_counter}")
print(f"Wasted space: {len(linear_probing_hash_table_2)-filled_counter}")
print(f"Construction time: {end-start}")
print("\n\n")



### Linear Probing Poor Function ### QUOTES

start = time.perf_counter()

linear_probing_hash_table_3 = [None for i in range(len(movies))]
linear_probing_hash_table_3_collision_counter = 0

for i in range(len(movies)):
    hash = title_hash1(quotes[i], len(movies))

    collision = True
    while collision:
        if linear_probing_hash_table_3[hash] == None:
                collision = False
        
        else: # linear probing, if space is full, go to previous until empty
            if hash == 0:
                hash = len(linear_probing_hash_table_3)
            hash -= 1
            linear_probing_hash_table_3_collision_counter += 1

    linear_probing_hash_table_3[hash] = movies[i]

end = time.perf_counter()

filled_counter = 0
for i in linear_probing_hash_table_3:
    if i != None:
        filled_counter += 1

print("Linear Probing Hash Table Method 1 Quotes")
print(f"Number of collisions: {linear_probing_hash_table_3_collision_counter}")
print(f"Total space filled: {filled_counter}")
print(f"Wasted space: {len(linear_probing_hash_table_3)-filled_counter}")
print(f"Construction time: {end-start}")
print("\n\n")



## Linear Probing Good Function ### QUOTES

start = time.perf_counter()

linear_probing_hash_table_4 = [None for i in range(len(movies))]
linear_probing_hash_table_4_collision_counter = 0

for i in range(len(movies)):
    hash = title_hash2(quotes[i], len(movies))

    collision = True
    while collision:
        if linear_probing_hash_table_4[hash] == None:
                collision = False
        
        else: # linear probing, if space is full, go to previous until empty
            if hash == 0:
                hash = len(linear_probing_hash_table_4)
            hash -= 1
            linear_probing_hash_table_4_collision_counter += 1

    linear_probing_hash_table_4[hash] = movies[i]

end = time.perf_counter()

filled_counter = 0
for i in linear_probing_hash_table_4:
    if i != None:
        filled_counter += 1

print("Linear Probing Hash Table Method 2 Quotes")
print(f"Number of collisions: {linear_probing_hash_table_4_collision_counter}")
print(f"Total space filled: {filled_counter}")
print(f"Wasted space: {len(linear_probing_hash_table_4)-filled_counter}")
print(f"Construction time: {end-start}")
print("\n\n")