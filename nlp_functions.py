# This is a set of functions from a previous project related to natural language processing.
# syllables works with diph_triph to find the number of syllables in a given sentence, returning a lsit of the syllables.
# Syllables are calculated by the number of vowels in a word, with some rules affecting += or -= values.

def syllables(data):
    vowels = ["a","e","i","o","u"]
    syls = []
    for word in data.split():
        word = word.lower()
        bin = []

        for cha in word:
            if cha in vowels:
                bin.append(1)
            else:
                bin.append(0)

        vs = diph_triph(bin)

        if word[-1] == "e":
            if word[len(word)-2] != "l":
                vs -= 1

        syls.append(vs)

    return syls
            
def diph_triph(binn):
    vowel_count = 0
    for i in binn:
        if i == 1:
            vowel_count +=1
    
    while 1 in binn:
        ind = binn.index(1)
        di_tri = 0
        try:
            if binn[ind+1] == 1:
                di_tri +=1
                vowel_count -=1
                if binn[ind+2] ==1:
                    di_tri += 1
                    vowel_count -= 1
        except:
            pass

        for n in range(0,di_tri+1):
            binn.remove(1)

    return vowel_count