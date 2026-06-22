import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
argv1 = ["-f", "--font"]
font_choice = figlet.getFonts()


def main():
    if len(sys.argv) == 1:
        user_input = random.choice(font_choice)
        style("Input: ", user_input)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in font_choice):
        user_input = sys.argv[2]
        style("Input: ", user_input)
    else:
        sys.exit("Invalid usage")

def style(prompt, f):
    user_msg = input(prompt)
    figlet.setFont(font=f)
    print("Output:")
    print(figlet.renderText(user_msg))





main()
