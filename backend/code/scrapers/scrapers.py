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
    except Error:
        return 0


def roto_guru_scraper(service, month, day, year, file_dest):
    """Accesses the data table from SERVICE, with statistics
    from MONTH-DAY-YEAR and saves to FILE_DEST
    SERVICE will be fd for FanDuel and dk for DraftKings"""

    url = 'http://rotoguru1.com/cgi-bin/hyday.pl' +\
        f'?game={service}&mon={month}&day={day}&year={year}'

    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-2]
    df.columns = ('position player points salary team opponent ' +
                  'score minutes stats').split()

    # ensure that the rows are only
    df = df[df['position'].apply(lambda x: len(x) < 3)]
    df.to_csv(file_dest, index=False)


if __name__ == '__main__':
    sports_line_scrape('/tmp/basketball.csv')
    roto_guru_scraper('fd', 11, 21, 2018, '/tmp/fd_11-21-2018.csv')
