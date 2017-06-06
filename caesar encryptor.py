''' This program will take a text and a key (a number), and return the text shifted (number) of letters to the right '''

# file-objet = open given file
# text object = file-object.readlines()

# alphabet = 'abcdef...' => I can import string module and use string.ascii_lowercase as the constant that contains the alphabet
# shifted_alphabet = last n letters + alphabet minus last n letters   => n is the given key

# iterate over each letter of the text and change it for the shifted letter

# using range:    (can it be done?)
# create empty new_text (text file, string? can't create this)
# for all letters in text object    How do I do this?  for lines in txt, for words in line, for chars in word?
    # new_text[i] = shifted alphabet[i]   this won't work, need to find a way to 'append' to the text file 
  # (create a class, that will have the required methods to create string char by char)
  # use the replace method of string, each char replaced by a new one?

# using list comprehension  (online example was return ''.join([`num` for num in xrange(loop_count)]))
# create list with text object, text_list   => mamushka of splits
# create an empty list with future shifted letters (needed?)
# for all letters (positions) in text_list
    # make the shift at each position and add it to the list (or create, whatever the method does) 
# turn the list into text, file name new_text

# return new_text as the 'encrypted text'
  
