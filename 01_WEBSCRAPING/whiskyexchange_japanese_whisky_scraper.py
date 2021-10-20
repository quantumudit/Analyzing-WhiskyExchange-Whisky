import pandas as pd
import datetime
import pyfiglet
from concurrent.futures import ThreadPoolExecutor
from fx_whiskyexchange_jap_whisky_scraper_template import *

def extract_all_product_links() -> None:
    """
    This function loops though each of the page and scrapes all the different whisky links
    """
    
    with ThreadPoolExecutor() as executor:
        executor.map(scrape_product_links, all_page_links)
    return
    
def scrape_all_product_details() -> None:
    """
    This function loops through all the individual whisky links and scrapes the details; that are get added to 'all_whisky' list
    """
    
    with ThreadPoolExecutor() as executor:
        executor.map(scrape_product_details, all_product_links)
    return

def load_data() -> None:
    """
    This function loads the scraped data into a CSV file
    """
    
    whisky_df = pd.DataFrame(all_whisky)
    whisky_df.to_csv('whiskyexchange_japanese_whisky_data.csv', index=False)

if __name__ == '__main__':
    
    scraper_title = "THE WHISKY EXCHANGE - JAPANESE WHISKY COLLECTOR"
    ascii_art_title = pyfiglet.figlet_format(scraper_title, font='small')
    
    start_time = datetime.datetime.now()
    
    print('\n\n')
    print(ascii_art_title)
    print('Collecting Japanese Whisky...')
    
    generate_page_links()
    
    print(f'Total Pages to scrape:{len(all_page_links)}')
    print('Gathering all whisky links to scrape...')
    
    extract_all_product_links()
    
    print(f'Total whisky to scrape: {len(all_product_links)}')
    print('\n')
    print('Scraping whisky details from each whisky link...')
    
    scrape_all_product_details()
    
    end_time = datetime.datetime.now()
    scraping_time = end_time - start_time
    
    print('\n')
    print('All Whisky Collected...')
    print(f'Time spent on scraping: {scraping_time}')
    print(f'Total whisky collected: {len(all_whisky)}')
    print('\n')
    print('Loading data into CSV...')
    
    load_data()
    
    print('Data Exported to CSV...')
    print('Webscraping completed !!!')

