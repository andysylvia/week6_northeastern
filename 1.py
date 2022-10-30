import urllib.request

def get_letters_count(lines):
    letters_dict = dict() # Creating a dict key = letter , value = frequency
    for line in lines:
        for word in line.split():
            for letter in word:
                if letter in letters_dict:
                    letters_dict[letter] = letters_dict[letter] + 1
                else:
                    letters_dict[letter] = 1
                    
    return (sorted(letters_dict.items(), key=lambda item: item[1], reverse=True))   


link = "https://raw.githubusercontent.com/AllenDowney/ThinkPython2/master/code/words.txt"

text_bytes = urllib.request.urlopen(link).read() # bytes

text_string = text_bytes.decode("utf-8") # passing the encoding and getting string

text_lines = text_string.splitlines()

# word_list = make_word_list(text_lines)

letters_freq = get_letters_count(text_lines)

print(letters_freq)

