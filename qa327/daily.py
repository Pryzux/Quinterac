import subprocess
import os

# Set Python command depending on OS
if os.name == "nt":
    python_cmd = "python"
else:
    python_cmd = "python3"

# Create 3 TSFs
for i in range(1, 4):
    subprocess.run([python_cmd, "app.py",
        "daily_transactions/valid_accounts_list_file.txt",
        "daily_transactions/transaction_summary_file_{}.txt".format(i)])
# Merge TSFs
subprocess.run([python_cmd, "merger/mergeMTSF.py",
    "daily_transactions/transaction_summary_file_1.txt",
    "daily_transactions/transaction_summary_file_2.txt",
    "daily_transactions/transaction_summary_file_3.txt"])
# Run back office with merged TSF
subprocess.run([python_cmd, "backoffice.py",
    "daily_transactions/master_accounts_file.txt",
    "daily_transactions/merged_tsf.txt",
    "daily_transactions/valid_accounts_list_file.txt"])
