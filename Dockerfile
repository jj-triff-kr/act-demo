FROM python:3.10-slim

WORKDIR /app

COPY hello.py .

# Set the default user parameter
ENV USER="World"

# Command to run when the container starts
CMD ["sh", "-c", "python hello.py $USER"]