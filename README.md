# CodeCure
# CodeCure - Code Analysis Tool

CodeCure is a web-based tool that allows users to analyze code snippets in various programming languages and save or delete these snippets for later use. The tool provides code analysis with a focus on best practices, potential improvements, and detailed feedback.

## Features

- **Code Analysis**: Analyze code snippets in Python, HTML, CSS, and JavaScript.
- **Snippet Management**: Save and delete code snippets.
- **Responsive Design**: Mobile-friendly interface with a collapsible menu.
- **User-Friendly UI**: Simple and clean interface using Tailwind CSS and Flowbite.

## Project Structure

- **`static/css/styles.css`**: Custom and Tailwind CSS styles.
- **`static/js/script.js`**: JavaScript for handling user interactions and snippet management.
- **`templates/home.html`**: Main HTML page for code analysis and snippet management.
- **`templates/partials/_header.html`**: Header template including both desktop and mobile navigation.
- **`app_init.py`**: Initializes the Flask application.
- **`main.py`**: Main application entry point and code analysis logic.
- **`routes.py`**: Defines application routes.

## Installation

To get started with CodeCure, follow these steps:

 **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/codecure.git
   cd codecure

Usage

Analyze Code: Enter code in the textarea, select the programming language, and click "Analyze Code" to get a detailed analysis.
Save Snippet: Click "Save Snippet" to save the current code for future use.
Load Saved Snippet: Use the dropdown to select and load a previously saved snippet.
Delete Snippet: Select a saved snippet and click "Delete Snippet" to remove it.
Configuration

Database: Currently, no database is configured. You can integrate one by modifying app_init.py.
Logging: Logs are configured in main.py for debugging and monitoring.
Development

Update Styles: Modify static/css/styles.css to customize the look and feel.
Enhance JavaScript: Edit static/js/script.js to add or improve functionality.
Expand Analysis: Add new analysis functions in main.py to support more languages or features
