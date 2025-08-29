#!/usr/bin/env python3
"""
Exotic Options Project - Main Entry Point

This is the main script for the exotic options pricing and analysis project.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
from scipy import stats

# Set style for matplotlib
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def main():
    """Main function to demonstrate the scientific computing setup."""
    print("🚀 Exotic Options Project")
    print("=" * 50)  
    # Demonstrate NumPy
    print("📊 NumPy Demo:")
    arr = np.random.normal(0, 1, 1000)
    print(f"   Random array shape: {arr.shape}")
    print(f"   Mean: {np.mean(arr):.4f}, Std: {np.std(arr):.4f}")  
    # Demonstrate Pandas
    print("\n📈 Pandas Demo:")
    df = pd.DataFrame({
        'price': np.random.exponential(100, 100),
        'volatility': np.random.uniform(0.1, 0.5, 100),
        'time_to_expiry': np.random.uniform(0.1, 2, 100)
    })
    print(f"   DataFrame shape: {df.shape}")
    print(f"   Columns: {list(df.columns)}") 
    # Demonstrate SciPy
    print("\n🧮 SciPy Demo:")
    sample_data = np.random.normal(100, 15, 50)
    t_stat, p_value = stats.ttest_1samp(sample_data, 100)
    print(f"   T-test statistic: {t_stat:.4f}")
    print(f"   P-value: {p_value:.4f}") 
    # Create a simple plot with Matplotlib
    print("\n📊 Creating sample plots...") 
    # Matplotlib plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) 
    # Plot 1: Option price simulation
    S0 = 100  # Initial stock price
    r = 0.05  # Risk-free rate
    sigma = 0.2  # Volatility
    T = 1.0  # Time to maturity
    dt = T/252  # Daily time step 
    # Simulate stock price paths
    np.random.seed(42)
    paths = []
    for _ in range(5):
        path = [S0]
        for _ in range(252):
            dS = path[-1] * (r * dt + sigma * np.sqrt(dt) * np.random.normal())
            path.append(path[-1] + dS)
        paths.append(path) 
    time_steps = np.linspace(0, T, 253)
    for i, path in enumerate(paths):
        ax1.plot(time_steps, path, alpha=0.7, label=f'Path {i+1}') 
    ax1.set_title('Stock Price Simulation')
    ax1.set_xlabel('Time (years)')
    ax1.set_ylabel('Stock Price')
    ax1.legend()
    ax1.grid(True, alpha=0.3) 
    # Plot 2: Volatility distribution
    volatilities = np.random.gamma(2, 0.1, 1000)
    ax2.hist(volatilities, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    ax2.set_title('Implied Volatility Distribution')
    ax2.set_xlabel('Volatility')
    ax2.set_ylabel('Frequency')
    ax2.grid(True, alpha=0.3) 
    plt.tight_layout()
    plt.savefig('data/sample_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()  
    # Create an interactive Plotly chart
    fig_plotly = go.Figure() 
    # Add stock price paths
    for i, path in enumerate(paths[:3]):  # Show first 3 paths
        fig_plotly.add_trace(go.Scatter(
            x=time_steps,
            y=path,
            mode='lines',
            name=f'Path {i+1}',
            line=dict(width=2)
        )) 
    fig_plotly.update_layout(
        title='Interactive Stock Price Simulation',
        xaxis_title='Time (years)',
        yaxis_title='Stock Price',
        hovermode='x unified',
        template='plotly_white'
    ) 
    # Save the interactive plot
    fig_plotly.write_html('data/interactive_analysis.html')
    print("   ✅ Static plot saved as 'data/sample_analysis.png'")
    print("   ✅ Interactive plot saved as 'data/interactive_analysis.html'") 
    print("\n🎉 Setup complete! All libraries are working correctly.")
    print("\n📝 Next steps:")
    print("   1. Activate conda environment: conda activate exotic-options")
    print("   2. Start Jupyter: jupyter lab")
    print("   3. Explore the notebooks/ directory")
    print("   4. Check out the generated plots in the data/ directory")

if __name__ == "__main__":
    main()
