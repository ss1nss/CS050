# define convert emojis and a main to define/ encapsualte all texts within

def main():

    a = input()
    print(convert(a))

def convert(emoji):
    emoji = emoji.replace(":)","🙂")
    emoji = emoji.replace(":(","🙁")
    return emoji

#def convert(emoji):
#    return emoji.replace(":)","🙂").replace(":(","🙁")






















main()
