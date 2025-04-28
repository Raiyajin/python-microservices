![Main workflow](https://github.com/Raiyajin/python-microservices/actions/workflows/main-workflow.yml/badge.svg) [![Powered by Nyx](https://img.shields.io/badge/powered%20by-Nyx-blue)](https://github.com/mooltiverse/nyx) 

# Flask App - Health Calculator Microservice

This repository serves as a template for a simple Flask-based DevOps project. The app provides basic calculator functionalities (addition and subtraction) and includes all necessary files for setting up a local environment, running tests, and deploying to a cloud service with best practices in DevOps.

## Project Structure

The repository is organized as follows:

```plaintext
python-microservices/
├── .gitignore
├── .github/workflows/
│   ├── build.yml
│   ├── deploy.yml
│   ├── main-workflow.yml
│   ├── release.yml
│   └── test.yml
├── README.md
└── health-calculator-service/
    ├── doc/
    ├── Dockerfile
    ├── Makefile
    ├── requirements.txt
    ├── app.py
    ├── src/
    │   ├── health_exceptions.py
    │   └── health_utils.py
    └── test/
        ├── test_api.py
        ├── test_bmi.py
        └── test_bmr.py
```

### File Descriptions

- **`.gitignore`**: Specifies files and directories that should be ignored by Git. It typically includes files such as `.env` and compiled Python files (`__pycache__`), as well as local environment and dependency caches.
- **`.github/workflows`**: Contains the github pipeline configuration.
  - **`main-workflow.yml`**: The main pipeline configuration file. It calls jobs from other file to build, test, release, and deploy the docker image.
  - **`build.yml`**: The build job configuration file. It defines the steps to build the docker image.
  - **`deploy.yml`**: The deploy job configuration file. It defines the steps to deploy the docker image to Azure.
  - **`test.yml`**: The test job configuration file. It defines the steps to run the tests.
  - **`release.yml`**: The release job configuration file. It defines the steps to release the docker image to Azure.
- **`README.md`**: The main documentation file that includes details about the project, its structure, and instructions for setting up the environment and running the application.
- **`health-calculator-service/`**: The health calculator microservice.
  - **`app.py`**: The main application file for the Flask app. It sets up routes and connects them to functions in `health_utils.py` to provide API endpoints for app operations.
  - **`src/health_utils.py`**: Contains utility functions for core operations like addition and subtraction. This file is designed to house the main logic for the app’s functionality.
  - **`src/health_exceptions.py`**: Contains custom exceptions classes.
  - **`test`**: A test directory that includes tests for the functions defined in `health_utils.py` and the flask api. This file ensures that the core functionality behaves as expected.
  - **`doc`**: A documentation directory that includes documentation related to the health calculator service.
  - **`requirements.txt`**: Lists the Python dependencies needed to run the application. This file is used to install the necessary packages in the project environment.
  - **`Makefile`**: A makefile to streamline project setup and operations. Includes commands for:
    - `make init`: Install project dependencies.
    - `make run`: Start the Flask app.
    - `make test`: Run all unit tests.
    - `make build`: Build the docker image
  - **`.env`**: A configuration file for environment variables. It’s used to securely store sensitive information (like API keys, database credentials, or environment-specific settings). **Note**: This file should not be committed to version control for security reasons.
    Here's an example of the `.env` file. If the file does not exist it takes the same default values of the given example:
    ```shell
    PORT=5000
    DEBUG=False
    ```

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd python-microservices/health-calculator-service
   ```

2. **Set Up the Environment**:
   - Create and activate a virtual environment (recommended for managing dependencies).
   - Install the dependencies:
     ```bash
     make init
     ```

3. **Run the Application**:
   - Start the Flask app locally:
     ```bash
     make run
     ```


4. **Run Tests**:
   - Execute unit tests to verify functionality:
     ```bash
     make test
     ```

5. **Build the Docker Image**:
   - Build the Docker image for the Flask app:
     ```bash
     make build
     ```

## Additional Configuration

- **Environment Variables**:
  - Use the `.env` file to store any environment-specific configurations or sensitive information. Be sure to keep this file out of version control by listing it in `.gitignore`.

## Deployment Instructions

The deployment CI/CD pipelines uses GitHub Actions
  - all the deployment configurations are in the `.github/workflows` directory
  - files ending with `*-workflow.yml` are the actual entry points for the CI/CD pipelines in github actions

## Author

The original template was created by **Ali Mokh** and is intended as an educational resource for DevOps projects involving Flask applications.

And the project was modified by **Rayan HAOUAS** for the purpose of the **Health Calculator Microservice with CI/CD Pipeline on Azure** project.

## License and Usage

This project template is open to use by anyone and may be freely adapted for personal or professional projects. If you use this template as part of teaching materials or educational content, please cite **Ali Mokh** as the original author.
