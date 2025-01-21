def main():
    print("Supermarket price of product")



    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    total_sum = 0

    while True:

        try:
            selection = int(input("Please select product (1-10) 0 to Quit: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if selection == 0:
            break
        elif 1 <= selection <= 10:
            product_price = prices[selection - 1]
            total_sum += product_price
            print(f"Product: {selection} Price: {product_price}")
        else:
            print("Invalid product number. Please select between 1 and 10.")


    print(f"Total: {total_sum}")


    try:
        payment = int(input("Payment: "))
        if payment >= total_sum:
            change = payment - total_sum
            print(f"Change: {change}")
        else:
            print("Insufficient payment. Please provide enough money.")
    except ValueError:
        print("Invalid input for payment. Please enter a number.")



if __name__ == "__main__":
    main()
