## Project Overview:

TriSquare is a finance application designed to provide users with comprehensive insights into stock data obtained from an API. The application's core functionality includes displaying stock details, visualizing sector-wise market capitalization, and analyzing fund movement between sectors.

## Installation:

1. Install git https://git-scm.com/downloads
2. Install Postgresql set username: Postgres, Password: Kenra123
3. Create Database named pulse.
4. Clone the repository to your local machine using `git clone https://github.com/kenrasoftorg/trisquare.git'
5. Open the cloned folder trisquare/src/pulse/scripts/pulseschema.sql
6. Run the table creation queries in postgresql under query tool or SQL editor and make sure tables were created
7. Open a terminal in vscode or cmd
8. Navigate to project directory trisquare
9. Type pip install -r requirements.txt
10. The above command installs all the requirements and denpendencies to run the project if faced errors for few packages continue to next step
11. run trisquare/src/main.py
12. If paced module not found or package not found error - use pip install {packagename} example: pip install numpy and rerun main
13. You will get the data in your database
14. Creating connection in DBeaver - set username: postgres, Password: Kenra123, Database: pulse, Hostname: 127.0.0.1, port: 5432
