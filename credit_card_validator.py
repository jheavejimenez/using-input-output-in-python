"""

 Implemented using  Luhn’s algorithm
 https://www.geeksforgeeks.org/luhn-algorithm/

"""


def main():
    # asking the user to enter
    credit_card_number = int(input("Please enter credit card number: "))

    # while credit_card_number < 0:
    if is_valid(credit_card_number):
        credit_card_brand(credit_card_number)
    else:
        print("INVALID")


# check if it is valid
def is_valid(credit_card_number):
    length = find_length(credit_card_number)
    if length in [13, 15, 16] and check_sum(credit_card_number):
        return 0
    else:
        return 1


# find the length of credit card
def find_length(credit_card_number):
    count = 0
    while credit_card_number > 0:
        credit_card_number = credit_card_number // 10
        count += 1

    return count


# checking if credit card is == 0
def check_sum(number):
    credit_card_sum = 0
    count = 0
    while number > 0:
        number = number // 10
        count += 1
        if count % 2 == 0:
            credit_card_sum += number % 10
        else:
            digit = 2 * (number % 10)
            credit_card_sum += digit / 10 + digit % 10

    return (credit_card_sum % 10) == 0


# for printing credit card brand   

def credit_card_brand(number):
    # checking 34 is the first 2 digit and 'e13' = 13 zero
    if 34e13 <= number < 35e13 or 37e13 <= number < 38e13:
        print("AMEX")
    elif 51e14 <= number < 56e14:
        print("MASTERCARD")
    elif 4e12 <= number < 5e12 or 4e15 <= number < 5e15:
        print("VISA")
    else:
        print("INVALID")


if __name__ == '__main__':
    main()
