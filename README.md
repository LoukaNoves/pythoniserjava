# PythoniserJava

PythoniserJava is a project that allows you to parse Python code, convert it to Java code, and then compile and run the Java code. This approach leverages Java's performance for executing the logic defined in Python.

## Project Structure

- `parser.py`: Contains functions to parse Python code into an Abstract Syntax Tree (AST) and handle different AST nodes.
- `generator.py`: Contains functions to generate Java code from the parsed Python AST.
- `compiler.py`: Contains functions to compile and run the generated Java code.
- `mainpythoniser.py`: The main script that ties everything together.
- `tests/test_parser.py`: Unit tests for the parser module.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pythoniserjava.git
    cd pythoniserjava
    ```

2. Ensure you have Python and Java installed on your system.

## Usage

1. Write your Python code in the `mainpythoniser.py` file:
    ```python
    python_code = """
    def add_numbers(a, b):
        return a + b

    result = add_numbers(3, 4)
    print(result)
    """
    ```

2. Run the main script:
    ```sh
    python mainpythoniser.py
    ```

3. The script will:
    - Parse the Python code into an AST.
    - Generate Java code from the parsed AST.
    - Compile and run the generated Java code.

## Running Tests

To run the unit tests for the parser module, use the following command:
```sh
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
