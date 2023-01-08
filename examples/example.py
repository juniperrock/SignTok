import requests

"""
Example using Python requests
"""

# You can replace this with your signing instance
SIGNING_URL = 'http://localhost:5000/signature'

EXAMPLE_URL = 'https://m.tiktok.com/api/post/item_list?count=30&id=6941611380308870149&cursor=0&type=1&secUid=MS4wLjABAAAA7DfOn_jwWM7Rscrl2SGPW06eYI0bUDXRoRoTcSpw_Bsndydsbk8zH3tZe2Tz9FoJ&sourceType=8&appId=1233&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-us&browser_name=Mozilla&browser_online=1&browser_platform=iPhone&browser_version=Mozilla%252F5.0%2B%2528Macintosh%253B%2BIntel%2BMac%2BOS%2BX%2B10_15_6%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F98.0.4758.109%2BSafari%252F537.36&channel=tiktok_web&cookie_enabled=1&device_platform=web_mobile&focus_state=1&history_len=3&is_fullscreen=0&is_page_visible=1&os=ios&priority_region=&referer=&region=us&screen_width=1920&screen_height=1080&timezone_name=America%2FChicago&webcast_language=en&device_id=9632257621121311443'

r = requests.post(SIGNING_URL, data=EXAMPLE_URL)

if r.ok:
    r_json = r.json()
    print(r_json['data']['signed_url'])
