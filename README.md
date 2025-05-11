# APP Deployment with GitHub Actions, AWS ECR, and ECS
**Deploy_App_Github_Action_AWS_ECS** repository automates the deployment of an API to AWS Elastic Container Service (ECS) using GitHub Actions. It includes CI/CD workflows for formatting, testing, building, and deploying containerized applications efficiently.

This repository demonstrates how to deploy a FastAPI-based application using GitHub Actions for CI/CD and AWS Elastic Container Service (ECS) for hosting. The project includes automated workflows for building, testing, and deploying containerized applications efficiently.

---

## Features

- **FastAPI Backend**: A lightweight Python web framework for building APIs.
- **Dockerized Application**: The application is containerized using Docker for portability.
- **CI/CD with GitHub Actions**: Automated workflows for code formatting, testing, and deployment.
- **AWS ECS Deployment**: The application is deployed to AWS ECS using Fargate for serverless container hosting.
- **MongoDB Integration**: Session history is stored in MongoDB for persistence.
- **Generative AI Models**: Supports OpenAI and Gemini models for generating responses.

---

## 1. Project Structure

The project is organized as follows:

```
|-- config/
|   |-- __init__.py
|   |-- config.py          # MongoDB configuration and connection setup
|
|-- model/
|   |-- __init__.py
|   |-- model.py           # Generative AI model logic (OpenAI and Gemini)
|
|-- routes/
|   |-- __init__.py
|   |-- routes.py          # API routes for query response and session history
|
|-- static/
|   |-- css/
|   |   |-- style.css      # Frontend styling
|
|-- templates/
|   |-- template.html      # HTML template for the frontend
|
|-- tests/
|   |-- __init__.py
|   |-- test_app_routes.py # Unit tests for API routes
|
|-- .github/
|   |-- workflows/
|   |   |-- ci-cd-pipeline.yaml # GitHub Actions workflow for CI/CD
|
|-- app.py                 # Main FastAPI application entry point
|-- requirements.txt       # Python dependencies
|-- README.md              # Project documentation
|-- .gitignore             # Files and directories to ignore in Git
|-- .env                   # Environment variables (not included in the repo)
|-- .dockerignore          # Files and directories to ignore in Docker builds
|-- Dockerfile             # Dockerfile for building the application image
|-- setup.py               # Python package setup file
```

---

## 2. Setting Up the Environment

### Step 1: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies

```bash
pip install --no-cache-dir -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file in the root directory and add the following variables:

```env
MONGODB_URI=mongodb://localhost:27017
MONGODB_DATABASE_NAME=your_database_name
MONGODB_SESSION_HISTORY_COLLECTION=your_collection_name
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

These variables are used for MongoDB connection and API keys for the generative AI models.

---

## 4. Running the Application Locally

Start the FastAPI application using Uvicorn:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

- The application will be accessible at `http://localhost:8000`.
- The frontend is served at the root endpoint (`/`).
- API endpoints:
  - `/query_response`: Accepts a user query and model type, returning a generated response.
  - `/session_history`: Retrieves the last 10 session histories from MongoDB.

---

## 5. Dockerizing the Application

### Step 1: Build the Docker Image

```bash
docker build -t generative_ai_app:latest .
```

### Step 2: Run the Docker Container

```bash
docker run -d -p 8000:8000 --name generative_ai_app_container generative_ai_app:latest
```

The application will now be accessible at `http://localhost:8000`.

---

## 6. CI/CD Pipeline with GitHub Actions

The project includes a GitHub Actions workflow for automating the following tasks:

1. **Code Formatting Check**: Ensures the code adheres to the Black formatting standard.
2. **Unit Testing**: Runs tests defined in `tests/test_app_routes.py` using pytest.
3. **Docker Image Build and Push**: Builds the Docker image and pushes it to Amazon Elastic Container Registry (ECR).
4. **Deployment to AWS ECS**: Updates the ECS task definition and deploys the new image to the ECS service.

The workflow file is located at `.github/workflows/ci-cd-pipeline.yaml`.

---

## 7. Deployment to AWS ECS

### 7.1 Create a S3 Bucket for the .env File

- Upload the .env file to the S3 bucket to store environment variables.

### 7.2 Create Cluster, Task Definition, & Service in AWS ECS

The application is deployed to AWS ECS using the following steps:

1. **Build and Push Docker Image**: The Docker image is built and pushed to Amazon ECR.
2. **Update ECS Task Definition**: The ECS task definition is updated with the new image.
3. **Deploy to ECS Service**: The updated task definition is deployed to the ECS service.

Ensure the following AWS secrets are configured in your GitHub repository:

### 7.3 Configure AWS Credentials in GIThub Secrets

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `AWS_ECR_REPO`
- `LATEST_IMAGE_URI`

---

## 8. Testing the Application

Run the unit tests using pytest:

```bash
pytest -v tests/test_app_routes.py
```

The tests cover the following scenarios:

- Successful responses from the `/query_response` endpoint.
- Error handling for missing or invalid input.
- Exception handling for model-related errors.
- Structure validation for session history responses.

---

## 9. License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 10. Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

---

## 11. Contact

For any questions or issues, please contact:

**Author**: Amir Aziz  
**Email**: amirds0235@gmail.com