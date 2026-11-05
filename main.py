# Bri Auspland
# COS 226 Hash Homework
# Starts by unloading the CSV file into three lists: titles, quotes, and the movie itself

############################# Functions ########################

def title_hash():
    pass

def quote_hash():
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

# print(movies[0])