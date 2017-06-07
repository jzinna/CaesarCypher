''' This program will take a text and a key (a number), and return the text shifted (number) of letters to the right '''

import string
CLASS
# class for text to be encrypted.  Will require also the key
    # define two private constants, string.ascii_lowercase and uppercase (these have the alphabet)
    
    # constructor will establish the two shifted alphabets, upper and lower case, based on the key provided
    
    # def encrypt using list
        # will take the text and apply split, creating a list with all the words in the whole text
        # will iterate through each position, each word
            # a list can be created, list(word), it should have each character in a different position (check if the list from the previous iteration is replaced, if not need to wipe it)
            # iterate through each character
                # find its position in the unshifted alphabet
                # new position will be (pos + key)
                # check if lower or upper case
                # if lower use lower alphabet
                    # find the new character in the shifted alphabet, using the shifted position
                # if upper case use upper alphabet
                    # find the new character in the shifted alphabet, using the shifted position
                # replace this character in the list
            # replace the original version of the word with the shifted version
        # once we have the whole list of words in the file shifted, convert the list to a string
        # return the string as the response, shifted text


MAIN

# file-objet = open given file
# text object = file-object.readlines()

# alphabet = 'abcdef...' => I can import string module and use string.ascii_lowercase as the constant that contains the alphabet
# shifted_alphabet = last n letters + alphabet minus last n letters   => n is the given key

# iterate over each letter of the text and change it for the shifted letter

# Try some object oriented things to do.

# using range:    (can it be done?)
# create empty new_text (text file, string? can't create this)
# for all letters in text object    How do I do this?  for lines in txt, for words in line, for chars in word?
    # new_text[i] = shifted alphabet[i]   this won't work, need to find a way to 'append' to the text file 
  # (create a class, that will have the required methods to create string char by char)
  # use the replace method of string, each char replaced by a new one?


# return new_text as the 'encrypted text'
  
