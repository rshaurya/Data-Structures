# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    d = {}
    k = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    for i in t:
        k[i] = k.get(i, 0) + 1

    for i, j in d.items():
        if i not in k or d[i] != k[i]:
            return False
    return True

assert isAnagram('rat', 'car') == False
assert isAnagram('aaabbb', 'bbaaab') == True

s, t = "anagram", "nagaram"
assert isAnagram(s, t) == True
