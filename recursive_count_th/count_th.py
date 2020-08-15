'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # working solution that does not contain loop, but does not utilize recursion
    # count = 0
    # if len(word) == 0:
    #     return count
    # else:
    #     count = word.count("th")
    #     # return count_th(word)
  
    # return count

    if len(word) == 0:
        return 0
    
    if "th" in word[0:2]:
        return 1 + count_th(word[1:])
    else:
         return count_th(word[1:])
    
