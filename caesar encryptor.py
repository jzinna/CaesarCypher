''' This program will take a text and a key (a number), and return the text shifted (number) of letters to the right
>>> main('test.txt', 14)
'bb'
'''

import string


class WorkingText:  # class for text to be encrypted.  Will require a string and also the key
    # create an empty private list, __encrypted_list => do I need it?

    # constructor __init__(self, lines_of_the_text, key):
        # create variable lns_txt from lines_of_the_text
        # create variable ky from key
        # if the key is > 26
            # show message 'key must be lower than 26')
            # raise KeyError for now, later may ask user for a viable key
        # if key is within range:
            # constructor will establish the two shifted alphabets, upper and lower case, based on the key provided
            # lowercase shifted alphabet will concatenate the original from the key to the end, and the original from
                        # start to key-1        self.lcase_shftd_alph = string.ascii_lowercase[(self.ky - 1):25] +
                        # string.ascii_lowercase[0:(self.ky - 2)]
            # uppercase uses same principle     self.ucase_shftd_alph = string.ascii_uppercase[(self.ky - 1):25] +
                        # string.ascii_uppercase[0:(self.ky - 2)]

    # define the principal method of the class, encrypt(self):
        # iterate through each position of the list lns_txt, which will each be a line of the text
            # on each line, a list can be created, list(line), ('characters_list') it should have each character in a different position
            # iterate through each character
                # check if it's alphanumeric (can list command create blank spaces or newline chars??)
                    # if it is, call method encrypted_character
                # if it's not alphanumeric, flow should go to next iteration
                # replace this character in the list (each position in the list is a character, so it's a simple list replacement)
            # replace the original version of the line with the shifted version, simple list replacement
        # once we have the whole list of words in the file shifted, convert the list to a string
        # return the string as the response, shifted text

    # define an internal method (function?) that will take each character and return the encrypted one
                    # method can be called encrypted_character (methods or functions should name what they return)
        # check if character is lower case
            # if it is, find its position pos in the unshifted lcase alphabet
            # determine the encrypted character by looking for variable pos in the shifted lcase alphabet
        # if not, it's upper case
            # find its position pos in the unshifted ucase alphabet
            # determine the encrypted character by looking for variable pos in the shifted ucase alphabet
        # return the encrypted character






    '''def encrypt_with_comprehension(self):
        encrypted_list = ['sonrisa' for item in self.lns_txt]
        print(encrypted_list)       '''


def main(path, key):
    file_object = open(path, 'r')
    lines_of_the_text = file_object.readlines() #each position in the list will be a string with one line of the given text
    # create an encrypted file object of class 'working_text', providing the list of strings and the key
    text_to_encrypt = WorkingText(lines_of_the_text, key)
    # call method encrypt, and assign the result (a string) to a variable, and print it, or create a new file with the encrypted message
    encrypted_text = text_to_encrypt.encrypt()

    # just for good habit, will close the file-object after coming back from the method and doing stuff with the result
    file_object.close()




if __name__== "__main__":
    import doctest
    doctest.testmod()
