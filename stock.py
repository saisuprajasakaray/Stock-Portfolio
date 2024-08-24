import pandas as pd
import requests

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = pd.DataFrame(columns=['Ticker', 'Shares', 'Price Paid', 'Current Price', 'Value', 'Gain/Loss'])

    def add_stock(self, ticker, shares, price_paid):
        current_price = self.get_current_price(ticker)
        if current_price is None:
            print(f"Failed to fetch current price for {ticker}. Stock not added.")
            return
        value = shares * current_price
        gain_loss = (current_price - price_paid) * shares
        new_stock = pd.DataFrame([[ticker, shares, price_paid, current_price, value, gain_loss]],
                                 columns=['Ticker', 'Shares', 'Price Paid', 'Current Price', 'Value', 'Gain/Loss'])
        self.portfolio = pd.concat([self.portfolio, new_stock], ignore_index=True)

    def remove_stock(self, ticker):
        self.portfolio = self.portfolio[self.portfolio['Ticker'] != ticker]

    def update_prices(self):
        for i, row in self.portfolio.iterrows():
            ticker = row['Ticker']
            current_price = self.get_current_price(ticker)
            if current_price is not None:
                self.portfolio.at[i, 'Current Price'] = current_price
                self.portfolio.at[i, 'Value'] = current_price * row['Shares']
                self.portfolio.at[i, 'Gain/Loss'] = (current_price - row['Price Paid']) * row['Shares']

    def get_current_price(self, ticker):
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()

        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            return float(data["Global Quote"]["05. price"])
        else:
            print(f"Error fetching data for {ticker}: {data.get('Note', 'No data available')}")
            return None

    def display_portfolio(self):
        self.update_prices()
        print(self.portfolio)

def main():
    api_key = "S7C8MGSVRMW0DKV7"  # Replace with your actual API key
    portfolio = StockPortfolio(api_key)

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            price_paid = float(input("Enter price paid per share: "))
            portfolio.add_stock(ticker, shares, price_paid)
        elif choice == '2':
            ticker = input("Enter stock ticker to remove: ").upper()
            portfolio.remove_stock(ticker)
        elif choice == '3':
            portfolio.display_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
