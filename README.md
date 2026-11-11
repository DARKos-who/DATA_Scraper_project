DATA Scraper Project

## Installation

Clone the repository, then create a Python environment in the project folder:

    git clone https://github.com/DARKos-who/DATA_Scraper_project.git
    cd DATA_Scraper_project
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Before every new work session in this folder:

    git pull

## Data Cleaning

Open `data_cleaning.ipynb` in VS Code, select the Python kernel from `.venv`, then run the cells in order.

- `RAW_scraped_data.csv`
- `cleaned_data.csv`
- `content_frequencies.csv`

Repeated lines remain in `cleaned_data.csv`: they may represent multiple appearances of the same text on the page. Some merged/pasted texts come from the HTML extraction and are not corrected automatically.

The scraper collects headings, paragraphs, and links from a page. It does not create structured product sheets with prices and categories.

**Warning:** re-running `Scraper.py` from the project folder replaces `RAW_scraped_data.csv`.

## Data Visualization

Open `visualisation_des_donnees.ipynb` in VS Code, select the Python kernel from `.venv`, and run the cells in order. The notebook loads `cleaned_data.csv` and presents six charts created with Matplotlib and Seaborn: element types, text length, comparison by type, repeated texts, words in H3 titles, and link domains. Each chart is accompanied by an interpretation.

The data describes the textual content of a page at a given moment. It contains no sales, structured prices, or reliable product categories.
