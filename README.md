# Simple WSGI Server in Python

This project implements a basic WSGI (Web Server Gateway Interface) server in Python using the built-in `socket` module. WSGI is a specification for a universal interface between web servers and web applications or frameworks for the Python programming language.

## Features

- Implements a WSGI server capable of serving WSGI applications.
- Supports basic HTTP request handling and response generation.
- Demonstrates handling of WSGI environment variables, request methods, and paths.
- Provides a simple example WSGI application (`app`) to demonstrate usage.

## Getting Started

To run the WSGI server, follow these steps:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Alan69/Simple_WSGI_Server.git
    ```

2. Navigate to the project directory:

    ```
    cd simple-wsgi-server
    ```

3. Run the server using Python:

    ```
    python wsgi_server.py
    ```

4. Access the WSGI application in your web browser at `http://127.0.0.1:8000/`.

## Usage

- Modify the `app` function in `wsgi_server.py` or create your own WSGI application.
- Customize the server configuration by modifying the `WSGIServer` class in `wsgi_server.py`.
- Add additional features or middleware to extend the functionality of the server.

## Dependencies

This project has no external dependencies beyond Python's built-in modules.


## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs, feature requests, or suggestions.
