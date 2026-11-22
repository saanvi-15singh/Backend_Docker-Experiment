# Backend Development – Docker Experiment Report

## 1. Project Title

**Student Management API using FastAPI and Docker**

## 2. Introduction

The objective of this experiment is to develop a simple backend application using FastAPI and deploy it using Docker. The project implements a Student Management API that allows users to perform basic operations such as adding, viewing, updating, and deleting student records.

The application is containerized using Docker so that it can run in an isolated environment without depending on the local system configuration. Docker Compose is also used to simplify the process of building and running the application.

This experiment also includes automated API testing to verify that all the application routes are working correctly.

## 3. Objectives

The main objectives of this experiment are:

1. To develop a backend application using FastAPI.
2. To understand the working of REST API endpoints.
3. To perform CRUD operations on student records.
4. To create automated tests for API routes.
5. To create a Dockerfile for containerizing the application.
6. To build and run a Docker image.
7. To configure Docker Compose for managing the application.
8. To understand the process of deploying backend applications using containers.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.13 | Programming language |
| FastAPI | Backend framework |
| Uvicorn | ASGI server |
| Requests | Sending HTTP requests during testing |
| Unittest | Automated testing |
| Docker Desktop | Container management |
| Docker | Application containerization |
| Docker Compose | Managing application containers |
| Visual Studio Code | Code editor |
| PowerShell | Command-line interface |

## 5. Project Description

The project is a Student Management API developed using FastAPI.

It maintains student information such as student ID, name, and course. The application provides different API endpoints to perform operations on student records.

The initial student records are stored in a Python list. This project uses temporary in-memory storage, so changes are not permanently saved after the application restarts.

### Features

- View the home page.
- Check application health.
- Display all student records.
- Search for a student using their ID.
- Add a new student.
- Update student information.
- Delete a student.
- Test API endpoints through interactive documentation.

## 6. API Endpoints

The following endpoints are implemented in the application:

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Displays the welcome message |
| GET | `/health` | Checks application status |
| GET | `/students` | Displays all students |
| GET | `/students/{student_id}` | Finds a student by ID |
| POST | `/students` | Adds a new student |
| PUT | `/students/{student_id}` | Updates student details |
| DELETE | `/students/{student_id}` | Deletes a student |

## 7. Project Structure

The project contains the following files and folders:

```text
Backend_Docker-Experiment/
│
├── venv/
│
├── main.py
├── requirements.txt
├── automationTesting.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── README.md
└── report.md
```

### Description of Files

- **main.py:** Contains the FastAPI application and API endpoints.
- **requirements.txt:** Contains the required Python packages.
- **automationTesting.py:** Contains automated test cases for API routes.
- **Dockerfile:** Contains instructions for building the Docker image.
- **docker-compose.yml:** Defines the application service and port mapping.
- **.dockerignore:** Excludes unnecessary files from the Docker build context.
- **.gitignore:** Prevents unnecessary files from being uploaded to GitHub.
- **report.md:** Contains the experiment documentation.

## 8. Implementation

### Step 1: Creating the Project Environment

A project folder named `Backend_Docker-Experiment` was created in Visual Studio Code.

A Python virtual environment was created to install and manage the dependencies separately from the system Python installation.

Command used:

```powershell
py -3.13 -m venv venv
```

The environment was activated using:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 2: Installing Dependencies

The required packages were installed using:

```powershell
python -m pip install fastapi uvicorn requests
```

The packages were also listed in `requirements.txt`.

### Step 3: Developing the Backend Application

The FastAPI application was developed in `main.py`.

Different routes were created to perform CRUD operations on student records.

The application was started using:

```powershell
uvicorn main:app --reload
```

The interactive API documentation was accessed through:

```text
http://127.0.0.1:8000/docs
```

### Step 4: Automated Testing

An automated testing file named `automationTesting.py` was created using Python's unittest framework and the Requests library.

The test cases verify:

1. Home route.
2. Health check route.
3. Displaying all students.
4. Fetching a student by ID.
5. Adding a student.
6. Updating student details.
7. Deleting a student.
8. Handling an invalid student ID.

The tests were executed using:

```powershell
python automationTesting.py
```

All eight automated test cases passed successfully.

### Step 5: Creating the Dockerfile

A Dockerfile was created to define the environment required to run the FastAPI application.

The Dockerfile uses the Python 3.13 slim base image, installs the required dependencies, copies the application files, and starts the Uvicorn server.

