def createHashmap(word):
    dict = {}
    for c in word:
        if c not in dict.keys():
            dict[c] = 1
        else:
            x = dict[c]
            dict.update({c:x+1})
    return dict


def checkPermutation(word1, word2):
    word1_hashmap = createHashmap(word1)
    word2_hashmap = createHashmap(word2)
    if word1_hashmap == word2_hashmap:
        return True
    else:
        return False

    
def main():
    print(checkPermutation("trivial", "atrivil"))

if __name__ == "__main__":
    main()
