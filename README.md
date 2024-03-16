# PostgreSQL Event Listener

## Overview

This repository contains a Python script for listening to events in a PostgreSQL database using the `LISTEN` and `NOTIFY` commands. PostgreSQL provides a powerful feature where you can listen for certain events happening in the database and get notified in real-time.

## Features

- Listens for specific events happening in a PostgreSQL database.
- Real-time notification of database events using `NOTIFY`.
- Example script to demonstrate how to use PostgreSQL's event listening feature.
- Simple and easy-to-understand Python codebase.

## Usage

### Using Docker Compose

1. Clone this repository to your local machine.
2. Ensure you have Docker and Docker Compose installed on your machine.
3. Navigate to the root directory of the cloned repository.
4. Open the `docker-compose.yaml` file and update the environment variables under the `listener` service to match your PostgreSQL database connection details.
5. Run the following command to start the PostgreSQL and Python services:

```bash
docker-compose up
```

## Requirements

- Python 3.x
- PostgreSQL database

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
