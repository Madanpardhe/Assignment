def main():
    shopping_list = []

    while True:

        print("\nWould you like to")
        print("(1) Add")
        print("(2) Remove items")
        print("(3) Quit?")
        choice = input("Choose an option: ")

        if choice == "1":
            item = input("What will be added?: ")
            shopping_list.append(item)

        elif choice == "2":
            if shopping_list:
                print(f"There are {len(shopping_list)} items in the list.")
                try:
                    index = int(input("Which item is deleted?: "))
                    if 0 <= index < len(shopping_list):
                        del shopping_list[index]
                    else:
                        print("Incorrect selection.")
                except ValueError:
                    print("Incorrect selection.")
            else:
                print("The list is empty.")

        elif choice == "3":
            print("The following items remain in the list:")
            for item in shopping_list:
                print(item)
            break

        else:
            print("Incorrect selection.")


if __name__ == "__main__":
    main()
