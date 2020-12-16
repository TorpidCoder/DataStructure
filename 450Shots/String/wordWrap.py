__author__ = "ResearchInMotion"


def word_wrapper(string, width):
    new_string=""
    while len(string)>width:
        #find the position of nearest whitespace char to left of "width"
        index=width-1
        #check the char in the index of string of given width
        #if it is space then continue
        #else reduce the index to check for the space.
        while not string[index].isspace():
            index=index-1
        #remove the line from original string and add it to the new string
        line=string[0:index] + "\n"#separated individual linelines
        new_string=new_string+line#add those line to new_string variable
        string=''+string[index+1:]#updating the string to the remaining words
    #finally string will be left with less than the width.
    #adding those to the output
    return new_string+string
word_to_be_wrapped = "Learn coding. happy coding. Codespeedy helps you to learn coding. It provides coding solutions along with various IT services ( web development, software development etc )."
print(word_wrapper(word_to_be_wrapped,30))