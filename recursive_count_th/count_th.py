'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    count = 0
    index_1 = 0
    index_2 = 1
    if index_2 < len(word):
        if (word[index_1] == 't') and (word[index_2] == 'h'):
            count += 1
            index_1 += 1
            index_2 += 1
            count_th(word[index_1:])
        else:
            index_1 += 1
            index_2 += 1
            count_th(word[index_1:])

    return count
