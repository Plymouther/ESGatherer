# ESGatherer

## About

**ESGatherer** is a Python project designed for learning web scraping techniques. It allows users to scrape ESG (Environmental, Social, and Governance) and sustainability reports from websites by searching for specific keywords such as "ESG", "Sustainability", "Annual Report", and their German equivalents like "Nachhaltigkeit". This project aims to help users collect and store ESG-related data from various websites into a CSV file for further analysis.

This project is a work in progress and is being actively developed. While it is functional, there are several improvements and new features that are being planned.

## Features

- **Scrape ESG Reports**: Allows users to scrape websites for ESG, sustainability, and annual reports.
- **CSV Output**: Stores the scraped reports in a CSV file (`sustainability_reports.csv`), including the title and URL of each report.
- **Error Handling**: Built-in retry mechanism to handle connection issues and website unavailability.
- **Extra Window for Results**: After scraping, an additional window displays the results before clearing them from the CSV file when the window is closed.

## What I Learned

- **Web Scraping**: How to use Python libraries such as `requests` and `BeautifulSoup` to scrape data from websites.
- **CSV Handling**: Writing to and modifying CSV files for storing scraped data.
- **Error Handling**: Implementing retry mechanisms to handle common issues like connection failures or timeouts.
- **GUI Interaction**: Displaying results in a new window and handling user interaction with the window.

## Installation

1. **Install the required dependencies**:
   ```bash
  You will need requests, beautifulsoup4, and tkinter for the GUI. Install them using pip:
  pip install requests beautifulsoup4 tk

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Plymouther/WebStetho.git
   cd WebStetho

## Usage

  **Run the script**:
  python3 main.py
  
  Enter Website URLs: You will be prompted to enter a list of URLs (comma-separated). You can enter them in the format https://google.com, https://github.com, or just google.com (the protocol will be added automatically).
  Scrape Reports: The script will scrape the websites and look for keywords related to ESG and sustainability reports. The results will be saved in a CSV file and displayed in a new window.
  Close the Window: When you close the results window, the CSV file will be cleared.
  
## Example

  When you run the program, it might look something like this:

Enter the website URLs separated by commas: https://example.com, https://anotherexample.com
Scraping https://example.com...
Found reports on https://example.com and saved to CSV.
Scraping https://anotherexample.com...
Found reports on https://anotherexample.com and saved to CSV.

## Dependencies


- **requests**: For making HTTP requests.
- **beautifulsoup4**: For parsing HTML content and scraping data.
- **tkinter**: For creating the GUI window to display the results.
  
## License

Open Source, feel Free to use as you desire

## Contribution

Feel free to fork this repository, open issues, and submit pull requests. Contributions are welcome!

## Author

Emin Gani #ESGatherer
