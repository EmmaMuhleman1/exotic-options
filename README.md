# Exotic Options Project

A Python project for exotic options pricing and analysis using scientific computing libraries.

## Setup

### Prerequisites

- Anaconda or Miniconda installed on your system

### Environment Setup

1. Create and activate the conda environment:

```bash
conda env create -f environment.yml
conda activate exotic-options
```

Alternatively, if you prefer using pip with a virtual environment:

```bash
conda create -n exotic-options python=3.11
conda activate exotic-options
pip install -r requirements.txt
```

### Running the Project

After activating the environment, you can run the main script:

```bash
python main.py
```

## Project Structure

- `main.py` - Main entry point
- `src/` - Source code modules
- `notebooks/` - Jupyter notebooks for analysis
- `tests/` - Unit tests
- `data/` - Data files
- `requirements.txt` - Python dependencies
- `environment.yml` - Conda environment specification

## Dependencies

This project uses the following scientific computing libraries:

- NumPy - Numerical computing
- SciPy - Scientific computing
- Matplotlib - Static plotting
- Plotly - Interactive plotting
- Pandas - Data manipulation
- Jupyter - Interactive notebooks
- QuantLib - Quantitative finance (optional)
