# A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX_ELEMENTS = 100


def calculate_sum(numbers):
    """Return the sum of a list of integers."""
    return sum(numbers)


def get_integer(prompt, min_value=None, max_value=None):
    """Prompt the user for an integer, with optional min/max validation."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    try:
        n = get_integer(f"Enter the number of elements (1-{MAX_ELEMENTS}): ", 1, MAX_ELEMENTS)
        numbers = []
        print(f"Enter {n} integers:")
        for i in range(n):
            num = get_integer(f"Element {i+1}: ")
            numbers.append(num)
        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit(1)


if __name__ == "__main__":
    main()
