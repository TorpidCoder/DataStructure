__author__ = "ResearchInMotion"




def validParanthesis(s):
    brackets = ['()', '{}', '[]']
    while any(x in s for x in brackets):
        for br in brackets:
            s = s.replace(br, '')
    return not s

string = "()"
print(string, "-", "Balanced" if validParanthesis(string) else "Unbalanced")
