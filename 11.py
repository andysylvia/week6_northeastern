import urllib.request


def create_word_dict(lines):
    word_dict = dict()
    for line in text_lines:
        # Each line
        for word in line.split():
            if word in word_dict:
                1
            else:
                word_dict[word]= 1
    return word_dict



link = "https://raw.githubusercontent.com/AllenDowney/ThinkPython2/master/code/words.txt"

text_bytes = urllib.request.urlopen(link).read() # bytes

text_string = text_bytes.decode("utf-8") # passing the encoding and getting string

# New line character  - \n, \r

text_lines = text_string.splitlines()

words_dictionary  = create_word_dict(text_lines)

print(words_dictionary)


