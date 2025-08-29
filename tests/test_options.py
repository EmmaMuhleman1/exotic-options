"""
Test suite for the options module.
"""

import numpy as np

from src.options import BlackScholesModel, monte_carlo_simulation


class TestBlackScholesModel:
    """Test cases for Black-Scholes model."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.model = BlackScholesModel(S0=100, r=0.05, sigma=0.2, T=1.0)
    
    def test_call_option_price(self):
        """Test European call option pricing."""
        call_price = self.model.european_call_price(K=100)
        
        # The call price should be positive
        assert call_price > 0
        
        # At-the-money call with positive interest rate should be > intrinsic value
        assert call_price > max(self.model.S0 - 100, 0)
    
    def test_put_option_price(self):
        """Test European put option pricing."""
        put_price = self.model.european_put_price(K=100)
        
        # The put price should be positive
        assert put_price > 0
        
        # At-the-money put should be less than strike price
        assert put_price < 100
    
    def test_put_call_parity(self):
        """Test put-call parity relationship."""
        K = 100
        call_price = self.model.european_call_price(K)
        put_price = self.model.european_put_price(K)
        
        # Put-call parity: C - P = S0 - K*e^(-rT)
        parity_diff = call_price - put_price
        theoretical_diff = self.model.S0 - K * np.exp(-self.model.r * self.model.T)
        
        assert abs(parity_diff - theoretical_diff) < 1e-10

class TestMonteCarloSimulation:
    """Test cases for Monte Carlo simulation."""
    
    def test_simulation_shape(self):
        """Test that simulation returns correct shape."""
        paths = monte_carlo_simulation(S0=100, r=0.05, sigma=0.2, T=1.0, 
                                     n_paths=1000, n_steps=252)
        
        assert paths.shape == (1000, 253)  # n_steps + 1
    
    def test_initial_price(self):
        """Test that all paths start at initial price."""
        S0 = 100
        paths = monte_carlo_simulation(S0=S0, r=0.05, sigma=0.2, T=1.0)
        
        assert np.all(paths[:, 0] == S0)
    
    def test_positive_prices(self):
        """Test that all simulated prices are positive."""
        paths = monte_carlo_simulation(S0=100, r=0.05, sigma=0.2, T=1.0)
        
        assert np.all(paths > 0)
