# MLOps Lab 1 - Temperature Converter

This lab focuses on creating a temperature conversion module with unit tests using pytest and unittest frameworks, and implementing GitHub Actions for continuous integration.

## Setting up the lab
1. Clone the repository and navigate to the project directory.
2. Create a virtual environment (e.g. **lab_01**):
   ```bash
   python -m venv lab_01
   ```
3. Activate the environment:
   - **macOS/Linux:** `source lab_01/bin/activate`
   - **Windows:** `lab_01\Scripts\activate`
4. Install the required packages using `pip install -r requirements.txt`.

### Project structure
```
MLOps-GithubLab1/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml
│       └── unittest_action.yml
├── data/
├── src/
│   ├── __init__.py
│   └── temperature_converter.py
├── test/
│   ├── __init__.py
│   ├── test_pytest.py
│   └── test_unittest.py
├── README.md
└── requirements.txt
```

## Running the Lab
1. To test the temperature converter module manually:
   ```bash
   python -c "from src import temperature_converter; print('Import successful!')"
   ```

2. To run pytest tests:
   ```bash
   pytest test/test_pytest.py -v
   ```

3. To run unittest tests:
   ```bash
   python -m unittest test.test_unittest -v
   ```

4. GitHub Actions will automatically run both test suites when you push to the main branch.

## Temperature Conversion Functions
The module provides functions to convert between:
- Celsius to Fahrenheit
- Fahrenheit to Celsius  
- Celsius to Kelvin
- Kelvin to Celsius

All functions include error handling for invalid inputs and temperatures below absolute zero.
