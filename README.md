# FastAPI Project Readme

## Overview

This project is a FastAPI-based web application that provides RESTful APIs for various functionalities. It includes routes for health checks, authorization, and CRUD operations on an employee table stored in SQLite.

## Project Structure

1. **run.py**: This file is used to run the FastAPI application. Execute this file to start the server.

2. **main.py**: The main entry point of the application. It registers routes and initializes the FastAPI app.

3. **exercise1.py**: Defines a route for the `/ping` API, which is used for health checks.

4. **exercise2.py**: Contains the route for the `/authorize` API. This endpoint validates the key in the request header with a hardcoded secret.

5. **exercise3.py**: Implements CRUD operations on an employee table (empid, name) in SQLite. Each endpoint in this route requires authentication.

6. **run_tests.py**: Executes tests for each route. Ensure that the application is running before running the tests.

## Running the Application

To run the FastAPI application, execute the `run.py` file. This will start the server, and the API will be accessible at `http://localhost:8000/nvish`.

```bash
python run.py
```

## Testing

Tests are available in the `tests` directory. To run the tests, use the `run_tests.py` file.

```bash
python run_tests.py
```

## API Endpoints

Check http://localhost/nvish/docs for Swagger UI that has detailed list of enpoints and models.
## Dependencies

```bash
pip install -r requirements.txt