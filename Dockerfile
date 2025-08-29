# Use official miniconda3 image as base
FROM continuumio/miniconda3:latest

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy environment file
COPY environment.yml .

# Create conda environment
RUN conda env create -f environment.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "exotic-options", "/bin/bash", "-c"]

# Copy project files
COPY . .

# Install the package in development mode
RUN pip install -e .

# Create a non-root user
RUN useradd -m -s /bin/bash appuser && chown -R appuser:appuser /app
USER appuser

# Expose port for Jupyter
EXPOSE 8888

# Set environment variables
ENV PYTHONPATH="/app/src:$PYTHONPATH"

# Default command
CMD ["conda", "run", "-n", "exotic-options", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
