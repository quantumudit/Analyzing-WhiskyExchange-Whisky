from requests_html import HTMLSession
import time

SESSION = HTMLSession()

all_whisky = []
all_page_links = []
all_product_links = []

def extract_total_pages() -> int:
    """
    This function returns the total number of pages to scrape
    """
    
    url = 'https://www.thewhiskyexchange.com/c/35/japanese-whisky'
    response = SESSION.get(url)
    return int(response.html.find('nav.paging.js-paging', first=True).attrs.get('data-totalpages'))

def generate_page_links() -> None:
    """
    This function generate the page URLs that are used to scrape product links
    """
    
    total_pages = extract_total_pages()
    
    for pgno in range(1, total_pages+1):
        page_url = f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={pgno}'
        all_page_links.append(page_url)
    return

def scrape_product_links(url: str) -> None:
    """
    This function fetches the product URLs from the page and adds them to the 'all_product_links' list
    """
    
    response = SESSION.get(url)
    
    print('\n')
    print(f'Scraping Whisky from: {url}')
    
    product_urls = list(response.html.find('div.product-grid ul.product-grid__list', first=True).absolute_links)
    all_product_links.extend(product_urls)
    
    time.sleep(1)
    return

def scrape_product_details(url: str) -> None:
    """
    This function takes a product URL; scrapes all the required details and adds them to the 'all_whisky' list
    Args:
        url (str): The product URL string
    Returns:
        It returns nothing but, adds the scraped product details to the list
    """
    
    response = SESSION.get(url)
    
    print('\n')
    print(f'Scraping details from: {url}')

    whisky_link = url
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
        'whisky_link': whisky_link
    }
    
    all_whisky.append(whisky_details)
    
    time.sleep(1)
    return

if __name__ == '__main__':
    
    total_pages = extract_total_pages()
    print('\n')
    print(f'Total pages to scrape: {total_pages}')
    print('\n')
    
    generate_page_links()
    print(all_page_links)
    
    page_url = 'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg=1'
    scrape_product_links(page_url)
    
    print('\n')
    print(all_product_links)
    print('\n')
    print(f'Total products available: {len(all_product_links)}')
    
    whisky_link = 'https://www.thewhiskyexchange.com/p/54219/suntory-hibiki-harmony-2021-limited-edition-design'
    scrape_product_details(whisky_link)
    print('\n')

    print(all_whisky)