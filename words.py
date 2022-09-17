from tkinter import E

file = open("words.txt")

def bigger_than_20(word):
    size = len(word)
    if size > 20:
        print(word)

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

    percentage = dont_have_e / count * 100
    print(percentage)

def word_has_no_letter(word, letter):
    for letter in word:
        if letter == 'e':
            return False
    return True

    #Never pass through here, just for studies
    if word.find(letter) != -1:
        return False
    else:
        return True

def avoids(word_to_check, forbiden_word):
    for letter in word_to_check:
        if letter in forbiden_word:
            return False
    return True

def uses_only(word_to_check, letters_list):
    for letter in word_to_check:
        if letter not in letters_list:
            return False
    return True

def uses_all(word, letters_list):
    return uses_only(letters_list, word)

def avoids_in_file(file, forbidden_words):
    for line in file:
        word_to_check = line.strip()
        if avoids(word_to_check, forbidden_words):
            print("There is no forbidden word in this string")



def exercise_nine_seven(file):
    i = 0
    count = 0
    for line in file:
        word = line.strip()
        if len(word) > 6:
            print(word)
            print(len(word))
            for letter in word:
                print(i)
                if (word[i] == word[i+1]) and (len(word) != i+2):
                    if word[i+2] == word[i+3]: 
                        if word[i+4] == word[i+5]:
                            return "achei porra"
                i = i+1
    return "achei nada"

#count_e_percentage(file)
print(exercise_nine_seven(file))

forbidden_words = ["a", "b", "c"]
#avoids_in_file(file, forbidden_words)

world_to_check = "split"
letters_list = ["s", "p", "l", "i", "t"]
#print(uses_only(world_to_check, letters_list))

world_to_check = "aeiou"
letters_list = ["a", "e", "i", "o", "u"]
#print(uses_all(world_to_check, letters_list))


