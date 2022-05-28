# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# from itertools import count


def read_file_content(filename):
    # [assignment] Add your code here 
    with open("story.txt", "r") as file:
       datta = file.read()
       
    return datta
       


def count_words():
    # [assignment] Add your code here

    text = read_file_content("story.txt")
    textSplit = text.split()

    count = dict()

    for i in textSplit:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count