import wget
import sites_for_scraping

def sports_line_scrape(file_dest):
    """Downloads the csv stored at the url indiciated
    in the sites_for_scraping script and saves it to FILE_DEST"""
    url = sites_for_scraping.sports_line_url
    try:
        wget.download(url, file_dest)
        return 1
    except:
        return 0


if __name__ == '__main__':
    sports_line_scrape('/tmp/basketball.csv')
