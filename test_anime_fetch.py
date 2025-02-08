# import requests

# all_anime = []
# page = 1
# max_pages = 3  # Adjust based on how many you want (each page = 25 anime)

# while page <= max_pages:
#     response = requests.get(f"https://api.jikan.moe/v4/top/anime?page={page}")
#     data = response.json()
    
#     if 'data' in data:
#         all_anime.extend(data['data'])  # Store anime data
#     else:
#         break  # Stop if no data is returned

#     page += 1

# print(f"Fetched {len(all_anime)} anime.")
# test_anime_fetch.py
import requests

def fetch_top_anime(max_pages=3):
    """
    Fetches the top anime from the Jikan API.
    :param max_pages: Number of pages to fetch (each page has 25 anime)
    :return: A list of anime data
    """
    all_anime = []
    page = 1

    while page <= max_pages:
        response = requests.get(f"https://api.jikan.moe/v4/top/anime?page={page}")
        data = response.json()
        
        if 'data' in data:
            all_anime.extend(data['data'])  # Add anime data to list
        else:
            break  # Stop if no data is returned

        page += 1

    return all_anime
