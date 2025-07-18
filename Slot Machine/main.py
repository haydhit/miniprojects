import random

MAX_LINES = 3                                                                               # MAX_LINES is in all caps is because its a constant value, meaning it will not change.
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range (lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():                                            # .items() gives us both the key and value associated in a dictionary and using both of them rather than looping, manually reference the values.
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def deposit():                                                                              # collecting user input to know how much they are depositing
    while True:                                                                             # while loop to continually ask the user to enter a deposit amount until valid amount.
        amount = input("How much would you like to deposit: $")
        if amount.isdigit():                                                                # isdigit is to check if it is a valid whole number.
            amount = int(amount)
            if amount > 0:
                break                                                                       # once conditions are met, while loop is broken and proceeds to next line of code.
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:                                                                             # while loop to continually ask the user to enter a deposit amount until valid amount.
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():                                                                # isdigit is to check if it is a valid whole number.
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break                                                                       # once conditions are met, while loop is broken and proceeds to next line of code.
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line: $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    f"Amount must be between ${MIN_BET} - ${MAX_BET}.")                   # "f String" is neater to concanenate.
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is ${balance}.")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}!")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():                                                                                 # this function is called back if user wants to re-run the program. (e.g. "Do you want to play again?")
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play! (Q to Quit...)")
        if answer == "Q":
            break
        balance += spin(balance)

    print(f"You are left with: ${balance}")

main()                