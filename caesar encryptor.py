''' This program will take a text and a key (a number), and return the text shifted (number) of letters to the right
>>> main('test.txt', 14)
'bb'
'''

import string


class WorkingText:  # class for text to be encrypted.  Will require a string and also the key
    # do I need this list?  __encrypted_list = []
    # __lcase_alph = string.ascii_lowercase
    # __ucase_alph = string.ascii_uppercase


    def __init__(self, lines_of_the_text, key):
        self.lns_txt = lines_of_the_text
        self.ky = key
    # constructor will establish the two shifted alphabets, upper and lower case, based on the key provided
        if self.ky > 26:
            print('key must be lower than 26')
            raise KeyError

        else:
            self.lcase_shftd_alph = string.ascii_lowercase[(self.ky - 1):25] + string.ascii_lowercase[0:(self.ky - 2)]
            self.ucase_shftd_alph = string.ascii_uppercase[(self.ky - 1):25] + string.ascii_uppercase[0:(self.ky - 2)]

    def encrypt(self):  # define the principal method of the class, encrypt(self):
        # iterate through each position of the list lns_txt, which will each be a line of the text
        for line in self.lns_txt:
            # on each line, a list can be created, list(line), it should have each character in a different position
            characters_list = list(line)
            # iterate through each character
            for char in characters_list:
                # check if it's alphanumeric (can list command create blank spaces or newline chars?? or any non-alphanumeric?)
                if char.isalpha():
                    __class__.encrypted_character(char)
                else:
                    # flow should continue.  If do nothing, will it continue?


                # replace the original version of the word with the shifted version
        # once we have the whole list of words in the file shifted, convert the list to a string
        # return the string as the response, shifted text

    def encrypted_character(self, char):
        # check if lower or upper case
        if char.islower():
            # find its position pos in the unshifted lcase alphabet
            pos = string.ascii_lowercase.find(char)
            # find the new character in the shifted lcase alphabet, using pos
            newchar = self.lcase_shftd_alph(pos)
        else:
            # find its position pos in the unshifted ucase alphabet
            pos = string.ascii_uppercase.find(char)
            # find the new character in the shifted ucase alphabet, using pos
            newchar = self.ucase_shftd_alph(pos)
            # replace this character in the list


def main(path, key):
    # key = 20
    # file_object = open('test.txt','r')
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
