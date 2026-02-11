# simulation.py

import numpy as np

def monte_carlo(mu, cov_matrix, risk_free_rate, num_portfolios):
    n = len(mu)
    results = np.zeros((3, num_portfolios))
    weights_record = []

    for i in range(num_portfolios):
        weights = np.random.random(n)
        weights /= np.sum(weights)

        port_return = np.dot(weights, mu)
        port_std = np.sqrt(np.dot(weights.T,
                                  np.dot(cov_matrix, weights)))

        results[0,i] = port_return
        results[1,i] = port_std
        results[2,i] = (port_return - risk_free_rate) / port_std

        weights_record.append(weights)

    return results, weights_record
