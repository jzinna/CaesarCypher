''' This program will take a text and a key (a number), and return the text shifted (number) of letters to the right '''

import string
CLASS (list of lines in the text, key)
# class for text to be encrypted.  Will require a string and also the key
    # define two private constants, string.ascii_lowercase and uppercase (these have the alphabet)
    
    # constructor will establish the two shifted alphabets, upper and lower case, based on the key provided
        # if key > 26
            # print that key must be lower than 26
            # break
        # else
            # lcase shifted alph = lcase alph[(key - 1) to 25] + lcase alph[0 to (key - 2)]
            # ucase shifted alph = ucase alph[(key - 1) to 25] + ucase alph[0 to (key - 2)]
    
    # def encrypt()
    check the whole way of dealing with the list
        # will iterate through each position, each line
        # a list can be created, list(line), it should have each character in a different position (check if the list from the previous iteration is replaced, if not need to wipe it)
        # iterate through each character
            # check if it's alphanumeric (list command can create blank spaces or newline chars??)        
            # find its position in the unshifted alphabet
            # new position will be (pos + key)
            # check if lower or upper case
            # if lower use lower alphabet
                # find the new character in the shifted alphabet, using the shifted position
            # else
                # find the new character in the shifted alphabet, using the shifted position
            # replace this character in the list (use comprehension??)
            # replace the original version of the word with the shifted version
        # once we have the whole list of words in the file shifted, convert the list to a string
        # return the string as the response, shifted text


MAIN (file path, key)

# file-objet = open given file
# list of strings = file-object.readlines() => each position in the list is a string with one line of text
# create an encrypted file object of class 'encrypted' or however I'll call it
# call method encrypt providing the list of strings and the key, and assign the result (a string) to a variable, and print it, or create a new file with the encrypted message

# just for good habit, will close the file-object after coming back from the 


IDEAS
# iterate over each letter of the text and change it for the shifted letter

# Try some object oriented things to do.

# using range:    (can it be done??)
# create empty new_text (text file, string? can't create this)
# for all letters in text object    How do I do this?  for lines in txt, for words in line, for chars in word?
    # new_text[i] = shifted alphabet[i]   this won't work, need to find a way to 'append' to the text file 
  # (create a class, that will have the required methods to create string char by char)
  # use the replace method of string, each char replaced by a new one?


# return new_text as the 'encrypted text'
  
