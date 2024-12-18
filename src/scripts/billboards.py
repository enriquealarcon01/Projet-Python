from lxml import etree
from urllib.request import urlopen
import pandas as pd
import re

# Billboard Top 200 URL
URL = "https://www.billboard.com/charts/billboard-global-200/"

def get_billboard_hits():
    response = urlopen(URL)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)

    xpath_song = f'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[1]/h3'
    xpath_artist = f'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[1]/span'
    song_elements = tree.xpath(xpath_song)
    artist_elements = tree.xpath(xpath_artist)

    dataframe = pd.DataFrame(columns=['Song', 'Artist'])
    for i in range(200):
        song_text = song_elements[i].text.strip().replace('\n', ' ').replace('  ', ' ')
        artist_text = artist_elements[i].text.strip().replace('\n', ' ').replace('  ', ' ')
        artist_text = re.split(r' & | Featuring ', artist_text)
        if 'ROSE' in artist_text:
            artist_text[artist_text.index('ROSE')] = 'Rosé'
        dataframe.loc[i] = [song_text, artist_text]
        
    return dataframe