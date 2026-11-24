"""Convert a positive decimal integer to binary and hexadecimal."""


def main():
    try:
        number = int(input("Enter a positive decimal number: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    if number <= 0:
        print("Please enter a number greater than zero.")
        return

    binary = bin(number)[2:]
    hexadecimal = hex(number)[2:].upper()

    print("Binary:", binary)
    print("Hexadecimal:", hexadecimal)


if __name__ == "__main__":
    main()
