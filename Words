def bigger_than_20(word):
    size = len(word)
    if size > 20:
        print(word)

def word_has_no_letter(word, letter):
    if word.find(letter) != -1:
        return True
    else:
        return False

def count_e_percentage(file):
    has_e = 0
    dont_have_e = 0
    count = 0

    for line in file:
        count = count + 1
        word = line.strip()
        letter = "e"
        if word_has_no_letter(word, letter):
            dont_have_e = dont_have_e + 1
        else:
            has_e = has_e + 1
        
    percetage = dont_have_e / count * 100

def avoids(word_to_check, forbiden_words):
    for restrict in forbiden_words:
        if word_has_no_letter(word_to_check, restrict):
            found_it = False
        else:
            found_it = True
    
    return found_it
        


file = open("words.txt")

forbiden_words = ["a", "b", "c"]
word_to_check = "split"

count_e_percentage(file)

if avoids(word_to_check, forbiden_words):
    print("There is no forbidden word in this string")
else:
    print("Tem boi na linha")
