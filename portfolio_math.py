# portfolio_math.py

import numpy as np

def expected_returns(returns, trading_days):
    return returns.mean() * trading_days

def covariance_matrix(returns, trading_days):
    return returns.cov() * trading_days

def correlation_matrix(returns):
    return returns.corr()

def portfolio_performance(weights, mu, cov_matrix):
    port_return = np.dot(weights, mu)
    port_std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return port_return, port_std
