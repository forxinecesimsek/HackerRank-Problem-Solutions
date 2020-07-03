n= int(input())
word = input()
shift_number= int(input())
word_new=""

original_alphabet = list("abcdefghijklmnopqrstuvwxyz")
rotated_alphabet = original_alphabet[shift_number%26:] + original_alphabet[:shift_number%26]

for y in word:
    if y in original_alphabet:
        index= original_alphabet.index(y)
        z=rotated_alphabet[index]
        word_new += z
    elif y.isupper():
        index= original_alphabet.index(y.lower())
        z=rotated_alphabet[index]
        word_new += z.upper()
    else:
        word_new += y

print(word_new)