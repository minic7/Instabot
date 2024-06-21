# Instabot

Instabot is a Python-based automation script that interacts with Instagram's web interface to perform tasks such as logging in, searching for profiles or tags, following accounts, and more. This script utilizes Selenium WebDriver to automate browser actions.

## Features

- Open Instagram login page and log in with provided credentials.
- Navigate through Instagram UI to perform actions such as searching for users and hashtags.
- Follow specified accounts.

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver compatible with your Chrome browser version
- Selenium package

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/instabot.git
    cd instabot
    ```

2. **Install the required Python packages:**

    ```sh
    pip install selenium
    ```

3. **Download and install ChromeDriver:**

    - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Make sure ChromeDriver is in your system's PATH or place it in the project directory.

## Usage

1. **Update login credentials:**

    Modify the script to include your Instagram username and password:

    ```python
    text_box.send_keys('your_username')
    password.send_keys('your_password')
    ```

2. **Run the script:**

    Execute the script using Python:

    ```sh
    python instabot.py
    ```

## Script Overview

The script performs the following steps:

1. Opens the Instagram login page.
2. Logs in with provided credentials.
3. Handles pop-ups such as "Save Login Info" and "Turn on Notifications".
4. Performs a search for specified keywords.
5. Extracts and prints search results.
6. Navigates to a specified profile and follows the account if not already followed.

## Error Handling

The script includes error handling for common Selenium exceptions:

- `NoSuchElementException`: Raised when an element is not found in the DOM.
- `ElementNotInteractableException`: Raised when an element is present in the DOM but cannot be interacted with.
- `StaleElementReferenceException`: Raised when an element is no longer attached to the DOM.
- `TimeoutException`: Raised when a command does not complete in enough time.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.


## Acknowledgements

- [Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

