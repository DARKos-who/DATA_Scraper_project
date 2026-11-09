import requests
from bs4 import BeautifulSoup
import csv
import time

def universal_scraper():
    # INPUT THE USER'S URL 
    url = input("Enter the FULL website URL you wish to scrap (ex: https://en.wikipedia.org): ")
    
    if not url.startswith('http'):
        print("Error: URL must start with http:// or https://")
        return

    # DISGUISE THE SCRIPT AS A REGULAR BROWSER
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'
    }

    print(f"\nConnecting to {url}...")
    
    try:
        #1 FETCIHNG WEBSITE CONTENT
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        time.sleep(1.5) # Polite delay
        
        #2 Parse the HTML tree
        soup = BeautifulSoup(response.text, 'html.parser')
        dataset = []

        print("Extracting universal elements...")

        #3 Extract standard tags found on almost every website
        
        # Extract headings (h1, h2, h3)
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            clean_text = heading.text.strip()
            if clean_text: # Only save if it contains actual text
                dataset.append([heading.name.upper(), clean_text])

        # Extract paragraphs (p)
        for p in soup.find_all('p'):
            clean_text = p.text.strip()
            if clean_text:
                dataset.append(['Paragraph', clean_text])
                
        # Extract links (a)
        for link in soup.find_all('a', href=True):
            clean_text = link.text.strip()
            href = link['href']
            # Only save links that have text and point to a full web address
            if clean_text and href.startswith('http'):
                dataset.append(['Link', f"{clean_text} ({href})"])

        # 4. Save to a structured CSV for the data preparation team
        filename = 'RAW_scraped_data.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Element Type', 'Content']) # Column headers
            writer.writerows(dataset)
            
        print(f"\nSuccess! Scraped {len(dataset)} items.")
        print(f"Data saved to {filename}. ")

    except Exception as e:
        print(f"\n[!] Error: {e}")
        print("Note: Some websites aggressively block generic scrapers, or the URL might be invalid.")

if __name__ == "__main__":
    universal_scraper()