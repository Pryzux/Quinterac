import sys

def main():
    # Parse command line arguments
    master_accounts_file_path = sys.argv[1]
    merged_transaction_summary_file_path = sys.argv[2]
    valid_accounts_file_path = sys.argv[-1]

    # Initialize an empty list to hold future transactions as dict objs
    transactions = []

    # Open merged transaction summary file
    with open(merged_transaction_summary_file_path, 'r') as merged_transaction_summary_file:
        lines = merged_transaction_summary_file.readlines()
        # Create dict objs for each transaction using the information from
        # each transaction line
        for line in lines:
            split_line = line.split()
            transaction = {}
            transaction["code"] = split_line[0]
            transaction["to"] = split_line[1]
            transaction["amount"] = split_line[2]
            transaction["from"] = split_line[3]
            transaction["name"] = split_line[4]
            transactions.append(transaction)

    # Create a dict holding all valid accounts during this back office session
    accounts = {}
    with open(master_accounts_file_path, 'r') as master_accounts_file:
        lines = master_accounts_file.readlines()
        for line in lines:
            split_line = line.split()
            # Ensure the master accoounts file has three
            # space-separated arguments
            if len(split_line) == 3:
                accounts[split_line[0]] = {
                    "balance": split_line[1],
                    "name": split_line[2]
                }

    # Update master accounts file
    with open(master_accounts_file_path, 'w+') as master_accounts_file:
        for transaction in transactions:
            if transaction["code"] == "DEP":
                str_balance = accounts[transaction["to"]]["balance"]
                balance = int(str_balance) + int(transaction["amount"])
                accounts[transaction["to"]]["balance"] = str(balance)
            elif transaction["code"] == "WDR":
                str_balance = accounts[transaction["from"]]["balance"]
                balance = int(str_balance) - int(transaction["amount"])
                if balance < 0:
                    print("ERROR: Withdraw would make account balance negative.")
                else:
                    accounts[transaction["from"]]["balance"] = str(balance)
            elif transaction["code"] == "XFR":
                str_balance = accounts[transaction["from"]]["balance"]
                balance = int(str_balance) - int(transaction["amount"])
                if balance < 0:
                    print("ERROR: Withdraw would make account balance negative.")
                else:
                    accounts[transaction["from"]]["balance"] = str(balance)
                    balance = int(accounts[transaction["to"]]["balance"]) + int(transaction["amount"])
                    accounts[transaction["to"]]["balance"] = balance
            elif transaction["code"] == "DEL":
                str_balance = accounts[transaction["to"]]["balance"]
                balance = int(str_balance) - int(transaction["amount"])
                if transaction["name"] != accounts[transaction["to"]]["name"]:
                    print("ERROR: {} to delete does not match master name.".format(transaction["name"]))
                elif balance != 0:
                    print("ERROR: Balance must be zero to delete account {}.".format(transaction["to"]))
                else:
                    del accounts[transaction["to"]]
            elif transaction["code"] == "NEW":
                if transaction["to"] in accounts:
                    print("ERROR: An account with the number {} has already been created.".format(transaction["to"]))
                else:
                    accounts[transaction["to"]] = {
                        "balance": "000",
                        "name": transaction["name"]
                    }
            else:
                print("ERROR: Invalid transaction code {}.".format(transaction["code"]))

        sorted_accounts = sorted(accounts.keys(), reverse=True)

        # Update the valid accounts file
        with open(valid_accounts_file_path, 'w+') as valid_accounts_file:
            for account in sorted_accounts:
                details = accounts[account]
                valid_accounts_file.write("{}\n".format(account))
                master_accounts_file.write("{} {} {}\n".format(account, details["balance"], details["name"]))
        # Add special account number 0000000 to end of valid accounts file
        with open(valid_accounts_file_path, 'a+') as valid_accounts_file:
            valid_accounts_file.write("{}\n".format("0000000"))

if __name__ == "__main__":
    main()
