import googlemaps #pip install googlemaps
import pandas as pd #pip install pandas
import time
from pprint import pprint
from openpyxl.workbook import Workbook
from openpyxl.utils import get_column_letter

# wb = Workbook()
# ws1 = wb.active
# ws1.title = "range names"

def miles_to_meter(miles):
    try:
        return miles * 1_609.344
    except:
        return 0

API_KEY = open('API_KEY.txt', 'r').read()
map_client = googlemaps.Client(API_KEY)

address = 'ศูนย์ดูแลผู้สูงอายุและผู้ป่วย บ้านลลิสา เนอร์สซิ่งโฮมลำปาง'
location = (18.32438350342902, 99.53261468281667)
search_string = 'elder'
distance = miles_to_meter(30)
business_list = []

response = map_client.places_nearby(
    location=location,
    keyword=search_string,
    name='elder',
    radius=distance,
)
pprint(response)
business_list.extend(response.get('results'))
next_page_token = response.get('next_page_token')

while next_page_token:
    time.sleep(2)        
    response = map_client.places_nearby(
        location=location,
        keyword=search_string,
        name='elder',
        radius=distance,
        page_token=next_page_token
    )

    business_list.extend(reponse.get('results'))
    next_page_token = response.get('next_page_token')

df = pd.DataFrame(business_list) 
df['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']
df.to_excel('{0}.xlsx'.format(search_string), index=False)
wb.save('{0}.xlsx')