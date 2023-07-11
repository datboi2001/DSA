
string = list(input())


# Deletes all vowels
# inserts a character '.' before each consonant
# replaces all uppercase consonants with corresponding lowercase ones.

vowels = set('aeiouyAEIOUY')

for i in range(len(string)):
    if string[i] in vowels:
        string[i] = ''
    else:
        string[i] = '.' + string[i].lower()
print(''.join(string))