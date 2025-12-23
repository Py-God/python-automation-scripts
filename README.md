# Automation & Scripting Portfolio

A collection of Python scripts developed to automate repetitive tasks, handle file systems, scrape web data, and manipulate data formats. These projects demonstrate practical application of Python for task automation and efficiency.

## 🛠 Technologies Used
* **Language:** Python 3.x
* **Libraries:** `os`, `shutil`, `re`, `requests`, `bs4` (BeautifulSoup), `selenium`, `openpyxl`, `PyPDF2`, `csv`, `json`, `smtplib`.

---

## 📂 Project Descriptions

### 🌐 Web Scraping & Browser Automation
* **`mapIt.py`**: A command-line script that automatically launches the browser and opens Google Maps to an address provided via command line arguments or the clipboard.
* **`searchpypi.py`**: A script that performs a Google search for a query and automatically opens the top search result tabs in the browser, streamlining research workflow.
* **`downloadXkcd.py`**: An automated web scraper that iterates through the XKCD comic website, downloading and archiving every comic image to a local directory.
* **`selenium_login.py`**: Demonstrates browser automation using Selenium to programmatically log in to websites or control page elements (e.g., clicking buttons, filling forms).

### 🗄️ File System & OS Operations
* **`renameDates.py`**: Scans a directory for files with American-style dates (MM-DD-YYYY) and bulk renames them to European-style dates (DD-MM-YYYY) using Regular Expressions (RegEx) and `shutil`.
* **`backupToZip.py`**: An archiving tool that walks through a folder tree and backs up the entire contents into a ZIP file, utilizing versioned filenames to prevent overwriting.
* **`selectiveCopy.py`**: A utility script that walks through a directory tree and searches for files with a specific extension (e.g., `.jpg`, `.pdf`) and copies them to a new folder.
* **`mcb.pyw` (Multiclipboard)**: A clipboard manager that saves multiple pieces of text to a shelf file and allows users to load them back to the clipboard via keywords.

### 📊 Data Processing (Excel, PDF, CSV, JSON)
* **`excelSpreadsheet.py`**: Demonstrates programmatic control of Excel files using `openpyxl`. Can update specific cells across thousands of rows instantly.
* **`combinePdfs.py`**: A PDF manipulation tool that takes all PDF files in the current directory and merges them into a single document using `PyPDF2`.
* **`removeCsvHeader.py`**: Batch processes hundreds of CSV files to remove the header row from each, streamlining data preparation for database ingestion.
* **`getOpenWeather.py`**: A script that interacts with the OpenWeatherMap API. It fetches weather data in JSON format, parses it, and prints the current forecast for a specific city.

### 🔍 Text Processing & RegEx
* **`phoneAndEmail.py`**: A powerful text scraper that finds all phone numbers and email addresses on the clipboard (or in a document) using complex Regular Expressions and formats them into a clean list.
* **`bulletPointAdder.py`**: Automates text formatting by taking text from the clipboard, adding a bullet point to the start of each line, and returning it to the clipboard.

---

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
