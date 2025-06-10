# Hello App with GCP Cloud Run Deployment

This repository contains a simple Python application that prints a greeting message and includes a GitHub Actions workflow to test out nektos/act.

## Python Script

The `hello.py` script is a simple Python application that prints a greeting message:

```
Hello Dear <user>
```

Where `<user>` is a parameter passed to the script. If no parameter is provided, it defaults to "World".

### Using act to run the workflow

```shell
act workflow_dispatch --workflows .github/workflows/python-app.yml -P self-hosted=krogertechnology-docker.jfrog.io/summerwind/actions-runner-dind --input user=Kroger --reuse --pull=false
```

### Debugging python inside of the workflow.

If using intellij use the saved python debug server config at `.idea/runConfigurations/act.xml`

```shell
act workflow_dispatch --workflows .github/workflows/python-debugging.yml -P self-hosted=krogertechnology-docker.jfrog.io/summerwind/actions-runner-dind --input user=Kroger --reuse --pull=false --container-options '-p 8838:8838'
```
