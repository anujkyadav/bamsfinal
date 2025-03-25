# test setup for API
import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://127.0.0.1:5000"  # Change this if the API is hosted elsewhere

def update_temperature():
    """Send temperature data to the Flask API."""
    try:
        temp = float(entry_temp.get())
        response = requests.post(f"{API_URL}/update_temperature", json={"temperature": temp})
        if response.status_code == 200:
            data = response.json()
            label_status.config(text=f"AC Status: {data['ac_status']}")
        else:
            messagebox.showerror("Error", "Failed to update temperature")
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid number for temperature")
    except requests.exceptions.RequestException:
        messagebox.showerror("Connection Error", "Failed to connect to the server")

def get_ac_status():
    """Retrieve AC status from the API."""
    try:
        response = requests.get(f"{API_URL}/get_ac_command")
        if response.status_code == 200:
            data = response.json()
            label_status.config(text=f"AC Status: {data['ac_status']}")
        else:
            messagebox.showerror("Error", "Failed to get AC status")
    except requests.exceptions.RequestException:
        messagebox.showerror("Connection Error", "Failed to connect to the server")

# GUI setup
root = tk.Tk()
root.title("AC Control Test")

tk.Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=10)
entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

btn_update = tk.Button(root, text="Update Temperature", command=update_temperature)
btn_update.grid(row=1, column=0, columnspan=2, pady=10)

btn_get_status = tk.Button(root, text="Get AC Status", command=get_ac_status)
btn_get_status.grid(row=2, column=0, columnspan=2, pady=10)

label_status = tk.Label(root, text="AC Status: Unknown", font=("Arial", 12))
label_status.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
