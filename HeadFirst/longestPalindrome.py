__author__ = "ResearchInMotion"

def longestPalindrome(st):
    longest = ""
    for i in range(len(st)):
        for j in range(len(st)-i-1):
            if st[i:j] == st[i:j][::-1] :
                if len(longest) < len(st[i:j]):
                    longest = st[i:j]
    return longest

print(longestPalindrome("babad"))

