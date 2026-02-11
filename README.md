# Portfolio Optimization and Efficient Frontier Analysis

This project performs portfolio optimization on selected S&P 500 stocks using **Python**, **matrix algebra**, and **quadratic programming**. It includes visualization of the **efficient frontier**, **Monte Carlo simulations**, **asset correlation heatmap**, **risk-return tradeoff curves**, and portfolio weights.

---

## **Project Purpose**

The goal of this project is to:

1. Optimize a stock portfolio to minimize risk (variance) or maximize return-adjusted risk (Sharpe ratio).  
2. Explore the tradeoff between risk and return using **efficient frontier analysis**.  
3. Visualize portfolio characteristics and correlations between assets.  
4. Simulate multiple portfolio outcomes using **Monte Carlo methods**.  

---

## **Features / Requirements Implemented**

1. **Efficient Frontier Plot** – Shows the optimal risk-return tradeoff.  
2. **Monte Carlo Portfolio Simulation** – Random portfolio generation and Sharpe ratio calculation.  
3. **Asset Correlation Heatmap** – Visualizes correlation between selected stocks.  
4. **Risk–Return Tradeoff Curve** – Shows distribution of simulated portfolios.  
5. **Portfolio Weight Pie Charts** – Visualizes allocation for minimum variance and maximum Sharpe portfolios.

---

## **Technologies / Libraries Used**

- Python 3.x  
- NumPy  
- Pandas  
- SciPy  
- Matplotlib  
- Seaborn  
- yfinance  

---

## **How to Run**

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/portfolio-optimization-s-p500.git
Install required libraries:

pip install -r requirements.txt


Run the main script:

python main.py


The script will generate all plots:

Efficient Frontier with Monte Carlo points

Monte Carlo Portfolio Simulation

Asset Correlation Heatmap

Risk-Return Tradeoff Curve

Portfolio Weight Pie Charts

Project Structure
Portfolio_Optimization_S&P500/
│
├─ main.py                 # Main execution script
├─ config.py               # Configuration (tickers, dates, parameters)
├─ data_loader.py          # Functions to download and process stock data
├─ portfolio_math.py       # Expected returns, covariance, correlation
├─ optimizer.py            # Portfolio optimization functions
├─ simulation.py           # Monte Carlo simulation
├─ visualization.py        # Plotting and visualization functions
├─ requirements.txt        # Python dependencies
└─ README.md               # Project documentation

Sample Portfolio Weights Output
Minimum Variance Weights:
AAPL    0.32
MSFT    0.12
GOOG    0.25
TSLA    0.31

Maximum Sharpe Weights:
META    0.71
NVDA    0.29
