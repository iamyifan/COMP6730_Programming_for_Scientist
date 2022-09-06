# coding: utf-8
## COMP1730/6730 S2 2022 - Homework 4
# Submission is due 09:00am, Monday the 19th of September, 2022.

## YOUR ANU ID: u7351505
## YOUR NAME: Yifan Luo

## You should implement one function stock_trade; you may define
## more functions if this will help you to achieve the functional
## correctness, and to improve the code quality of you program

import math

def stock_trade(stock_price, capital, p):
    '''
    A simple trading strategy for buying and selling shares.
    Given the starting cash and the prudence coefficient, the stock trader program will
    use a fixed fraction (1-p) of available capital to buy stocks if the price increases.
    Otherwise, sell a fraction (1-p) of shares owned. The program will return the profit/loss
    according to its available cash and shares at the final stage,
    i.e. (final cash + final share price) - starting cash.

    Parameters:
        stock_price (sequence of numbers): stock price at each stage, a sequence of positive numbers
        capital (float): starting cash used to buy shares, a positive number
        p (float): prudence coefficient, range [0, 1]

    Returns:
        profit (float): gain or loss in the value of the entire assets
    '''

    assert type(stock_price) in [list, tuple], "the stock price has to be a sequence of numbers"
    for sp in stock_price:
        if type(sp) not in [int, float]:
            print("stock price {} has to be a number".format(sp))
            raise TypeError
        if sp <= 0:
            print("stock price {} is not positive".format(sp))
            raise ValueError
    assert type(capital) == float or type(capital) == int, "the capital has to be a number"
    assert capital > 0, "the capital has to be positive"
    assert type(p) == float or type(p) == int, "the prudence coefficient has to be a number"
    assert 0 <= p <= 1, "the prudence coefficient has range [0, 1]"

    curr_capital = capital  # used to represent the current capital at each stage
    last_price = math.inf   # used to represent the share price of last time
    curr_shares = 0         # used to calculate the current owned shares at each stage
    for i in range(len(stock_price)):
        if stock_price[i] > last_price:    # if the price increases, sell stocks
            # the maximum current owned shares can be sold
            curr_shares_sell = (curr_shares * (1 - p)) // 1
            # update the current capital after this selling
            curr_capital += curr_shares_sell * stock_price[i]
            # update the current total number of shares
            curr_shares -= curr_shares_sell
        elif stock_price[i] < last_price:  # if the price decreases, buy stocks
            curr_capital_available = round(curr_capital * (1 - p))
            # buy stocks if the current available capital is sufficient,
            # otherwise, only record the current stock price as the last stock price
            if curr_capital_available >= stock_price[i]:
                # calculate the maximum number of shares with the total cost not exceeding that fraction
                curr_shares_buy = curr_capital_available // stock_price[i]
                # update the current capital after this buying
                curr_capital -= curr_shares_buy * stock_price[i]
                # update the current total number of shares
                curr_shares += curr_shares_buy
        else:  # if the price doesn't change, jump to the next stage
            continue
        last_price = stock_price[i]

    # if the last price is a math.nan, it means the program never bought any stocks,
    # and the profit will also be a math.nan. in that case, return a float 0.0
    profit = (curr_capital + curr_shares * last_price) - capital

    return float(profit) if not math.isnan(profit) else float(0)
    

def test_stock_trade():
    ''' some typical trading situations but by no means exhaustive
    '''
    assert math.isclose( stock_trade([1,1,1,1,1], 100, 0.5), 0.0 ) 
    assert math.isclose( stock_trade([100, 50, 50], 10, 0.01), 0.0 ) 
    assert math.isclose( stock_trade([50, 100, 50], 10, 0.01), 0.0 ) 
    assert math.isclose( stock_trade([1,2,3,4,5], 2, 0.5), 5-1 )
    assert math.isclose( stock_trade(tuple(), 100, 0.5), 0.0 )
    assert math.isclose( stock_trade([1, 10, 2.0, 5.0], 50, 0.5), 268.0 )
    assert math.isclose( stock_trade([1, 10, 2.0, 2.0, 5.0, 5], 50, 0.5), 268.0 )


def test_stock_trade_more():
    ''' some typical trading situations but by no means exhaustive
    '''
    assert math.isclose( stock_trade([1, 100, 10, 10], 10, 0.9), 10-1 )
    assert math.isclose( stock_trade([], 100, 0.5), 0.0 )
    assert math.isclose( stock_trade(tuple(), 100, 0.5), 0.0 )
    print('all tests passed')

