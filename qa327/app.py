# Import sys to get text file arguments
import sys
# Import re to ensure number and name validity
import re

# Definie constants
LOGIN = "login"
LOGGED_OUT = "logged_out"
NOT_LOGGED_IN = "not_logged_in"
NO_MODE = "no_mode"
MACHINE = "machine"
AGENT = "agent"
LOGOUT = "logout"
CREATEACC = "createacct"
DELETEACC = "deleteacct"
WITHDRAW = "withdraw"
DEPOSIT = "deposit"
TRANSFER = "transfer"

# Return a formatted transaction summary line given the 5 data pieces
def summary_line(code, to_acc, amount, from_acc, name):
    if code == LOGOUT:
        return "EOS 0000000 000 0000000 ***\n"
    elif code == CREATEACC:
        return "NEW {} 000 0000000 {}\n".format(to_acc, name)
    elif code == DELETEACC:
        return "DEL {} 000 0000000 {}\n".format(to_acc, name)
    elif code == DEPOSIT:
        return "DEP {} {} 0000000 ***\n".format(to_acc, amount)
    elif code == WITHDRAW:
        return "WDR 0000000 {} {} ***\n".format(amount, from_acc)
    elif code == TRANSFER:
        return "XFR {} {} {} ***\n".format(to_acc, amount, from_acc)
    else:
        return "ERROR"

# Ensure account number string is valid
def valid_number(number):
    return re.match(r'^[1-9][0-9]{6}$', number)

# Ensure account name string is valid
def valid_name(name):
    return re.match(r'^[a-zA-Z\d][\w\s]{1,28}[a-zA-Z\d]$', name)

