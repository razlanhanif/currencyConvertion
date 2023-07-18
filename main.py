import tkinter as tk
from tkinter import ttk
import requests

# API endpoint for currency conversion
API_URL = "https://api.exchangerate-api.com/v4/latest/"

def convert_currency():
    try:
        amount = float(amount_entry.get())
        base_currency = base_currency_combobox.get()
        target_currency = target_currency_combobox.get()

        response = requests.get(f"{API_URL}{base_currency}")
        data = response.json()

        target_rate = data["rates"][target_currency]
        result = amount * target_rate
        result_label.config(text=f"{amount} {base_currency} = {result:.2f} {target_currency}")

    except Exception as e:
        result_label.config(text="Error: Invalid Input")

# Create the main application window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x300")
root.resizable(False,False)

# Amount Entry
amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# Base Currency Dropdown
base_currency_label = tk.Label(root, text="From:")
base_currency_label.pack(pady=5)
base_currency_combobox = ttk.Combobox(root, values=["MYR", "EUR", "GBP", "JPY", "TRY"])
base_currency_combobox.pack(pady=5)
base_currency_combobox.set("MYR")

# Target Currency Dropdown
target_currency_label = tk.Label(root, text="To:")
target_currency_label.pack(pady=5)
target_currency_combobox = ttk.Combobox(root, values=["MYR", "EUR", "GBP", "JPY", "TRY"])
target_currency_combobox.pack(pady=5)
target_currency_combobox.set("EUR")

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack()

# Start the main event loop
root.mainloop()