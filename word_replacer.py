#replace a word

def replace_word():
    str= "Hi guys, I am Ram and bla bla bla"
    word_to_replace=input("enter the word to replace: ")
    word_replacement=input("enter the word replacement: ")
    print(str.replace(word_to_replace,word_replacement))

replace_word()    