'''
Reverse Words in a Sentence + Reverse The Order
Problem Statement:
Write a function reverse_words(sentence) that takes a string and returns the sentence with
each word reversed and also the order of words reversed.
Input:
reverse_words("Hello World")
reverse_words("I am a Data Engineer")
output:
"olleH dlroW"
"reenignE ataD a ma I"
'''

def reverse_words(sentence):
    #sentence = "I am a Data Engineer"
    words = sentence.split() # ["I", "am", "a", "Data", "Engineer"]
    reverse_words = words[::-1] # ["Engineer", "Data", "a", "am", "I"]
    result = []
    for word in reverse_words:
        result.append(word[::-1]) # ["reenignE", "ataD", "a", "ma", "I"]
    return ' '.join(result)


# Example usage:
input_sentence = "I am a Data Engineer"
print(reverse_words(input_sentence)) # "reenignE ataD a ma I"

input_sentence = "Hello World"
print(reverse_words(input_sentence)) # "olleH dlroW"
