
import config
from data_loader import download_data, calculate_returns
from portfolio_math import expected_returns, covariance_matrix, correlation_matrix
from optimizer import minimum_variance, maximum_sharpe, efficient_frontier
from simulation import monte_carlo
from visualization import plot_efficient_frontier, plot_monte_carlo, plot_heatmap, plot_risk_return, plot_pie

import pandas as pd


data = download_data(config.TICKERS,
                     config.START_DATE,
                     config.END_DATE)

returns = calculate_returns(data)


mu = expected_returns(returns, config.TRADING_DAYS)
cov_matrix = covariance_matrix(returns, config.TRADING_DAYS)
corr_matrix = correlation_matrix(returns)


min_var_weights = minimum_variance(mu, cov_matrix)
max_sharpe_weights = maximum_sharpe(mu, cov_matrix,
                                    config.RISK_FREE_RATE)


target_returns, efficient_risk = efficient_frontier(mu, cov_matrix)


results, weights_record = monte_carlo(
    mu,
    cov_matrix,
    config.RISK_FREE_RATE,
    config.MONTE_CARLO_PORTFOLIOS
)




plot_efficient_frontier(target_returns, efficient_risk, results)

# 6b. Monte Carlo Simulation (Standalone)
plot_monte_carlo(results)


plot_heatmap(corr_matrix)


plot_risk_return(results)


plot_pie(min_var_weights, config.TICKERS, "Minimum Variance Portfolio")
plot_pie(max_sharpe_weights, config.TICKERS, "Maximum Sharpe Portfolio")


print("\nMinimum Variance Weights:")
print(pd.Series(min_var_weights, index=config.TICKERS))

print("\nMaximum Sharpe Weights:")
print(pd.Series(max_sharpe_weights, index=config.TICKERS))
