''' This program will take a text and a key (a number), and return the text shifted (number) of letters to the right '''

import string
class WorkingText
# class for text to be encrypted.  Will require a list of lines and a key
    def __new__(self , lines_of_the_text , key)
        if key > 26:
            raise TypeError('key must be lower than 26')
            # break => won't work here, other ideas for not allowing creation of the object?
        else:
            return WorkingText.__new__(self , lines_of_the_text , key)
    
    def __init__(self , lines_of_the_text , key):
        self.lns_txt = lines_of_the_text
        self.ky = key
        __lcase_alph = string.ascii_lowercase
        __ucase_alph = string.ascii_uppercase
        # constructor will establish the two shifted alphabets, upper and lower case, based on the key provided
        lcase_shftd_alph = __lcase_alph[(self.ky - 1):25] + __lcase_alph[0:(self.ky - 2)]
        ucase_shftd_alph = __ucase_alph[(self.ky - 1):25] + __ucase_alph[0:(self.ky - 2)]
    
    # def encrypt()
        # iterate through each position, which will each be a line of the text
            # on each line, a list can be created, list(line), it should have each character in a different position (check if the... 
                                                        # ...list from the previous iteration is replaced, if not need to wipe it)
            # iterate through each character
                # get_shifted_char(char)
                # replace this character in the list (use comprehension??)
                # replace the original version of the word with the shifted version
        # once we have the whole list of words in the file shifted, convert the list to a string
        # return the string as the response, shifted text
        
        
    # def encrypt_with_comprehension():
        
        
    # def get_shifted_char(char)
        # check if it's alphanumeric (can list command create blank spaces or newline chars??)        
        # check if lower or upper case
        # if lower 
            # find its position pos in the unshifted lcase alphabet
            # find the new character in the shifted lcase alphabet, using pos
        # else
            # find its position pos in the unshifted ucase alphabet
            # find the new character in the shifted ucase alphabet, using pos

script
    # file-objet = open given file, from file path
    # list of strings = file-object.readlines() => each position in the list will be a string with one line of text
    # create an encrypted file object of class 'working_text', providing the list of strings and the key
    # call method encrypt, and assign the result (a string) to a variable, and print it, or create a new file with the encrypted message

    # just for good habit, will close the file-object after coming back from the method and doing stuff with the result


IDEAS
# iterate over each letter of the text and change it for the shifted letter

# don't use a shifted alphabet
    # find the character in the alph, note its position
    # add the key to the position, checking for overflow
    # look for the new position in the alph, note the char
    # replace the old char with the new one, whatever method I use for that

# using range:    (can it be done??)
# create empty new_text (text file, string? can't create this)
# for all letters in text object    How do I do this?  for lines in txt, for words in line, for chars in word?
    # new_text[i] = shifted alphabet[i]   this won't work, need to find a way to 'append' to the text file 
  # (create a class, that will have the required methods to create string char by char)
  # use the replace method of string, each char replaced by a new one?
# return new_text as the 'encrypted text'

# comprehension:
    # I receive a list, a character on each position.  I take that character, apply a function and get a new character (shifted), and...
                            # ...create a new list to hold all new characters
        # if I call the list 'line'
    # shifted line = [function for char in line]
    # the function can be:
    # is character alphanumeric [not sure if needed]
    # check if lower or upper case
    # if lower 
        # find its position pos in the unshifted lcase alphabet
        # find the new character in the shifted lcase alphabet, using pos
    # else
        # find its position pos in the unshifted ucase alphabet
        # find the new character in the shifted ucase alphabet, using pos
  
