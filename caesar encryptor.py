''' This program will take a text and a key (a number), and return the text shifted (number) of letters to the right
#>>> main('test.txt', 1)
'bb'
'''

import string

class Word
    l_case = string.ascii_lowercase
    u_case = string.ascii_uppercase
    
    def __init__(self,word,key)
        self.word = word
        self.key = key
    
    
    
    
    
class WorkingText:  # class for text to be encrypted.  Will require a string and also the key
    
    def __init__(self, lines_of_the_text, key):
        self.lns_txt = lines_of_the_text
        self.ky = key
    # constructor will establish the two shifted alphabets, upper and lower case, based on the key provided
        if self.ky > 26:        # place this in the main clause?
            print('key must be lower than 26')
            raise KeyError      # in the future, return to the user and ask for a viable key

        else:
            self.lcase_shftd_alph = string.ascii_lowercase[self.ky:26] + string.ascii_lowercase[0:self.ky]
            self.ucase_shftd_alph = string.ascii_uppercase[self.ky:26] + string.ascii_uppercase[0:self.ky]

    def encrypt(self):  # define the principal method of the class, encrypt(self):
        # iterate through the positions of the list lns_txt, which will each be a line of the text
        for j in range(len(self.lns_txt)):
            # on each line, a list can be created, list(line), it should have each character in a different position
            characters_list = list(self.lns_txt[j])
            # iterate through each character

            for i in range(len(characters_list)):
            # check if it's alphanumeric (list command creates non-alphanumeric characters)
                if characters_list[i].isalpha():
                    new_char = __class__.encrypt_char(self, characters_list[i])
                    characters_list[i] = new_char
                else:
                    continue

            self.lns_txt[j] = ''.join(characters_list)  # replace the original version of the line with the shifted version
        # once we have the whole list of words in the file shifted, convert the list to a string
        response = ''.join(self.lns_txt)
        # return the string as the response, shifted text
        return response

    def encrypt_char(self,ch):
        new_char = ch
        if ch.islower():
            # find its position pos in the unshifted lcase alphabet
            pos = string.ascii_lowercase.find(ch)
            # find the new character in the shifted lcase alphabet, using pos
            new_char = self.lcase_shftd_alph[pos]
        if ch.isupper():
            # find its position pos in the unshifted ucase alphabet
            pos = string.ascii_uppercase.find(ch)
            # find the new character in the shifted ucase alphabet, using pos
            new_char = self.ucase_shftd_alph[pos]
        return new_char


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
    file_object = open('result.txt','w')
    file_object.write(encrypted_text)
    file_object.close()

main('hamlet.txt', 1)
"""
if __name__== "__main__":
    import doctest
    doctest.testmod()
"""
