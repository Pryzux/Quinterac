# Quinterac
An extremely thorough ATM simulator created to demonstrate technical ability and quality assurance measures when creating safety critical systems in an agile enviornment. Contains source code and testing code; as well as comprehensive documentation for: the requirements of the system, test cases and test case design, intial/final design, deployment, test results, and more
  
## Description

This program is a year long technology project designed to be a fully functioning series of ATM subprocesses, that all work in parrallel sending and recieving information from a central bank. The purpose of this project was to learn and demonstrate how to develop rigourous & error-free code in complex systems. Since this is a complicated project containing many parts, I will provide a broad overview of the components here and if you would like to know more I have attached all of the supporting documentation to the project repository.



**Overview**

This project contains a two systems, 1) **The ATM processes** 2) **The bank or 'back office'**

Each ATM has access to the Master Accounts File, which helps determine which accounts are allowed to login to a machine, how much money is in each account, etc. When using an ATM, Each subprocess records a history of its own transactions in a transaction summary file, that is continually merged to the 'back office' or main bank. This information is then re-updated and reflected in the Master Accounts File for other atms to use. When a file is being merged, thread locks used to avoid a race condition or innacurate data retrieval between ATMs.

**The ATM Processes**

Each ATM has similar functionality and states to a regular ATM: Withdrawels, deposits, account balance, creating and deleting accounts, etc. One can simulate an ATM through 'app.py', and this program can be loaded multiple times for as many as you would like to simulate.

The core states/features:

```
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

```
Sample Snippet of the codebase:

```
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
                mode_choice = input("Please choose either '{}' or '{}' mode:\n".format(MACHINE, AGENT))...
```
_View the full program at "app.py"_

**The Bank**

The bank is a program that facilitates the coordination of ATMs used in parralell and handles storing and updating information collected by the ATMs. This file can be reviewed in 'back_office.py'.

Some sample functions that the bank program contains:

```
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
```

```
# Update the valid accounts file
        with open(valid_accounts_file_path, 'w+') as valid_accounts_file:
            for account in sorted_accounts:
                details = accounts[account]
                valid_accounts_file.write("{}\n".format(account))
                master_accounts_file.write("{} {} {}\n".format(account, details["balance"], details["name"]))
        # Add special account number 0000000 to end of valid accounts file
        with open(valid_accounts_file_path, 'a+') as valid_accounts_file:
            valid_accounts_file.write("{}\n".format("0000000"))
```

## Data Storage

All information used by the atm subprocesses and centralized bank are stored and sent using text files. These are the differen't types of data files passed through the systems:

1) Master Accounts File
2) Daily Transactions List
3) Transaction Summary File
4) Valid Accounts List
5) Merged Transaction Summary File

_If you would like to know more about the details of each file type, please visit the requirements documentation provided in the repository._

## Security && Test Cases

Assuming this is to be a safety critical system, multiple types of testing were used. Primarily White & Black box testing, and The methodology for how each test algorithm and case was derived, as well as the full list of test cases, is in the supporting documentation 'A4_Report', and 'A5_Report'. PyTest was used to automate and provide a pass/fail for each scenario.  

Here are some examples of various rigiourous/algorithmic tests that were conducted on the system:

**1) some of the basic test cases created for the login interface**

![image](https://github.com/Pryzux/Quinterac/assets/33528419/2283dbeb-495e-40cd-96c4-ad33506c4b1b)

**2) Analysis of Basic Block Coverage Testing For Account Creation**

![image](https://github.com/Pryzux/Quinterac/assets/33528419/8421a011-7bae-4851-8d6c-7c4cb5cf53df)
![image](https://github.com/Pryzux/Quinterac/assets/33528419/39ba3aef-71e1-465a-bb5f-f95b8bebfb78)
![image](https://github.com/Pryzux/Quinterac/assets/33528419/6b942309-9b7f-48f2-a555-995568ee4edd)

_all test scenarios and methods provided in the repository under A4_Report, and A5_Report._





