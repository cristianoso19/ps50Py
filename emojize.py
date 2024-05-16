import emoji

def main():
    text = input("Input: ")
    if emoji.emoji_count(text) >= 1 :
        print(emoji.emojize(text))
    else:
        print(emoji.emojize(text, language='alias'))
main()