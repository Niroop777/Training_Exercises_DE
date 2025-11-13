#Ex 4

#Given a list of words, create a dictionary where keys are words and values are the counts of vowels in each word.

def Vow_word_count(words):

    vowels="aeiouAEIOU"

    return {word: sum(1 for ch in word if ch in vowels) for word in words}


inp_lst = ["apple","kane","harry","shoot","gamblers","english","opinion","AEIOU"]
print(Vow_word_count(inp_lst)) 


"""

This function takes a list of words and uses dictionary comprehension.

For each word, it counts how many characters are vowels.

It returns a dictionary with words as keys and vowel counts as values.

"""
