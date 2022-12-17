import colorama
import requests
import pandas as pd
import dash_trich_components as dtc
import json


def request_map_data():
    df = 'This will be a dataframe'

    try:
        req = requests.get('https://pipinstallpython.pythonanywhere.com/map/api/', timeout=5)

        if req.status_code == 200:
            df = pd.DataFrame(req.json())
            df = df.drop(['description'], axis=1)

            # Print the data
            # print_terminal_screen()

            # Remove Not Active On Map
            for index, test_active, name in zip(df.index, df['active_on_map'], df['name']):

                if test_active == False:
                    df.pop(index)
                    print(colorama.Fore.RED + f"{name} was removed from the map.")



    except:
        sample_data = {"pk": {"0": 8, "1": 9, "2": 13, "3": 3, "4": 4},
                       "active_on_map": {"0": True, "1": True, "2": True, "3": True, "4": True},
                       "name": {"0": "Camp Aranzazo", "1": "Chamber of Comerce", "2": "JJ's Cafe",
                                "3": "Panjo's Pizza & Pasta", "4": "KLADS Boat Storage"},
                       "m_type": {"0": "nonprofit", "1": "stores", "2": "restaurants", "3": "restaurants",
                                  "4": "vacation_rental"},
                       "picture": {"0": "\/media\/map_location_pictures\/2022\/08\/02\/camp_aranzazu.jpeg",
                                   "1": "\/media\/map_location_pictures\/2022\/08\/02\/chamber_of_comerce.jpeg",
                                   "2": "\/media\/map_location_pictures\/2022\/08\/02\/jjscafee.jpg",
                                   "3": "\/media\/map_location_pictures\/2022\/08\/02\/panjosRockport.jpg",
                                   "4": "\/media\/map_location_pictures\/2022\/08\/02\/Klads.jpeg"},
                       "phone_number": {"0": "", "1": "", "2": "", "3": "", "4": "3612303223"},
                       "lat": {"0": 28.113, "1": 28.02618, "2": 28.04631, "3": 28.05503, "4": 28.16364},
                       "lon": {"0": -97.04, "1": -97.05021, "2": -97.044, "3": -97.04046, "4": -96.99853},
                       "address": {"0": "", "1": "", "2": "", "3": "", "4": ""},
                       "city": {"0": "Rockport", "1": "Rockport", "2": "Rockport", "3": "Rockport", "4": "Rockport"},
                       "state": {"0": "Texas", "1": "Texas", "2": "Texas", "3": "Texas", "4": "Texas"},
                       "zip_code": {"0": 78382, "1": 78382, "2": 78382, "3": 78382, "4": 78382},
                       "url": {"0": "", "1": "", "2": "https:\/\/www.yelp.com\/biz\/jjs-cafe-rockport", "3": "",
                               "4": ""}, "author": {"0": 1, "1": 1, "2": 1, "3": 1, "4": 1},
                       "QR_image": {"0": "\/media\/QR_Location\/2022\/08\/02\/qr-_edY2l4T.png",
                                    "1": "\/media\/QR_Location\/2022\/08\/02\/qr-_TnPDqKi.png",
                                    "2": "\/media\/QR_Location\/2022\/08\/02\/qr-https%3A\/www.yelp.com\/biz\/jjs-cafe-rockport.png",
                                    "3": "\/media\/QR_Location\/2022\/08\/02\/qr-_MHLGlhc.png",
                                    "4": "\/media\/QR_Location\/2022\/08\/02\/qr-_qm1uNhq.png"},
                       "date_created": {"0": "2022-08-02", "1": "2022-08-02", "2": "2022-08-02", "3": "2022-08-02",
                                        "4": "2022-08-02"},
                       "icon_data": {"0": "https:\/\/cdn-icons-png.flaticon.com\/512\/1043\/1043927.png",
                                     "1": "https:\/\/cdn-icons-png.flaticon.com\/512\/2830\/2830346.png",
                                     "2": "https:\/\/cdn-icons-png.flaticon.com\/512\/926\/926292.png",
                                     "3": "https:\/\/cdn-icons-png.flaticon.com\/512\/7836\/7836772.png",
                                     "4": "https:\/\/cdn-icons-png.flaticon.com\/512\/754\/754822.png"},
                       "width": {"0": 242, "1": 242, "2": 242, "3": 242, "4": 242},
                       "height": {"0": 242, "1": 242, "2": 242, "3": 242, "4": 242},
                       "anchorY": {"0": 242, "1": 242, "2": 242, "3": 242, "4": 242}}

        print(colorama.Fore.RED + f"Error Loading API Data: Using Backup Data")
        df = pd.DataFrame(sample_data)

        print(colorama.Fore.LIGHTYELLOW_EX + "Server Calls:" + colorama.Fore.RESET + f" {df.columns.values}")
        print(colorama.Fore.LIGHTYELLOW_EX + 'SampleData:')
        print(colorama.Fore.RESET + f"{df.head()}")
        print(colorama.Fore.LIGHTYELLOW_EX + f'{df.index}')

    return df


if __name__ == '__main__':
    data = request_map_data()