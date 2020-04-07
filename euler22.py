'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

'''

import string


filename = 'p022_names.csv'
# alphabet_dictionary = dict.fromkeys(string.ascii_uppercase, 1)
# print(alphabet_dictionary)


alphabet_dictionary = {}
i = 1
for c in string.ascii_uppercase:
    alphabet_dictionary.update({c:i})
    i += 1



def sortNames(filename):
    # opens file, reads name and sorts alphabetically using built in sort() method

    names_array = []

    with open(filename, 'r') as f, open('output.txt', 'w') as fo: #the file has unwanted double quotes, remove them
        for line in f:
            fo.write(line.replace('"', ''))

    with open('output.txt', 'r') as txt_file:
        names_array = txt_file.read().split(',')

    
    return sorted(names_array)



sorted_names_array = sortNames(filename)
# print(sorted_names_array[0])




def nameScoreFunc(sorted_names_array, alphabet_dictionary):
    nameSum = 0
    nameScore = []
    for name in range(len(sorted_names_array)):
        nameSum = 0
        for character in sorted_names_array[name]:
            nameSum += alphabet_dictionary.get(character)
        nameScore.append((name+1)*nameSum)
    
    return nameScore



print(sum(nameScoreFunc(sorted_names_array, alphabet_dictionary)))








    
