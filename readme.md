# Calculator Learning Project

This repository is a learning project focused on building and experimenting with Python-based calculators. The goal is to explore different ways to implement calculator logic, user interfaces, and testing in Python. The project includes both command-line and graphical calculator scripts, as well as automated tests.

## Technologies & Python Packages Used

- **Python 3.10+**
- **tkinter** (for GUI calculator)
- **pytest** (for automated testing)
- **GitHub Actions** (for CI/CD with pytest)
- **Standard Library** (no external dependencies except for pytest in tests)

## Project Structure

```
calculator-project/
├── calc.py                    # Main GUI calculator application (tkinter-based)
├── practice_scripts/          # Practice scripts directory
├── __tests__/                 # Test suite directory
├── .github/workflows/         # CI/CD configuration
│   └── test.yaml             # GitHub Actions workflow for automated testing
├── .gitignore                # Git ignore file
└── readme.md                 # This file
```

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jakekohl/calculator-project
   cd calculator-project
   ```

2. **Install Python (if not already installed):**
   - This project requires Python 3.10 or higher
   - Download from [python.org](https://www.python.org/downloads/) or by using HomeBrew `brew install python3` 

3. **Install pytest for running tests:**
   ```bash
   pip install pytest
   ```

## Running the Calculator Programs

### Main GUI Calculator (`calc.py`)

The main calculator is a graphical application built with tkinter that provides a full-featured calculator interface with a modern black theme.

**Features:**
- Graphical user interface (GUI)
- Basic operations: addition (+), subtraction (-), multiplication (*), division (/)
- Numbers 0-9
- Clear button (C) to reset
- Equals button (=) to calculate results
- Error handling for invalid expressions

**How To Run:**
```bash
# Run the main calculator
python calc.py
```

This will open a calculator window where you can click buttons to perform calculations.

## Running Tests

This project uses pytest for automated testing. The test suite includes basic unit tests for the main calculator operations.

### Running pytest:
```bash
# Basic Command
pytest

# No Verbose
pytest -v

# Output Coverage Report
pytest --cov
```

## Continuous Integration

This project includes a GitHub Actions workflow that automatically runs pytest whenever code is pushed to the repository or a pull request is created. The workflow configuration is located in `.github/workflows/test.yaml`.

## Practice Scripts

The Practice Scripts directory is a ad-hoc source of scripts to work through practice problems and try out ideas before committing to the main calculator project. Scripts here are not meant for production and are purely here to showcase thought processes or quick logic/functionality validations.

## Learning Objectives

This project demonstrates:
- Building GUI applications with tkinter
- Creating command-line interfaces in Python
- Writing unit tests with pytest
- Setting up CI/CD with GitHub Actions
- Python class-based programming (OOP)
- Event-driven programming with GUI callbacks
- Error handling and input validation

## License

This is a learning project for educational purposes.
