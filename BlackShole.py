
#incl.Vega function and implied volatility estimates
#bsm_function.py
#
#Analytical Black_Scholes_Merton(BSM) Formula

def bsm_call_value(S_0, K, T, r, sigma):
    '''Valuation of European call option in BSM model.
    Analytical formula.

    Parameters
    ==========
    S0 :float
        strike price
    T: float
        Maturity date(in year functions)
    r: float
        constant risk free short rate
    sigma: float
        volatility factor in diffusion term

    Returns
    ======
    value: float
        present value of the European call option

    '''

    from math import log, sqrt, exp
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0 /K) + (r + 0.05 * sigma ** 2) * T)/(sigma * sqrt(T))
    d2 = (log(S0/K) + (r - 0.5 * sigma ** 2)* T /(sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0) - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    return value



