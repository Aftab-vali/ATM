Python ATM Application
This Python ATM application simulates a basic Automated Teller Machine (ATM) system, allowing users to perform common banking operations such as checking their balance, withdrawing money, and depositing money.

Features:
Balance Check: Users can check their account balance.
Withdrawal: Users can withdraw money from their account.
Deposit: Users can deposit money into their account.
Data Persistence: User account balances are stored in a text file (test.txt) and are loaded upon initializing the ATM object. Any updates to account balances are also written back to the file.
How to Use:
Clone the Repository:
bash
Copy code
git clone <repository_url>
Navigate to the Directory:
bash
Copy code
cd Python-ATM-Application
Run the Script:
Copy code
python atm.py
Follow On-screen Instructions:
Enter the choice corresponding to the action you want to perform.
If you choose to withdraw or deposit, you will be prompted to enter your username and the amount.
Upon balance check, withdrawal, or deposit, the program will display the updated account balance.
Requirements:
Python 3.x
File Structure:
atm.py: Contains the main Python script implementing the ATM functionality.
test.txt: Text file where user account balances are stored.
Contributions:
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

License:
This project is licensed under the MIT License.
