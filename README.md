# Microservices-based Application

This project is a simple microservices-based application built using Flask, Docker, and Docker Compose. It consists of three services: user, post, and notification.

## Features

- **User Service**: Handles user-related operations like registration and login.
- **Post Service**: Manages creating and retrieving posts.
- **Notification Service**: Handles sending notifications to users.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Docker
- Docker Compose

```
project-name/
├── user/
│   ├── app.py
│   └── Dockerfile
├── post/
│   ├── app.py
│   └── Dockerfile
├── notification/
│   ├── app.py
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```


### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   
1. Navigate to the project directory:
   ```bash
   cd microservices-based-application
2. Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build

    
  



