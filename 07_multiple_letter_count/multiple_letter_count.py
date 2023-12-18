def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    myHashTable = {} 
    for letter in phrase:
        if letter in myHashTable:
            myHashTable[letter] += 1
        else: 
            myHashTable[letter] = 1
    return myHashTable




# print(multiple_letter_count('yay'))
# print("--------------------------------------")
# print(multiple_letter_count('Aequeosalinocalcalinoceraceoaluminosocupreovitriolic'))
# print("---------------------------------------")
# print(multiple_letter_count('TampA'))