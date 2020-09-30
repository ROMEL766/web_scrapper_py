import argparse
import csv
import datetime
import logging
logging.basicConfig(level=logging.INFO)

import news_page_objects as news
from common import config

logger = logging.getLogger(__name__)

def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info(f'Beginning scrape for {host}')
    homepage = news.HomePage(news_site_uid, host)

    for link in homepage.article_links:
        print(link)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    news_sites_choices = list(config() ['news_sites'].keys())
    parser.add_argument('news_site',
    articles = []
    for link in homepage.article_links:
        #print(link)
        article = _fetch_article(news_site_uid, host, link)

        if article:
            logger.info('Article fetched!!')
            articles.append(articles)
            print(article.title)

    print(len(articles))


def _save_articles(news_site_uid, articles):
    now = datetime.datetime.now().strftime('%Y_%n_%d')
    out_file_name = f'{news_site_uid}_{now}_article.csv'

    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))

    with open(out_file_name, mode='w+') as f:
        writer = csv.writer(r)
        writer.writerow(csv_headers)
        
        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)
                                    
                        help='The news site that you want to scrape',
                        type=str,
                        choices=news_sites_choices)
    
    


args = parser.parse_args()
_news_scraper(args.news_site)
