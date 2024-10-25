# Midterm-Project: Interactive Command-Line Calculator

## Project Overview

The Midterm Calculator Project is an interactive command-line calculator designed to facilitate basic arithmetic operations while maintaining a comprehensive history of calculations. The project is built using Python and it incorporates essential programming concepts such as object-oriented design, error handling, and data management with the Pandas library. 

## Goals and Objectives
- **User-Friendly Interface**: Provide an intuitive command-line interface for easy input and result viewing.
- **Support for Basic Operations**: Implement fundamental arithmetic functions, including addition, subtraction, multiplication, and division, ensuring accuracy and reliability.
- **History Management**: Develop a history management system using the HistoryManager class, allowing users to review and track past calculations in a structured format.
- **Logging and Error Handling**: Implement logging functionality to capture operations and potential errors, enhancing transparency and ease of debugging.
- **Code Quality and Testing**: Conduct regular Pylint checks and comprehensive testing using Pytest to ensure efficiency and bug-free operation.
## Setup
- Install python
- Clone the repository
- Create a Virtual Environment
     -python -m venv venv
- Activate Virtual Environment
     - source venv/bin/activate
- Install Dependencies
     - pip install -r requirements.txt
- Run the Application
  - python3 midterm_calculator/main.py  
## Usage Examples
Basic Operations
- Addition:
    add 5 3
    Output: Result: 8
- Subtraction:
    subtract 10 4
    Output: Result: 6
- Multiplication:
    multiply 7 2
    Output: Result: 14
- Division:
    divide 12 3
    Output: Result: 4

- View History:
    history
    Output: Displays previous calculations.

- Exit:
    exit
## Planning and Design
This project utilizes the Command Pattern and Read-Eval-Print Loop (REPL) principles to create a structured and interactive user experience. The Command Pattern encapsulates each arithmetic operation as an object, facilitating easy addition and modification of commands. The REPL approach allows users to enter commands in a continuous loop until they choose to exit, providing immediate feedback for each calculation. The code is structured into modular components, with a Calculator class for arithmetic operations and a HistoryManager class logging past calculations using a Pandas DataFrame. A flowchart illustrates the architecture, highlighting interactions between the main application loop, command handling, and history management.

## Development Process
The development environment was set up using Python as the primary programming language, along with libraries such as Pandas for data management and Pylint for code quality checks. The first step involved installing Python and creating a virtual environment to organize project dependencies. After activating the virtual environment, I installed the necessary packages listed in the requirements.txt file.

Implementation commenced with creating the fundamental calculator functions for addition, subtraction, multiplication, and division. The Command Pattern was integrated to manage arithmetic operations as distinct command objects, facilitating future application expansion. A REPL (Read-Eval-Print Loop) interface was developed for user interaction, providing immediate feedback. Additionally, dynamic plugin loading was incorporated to accommodate potential new functionalities. Tests were conducted using Pytest to verify the accuracy and functionality of each feature.

Throughout the implementation process, challenges arose, such as ensuring compatibility among various components and effectively managing user input. These obstacles were addressed through iterative testing and the use of debugging tools to promptly identify and resolve issues.

## Testing Process
I structured the testing process into unit tests for individual functions and integration tests for overall application functionality. Using Pytest facilitated easy test execution and result interpretation. To achieve 100% coverage, I wrote tests for all calculator operations, including various edge cases. Running the tests was straightforward—executing `pytest` in the terminal provided detailed output and coverage reports. During testing, I encountered bugs, including issues with division handling in specific scenarios. I addressed these by adjusting the code and adding more test cases to cover those edge cases, ensuring the application's overall correctness.

## Finalizing the project
To finalize the project, I conducted a thorough code refactoring to enhance readability and maintainability. Comprehensive testing was performed to ensure that all features functioned as intended, addressing any bugs or issues identified during development. This process solidified the application's stability and reliability, preparing it for deployment and use.

## Conclusion
Throughout this project, I gained valuable insights into implementing design patterns and managing data effectively. The experience of creating an interactive command-line calculator deepened my understanding of Python programming, software architecture, and testing methodologies. Reflecting on the project, I recognize the importance of structured planning and iterative testing in developing robust applications. This project not only strengthened my coding skills but also enhanced my ability to tackle challenges methodically.
