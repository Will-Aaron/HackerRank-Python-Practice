'''
Kevin and stuart play a game where they are given a string S where they have to make
substrings of S. Stuart must make words starting with a constonant while kevin must make
words starting with a vowel. The game ends when both players have made all possible substrings.
They get a point for each occurence of each substring.
'''

#It would be very inefficient to permute across S and make every possible substring
#put that in a list, and count the occurences of that list.

#Actually now that I think about it I don't need to find every occurence of
#a particular word, especially since the existance of another copy of the word merely
#adds another point.

#Most efficient methods, start with a letter of one type, then the length of the remaining parts of that string
#is all the possible extra substrings, so permute, find a vowel, and each time
#you find a vowel, the length of the rest of string is added to score.


def minion_game(string):
    stuart_score, kevin_score = 0,0
    string_length = len(string)
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U']:
            kevin_score += string_length - i
        else:
            stuart_score += string_length - i
    if stuart_score == kevin_score:
        print('Draw')
    elif stuart_score > kevin_score:
        print('Stuart {}'.format(stuart_score))
    else:
        print('Kevin {}'.format(kevin_score))

if __name__ == '__main__':
    s = input()
    minion_game(s)
