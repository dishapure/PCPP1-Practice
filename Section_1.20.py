import tkinter as tk
from tkinter import messagebox


class AirportSecurityCheck:
    restricted_items = ["knife", "gun", "liquid over 100ml", "explosives"]

    def __init__(self, passenger_name, luggage_items):
        if not self.is_valid_passenger(passenger_name):
            raise ValueError("Invalid passenger name.")
        self.passenger_name = passenger_name
        self.luggage_items = luggage_items

    def scan_passenger(self):
        print(f"\n🔍 Scanning luggage of {self.passenger_name}...")
        restricted_found = [item for item in self.luggage_items if
                            item.lower() in AirportSecurityCheck.restricted_items]

        if restricted_found:
            print("🚨 Restricted items found:", restricted_found)
            self.alert()
        else:
            print("🟢 No restricted items found.")

    def alert(self):
        print("⚠️ ALERT: Security team has been notified!")

        # Create a simple popup window
        root = tk.Tk()
        root.withdraw()  # Hides the main tkinter window
        messagebox.showwarning("Security Alert", f"Restricted items found in {self.passenger_name}'s luggage!")
        root.destroy()  # Close tkinter instance after showing the message

    @classmethod
    def update_restricted_items(cls, new_list):
        cls.restricted_items = new_list
        print("Restricted items list updated.")

    @staticmethod
    def is_valid_passenger(name):
        return isinstance(name, str) and name.replace(" ", "").isalpha()


# Example
p1 = AirportSecurityCheck("Babar khan sahid", ["knife", "book"])
p1.scan_passenger()
p2 = AirportSecurityCheck("Hussain Sheikh", ["gun", "bomb"])
p2.scan_passenger()