# Start machine core logic
def main():
    PATH_VALID_ACCOUNTS = sys.argv[1]
    PATH_TRANSACTION_SUMMARY = sys.argv[2]
    # Begin machine without logging in
    state = NOT_LOGGED_IN
    # Keep a transaction log of all the transactions then write to
    # TSF at the end
    transaction_log = []
    # Keep a dictionary of valid accounts so they may be accessed in O(1)
    valid_accounts_list = {}

    # Perpetually loop the program using state logic
    while state == NOT_LOGGED_IN:
        # Set blank dictionary to track the total withdrawn, deposited,
        # and transferred out of a given account to ensure the account never
        # surpasses the machine limits
        total_withdrawn = {}
        total_deposited = {}
        total_transferred_out = {}
        # Prompt user to login
        login = input("Enter '{}' to begin.\n".format(LOGIN))
        if login == LOGIN:
            # Enter a mode-less state after the user has logged in
            state = NO_MODE
            while state == NO_MODE:
                # Allow the user to choose their mode or log out without choosing one
                mode_choice = input("Please choose either '{}' or '{}' mode:\n".format(MACHINE, AGENT))
                if mode_choice == MACHINE or mode_choice == AGENT:
                    # Read the accounts file once machine or agent is chosen
                    print("Using {} mode.".format(mode_choice))
                    print("Attempting to read valid accounts file.")
                    try:
                        with open(PATH_VALID_ACCOUNTS, 'r') as valid_accounts_file:
                            # Scrape the accounts from the file into a dictionary
                            # NOTE: Exclude special number
                            print("Successfully read valid accounts file.")
                            spec_num_encountered = False
                            read_successful = True
                            for account in valid_accounts_file:
                                current = account.split()[0]
                                try:
                                    # Ensure current is an integer
                                    currentInt = int(current)
                                    if len(current) != 7:
                                        print("Account in list of valid accounts is not 7 digits.")
                                        read_successful = False
                                        break
                                    if current == "0000000":
                                        if spec_num_encountered:
                                            print("Account in list of valid accounts is the illegal special number.")
                                            read_successful = False
                                            break
                                        else:
                                            valid_accounts_list[current] = None
                                            spec_num_encountered = True
                                    else:
                                        if valid_number(current):
                                            valid_accounts_list[current] = None
                                        else:
                                            valid_accounts_list[current] = None
                                            read_successful = False
                                            print("Account in list of valid accounts is invalid.")
                                            print("Should not begin with a 0 and should be 7 digits long.")
                                            break
                                except ValueError:
                                    print("Account in list of valid accounts is not a proper integer.")
                                    read_successful = False
                                    break
                            if not valid_accounts_list:
                                print("Failed to load accounts file.")
                            elif read_successful:
                                if spec_num_encountered:
                                    state = mode_choice
                                else:
                                    print("Valid accounts list does not contain special number 0000000.")
                                    state = LOGGED_OUT
                            else:
                                state = LOGGED_OUT
                        # Set the state to either agent or machine

                    except Exception as error:
                        # Error handle
                        print("Error reading valid accounts file.")
                        print(error)
                # Write EOS to the TSF if the user never chose a mode
                elif mode_choice == LOGOUT:
                    print("Logging out.")
                    transaction_log.append(summary_line(LOGOUT, "", "", "", ""))
                    state = LOGGED_OUT
                    with open(PATH_TRANSACTION_SUMMARY, 'a+') as transaction_summary_file:
                        for line in transaction_log:
                            transaction_summary_file.write(line)
                else:
                    # Error handle and stay in NO_MODE state
                    print("Error selecting mode.")
                    print("'{}' is not a valid login mode.".format(mode_choice))

            # Enter agent mode state loop
            while state == AGENT:
                transaction = input("Please input an {} transaction or log out:\n".format(AGENT))
                if transaction == LOGOUT:
                    print("Logging out.")
                    transaction_log.append(summary_line(LOGOUT, "", "", "", ""))
                    state = LOGGED_OUT
                    # Write out transaction log to the TSF
                    with open(PATH_TRANSACTION_SUMMARY, 'a+') as transaction_summary_file:
                        for line in transaction_log:
                            transaction_summary_file.write(line)
                # CREATEACC - Agent only priv.
                elif transaction == CREATEACC:
                    # Check number validity
                    number_valid = False
                    while not number_valid:
                        account_number = input("Please input account number:\n")
                        if not valid_number(account_number):
                            print("Invalid account number. Must be exactly 7 digits, not beginning with 0.")
                        elif account_number in valid_accounts_list:
                            print("Account number is taken. Choose something unique.")
                        else:
                            number_valid = True
                    # Check name validity
                    name_valid = False
                    while not name_valid:
                        account_name = input("Please input account name:\n")
                        if not valid_name(account_name):
                            print("Invalid account name. Must be between 3 and 30 characters, not starting or ending with a space.")
                        else:
                            name_valid = True
                    # Append line to transaction log
                    transaction_log.append(summary_line(CREATEACC, account_number, "", "", account_name))
                    print("Successfully created account {} - {}".format(account_number, account_name))
                # Continue for each other transaction
                elif transaction == DELETEACC:
                    number_valid = False
                    while not number_valid:
                        account_number = input("Please input account number:\n")
                        if not valid_number(account_number):
                            print("Invalid account number. Must be exactly 7 digits, not beginning with 0.")
                        else:
                            number_valid = True
                    name_valid = False
                    while not name_valid:
                        account_name = input("Please input account name:\n")
                        if not valid_name(account_name):
                            print("Invalid account name. Must be between 3 and 30 characters, not starting or ending with a space.")
                        else:
                            name_valid = True
                    if account_number in valid_accounts_list:
                        del valid_accounts_list[account_number]
                        transaction_log.append(summary_line(DELETEACC, account_number, "", "", account_name))
                        print("Successfully deleted account {} - {}".format(account_number, account_name))
                    else:
                        print("Account not found, could not be deleted.")
                elif transaction == WITHDRAW:
                    number_valid = False
                    while not number_valid:
                        account_number = input("Please input account number:\n")
                        if not valid_number(account_number):
                            print("Invalid account number. Must be exactly 7 digits, not beginning with 0.")
                        else:
                            number_valid = True

                    # Ensure amount limit is not surpassed
                    amount_valid = False
                    while not amount_valid:
                        amount = input("Please input an amount to withdraw (in cents):\n")
                        try:
                            if int(amount) > 99999999:
                                print("Invalid amount. Unable to make withdrawls above $999,999.99.")
                            else:
                                amount_valid = True
                        except ValueError:
                            print("Invalid amount. Must be an integer.")

                    if account_number in valid_accounts_list:
                        tempLog = summary_line(WITHDRAW, "", amount, account_number, "")
                        if len(tempLog) > 61:
                            print("Transaction would exceed 61-character summary limit.")
                        else:
                            transaction_log.append(tempLog)
                            print("Successfully withdrew {} from {}".format(amount, account_number))
                    else:
                        print("Account not found, could not withdraw.")
                elif transaction == DEPOSIT:
                    number_valid = False
                    while not number_valid:
                        account_number = input("Please input account number:\n")
                        if not valid_number(account_number):
                            print("Invalid account number. Must be exactly 7 digits, not beginning with 0.")
                        else:
                            number_valid = True
                    amount_valid = False
                    while not amount_valid:
                        amount = input("Please input an amount to deposit (in cents):\n")
                        try:
                            if int(amount) > 99999999:
                                print("Invalid amount. Unable to make deposits above $999,999.99.")
                            else:
                                amount_valid = True
                        except ValueError:
                            print("Invalid amount. Must be an integer.")

                    if account_number in valid_accounts_list:
                        tempLog = summary_line(DEPOSIT, account_number, amount, "", "")
                        if len(tempLog) > 61:
                            print("Transaction would exceed 61-character summary limit.")
                        else:
                            transaction_log.append(tempLog)
                            print("Successfully deposited {} into {}".format(amount, account_number))
                    else:
                        print("Account not found, could not deposit.")

                elif transaction == TRANSFER:
                    number_sender_valid = False
                    while not number_sender_valid:
                        account_number_sender = input("Please input sender account number:\n")
                        if not valid_number(account_number_sender):
                            print("Invalid sender account number. Must be exactly 7 digits, not beginning with 0.")
                        else:
                            number_sender_valid = True
                    number_recipient_valid = False
                    while not number_recipient_valid:
                        account_number_recipient = input("Please input recipient account number:\n")
                        if not valid_number(account_number_recipient):
                            print("Invalid sender account number. Must be exactly 7 digits, not beginning with 0.")
                        else:
                            number_recipient_valid = True
                    amount_valid = False
                    while not amount_valid:
                        amount = input("Please input an amount to withdraw (in cents):\n")
                        try:
                            if int(amount) > 99999999:
                                print("Invalid amount. Unable to make deposits above $999,999.99.")
                            else:
                                amount_valid = True
                        except ValueError:
                            print("Invalid amount. Must be an integer.")

                    if account_number_sender in valid_accounts_list and account_number_recipient in valid_accounts_list:
                        tempLog = summary_line(TRANSFER, account_number_sender, amount, account_number_recipient, "")
                        if len(tempLog) > 61:
                            print("Transaction would exceed 61-character summary limit.")
                        else:
                            transaction_log.append(tempLog)
                            print("Successfully transferred {} from {} into {}".format(amount, account_number_sender, account_number_recipient))
                    elif account_number_sender in valid_accounts_list and not account_number_recipient in valid_accounts_list:
                        print("Recipient account not found, could not transfer.")
                    elif account_number_recipient in valid_accounts_list and not account_number_sender in valid_accounts_list:
                        print("Sender account not found, could not transfer.")
                    else:
                        print("Both sender and recipient accounts not found, could not transfer.")

                else:
                    print("Invalid transaction code '{}'.".format(transaction))

            while state == MACHINE:
                transaction = input("Please input an {} transaction or log out:\n".format(AGENT))
                if transaction == LOGOUT:
                    print("Logging out.")
                    transaction_log.append(summary_line(LOGOUT, "", "", "", ""))
                    state = LOGGED_OUT
                    with open(PATH_TRANSACTION_SUMMARY, 'a+') as transaction_summary_file:
                        for line in transaction_log:
                            transaction_summary_file.write(line)
                elif transaction == WITHDRAW:
                    number_valid = False
                    while not number_valid:
                        account_number = input("Please input account number:\n")
                        if not valid_number(account_number):
                            print("Invalid account number. Must be exactly 7 digits, not beginning with 0.")
                        else:
                            number_valid = True
                    if not account_number in total_withdrawn:
                        total_withdrawn[account_number] = 0
                    amount_valid = False
                    while not amount_valid:
                        amount = input("Please input an amount to withdraw (in cents):\n")
                        try:
                            if int(amount) > 100000:
                                print("Invalid amount. Unable to make withdrawls above $1,000.00.")
                            # Check total withdrawals for this account and check limit
                            elif total_withdrawn[account_number] + int(amount) > 500000:
                                print("Invalid amount. Withdrawl would exceed $5,000.00 daily limit.")
                            else:
                                amount_valid = True
                        except ValueError:
                            print("Invalid amount. Must be an integer.")
                    total_withdrawn[account_number] += int(amount)
                    if account_number in valid_accounts_list:
                        tempLog = summary_line(WITHDRAW, "", amount, account_number, "")
                        if len(tempLog) > 61:
                            print("Transaction would exceed 61-character summary limit.")
                        else:
                            transaction_log.append(tempLog)
                            print("Successfully withdrew {} from {}".format(amount, account_number))
                    else:
                        print("Account not found, could not withdraw.")

                elif transaction == DEPOSIT:
                    number_valid = False
                    while not number_valid:
                        account_number = input("Please input account number:\n")
                        if not valid_number(account_number):
                            print("Invalid account number. Must be exactly 7 digits, not beginning with 0.")
                        else:
                            number_valid = True
                    if not account_number in total_deposited:
                        total_deposited[account_number] = 0
                    amount_valid = False
                    while not amount_valid:
                        amount = input("Please input an amount to deposit (in cents):\n")
                        try:
                            if int(amount) > 200000:
                                print("Invalid amount. Unable to make deposits above $2,000.00.")
                            # Check total deposits for this account and check limit
                            elif total_deposited[account_number] + int(amount) > 500000:
                                print("Invalid amount. Deposit would exceed daily limit of $5,000.00.")
                            else:
                                amount_valid = True
                        except ValueError:
                            print("Invalid amount. Must be an integer.")
                    total_deposited[account_number] += int(amount)
                    if account_number in valid_accounts_list:
                        tempLog = summary_line(DEPOSIT, account_number, amount, "", "")
                        if len(tempLog) > 61:
                            print("Transaction would exceed 61-character summary limit.")
                        else:
                            transaction_log.append(tempLog)
                            print("Successfully deposited {} into {}".format(amount, account_number))

                    else:
                        print("Account not found, could not deposit.")
                elif transaction == TRANSFER:
                    number_sender_valid = False
                    while not number_sender_valid:
                        account_number_sender = input("Please input sender account number:\n")
                        if not valid_number(account_number_sender):
                            print("Invalid sender account number. Must be exactly 7 digits, not beginning with 0.")
                        else:
                            number_sender_valid = True
                    if not account_number_sender in total_transferred_out:
                        total_transferred_out[account_number_sender] = 0
                    number_recipient_valid = False
                    while not number_recipient_valid:
                        account_number_recipient = input("Please input recipient account number:\n")
                        if not valid_number(account_number_recipient):
                            print("Invalid sender account number. Must be exactly 7 digits, not beginning with 0.")
                        else:
                            number_recipient_valid = True
                    amount_valid = False
                    while not amount_valid:
                        amount = input("Please input an amount to withdraw (in cents):\n")
                        try:
                            if int(amount) > 1000000:
                                print("Invalid amount. Unable to make transfers above $10,000.00.")
                            # Check total transfers out of this account and check limit
                            elif total_transferred_out[account_number_sender] + int(amount) > 1000000:
                                print("Invalid amount. Transfer would exceed daily limit of $10,000.00.")
                            else:
                                amount_valid = True
                        except ValueError:
                            print("Invalid amount. Must be an integer.")
                    total_transferred_out[account_number_sender] += int(amount)
                    if account_number_sender in valid_accounts_list and account_number_recipient in valid_accounts_list:
                        tempLog = summary_line(TRANSFER, account_number_sender, amount, account_number_recipient, "")
                        if len(tempLog) > 61:
                            print("Transaction would exceed 61-character summary limit.")
                        else:
                            transaction_log.append(tempLog)
                            print("Successfully transferred {} from {} into {}".format(amount, account_number_sender, account_number_recipient))

                    elif account_number_sender in valid_accounts_list and not account_number_recipient in valid_accounts_list:
                        print("Recipient account not found, could not transfer.")
                    elif account_number_recipient in valid_accounts_list and not account_number_sender in valid_accounts_list:
                        print("Sender account not found, could not transfer.")
                    else:
                        print("Both sender and recipient accounts not found, could not transfer.")
                else:
                    print("Invalid transaction code '{}'.".format(transaction))
        elif login == LOGOUT:
            print("Logging out.")
            transaction_log.append(summary_line(LOGOUT, "", "", "", ""))
            state = LOGGED_OUT
            with open(PATH_TRANSACTION_SUMMARY, 'a+') as transaction_summary_file:
                for line in transaction_log:
                    transaction_summary_file.write(line)
        else:
            print("Invalid login attempt.")
            print("Please log in before attempting any transactions.")

if __name__ == "__main__":
    main()
