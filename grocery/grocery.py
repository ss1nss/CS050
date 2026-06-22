def main():

    prompt_item("") #probably don't need to make a str function...

def prompt_item(item_list):
    grocery = {}

    while True:
        try:
           item = input(item_list).upper().strip()
           if item in grocery:
               grocery[item] += 1
           else:
               grocery[item] = 1
        except EOFError:
            for i in sorted(grocery):
                print(grocery[i], i)
            break
        except (KeyError):
            pass


main()
