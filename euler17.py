'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there 
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''




def nlc(number):
    s = 0
    for i in range(1, number+1):
        letter_count = getLetterCount(i)
        s += letter_count
    return s



def getLetterCount(i):
        
    dictionary = dict.fromkeys(['and', 1, 2, 6, 10, ], 3)
    dictionary.update(dict.fromkeys([0, 4, 5, 9], 4))
    dictionary.update(dict.fromkeys([3, 7, 8, 40, 50, 60], 5))
    dictionary.update(dict.fromkeys([11, 12, 20, 30, 80, 90], 6))
    dictionary.update(dict.fromkeys([15, 16, 100], 7))
    dictionary.update(dict.fromkeys([13, 14, 18, 19, 1000], 8))
    dictionary.update(dict.fromkeys([17], 9))
    # print(dictionary[14])


    count = 0
    temp_i = i

    while(temp_i != 0):
        count += 1
        temp_i //= 10

    if count == 1:
        return dictionary[i]

    if count == 2:
        pass






