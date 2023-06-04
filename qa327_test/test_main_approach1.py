import tempfile
from importlib import reload
import os
import io
import sys
import qa327.app as app

path = os.path.dirname(os.path.abspath(__file__))
transactions_path = os.path.join("test_files", "transactions")

def test_login_r1_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R1", "T1")
    )

def test_login_r1_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R1", "T2")
    )

def test_login_r1_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R1", "T3")
    )

def test_login_r1_t4(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R1", "T4")
    )

def test_login_r1_t5(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R1", "T5")
    )

def test_login_r1_t6(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R1", "T6")
    )

def test_login_r2_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R2", "T1")
    )

def test_login_r3_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R3", "T1")
    )

def test_login_r3_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R3", "T2")
    )

def test_login_r3_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R3", "T3")
    )

def test_login_r4_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R4", "T1")
    )

def test_login_r5_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R5", "T1")
    )

def test_login_r6_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R6", "T1")
    )

def test_login_r6_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R6", "T2")
    )

def test_login_r6_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R6", "T3")
    )

def test_login_r6_t4(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R6", "T4")
    )

def test_login_r7_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R7", "T1")
    )

def test_login_r7_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R7", "T2")
    )

def test_login_r7_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "login", "R7", "T3")
    )

def test_logout_r1_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "logout", "R1", "T1")
    )

def test_logout_r2_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "logout", "R2", "T1")
    )

def test_logout_r2_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "logout", "R2", "T2")
    )

def test_logout_r2_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "logout", "R2", "T3")
    )

def test_logout_r2_t4(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "logout", "R2", "T4")
    )

def test_logout_r2_t5(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "logout", "R2", "T5")
    )

def test_logout_r2_t6(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "logout", "R2", "T6")
    )

def test_logout_r3_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "logout", "R3", "T1")
    )

def test_createacct_r1_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R1", "T1")
    )

def test_createacct_r1_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R1", "T2")
    )

def test_createacct_r2_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R2", "T1")
    )

def test_createacct_r2_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R2", "T2")
    )

def test_createacct_r2_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R2", "T3")
    )

def test_createacct_r3_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R3", "T1")
    )

def test_createacct_r3_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R3", "T2")
    )

def test_createacct_r4_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R4", "T1")
    )

def test_createacct_r4_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R4", "T2")
    )

def test_createacct_r4_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R4", "T3")
    )

def test_createacct_r4_t4(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "createacct", "R4", "T4")
    )

def test_deleteacct_r1_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R1", "T1")
    )

def test_deleteacct_r1_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R1", "T2")
    )

def test_deleteacct_r2_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R2", "T1")
    )

def test_deleteacct_r3_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R3", "T1")
    )

def test_deleteacct_r4_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R4", "T1")
    )

def test_deleteacct_r5_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R5", "T1")
    )

def test_deleteacct_r5_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R5", "T2")
    )

def test_deleteacct_r6_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R6", "T1")
    )

def test_deleteacct_r6_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R6", "T2")
    )

def test_deleteacct_r6_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R6", "T3")
    )

def test_deleteacct_r6_t4(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deleteacct", "R6", "T4")
    )

def test_deposit_r1_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deposit", "R1", "T1")
    )

def test_deposit_r1_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deposit", "R1", "T2")
    )

def test_deposit_r1_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deposit", "R1", "T3")
    )

def test_deposit_r1_t4(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deposit", "R1", "T4")
    )

def test_deposit_r2_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deposit", "R2", "T1")
    )

def test_deposit_r2_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deposit", "R2", "T2")
    )

def test_deposit_r2_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deposit", "R2", "T3")
    )

def test_deposit_r2_t4(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deposit", "R2", "T4")
    )

def test_deposit_r3_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "deposit", "R3", "T1")
    )

def test_transfer_r1_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R1", "T1")
    )

def test_transfer_r1_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R1", "T2")
    )

def test_transfer_r1_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R1", "T3")
    )

def test_transfer_r1_t4(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R1", "T4")
    )

def test_transfer_r1_t5(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R1", "T5")
    )

def test_transfer_r1_t6(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R1", "T6")
    )

def test_transfer_r2_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R2", "T1")
    )

def test_transfer_r2_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R2", "T2")
    )

def test_transfer_r2_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R2", "T3")
    )

def test_transfer_r2_t4(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R2", "T4")
    )

def test_transfer_r3_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transfer", "R3", "T1")
    )

def test_withdraw_r1_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R1", "T1")
    )

def test_withdraw_r1_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R1", "T2")
    )

def test_withdraw_r2_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R2", "T1")
    )

def test_withdraw_r2_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R2", "T2")
    )

def test_withdraw_r3_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R3", "T1")
    )

def test_withdraw_r3_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R3", "T2")
    )

def test_withdraw_r4_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R4", "T1")
    )

def test_withdraw_r4_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R4", "T2")
    )

def test_withdraw_r4_t3(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R4", "T3")
    )

def test_withdraw_r4_t4(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R4", "T4")
    )

def test_withdraw_r5_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R5", "T1")
    )

def test_withdraw_r5_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R5", "T2")
    )

def test_withdraw_r6_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R6", "T1")
    )

def test_withdraw_r6_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "withdraw", "R6", "T2")
    )

def test_transaction_summary_file_r1_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "transactionsummaryfile", "R1", "T1")
    )

def test_valid_accounts_file_r1_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "validaccountslistfile", "R1", "T1")
    )

def test_valid_accounts_file_r1_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "validaccountslistfile", "R1", "T2")
    )

def test_valid_accounts_file_r2_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "validaccountslistfile", "R2", "T1")
    )

def test_valid_accounts_file_r2_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "validaccountslistfile", "R2", "T2")
    )

def test_valid_accounts_file_r3_t1(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "validaccountslistfile", "R3", "T1")
    )

def test_valid_accounts_file_r3_t2(capsys):
    helper(
        capsys=capsys,
        test_id=os.path.join(transactions_path, "validaccountslistfile", "R3", "T2")
    )

def helper(capsys, test_id):

    # cleanup package
    reload(app)

    # locate test case folder:
    case_folder = os.path.join(path, test_id)

    # read terminal input:
    with open(
        os.path.join(
            case_folder, 'input.txt')) as rf:
        terminal_input = rf.read().splitlines()

    # read expected tail portion of the terminal output:
    with open(
        os.path.join(
            case_folder, 'output_expected.txt')) as rf:
        terminal_output_tail = rf.read().splitlines()

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file

    # prepare program parameters
    sys.argv = [
        'app.py',
        os.path.join(case_folder, 'accounts.txt'),
        transaction_summary_file]

    # set terminal input
    sys.stdin = io.StringIO(
        "\n".join(terminal_input))

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    print(out)

    # split terminal output in lines
    out_lines = out.splitlines()

    # compare terminal outputs at the end.`
    for i in range(1, len(terminal_output_tail) + 1):
        index = i * -1
        assert terminal_output_tail[index] == out_lines[index]

    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
        content = of.read()
        with open(os.path.join(case_folder, 'transaction_summary_file.txt'), 'r') as exp_file_of:
            expected_content = exp_file_of.read()
            assert content == expected_content

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
