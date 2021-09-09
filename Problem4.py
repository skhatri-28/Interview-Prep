def palindromePermutation(word):
    dict={}
    for c in word:
        if (c!=" "):
            if (c not in dict):
                dict[c] = 1
            else:
                x = dict[c]
                dict.update({c: x+1})
    counter = 0
    for x in dict:
        incorrect_chars = False
        if dict[x] == 1:
            counter+=1
        elif dict[x]%2==1:
            incorect_chars = True
    word = word.replace(" ", "")
    if ((len(word))%2 == 1 and counter==1 and incorrect_chars == False):
        return True
    elif ((len(word))%2==0 and counter==0 and incorrect_chars == False):
        return True
    else:
        return False

def main():
    print(palindromePermutation("braid"))

if __name__ == "__main__":
    main()