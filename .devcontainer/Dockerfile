# .devcontainer/Dockerfile

FROM mcr.microsoft.com/devcontainers/python:3.11

# Install any OS-level dependencies if required
# RUN apt-get update && apt-get install -y [your-deps]

WORKDIR /workspace

# Copy requirements and install
COPY app/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# If you have any global tooling needed for onboarding tests:
# RUN pip install pylint black mypy

# Expose the typical Flask port
EXPOSE 5000

# Default command (not strictly necessary since we run in dev mode)
CMD [ "sleep", "infinity" ]
