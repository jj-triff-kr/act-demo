# Hello App with GCP Cloud Run Deployment

This repository contains a simple Python application that prints a greeting message and includes a GitHub Actions workflow to deploy it to Google Cloud Run.

## Python Script

The `hello.py` script is a simple Python application that prints a greeting message:

```
Hello Dear <user>
```

Where `<user>` is a parameter passed to the script. If no parameter is provided, it defaults to "World".

### Running Locally

To run the script locally:

```bash
python hello.py "Your Name"
```

## Docker Container

The repository includes a Dockerfile to containerize the application. The container accepts a `USER` environment variable to customize the greeting.

### Building and Running Locally

Build the Docker image:

```bash
docker build -t hello-app .
```

Run the container:

```bash
docker run -e USER="Your Name" hello-app
```

## GitHub Actions Workflow

The repository includes a GitHub Actions workflow that:

1. Runs the Python script
2. Builds a Docker image
3. Pushes the image to Google Container Registry
4. Deploys the image to Google Cloud Run

### Required Secrets

To use the GitHub Actions workflow, you need to set up the following secrets in your GitHub repository:

- `GCP_PROJECT_ID`: Your Google Cloud Project ID
- `WIF_PROVIDER`: Your Workload Identity Federation provider
- `WIF_SERVICE_ACCOUNT`: Your service account email for authentication

### Setting Up Google Cloud

1. Create a Google Cloud Project
2. Enable the Cloud Run API and Container Registry API
3. Set up Workload Identity Federation for GitHub Actions
4. Create a service account with the necessary permissions

For detailed instructions on setting up Workload Identity Federation, see the [Google GitHub Actions documentation](https://github.com/google-github-actions/auth).

## Deployment

The application is automatically deployed to Google Cloud Run when changes are pushed to the main branch. The deployed URL is printed at the end of the GitHub Actions workflow run.
