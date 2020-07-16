# Your code here
ignored_characters = ['"', ":", ";", ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def histogram():
    counts = dict()
    with open("applications/histo/robin.txt") as f:
        words = f.read()
        split_words = words.split()
    
    for word in split_words:
        histo = ""
        for char in word:
            if char is not ignored_characters:
                histo += char
        word = histo.lower()

        if word in counts:
            counts[word] += 1
        elif word == "" or word == " ":
            break
        else:
            counts[word] = 1

    items = list(counts.items())
    items.sort(key = lambda e: e[1], reverse = True)
    counts = (dict(items))
    for (string, value) in counts.items():
        print(f'{string} {" " * (20 - len(string))} {"#" * value}')

print(histogram())