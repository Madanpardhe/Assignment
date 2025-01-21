def tester(string="Too short"):

    if len(string) < 20:
        print("Too short")
    else:
        print(string)

def main():

    while True:
        user_input = input("Write something what you want: ")
        if user_input.lower() == "quit":
            break
        tester(user_input)

if __name__ == "__main__":
    main()
