# Customer Banking Application

## Overview

The Customer Banking Application is a simple Python project that simulates the creation and management of savings and CD (Certificate of Deposit) accounts. Users can input account details, and the application will calculate the interest earned and update the account balances accordingly.

## Files

The project consists of the following files:

1. **Accounts.py**: Contains the `Account` class, which provides methods to set the balance, set the interest, deposit funds, and retrieve balance and interest earned.
2. **savings_account.py**: Contains the function `create_savings_account`, which creates a savings account instance, calculates interest earned, updates the balance, and returns the updated balance and interest earned.
3. **cd_account.py**: Contains the function `create_cd_account`, which creates a CD account instance, calculates interest earned, updates the balance, and returns the updated balance and interest earned.
4. **customer_banking.py**: The main script that prompts the user for account details, uses the functions from `savings_account.py` and `cd_account.py` to perform calculations, and displays the results.

## How to Use

1. **Clone the repository**:
    ```
    git clone https://github.com/timwillard24/customer_banking.git
    cd customer_banking
    ```

2. **Run the application**:
    ```
    python customer_banking.py
    ```

3. **Follow the prompts**:
    - Enter the initial balance, APR (Annual Percentage Rate), and the number of months for the savings account.
    - The application will display the interest earned and the updated savings account balance.
    - Enter the initial balance, APR, and the number of months for the CD account.
    - The application will display the interest earned and the updated CD account balance.

## Example

Here is an example of the application's output:

Enter the initial balance for the savings account: 1000
Enter the annual percentage rate (APR) for the savings account: 5
Enter the number of months for the savings account: 12
Savings Account: Interest Earned: $50.00, Updated Balance: $1050.00

Enter the initial balance for the CD account: 2000
Enter the annual percentage rate (APR) for the CD account: 3
Enter the number of months for the CD account: 12
CD Account: Interest Earned: $60.00, Updated Balance: $2060.00

