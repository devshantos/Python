'''# Import necessary modules
from tkinter import *
from tkinter import messagebox

# Define the login function
def login():
    # Get the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "admin" and password == "admin123":
        messagebox.showinfo("Login Successful", "Welcome, " + username)
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

# Create the main window
root = Tk()
root.title("Login Form")

# Create the username and password labels and entries
username_label = Label(root, text="Username")
username_label.grid(row=0, column=0, sticky="w")
username_entry = Entry(root)
username_entry.grid(row=0, column=1)

password_label = Label(root, text="Password")
password_label.grid(row=1, column=0, sticky="w")
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Create the login button
login_button = Button(root, text="Login", command=login)
login_button.grid(row=2, column=1, sticky="e")

# Start the main event loop
root.mainloop()
'''

# Import necessary modules
import pandas as pd
import yfinance as yf

# Define the function to get live stock prices
def get_live_prices(tickers):
    # Create an empty DataFrame to store the prices
    live_prices = pd.DataFrame()

    # Loop through the ticker symbols and get the current price
    for ticker in tickers:
        # Get the stock data
        stock = yf.Ticker(ticker)

        # Get the current price
        price = stock.info["regularMarketPrice"]

        # Add the current price to the DataFrame
        live_prices = live_prices.append(pd.DataFrame({"Ticker": ticker, "Price": price}, index=[0]))

    return live_prices

# Define the ticker symbols of the stocks you want to track
tickers = ["META","TSLA","PEP","GOOGL","AMGN", "NASDAQ"]

# Get the live stock prices
live_prices = get_live_prices(tickers)

# Print the live prices
print(live_prices)
