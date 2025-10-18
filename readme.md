# Assignment 7: Dockerizing the QR Code Generator Application
**Submitted by:** Nandan Kumar
**GitHub Repository:** : https://github.com/nandanksingh/IS601_Assignment7 
**DockerHub Repository:** : https://hub.docker.com/repository/docker/nandanksingh/is601_assignment7 


## Objective:

The goal of this assignment was to Dockerize a Python-based QR Code Generator application.
The task involved building a secure Docker image, running the application inside a container, and pushing the final image to DockerHub.

This assignment helped me understand how containerization makes applications portable, efficient, and consistent across environments.

## Setup: 
## Step 1 – Setting Up the Environment

Since I am using Windows 11, I installed and configured the following tools:

* Git for Windows – to clone and manage code repositories
* Python 3.12 or higher – to test and verify the QR Code Generator application
* Docker Desktop (with WSL2 backend) – to build and run containers

After installation, I verified each tool with these commands:

```
git --version
python --version
docker --version
```

All tools were installed successfully and ready to use.

---

## Step 2 – Running the Python Application Locally

Before containerizing the project, I verified that the Python code worked correctly on my system.

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py --url http://www.njit.edu
```

The application generated a QR code image and saved it inside the **qr_codes** folder.
This confirmed that all dependencies were installed and the script was functioning properly before moving to Docker.

---

## Step 3 – Writing the Dockerfile

I created a Dockerfile that defines the steps to build and run the application inside a container.
The Dockerfile uses the lightweight **python:3.12-slim-bullseye** base image, installs dependencies, creates a non-root user for security, and defines the entry point for the application.

Key points included in the Dockerfile:

* Uses a minimal base image for better performance
* Installs dependencies from requirements.txt
* Creates a non-root user named "myuser"
* Configures directories for logs and generated QR codes
* Uses ENTRYPOINT and CMD for flexible runtime arguments

This Dockerfile ensures that the application runs securely and efficiently inside the container.

---

## Step 4 – Building the Docker Image

I built the Docker image using the following command:

```
docker build -t nandanksingh/is601_assignment7 .
```

The image built successfully without errors.
I confirmed the image was available locally using:

```
docker images
```

## Step 5 – Running the Docker Container

Once the image was built, I ran the container to test the QR Code Generator.

```
docker run -d --name qr-generator nandanksingh/is601_assignment7
docker logs qr-generator
```

The logs showed that the QR code was created successfully and saved in the container’s **/app/qr_codes** directory.

To save the generated QR code file to my local system, I used volume mapping:

```
docker run -d --name qr-njit ^
 -v %cd%\qr_codes:/app/qr_codes ^
 nandanksingh/is601_assignment7 --url http://www.njit.edu
```

The QR code was generated and saved in my local **qr_codes** folder, confirming that the container and host system were properly connected.

---

## Step 6 – Using Docker Compose (Optional)

I also tested the Docker Compose file provided in the project to simplify running the container.

```
docker-compose up --build -d
docker-compose logs -f
docker-compose down
```

The compose file automatically built the image, passed environment variables, and mapped local directories.
It worked correctly and produced the same results as the direct Docker commands.

---

## Step 7 – Pushing the Image to DockerHub

After confirming the container worked correctly, I pushed my image to DockerHub.

```
docker login
docker push nandanksingh/is601_assignment7
```

The image is now available publicly and can be pulled using:

```
docker pull nandanksingh/is601_assignment7
```

This ensures that anyone can access and run my containerized application.

---

## QR codes:
## GitHub Repository Image
![GitHub QR Code](./qr_codes/QRCode_20251017210937.png "GitHub Repository QR Code")

## DockerHub Image 
![DockerHub QR Code](./qr_codes/QRCode_20251017210937.png "DockerHub Repository QR Code")

## Reflection:

This assignment provided valuable hands-on experience with Docker and containerization.
I learned how to:

* Build and run Python applications inside Docker containers
* Use environment variables and volume mounts for flexibility
* Apply security best practices by running containers with non-root users
* Push and manage Docker images on DockerHub

I also gained a better understanding of how Docker simplifies deployment and ensures application consistency across different systems.
Working with WSL2 and Docker on Windows helped me appreciate how closely modern development environments simulate Linux systems for container-based workflows.

---

## Conclusion:

This was one of the most practical and informative assignments of the course.
It combined the concepts of Python programming, version control, and Docker-based deployment into a single project.

By completing this assignment, I now have a strong understanding of:

* Creating Dockerfiles
* Building and testing container images
* Running applications securely in isolated environments
* Sharing and distributing containers using DockerHub

This project gave me confidence in working with modern DevOps tools and applying them in real-world software development workflows.


