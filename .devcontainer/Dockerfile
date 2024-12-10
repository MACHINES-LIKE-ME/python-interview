# Base image
FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

# Set working directory
WORKDIR /workspace

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the Flask app port
EXPOSE 5050

# Set default command
CMD ["bash"]
