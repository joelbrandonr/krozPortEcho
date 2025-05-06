# Kingdom of Kroz 2 - Group Echo

## Description

Python-based for of KINGDOM Of KROZ II.

## Producing an Executable

### Linux Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/joelbrandonr/krozPortEcho.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd krozPortEcho
    ```

3. **Create a virtual environment and activate it**:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

4. **Install the required dependencies**:

    ```bash
    pip install pygame numpy pyinstaller
    ```

5. **Build the standalone executable**:

    ```bash
    pyinstaller --onefile --add-data "PerfectDOSVGA437.ttf:." main.py
    ```

5. **Standalone executable will be located at `./dist/main`**

### Windows Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/joelbrandonr/krozPortEcho.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd krozPortEcho
    ```

3. **Create a virtual environment and activate it**:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

4. **Install the required dependencies**:

    ```bash
    pip install pygame numpy pyinstaller
    ```

5. **Build the standalone executable**:

    ```bash
    pyinstaller --onefile --add-data "PerfectDOSVGA437.ttf;." main.py
    ```

5. **Standalone executable will be located at `.\dist\main`**
