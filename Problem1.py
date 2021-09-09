def findDups(word):
    dict = {}
    for c in word:
        if c in dict.keys():
            x = dict.get(c)
            dict.update({c:x+1})
        else:
            dict[c]=1
    if len(dict) != len(word):
        return False
    else:
        return True

def findDups2(word):
    sorted_word = sorted(word)
    sorted_string = ''.join(sorted_word)
    for i in range(1, len(sorted_string)):
        if (sorted_string[i] == sorted_string[i-1]):
            return False
    return True

def main():
    print(findDups2("start"))

if __name__ == "__main__":
    main()