# Bri Auspland
# COS 226 Hash Homework
# Starts by unloading the CSV file into three lists: titles, quotes, and the movie itself

############################# Imports ##########################

from math import sqrt
from nlp_functions import syllables
import time

############################# Functions ########################

def title_hash1(title, maximum):
    # initial idea: have the key be based off the syllables in the title
    # for every word, multiply the length by the syllables in it
    # then, add all of those together and square it
    # finally, subtract the amount of syllables squared
    # if the key is too high, square root it
    # if key is too low, square it

    # edit for quotes, bee movie is too large, set just to 15000.

    words = title.split()
    length = len(words)
    syls = syllables(title)

    x = []

    for i in range(length):
        x.append(len(words[i]) * syls[i])

    key = (sum(x) ** 2) - (len(syls) ** 2)

    if key >= maximum:
        key = round(sqrt(key))
        if key >= maximum:
            key = maximum-1

    elif key < 0:
        key = key ** 2

    return key

def title_hash2(title, maximum):
    # Initial idea: Use ord() somehow
    # Function sums every character's ASCII value
    # Then, multiplies that by the number of words, and adds the sum again
    # If too large, floor divife by the number of words plus 8 (to account for one word titles)
    # 8 had the best success rate, which is why it is 8

    sum = 0
    for character in title.strip():
        sum += ord(character)

    key = (sum * len(title.split())) + sum

    if key >= maximum:
        key = key // (len(title.split())+8)

    return key

def quote_hash1(quote):
    pass

def quote_hash2(quote):
    pass

############################# Code #############################

path = "MOCK_DATA.csv"

# assuming title is first category, quote is last
# need to have viewed the data for this to be true
title_key = 0
quote_key = -1

titles = []
quotes = []

movies = {}

with open(path, "r") as f:
    categories = f.readline().strip().split(",")
    length = len(categories) # total number of categories is: 9

    movie_index = 0
    for i in f.readlines():

        f_list = i.strip().split(",")
        
        if len(f_list) > length: # if there were commas in the movie title,
            title = ''
            while len(f_list) >= length: # go through until there are no movie title chunks
                title += f_list[0].replace('\"', "") # and put them into a title string
                f_list = f_list[1:]

            f_list = [title] + f_list # then, put the title back at the beginning of the list

        if f_list != [""]: # if the current row is not fully empty
            if f_list[title_key] == "" or f_list[quote_key] == "":
                f_list[title_key] = "MISSING TITLE"
                f_list[quote_key] = "MISSING QUOTE"

            titles.append(f_list[title_key])
            quotes.append(f_list[quote_key])

            movies[movie_index] = {}
            for x in range(len(categories)):
                movies[movie_index][categories[x]] = f_list[x]

            movie_index+=1


### Linear Probing Poor Function ###

# start = time.perf_counter()

# linear_probing_hash_table_1 = [None for i in range(len(movies))]
# linear_probing_hash_table_1_collision_counter = 0

# for i in range(len(movies)):
#     hash = title_hash1(titles[i], len(movies))

#     collision = True
#     counter = 0
#     while collision:
#         if linear_probing_hash_table_1[hash] == None:
#                 collision = False
        
#         else: # linear probing, if space is full, go to previous until empty
#             if hash == 0:
#                 hash = len(linear_probing_hash_table_1)
#             hash -= 1

#             counter += 1

#     if counter > 0:
#         linear_probing_hash_table_1_collision_counter += 1

#     linear_probing_hash_table_1[hash] = movies[i]

# end = time.perf_counter()

# filled_counter = 0
# for i in linear_probing_hash_table_1:
#     if i != None:
#         filled_counter += 1

# print("Linear Probing Hash Table Method 1 Titles")
# print(f"Number of collisions: {linear_probing_hash_table_1_collision_counter}")
# print(f"Total space filled: {filled_counter}")
# print(f"Wasted space: {len(linear_probing_hash_table_1)-filled_counter}")
# print(f"Construction time: {end-start}")



### Linear Probing Good Function ###

# start = time.perf_counter()

# linear_probing_hash_table_2 = [None for i in range(len(movies))]
# linear_probing_hash_table_2_collision_counter = 0

# for i in range(len(movies)):
#     hash = title_hash2(titles[i], len(movies))

#     collision = True
#     counter = 0
#     while collision:
#         if linear_probing_hash_table_2[hash] == None:
#                 collision = False
        
#         else: # linear probing, if space is full, go to previous until empty
#             if hash == 0:
#                 hash = len(linear_probing_hash_table_2)
#             hash -= 1

#             counter += 1

#     if counter > 0:
#         linear_probing_hash_table_2_collision_counter += 1

#     linear_probing_hash_table_2[hash] = movies[i]

# end = time.perf_counter()

# filled_counter = 0
# for i in linear_probing_hash_table_2:
#     if i != None:
#         filled_counter += 1

# print("Linear Probing Hash Table Method 2 Titles")
# print(f"Number of collisions: {linear_probing_hash_table_2_collision_counter}")
# print(f"Total space filled: {filled_counter}")
# print(f"Wasted space: {len(linear_probing_hash_table_2)-filled_counter}")
# print(f"Construction time: {end-start}")



# Linear Probing Poor Function

start = time.perf_counter()

linear_probing_hash_table_3 = [None for i in range(len(movies))]
linear_probing_hash_table_3_collision_counter = 0

for i in range(len(movies)):
    hash = title_hash1(quotes[i], len(movies))

    collision = True
    counter = 0
    while collision:
        if linear_probing_hash_table_3[hash] == None:
                collision = False
        
        else: # linear probing, if space is full, go to previous until empty
            if hash == 0:
                hash = len(linear_probing_hash_table_3)
            hash -= 1

            counter += 1

    if counter > 0:
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