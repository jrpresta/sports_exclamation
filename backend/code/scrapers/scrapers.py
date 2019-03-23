import wget
import sites_for_scraping
import pandas as pd
import requests

def sports_line_scrape(file_dest):
    """Downloads the csv stored at the url indiciated
    in the sites_for_scraping script and saves it to FILE_DEST"""
    url = sites_for_scraping.sports_line_url
    try:
        wget.download(url, file_dest)
        return 1
    except:
        return 0


def roto_guru_scraper(service, month, day, year, file_dest):
    """Accesses the data table from SERVICE, with statistics
    from MONTH-DAY-YEAR and saves to FILE_DEST"""
    url = 'http://rotoguru1.com/cgi-bin/hyday.pl' +\
         f'?game={service}&mon={month}&day={day}&year={year}'

    print(url)
    html = requests.get(url).content
    # TODO: Clean up the rows that have the "jump to"
    df_list = pd.read_html(html)
    df = df_list[-2]
    df.to_csv(file_dest, index=False)

if __name__ == '__main__':
    # sports_line_scrape('/tmp/basketball.csv')
    roto_guru_scraper('fd', 11, 21, 2018, '/tmp/roto.csv')
