def urlify(word, char_count):
    temp_holder = char_count
    for i in range(temp_holder):
        if word[i] == ' ':
            word = shift(word, temp_holder, i)
            temp_holder+=2
    return word
    

def shift(word, char_count, i):
    for j in range(char_count-1, i, -1):
        word[j+2] = word[j]
    word[i] = '%'
    word[i+1] = '2'
    word[i+2] = '0'
    return word


def main():
    temp = ['M', 'R', ' ', 'J', 'O', 'H', 'N', ' ', 'S', 'M', 'I', 'T', 'H', ' ', ' ', ' ', ' ']
    result = urlify(temp, 13)
    print(result)

if __name__ == "__main__":
    main()
