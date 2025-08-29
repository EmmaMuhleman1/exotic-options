"""
Options pricing models and utilities.

This module contains various exotic options pricing models using Monte Carlo
simulation, finite difference methods, and analytical solutions.
"""

import numpy as np
from scipy import stats


class BlackScholesModel:
    """Black-Scholes model for option pricing."""
    
    def __init__(self, S0: float, r: float, sigma: float, T: float):
        """
        Initialize the Black-Scholes model.
        
        Args:
            S0: Initial stock price
            r: Risk-free interest rate
            sigma: Volatility
            T: Time to maturity
        """
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
    
    def european_call_price(self, K: float) -> float:
        """
        Calculate European call option price using Black-Scholes formula.
        
        Args:
            K: Strike price
            
        Returns:
            Call option price
        """
        d1 = (np.log(self.S0/K) + (self.r + 0.5*self.sigma**2)*self.T) / (self.sigma*np.sqrt(self.T))
        d2 = d1 - self.sigma*np.sqrt(self.T)
        
        call_price = self.S0*stats.norm.cdf(d1) - K*np.exp(-self.r*self.T)*stats.norm.cdf(d2)
        return call_price
    
    def european_put_price(self, K: float) -> float:
        """
        Calculate European put option price using Black-Scholes formula.
        
        Args:
            K: Strike price
            
        Returns:
            Put option price
        """
        d1 = (np.log(self.S0/K) + (self.r + 0.5*self.sigma**2)*self.T) / (self.sigma*np.sqrt(self.T))
        d2 = d1 - self.sigma*np.sqrt(self.T)
        
        put_price = K*np.exp(-self.r*self.T)*stats.norm.cdf(-d2) - self.S0*stats.norm.cdf(-d1)
        return put_price

def monte_carlo_simulation(S0: float, r: float, sigma: float, T: float, 
                          n_paths: int = 10000, n_steps: int = 252) -> np.ndarray:
    """
    Simulate stock price paths using Monte Carlo method.
    
    Args:
        S0: Initial stock price
        r: Risk-free rate
        sigma: Volatility
        T: Time to maturity
        n_paths: Number of simulation paths
        n_steps: Number of time steps
        
    Returns:
        Array of simulated stock prices (n_paths x n_steps+1)
    """
    dt = T / n_steps
    paths = np.zeros((n_paths, n_steps + 1))
    paths[:, 0] = S0
    
    for i in range(1, n_steps + 1):
        z = np.random.standard_normal(n_paths)
        paths[:, i] = paths[:, i-1] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)
    
    return paths