### Step 6: Building the Docker Image

The Docker image was built using:

```powershell
docker build -t student-api:v1 .
```

The image was successfully created with the name `student-api` and tag `v1`.

### Step 7: Running the Docker Container

The application was started inside a Docker container using:

```powershell
docker run -d --name student-api-container -p 8000:8000 student-api:v1
```

The container status was checked using:

```powershell
docker ps
```

The container showed the status **Up**, confirming that the application was running successfully.

### Step 8: Docker Compose Configuration

A file named `docker-compose.yml` was created to manage the application.

The configuration uses the Dockerfile to build the image and maps port 8000 of the host machine to port 8000 inside the container.

The application was started using:

```powershell
docker compose up -d --build
```

The running service was checked using:

```powershell
docker compose ps
```

The application was also tested through its browser endpoints.

## 9. Testing and Results

The application was tested both before and after containerization.

### Manual Testing

The following URLs were checked:

| URL | Expected Result |
|---|---|
| `http://127.0.0.1:8000/` | Welcome message |
| `http://127.0.0.1:8000/health` | Application running status |
| `http://127.0.0.1:8000/students` | Student records |
| `http://127.0.0.1:8000/docs` | Interactive API documentation |

All these endpoints responded successfully.

### Automated Testing

The automated testing script executed eight test cases.

**Result: 8 tests passed successfully.**

### Docker Testing

The Docker image was built successfully, and the container started with the following configuration:

- Image name: `student-api:v1`
- Container name: `student-api-container`
- Host port: `8000`
- Container port: `8000`

The application was accessible through the browser while running inside the Docker container.

## 10. Problems Faced During the Experiment

During the implementation of this experiment, I faced several issues. These problems helped me understand the project setup, Python environments, PowerShell commands, and Docker operations.

### Problem 1: Virtual Environment Path Error

Initially, the virtual environment was created in the parent folder and later moved into the project folder.

After moving it, the environment continued referring to its previous location. Because of this, the pip installation command displayed a fatal error.

**Solution:** The old virtual environment was deleted, and a new environment was created directly inside the project folder using:

```powershell
py -3.13 -m venv venv
```

### Problem 2: Incorrect Directory Navigation

While using PowerShell, I tried to enter the project folder again even though the terminal was already inside it.

This resulted in a path-not-found error.

**Solution:** I checked the current directory displayed in the terminal and continued working without repeating the `cd` command.

### Problem 3: Virtual Environment Activation

Initially, activating the Python virtual environment was confusing because PowerShell requires the correct activation script path.

**Solution:** The environment was activated using:

```powershell
.\venv\Scripts\Activate.ps1
```

### Problem 4: Understanding API Responses and Terminal Output

Initially, I was confused between the JSON response displayed in the browser and the output shown in the VS Code terminal.

**Solution:** I learned that the browser displays API responses, Terminal 1 runs the FastAPI server, and Terminal 2 is used to execute automated testing commands.

### Problem 5: Understanding Docker Container Execution

Initially, it was difficult to understand the difference between a Docker image and a Docker container.

**Solution:** By building the image and running it using `docker run`, I understood that an image is the packaged application environment, while a container is the running instance of that image.

### Problem 6: Managing the Same Port

The application was initially running through a standalone Docker container. Before using Docker Compose, the existing container needed to be stopped and removed to avoid conflicts on port 8000.

**Solution:** The following commands were used:

```powershell
docker stop student-api-container
docker rm student-api-container
```

After that, Docker Compose was used to manage the application.

## 11. Learning Outcomes

Through this experiment, I learned:

1. How to create a backend application using FastAPI.
2. How REST API endpoints work.
3. How to perform CRUD operations.
4. How to create automated test cases using unittest.
5. How to create and build a Docker image.
6. How to run an application inside a Docker container.
7. How to use Docker Compose to manage application services.
8. How to troubleshoot Python environment and Docker-related issues.
9. How to test an application before and after containerization.

## 12. Conclusion

This experiment helped me understand the process of developing, testing, and containerizing a backend application.

A Student Management API was successfully developed using FastAPI. Automated testing was performed to verify its routes, and all eight test cases passed.

The application was then containerized using Docker, and Docker Compose was configured to simplify its execution and management.

Overall, this experiment provided practical knowledge of backend development, API testing, Docker images, containers, and container management.