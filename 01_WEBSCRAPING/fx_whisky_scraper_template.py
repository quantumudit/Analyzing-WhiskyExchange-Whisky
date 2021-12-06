from requests_html import HTMLSession
from datetime import datetime, timezone
import time

SESSION = HTMLSession()

all_whisky = []
all_page_links = []
all_product_links = []

def generate_page_links() -> None:
    """
    This function generate the page URLs that are used to scrape product links
    """
    
    url = 'https://www.thewhiskyexchange.com/c/35/japanese-whisky'
    response = SESSION.get(url)
    
    total_pages = int(response.html.find('nav.paging.js-paging', first=True).attrs.get('data-totalpages'))
    
    for pgno in range(1, total_pages+1):
        page_url = f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={pgno}'
        all_page_links.append(page_url)
    return

def scrape_product_links(page_url: str) -> None:
    """
    This function fetches the product URLs from the page and adds them to the 'all_product_links' list
    """
    
    response = SESSION.get(page_url)
    
    print('\n')
    print(f'Scraping Whisky from: {page_url}')
    
    product_urls = list(response.html.find('div.product-grid ul.product-grid__list', first=True).absolute_links)
    all_product_links.extend(product_urls)
    
    time.sleep(1)
    return

def scrape_product_details(product_url: str) -> None:
    """
    This function takes a product URL; scrapes all the required details and adds them to the 'all_whisky' list
    Args:
        url (str): The product URL string
    Returns:
        It returns nothing but, adds the scraped product details to the list
    """
    
    utc_timezone = timezone.utc
    current_utc_timestamp = datetime.now(utc_timezone).strftime('%d-%b-%Y %H:%M:%S')
    
    response = SESSION.get(product_url)
    
    print('\n')
    print(f'Scraping details from: {product_url}')

    whisky_link = product_url
    whisky_name = response.html.find('header h1.product-main__name', first=True).text
    whisky_image = response.html.find('div.product-main__image-container img', first=True).attrs.get('src')
    volume_alcoholpercent = response.html.find('header p.product-main__data', first=True).text
    whisky_price = response.html.find('p.product-action__price', first=True).text

    try:
        whisky_description = response.html.find('div.product-main__description p', first=True).text
    except:
        whisky_description = None
    
    try:
        stock_flag = response.html.find('p.product-action__stock-flag', first=True).text
    except:
        stock_flag = None

    try:
        whisky_type = response.html.find('header ul.product-main__meta li', first=True).text
    except:
        whisky_type = None
        
    try:
        rating = response.html.find('span.review-overview__rating span', first=True).text
        reviews_count = response.html.find('span.review-overview__count ', first=True).text.replace('\xa0',' ')
    except:
        rating = None
        reviews_count = None
        
    whisky_details = {
        'whisky_name': whisky_name,
        'whisky_type': whisky_type,
        'ratings': rating,
        'reviews_count': reviews_count,
        'volume_alcohol_percentage': volume_alcoholpercent,
        'stock_flag': stock_flag,
        'price': whisky_price,
        'description': whisky_description,
        'image_url': whisky_image,
        'whisky_link': whisky_link,
        'last_updated_at_UTC': current_utc_timestamp
    }
    
    all_whisky.append(whisky_details)
    
    time.sleep(1)
    return

# Testing the scraper template #
# ---------------------------- #

if __name__ == '__main__':
    
    generate_page_links()
    
    print('\n')
    print(f'Total pages to scrape: {len(all_page_links)}')
    print('\n')
    print(all_page_links)
    
    page_url = 'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg=1'
    scrape_product_links(page_url)
    
    print('\n')
    print(all_product_links)
    print('\n')
    print(f'Total products available: {len(all_product_links)}')
    
    product_url= 'https://www.thewhiskyexchange.com/p/29388/suntory-hibiki-harmony'
    scrape_product_details(product_url)
    print('\n')
    print(all_whisky)