# DNS-Scanner

DNS-Scanner is a Python script to scan DNS information for a given website using the DNSDumpster service.

## Features

- Retrieves DNS information such as DNS servers, MX records, TXT records, and HOST records (A).
- Utilizes requests, BeautifulSoup, and fake_useragent libraries for web scraping.
- Outputs the obtained information in a structured format using pandas DataFrames.

## Prerequisites

- Python 3.x installed on your system.
- Required Python packages listed in `requirements.txt`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DNS-Scanner.git
   ```
2. Navigate to the script:
   ```bash
   cd DNS-Scanner
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Example Usage

1. Run the main.py script:
   ```bash
   python main.py
   ```
2. Insert target url:
   ```bash
   Masukkan url website yang ingin di scan: example.com
   ```
