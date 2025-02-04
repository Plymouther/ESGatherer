import requests
from bs4 import BeautifulSoup
import time
import csv
import tkinter as tk
from tkinter import messagebox
import os

# Function to handle the connection retry logic
def get_with_retry(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    return None  # Return None if the request fails after retries

# Function to scrape the reports
def scrape_reports(url):
    response = get_with_retry(url)
    
    if not response:
        print(f"Skipping {url}: Unable to retrieve the website.")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Try to find ESG or sustainability report links
    reports = []
    for item in soup.find_all(['a', 'div'], text=True):
        if 'esg' in item.get_text().lower() or 'sustainability' in item.get_text().lower() or 'annual report' in item.get_text().lower() or 'nachhaltigkeit' in item.get_text().lower() or 'nachhaltigkeits' in item.get_text().lower() or 'bericht' in item.get_text().lower():
            link = item.get('href')
            if link and link.startswith('http'):
                reports.append({'title': item.get_text(), 'link': link})

    return reports

# Function to write the found reports to a CSV file
def write_to_csv(reports):
    with open('sustainability_reports.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # If the file is empty, write the header
        file.seek(0, 2)  # Move to end of file
        if file.tell() == 0:
            writer.writerow(['Title', 'Link'])
        
        for report in reports:
            writer.writerow([report['title'], report['link']])

# Function to clear the CSV file
def clear_csv():
    if os.path.exists('sustainability_reports.csv'):
        open('sustainability_reports.csv', 'w').close()  # This will clear the content of the file

# Function to show the results in a new window
def show_results_window():
    window = tk.Tk()
    window.title("ESG Sustainability Reports")

    text = tk.Text(window, wrap='word', height=20, width=80)
    text.pack(expand=True, fill='both')

    # Read the CSV content and show it in the window
    try:
        with open('sustainability_reports.csv', 'r', encoding='utf-8') as file:
            csv_content = file.read()
            text.insert(tk.END, csv_content)
    except FileNotFoundError:
        text.insert(tk.END, "No reports found yet.")

    # Function to handle window close event
    def on_close():
        clear_csv()  # Clear the CSV file when the window is closed
        window.destroy()

    # Bind the window close event to the function
    window.protocol("WM_DELETE_WINDOW", on_close)

    window.mainloop()

# Main function
def main():
    # Get multiple URLs as input, split by commas
    websites = input("Enter the website URLs separated by commas: ").split(',')
    
    for website in websites:
        website = website.strip()  # Remove any leading/trailing spaces
        if not website.startswith('http'):
            website = 'https://' + website  # Add https:// if missing
        print(f"Scraping {website}...")
        
        reports = scrape_reports(website)
        
        if reports:
            write_to_csv(reports)
            print(f"Found reports on {website} and saved to CSV.")
        else:
            print(f"No ESG/Sustainability reports found on {website}.")

    # Show the results in a new window after scraping
    show_results_window()

if __name__ == "__main__":
    main()
