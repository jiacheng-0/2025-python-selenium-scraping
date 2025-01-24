# Docker Python Project: Scraping with Selenium

This repository contains a Dockerized Python application for web scraping using Selenium. The project is designed to be easily set up and run in a Docker container, ensuring a consistent environment across different systems.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose (optional): [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/scraping-selenium.git
cd scraping-selenium
```

### 2. Build the Docker Image

To build the Docker image, run the following command:

```bash
docker build -t scraping-selenium .
```

This command will create a Docker image named scraping-selenium based on the Dockerfile provided in the repository.

### 3. Run the Docker Container

Once the image is built, you can run the container using:
```bash
docker run -it scraping-selenium
```

This will start the container and drop you into an interactive shell where you can run your Python scripts.

### 4. Check Running Containers

To see the list of running Docker containers, use:
```bash
docker ps
```

### 5. List Installed Python Packages

To list the Python packages installed in the container, you can use:

```bash
pip list
```

## Dockerfile Overview

The Dockerfile in this repository is configured to:

- Use a base Python image.
- Install necessary dependencies from requirements.txt.
- Set up the working directory.
- Copy the application code into the container.

## Project Structure

scraping-selenium/
│
├── Dockerfile
├── requirements.txt
├── src/
│   └── main.py
└── README.md

- Dockerfile: Contains the instructions to build the Docker image.
- requirements.txt: Lists the Python dependencies required for the project.
- src/main.py: The main Python script for web scraping.
- README.md: This file, providing an overview and setup instructions.

## Customization

### Adding More Dependencies

If you need to add more Python packages, simply add them to the requirements.txt file and rebuild the Docker image.

### Running Specific Scripts

To run a specific Python script inside the container, you can modify the docker run command:
docker run -it scraping-selenium python src/main.py

## Troubleshooting

### Docker Container Issues

If you encounter issues with the Docker container, you can check the logs using:
docker logs <container_id>

Replace <container_id> with the actual container ID obtained from docker ps.

### Dependency Conflicts

If there are conflicts or missing dependencies, ensure that requirements.txt is up-to-date and rebuild the Docker image.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy Scraping! 🚀