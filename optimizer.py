# optimizer.py

import numpy as np
import cvxpy as cp
from scipy.optimize import minimize

def minimum_variance(mu, cov_matrix):
    n = len(mu)
    w = cp.Variable(n)

    portfolio_variance = cp.quad_form(w, cov_matrix.values)
    constraints = [cp.sum(w) == 1, w >= 0]

    problem = cp.Problem(cp.Minimize(portfolio_variance), constraints)
    problem.solve()

    return w.value


def maximum_sharpe(mu, cov_matrix, risk_free_rate):
    n = len(mu)

    def neg_sharpe(weights):
        port_return = np.dot(weights, mu)
        port_std = np.sqrt(np.dot(weights.T,
                                  np.dot(cov_matrix, weights)))
        return -(port_return - risk_free_rate) / port_std

    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0,1) for _ in range(n))
    initial_weights = n * [1./n]

    result = minimize(neg_sharpe,
                      initial_weights,
                      method='SLSQP',
                      bounds=bounds,
                      constraints=constraints)

    return result.x


def efficient_frontier(mu, cov_matrix, num_points=50):
    n = len(mu)
    target_returns = np.linspace(mu.min(), mu.max(), num_points)
    efficient_risk = []

    for target in target_returns:
        w = cp.Variable(n)
        risk = cp.quad_form(w, cov_matrix.values)

        constraints = [
            cp.sum(w) == 1,
            mu.values @ w == target,
            w >= 0
        ]

        prob = cp.Problem(cp.Minimize(risk), constraints)
        prob.solve()

        efficient_risk.append(np.sqrt(prob.value))

    return target_returns, efficient_risk
