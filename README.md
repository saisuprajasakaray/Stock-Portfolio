# Stock-Portfolio

Creating a detailed README file for your Stock Portfolio Tracker will help others understand how to use your program, what it does, and how to set it up. Below is a template you can use and customize according to your project's specifics.


**Overview**

The Stock Portfolio Tracker is a Python-based application that allows users to manage their stock investments. Users can add stocks, remove stocks, and view the performance of their portfolio, including real-time updates on stock prices.


**Features**

Add Stock: Add a stock to your portfolio by entering the ticker symbol, the number of shares, and the price paid per share.


Remove Stock: Remove a stock from your portfolio by specifying the ticker symbol.


View Portfolio: View a summary of your portfolio, including the ticker symbols, number of shares, price paid, and current market value.


Real-time Stock Data: Fetches real-time stock prices using the Alpha Vantage API.


**Prerequisites**

Before you begin, ensure you have met the following requirements:


Python 3.x installed on your system.

The following Python packages:

pandas

requests

You can install the required packages using pip:

pip install pandas requests

**Installation**

Clone the Repository: (or download the files)

git clone

https://github.com/yourusername/stock-portfolio-tracker.git


cd stock-portfolio-tracker

Install Dependencies:

Navigate to the project directory and install the necessary Python packages:


pip install pandas requests


**Set Up API Key:**


The application uses the Alpha Vantage API for fetching real-time stock data.


Obtain a free API key from Alpha Vantage.


Once you have the API key, add it to your Python script as follows:


self.api_key = "S7C8MGSVRMW0DKV7"

Run the Application:


After setting up the API key, you can run the application:


python stock_portfolio_tracker.py

**Usage**

Starting the Application:


Run the script using Python:


python stock_portfolio_tracker.py

**Main Menu:**


The main menu will prompt you with the following options:


Stock Portfolio Tracker


1. Add Stock
2. Remove Stock

3. View Portfolio

4. Exit

Adding a Stock:


Select 1 to add a stock.


Enter the stock ticker (e.g., AAPL for Apple).


Enter the number of shares and the price paid per share.


Removing a Stock:


Select 2 to remove a stock.


Enter the ticker symbol of the stock you wish to remove.


Viewing the Portfolio:


Select 3 to view your portfolio.


The portfolio will display each stock's ticker, number of shares, price paid, current price, and market value.

**Exiting the Application:**

Select 4 to exit the application.
Example
Here is an example of how the application might look when running:

Stock Portfolio Tracker

1. Add Stock

2. Remove Stock

3. View Portfolio

4. Exit


Enter your choice: 1

Enter stock ticker: AAPL

Enter number of shares: 10

Enter price paid per share: 150


Stock added successfully!


Stock Portfolio Tracker

1. Add Stock

2. Remove Stock

3. View Portfolio

4. Exit

Enter your choice: 3

Your Portfolio:
----------------
Ticker: AAPL

Shares: 10

Price Paid per Share: $150

Current Price per Share: $145.23

Market Value: $1452.30

**Error Handling**

Invalid Ticker Symbols: The application checks for valid ticker symbols. If the ticker symbol is not found, an error message will be displayed.

API Rate Limiting: Alpha Vantage has a limit on the number of API calls per minute. The application handles this by alerting the user if the limit is reached.
Known Issues

API Key Limitations: The free version of the Alpha Vantage API has rate limits that may affect the performance if multiple requests are made within a short period.

No Database Integration: The current version stores portfolio data in memory, which will be lost when the application is closed. Future versions may include database integration for persistent storage.

**Contributing**

Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make your changes and commit them (git commit -m 'Add some feature').

Push to the branch (git push origin feature-branch).

Create a pull request.
