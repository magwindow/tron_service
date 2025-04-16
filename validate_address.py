from tronpy import Tron

client = Tron()
try:
    addr = client.get_account("TUjx6w55Nx9G4GjjRNEB4e7w5BUH3WmJTZ")
except ValueError as e:
    print("Invalid address:", e)
