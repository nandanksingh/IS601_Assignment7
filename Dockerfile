# -----------------------------------------------------------------------------
# IS601 - Assignment 7: Dockerizing the QR Code Generator Application
# Author: Nandan Kumar
# GitHub: https://github.com/nandanksingh/IS601_Assignment7
# DockerHub: https://hub.docker.com/repository/docker/nandanksingh/is601_assignment7
# -----------------------------------------------------------------------------

# Use the official lightweight Python image from DockerHub as the base
FROM python:3.12-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file first (for layer caching)
COPY requirements.txt ./

# Create a non-root user, install dependencies, and prepare directories
RUN useradd -m myuser && \
    pip install --no-cache-dir -r requirements.txt && \
    mkdir -p logs qr_codes && \
    chown -R myuser:myuser /app

# Copy all remaining application files and ensure correct ownership
COPY --chown=myuser:myuser . .

# Switch to the non-root user for security
USER myuser

# (Optional) Expose a port if needed for API/web extension
# EXPOSE 8080

# Define the container’s entry point and default arguments
ENTRYPOINT ["python", "main.py"]
CMD ["--url", "http://github.com/nandanksingh"]

# -----------------------------------------------------------------------------
# Build command:
#   docker build -t nandanksingh/is601_assignment7 .
#
# Run command:
#   docker run -d --name qr-generator nandanksingh/is601_assignment7
#
# Run with custom URL and volume mapping:
#   docker run -d --name qr-njit \
#     -v /mnt/c/Users/nanda/IS601_Assignment7/qr_codes:/app/qr_codes \
#     nandanksingh/is601_assignment7 --url http://www.njit.edu
#
# Push to DockerHub:
#   docker push nandanksingh/is601_assignment7
# -----------------------------------------------------------------------------
