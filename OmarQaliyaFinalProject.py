import tkinter as tk
from tkinter import messagebox

class bakeryOrder:
    def __init__(self, master):
        self.master = master
        master.title("Sweet Cakes Order Form")

        # Create input labels and entry boxes
        self.lemon_meringue_lbl = tk.Label(master, text="lemon meringue pie ($10.99)")
        self.lemon_meringue_ent = tk.Entry(master)
        self.strawberry_shortcake_lbl = tk.Label(master, text="Strawberry Shortcake ($15.99)")
        self.strawberry_shortcake_ent = tk.Entry(master)
        self.chocolatechip_cookies_lbl = tk.Label(master, text="Chocolate Chip Cookies ($5.99)")
        self.chocolatechip_cookies_ent = tk.Entry(master)
        self.frosted_cupcakes_lbl = tk.Label(master, text="Frosted Cupcakes ($6.99)")
        self.frosted_cupcakes_ent = tk.Entry(master)
        self.chocolate_croissants_lbl = tk.Label(master, text="Chocolate Croissants ($7.99)")
        self.chocolate_croissants_ent = tk.Entry(master)
        self.apple_fritters_lbl = tk.Label(master, text="Apple Fritters ($4.99)")
        self.apple_fritters_ent = tk.Entry(master)

        # Create order button
        self.order_btn = tk.Button(master, text="Place Order", command=self.calculate_total)

        # Create exit button
        self.exit_btn = tk.Button(master, text="Exit", command=master.quit)
        
        # Pack labels, entry boxes and buttons to the form
        self.lemon_meringue_lbl.pack()
        self.lemon_meringue_ent.pack()
        self.strawberry_shortcake_lbl.pack()
        self.strawberry_shortcake_ent.pack()
        self.chocolatechip_cookies_lbl.pack()
        self.chocolatechip_cookies_ent.pack()
        self.frosted_cupcakes_lbl.pack()
        self.frosted_cupcakes_ent.pack()
        self.chocolate_croissants_lbl.pack()
        self.chocolate_croissants_ent.pack()
        self.apple_fritters_lbl.pack()
        self.apple_fritters_ent.pack()
        self.order_btn.pack()
        self.exit_btn.pack()

    def calculate_total(self):
        try:
            # Get input values and calculate total price
            lemon_meringue = int(self.lemon_meringue_ent.get())
            strawberry_shortcake = int(self.strawberry_shortcake_ent.get())
            chocolatechip_cookies = int(self.chocolatechip_cookies_ent.get())
            frosted_cupcakes = int(self.frosted_cupcakes_ent.get())
            chocolate_croissants = int(self.chocolate_croissants_ent.get())
            apple_fritters = int(self.apple_fritters_ent.get())

            total_price = (lemon_meringue + strawberry_shortcake + chocolatechip_cookies) * 8.99 + \
                          (frosted_cupcakes + chocolate_croissants + apple_fritters) * 1.99
            total_price *= 1.07 # Add 7% sales tax

            # Display total price in a message box
            messagebox.showinfo("Total Price", f"Your total bill is ${total_price:.2f}")
        except ValueError:
            # Display error message if input is invalid
            messagebox.showerror("Invalid Input", "Please enter a valid integer for each item.")

# Create main window
root = tk.Tk()

# Create bakery order form
order_form = bakeryOrder(root)

# Run main loop
root.mainloop()

#Validation testing
import unittest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch

class TestBakeryOrder(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.order_form = bakeryOrder(self.root)
        self.app = self.order_form.master

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.messagebox.showinfo')
    def test_calculate_total(self, mock_showinfo):
        # Mock input values
        self.order_form.lemon_meringue_ent.insert(0, "2")
        self.order_form.strawberry_shortcake_ent.insert(0, "3")
        self.order_form.chocolatechip_cookies_ent.insert(0, "4")
        self.order_form.frosted_cupcakes_ent.insert(0, "1")
        self.order_form.chocolate_croissants_ent.insert(0, "2")
        self.order_form.apple_fritters_ent.insert(0, "1")

        # Call calculate_total method
        self.order_form.calculate_total()

        # Assert that the mock showinfo method was called with the correct arguments
        mock_showinfo.assert_called_with("Total Price", "Your total bill is $47.34")

    @patch('tkinter.messagebox.showerror')
    def test_invalid_input(self, mock_showerror):
        # Mock invalid input values (non-integer)
        self.order_form.lemon_meringue_ent.insert(0, "invalid")
        self.order_form.strawberry_shortcake_ent.insert(0, "3")
        self.order_form.chocolatechip_cookies_ent.insert(0, "4")
        self.order_form.frosted_cupcakes_ent.insert(0, "1")
        self.order_form.chocolate_croissants_ent.insert(0, "2")
        self.order_form.apple_fritters_ent.insert(0, "1")

        # Call calculate_total method
        self.order_form.calculate_total()

        # Assert that the mock showerror method was called with the correct arguments
        mock_showerror.assert_called_with("Invalid Input", "Please enter a valid integer for each item.")

if __name__ == '__main__':
    unittest.main()        
