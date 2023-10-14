# Documentation structure

## Introduction

Currently, finance professionals rely on manual data collection and analysis from various sources. There's a lack of a consolidated platform to assess sector-wise market capitalization and track fund movement across sectors.

TriSquare will address these challenges by offering a user-friendly interface to access real-time stock data, visualize sector-wise market capitalization, and provide insights into the flow of funds between sectors.

## Installation

1. Install git: [Git Downloads](https://git-scm.com/downloads)

2. Install Postgresql and set the following credentials:
   - Username: Postgres
   - Password: Kenra123

3. Create a Database named pulse.

4. Clone the repository to your local machine using the following command:

    git clone https://github.com/kenrasoftorg/trisquare.git


5. Open the cloned folder `trisquare/src/pulse/scripts/pulseschema.sql`.

6. Run the table creation queries in PostgreSQL under the query tool or SQL editor and make sure tables are created.

7. Open a terminal in VSCode or CMD.

8. Navigate to the project directory `trisquare`.

9. Type the following command to install all the requirements and dependencies:

    pip install -r requirements.txt 


10. If you face errors for a few packages, continue to the next step.

11. Run `trisquare/src/main.py`.

12. If you encounter a "module not found" or "package not found" error, use the following command to install the missing package. For example:
 ```
 pip install {packagename}
 ```
 And then rerun the `dataloader.py` script.

13. You will get the data in your database.

14. Creating a connection in DBeaver using the configurational details mentioned under 'Configuration' section.



## Configuration

Create a connection to the Data base using:
 - Set the following credentials:
   - Username: postgres
   - Password: Kenra123
   - Database: pulse
   - Hostname: 127.0.0.1
   - Port: 5432

Access the financial modelling API using:
 - Set the following credentials:
   - uri: https://financialmodelingprep.com/api/v3/
   - key: apikey=304459a7a227a31923b63192971bc245


## Contributing

Team members contributed to the Project:

 - Project owners
   - Anand 
   - Murali

 - Team members
   - Afreen
   - Anusha
   - Avinash
   - Charan
   - Mahendra
   - Manasa
   - Megha 
   - Om sai
   - Shobhana
   - Sirisha
   - Suneetha
   - Tejus
   - Vani
   - Vijaya
