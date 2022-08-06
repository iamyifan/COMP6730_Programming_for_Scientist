"""
Our very own mortgage calculator
"""

import matplotlib.pyplot as plt


def calculate_repayments(principle, years, rate_in_percent):
    """
    Calculate the monthly loan repayments
    principle : int or float - amount in dollars
    years : int - loan duration in years
    rate_in_percent : float - interest rate. 5.5% interest would be 5.5

    Returns float - the monthly repayments on the loan
    """

    months = years * 12
    rate_yearly = rate_in_percent / 100 
    rate = rate_yearly / 12
    
    amount = principle * (rate * (1 + rate) ** months)/((1 + rate) ** months - 1)

    return amount


principle = 750000  # Amount in dollars
years = range(10, 26)

# Calculate and display the output

mc = [calculate_repayments(principle, y, 5.5) for y in years]
plt.plot(years, mc, 'g-')
mc = [calculate_repayments(principle, y, 6.5) for y in years]
plt.plot(years, mc, 'b-')
mc = [calculate_repayments(principle, y, 7.5) for y in years]
plt.plot(years, mc, 'r-')
plt.title("Repayments on loan of ${}".format(principle))
plt.xlabel("Loan term (years)")
plt.ylabel("Monthly repayments ($)")
plt.show()

