# Import the pandas library.
import pandas as pd

# Define the calculate_commission function with default values for the variables.
def calculate_commission(ppw=None, total_sales=0, redline=0, dealer_fee=0, adders=0, max_ppw=0, term=0, apr=0, cash_price=0, financed_amount=0, system_size=0):
    # Define the commission rate for sales below the redline.
    below_redline_rate = 0.1

    # Define the commission rate for sales at or above the redline.
    above_redline_rate = 0.15

    # Calculate the total number of watts sold. If the PPW value is not
    # provided, divide the total sales by the PPW value to calculate the
    # total number of watts. Otherwise, divide the total sales by the
    # PPW value to calculate the total sales in dollars, and then
    # divide the total sales in dollars by the PPW value to calculate
    # the total number of watts.
    if ppw is None:
        total_watts = total_sales / ppw
    else:
        total_sales_in_dollars = total_sales / ppw
        total_watts = total_sales_in_dollars / ppw

    # Calculate the adjusted PPW value by adding the adders to the
    # original PPW value.
    adjusted_ppw = ppw + adders

    # Check if the adjusted PPW value is greater than the maximum allowed
    # PPW value. If it is, set the total number of watts to zero and
    # the commission rate to zero.
    if adjusted_ppw > max_ppw:
        total_watts = 0
        rate = 0
    else:
        # Calculate the commission rate based on whether the total number
        # of watts is below or above the redline.
        if total_watts < redline:
            rate = below
