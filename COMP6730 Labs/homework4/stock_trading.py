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
    ''' A simple trading strategy for buying and selling shares.
    Given the starting cash and the prudence coefficient, the program will use a fixed fraction (1-p) of
    available capital to buy stocks if the price increases; Otherwise, the program will sell a fraction (1-p)
    of shares owned. The profit will be returned according to its available cash and shares at the end,
    i.e. profit = (available cash + number of shares * last stock price) - starting cash.

    Parameters:
        stock_price (list[int/float]/tuple(int/float)): stock price at each stage, a sequence of positive numbers
        capital (int/float): starting cash used to buy shares, a positive number
        p (int/float): prudence coefficient, range [0, 1]

    Returns:
        profit (float): gain or loss in the value of the entire assets
    '''

    assert type(stock_price) in [list, tuple], "stock price has to be iterable"
    for sp in stock_price:
        assert type(sp) in [int, float], "stock price {} has to be a number".format(sp)
        assert sp > 0, "stock price {} has to be positive".format(sp)
    assert type(capital) in [int, float], "capital has to be a number"
    assert capital > 0, "capital has to be positive"
    assert type(p) in [int, float], "prudence coefficient has to be a number"
    assert 0 <= p <= 1, "prudence coefficient has range [0, 1]"

    curr_capital = capital  # available capital at each stage, init with starting capital
    last_price = math.inf   # share price of last time, init with infinity for first-buy scenarios
    curr_shares = 0         # owned shares at each stage, init with no shares

    for i in range(len(stock_price)):
        if stock_price[i] > last_price:          # sell stocks if price increases
            n_shares_sell = (curr_shares * (1 - p)) // 1        # maximum shares can sell
            curr_capital += n_shares_sell * stock_price[i]      # update available capital after selling
            curr_shares -= n_shares_sell                        # update owned shares after selling
        elif stock_price[i] < last_price:        # buy stocks if price decreases
            n_capital_buy = round(curr_capital * (1 - p))       # maximum capital used to buy
            if n_capital_buy >= stock_price[i]:  # buy stocks if available capital is enough
                n_shares_buy = n_capital_buy // stock_price[i]  # maximum shares can buy
                curr_capital -= n_shares_buy * stock_price[i]   # update available capital after buying
                curr_shares += n_shares_buy                     # update owned shares after buying
        # if owned shares == 0, no shares hold, need to buy shares before any selling
        # (it happens in first-buy, or when some trades were done but no shares left)
        # keep last price math.inf, wait until price drops low enough
        # if owned shares > 0, trades happened, continually update last price
        # (when price doesn't change, updating won't hurt, since price is same)
        last_price = stock_price[i] if curr_shares > 0 else math.inf

    if curr_shares == 0:  # no shares hold, profit is capital's difference, whether trades happened or not
        profit = float(curr_capital - capital)
    else:                 # can't merge two equations, since 0 * math.inf == math.nan will have issues
        profit = float((curr_capital + curr_shares * last_price) - capital)

    return profit
    

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

