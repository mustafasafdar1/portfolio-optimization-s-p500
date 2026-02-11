# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (9, 6)
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12



def plot_efficient_frontier(target_returns, efficient_risk, results):
    plt.figure(figsize=(10, 6))


    plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap='viridis',
                marker='o', s=30, alpha=0.6, label="Random Portfolios")


    plt.plot(efficient_risk, target_returns, 'r--', linewidth=3, label="Efficient Frontier")

    plt.xlabel("Risk (Std Dev)")
    plt.ylabel("Expected Return")
    plt.title("Efficient Frontier with Monte Carlo Simulation")
    plt.colorbar(label='Sharpe Ratio')
    plt.legend()
    plt.grid(True)
    plt.show()



def plot_monte_carlo(results):
    plt.figure(figsize=(10, 6))
    plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap='plasma',
                s=50, alpha=0.6, edgecolor='k')
    plt.xlabel("Risk (Std Dev)")
    plt.ylabel("Expected Return")
    plt.title("Monte Carlo Portfolio Simulation")
    plt.colorbar(label='Sharpe Ratio')
    plt.grid(True)
    plt.show()



def plot_heatmap(corr_matrix):
    plt.figure(figsize=(9, 7))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0,
                linewidths=0.5, linecolor='gray', fmt=".2f", cbar_kws={"shrink": 0.8})
    plt.title("Asset Correlation Heatmap")
    plt.show()



def plot_risk_return(results):
    plt.figure(figsize=(10, 6))
    plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap='inferno',
                s=50, alpha=0.6, edgecolor='k')
    plt.xlabel("Risk (Std Dev)")
    plt.ylabel("Expected Return")
    plt.title("Risk–Return Tradeoff")
    plt.colorbar(label='Sharpe Ratio')
    plt.grid(True)
    plt.show()



def plot_pie(weights, labels, title):

    weights = np.array(weights)
    weights[weights < 0] = 0
    weights = weights / np.sum(weights)  # normalize to sum=1

    colors = sns.color_palette('pastel', len(labels))

    plt.figure(figsize=(7, 7))
    plt.pie(weights,
            labels=labels,
            autopct='%1.1f%%',
            colors=colors,
            startangle=140,
            wedgeprops={'edgecolor': 'k', 'linewidth': 1.2})
    plt.title(title)
    plt.show()
