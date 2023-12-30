from validation import isfloat


def main():
    number = input("Enter a number: ")
    if isfloat(number):
        print("The number is float.")
    else:
        print("The number is not float.")


if __name__ == "__main__":
    main()
