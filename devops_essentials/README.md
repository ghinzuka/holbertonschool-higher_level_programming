# Project Badge

![download](https://github.com/ghinzuka/holbertonschool-higher_level_programming/assets/102736316/d0d7fb5a-6479-4f0f-9947-dc14a72c9772)

**Completion:** 100%

**Title:** Containerization and Orchestration Essentials

**Level:** Amateur

**By:** Javier Valenzani

**Weight:** 1

**Migrated to checker v2:** 

Manual QA review was done by Matthieu Grauleau on Jun 11, 2024 3:55 PM

AUTHOR : BAPTISTE POUQUEROU

## Description

This project is designed to immerse students in the fundamentals of containerization and orchestration using Docker, Docker Compose, and GitHub Actions. Through a series of hands-on tasks, students will gain practical experience in creating, customizing, and deploying Docker images, managing data persistence, and orchestrating simple multi-service infrastructures. The project adopts a learn-by-doing approach, encouraging students to leverage provided resources, explore solutions independently, and collaborate to overcome challenges.

## Objectives

- **Understanding Containerization:** Grasp the basics of containerization by creating and customizing Docker images based on the Alpine base image.
  
- **Automating Workflows:** Learn how to automate the build and deployment of Docker images using GitHub Actions, fostering an understanding of CI/CD principles.
  
- **Managing Data Persistence:** Explore the concept of data persistence in Docker by working with volumes to retain data across container restarts.
  
- **Exploring Orchestration:** Dive into basic orchestration by setting up a simple infrastructure using Docker Compose, facilitating an understanding of multi-service deployments and inter-service communication.
  
- **Applying Best Practices:** Implement best practices in Dockerfile creation, GitHub Actions workflow configuration, and Docker Compose setup to build a solid foundation for more complex projects.

## Resources

Please, be sure to watch the following introductory videos:

- [Containers and VMs - A Practical Comparison](video-url)
- [What is a Container?](video-url)
- [Containers 101](video-url)

The following documentation will help you get a deeper understanding of the concepts:

- Familiarize yourself with Docker by going through the [Docker Official Documentation](https://docs.docker.com/) and [Docker 101 Tutorial](https://www.docker.com/101-tutorial).
- Learn about Docker Compose through the [Docker Compose Documentation](https://docs.docker.com/compose/).
- Look into Docker image creation on [devopscube.com](https://devopscube.com/docker-tutorial/) and [linux.com](https://www.linux.com/topic/containers/).

| Task Number | Task Title                                    | Description                                                                                                                                                                                                           |
|-------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0           | Create a Simple Docker Image Based on Alpine   | Dockerfile to create an Alpine-based image printing "Hello, World!" when run.                                                                                                                                           |
| 1           | Customize Your Alpine-based Docker Image       | Extend previous Docker image by installing curl and adding config.txt.                                                                                                                                                |
| 2           | Automate Container Image Build and Push        | Implement GitHub Actions workflow to build Docker image on push and push it to GitHub Container Registry.                                                                                                             |
| 3           | Persist Data Using Volumes                     | Modify Dockerfile to include a volume at /data and demonstrate data persistence.                                                                                                                                        |
| 4           | Set Up a Simple Infrastructure Using Docker Compose | Define Docker Compose YAML file with PostgreSQL and pgAdmin services, configuring a private network and ensuring pgAdmin can manage PostgreSQL.                                                                      |

AUTHOR : BAPTISTE POUQUEROU
