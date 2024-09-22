import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
import re

def data_cleaning():
    df = pd.read_excel("/Users/bowiechuang/Documents/GitHub/DS-Project-1/SB_Hotel_Project/Expedia_hotel_dataset.xlsx")
    df = df.drop('hotel_details', axis = 1)

    hotel_list = [
    "Hotel Milo Santa Barbara", "Motel 6 Santa Barbara, CA - Beach", "Avania Inn of Santa Barbara", 
    "West Beach Inn, a Coast Hotel", "Sandpiper Lodge", "Riviera Beach House", 
    "Drift Santa Barbara, a Member of Design Hotels", "Hyatt Place Santa Barbara", 
    "Best Western Plus Santa Barbara", "Ramada by Wyndham Santa Barbara", "Hotel Californian", 
    "Inn By The Harbor", "Mason Beach Inn", "Lavender Inn by the Sea", "The Eagle Inn", 
    "El Encanto, A Belmond Hotel, Santa Barbara", "Brisas del Mar, Inn at the Beach", 
    "Residence Inn by Marriott Santa Barbara Goleta", "La Playa Inn", "Ojai Valley Inn", 
    "Hotel Santa Barbara", "The Franciscan Hotel", "Mar Monte Hotel, in The Unbound Collection by Hyatt", 
    "The Upham Hotel", "Harbor View Inn", "Wine Valley Inn", "The Inn at Mattei's Tavern", 
    "Simpson House Inn", "Cheshire Cat Inn & Cottages", "Montecito Inn", 
    "Courtyard Santa Barbara Goleta", "Harbor House Inn", "Hilton Santa Barbara Beachfront Resort", 
    "Best Western Plus Pepper Tree Inn", "Marina Beach Motel", "Bath Street Inn", "Lemon Tree Inn", 
    "Castillo Inn at the Beach", "Cliff House Inn On The Ocean", "Casa Jardin", "Casa De La Vina", 
    "Rosewood Miramar Beach", "New Haven Inn", "Agave Inn", "Pacific Crest Hotel Santa Barbara", 
    "The Inn at East Beach", "Hamlet Inn", "Kimpton Canary Hotel, an IHG Hotel", 
    "The Leta Santa Barbara Goleta, Tapestry Collection by Hilton", "Sideways Inn", 
    "Hotel Corque", "Vinland Hotel and Lounge", "Palihouse Santa Barbara", "Oakridge Inn", 
    "Extended Stay America Suites Santa Barbara Calle Real", "Secret Garden Inn and Cottages", 
    "Santa Barbara Mission Studio", "Santa Ynez Valley Marriott", "Motel 6 Goleta, CA - Santa Barbara", 
    "King Frederik Inn", "The Winston Solvang", "Hotel Hygge", "Best Western Plus South Coast Inn", 
    "The M Solvang", "Holiday Inn Express Hotel & Suites Carpinteria", "The Ritz-Carlton Bacara, Santa Barbara", 
    "Hilton Garden Inn Santa Barbara / Goleta", "Motel 6 Carpinteria, CA - Santa Barbara - South", 
    "Motel 6 Santa Barbara, CA - State Street", 
    "Moxy Santa Barbara", "Inn on Summer Hill", "Quality Inn Buellton - Solvang", 
    "ForFriends Inn Bed and Breakfast", "Flying Flags RV Resort & Campground", 
    "Orange Tree Inn", "Coast Village Inn - Santa Barbara", 
    "Ojai Retreat & Inn", 
    "Villa Rosa Inn", 
    "The Hadsten Solvang, Tapestry Collection by Hilton", "Royal Copenhagen Inn", 
    "Hampton Inn Santa Barbara/Goleta", 
    "Relax in the heart of Montecito", "Oasis Inn & Suites", "Solvang Inn and Cottages", 
    "Courtyard by Marriott Santa Barbara Downtown", "Beachside Inn", 
    "Hotel Virginia Santa Barbara, Tapestry Collection by Hilton", "Pea Soup Andersen's Inn", 
    "Hideaway Santa Barbara, A Kirkwood Collection Property", 
    "Best Western Plus Carpinteria Inn", 
    "Ocean, Sunset, Mountain Views, Private Deck: Villa Floresco: Tuscan-like getaway", 
    "The Ballard Inn, A Kirkwood Collection Hotel", 
    "The Steward, Santa Barbara, a Tribute Portfolio Hotel", "Motel 6 Carpinteria, CA - Santa Barbara - North", 
    "The Landsby", "Rancho Oso RV & Camping Resort", 
    "Chantico Inn", "Summerland Guest Cottage just steps to downtown and the beach! Pet Friendly", 
    "Viking Inn", "Casita Eco-Glamping", 
    "Hilton Garden Inn Lompoc", "AGAVE INN HOTEL", 
    "The perfect Los Olivos Guest House", 
    "Rose Garden Inn", 
    "The Presidio", "Kronborg Inn", 
    "Motel 6 Buellton, CA - Solvang Area", "The Genevieve", "Ala Mar by the Sea", 
    "Town and Country Inn", 
    "Holiday Inn Express Lompoc, an IHG Hotel",
    "Lompoc Valley Inn and Suites", "Atterdag Inn", 
    "WorldMark Solvang", 
    "Sandyland Beach Studio Carpinteria", 
    "Chumash Casino Resort", 
    "Haley Hotel", "Embassy Suites by Hilton Lompoc Central Coast", 
    "Hampton Inn & Suites Buellton/Santa Ynez Valley", "Blue Door Bungalow.", 
    "Papa Dux - A Playful Urban Penthouse", "Tide Pool Villas", 
    "Copenhagen Airy Apartment", "The Wine Valley Cottage - est. 2011", "Santa Barbara Inn", 
    "Mirabelle Inn and Restaurant", "Inn at Highway 1", "Sunset Motel", 
    "Casa Del Sol", 
    "Blue Iguana Inn", "The Inn at Zaca Creek",
    "Perfect Resort in Charming Solvang California", "The De La Vina Inn", 
    "La Petite Maison in Santa Ynez", 
    "Mama Dux - A Sumptuous Urban Sanctuary", "The Los Alamos Roadhouse",
    "Los Aguajes",
    "The 3 Dux", "Svendsgaard's Danish Lodge Americas Best Value Inn", 
    "Summerland Ocean View no. 3",
    "Alamo Motel", "Charming Santa Ynez farmhouse", "San Marcos Motel", "The COOP - SYV", 
    "The Oakley at the Los Alamos Mercantile",  
    "Blue Sands Inn, A Kirkwood Collection Hotel", 
    "Villa Verde - Luxurious Ocean and Mountain View Villa", 
    "Shoreline Escape", 
    "La Cabana Paradise Across Street To The Beach", 
    "Palmoro House",
    "Hidden Valley Retreat - Near Beach + Dtwn", 
    "HYGGE TOWER APARTMENT", "Rustic Elegance in Los Olivos", 
    "WorldMark Solvang - 2 Bedroom Twin Accessible", 
    "The Santa Barbara Whale House", 
    "Skyview Hotel - 21 & Over Pool", 
    "The Rose Mar Four Bedroom Villa Near Ocean", 
    "Hotel Ynez", 
    "Budget Inn Lompoc", "Downtown Hideaway with Patio", 
    "Ojai Serenity Retreat, a haven of tranquility for both couples and families.", 
    "Merkantile-4 Solvang / Luxury Lofts near downtown", 
    "Coffee House 1906 Craftsman Cottage, 2 blks State St, 5 Amtrak PET!", 
    "Chic & Sophisticated Studio with Panoramic Views & Privacy (yard, pet friendly!)", 
    "Lotus of Lompoc - A Great Hospitality Inn", 
    "The Craft House Inn",
    "O'cairns Inn & Suites", 
    "Comfort Inn & Suites Ventura Beach", "Hilton Garden Inn Oxnard/Camarillo", 
    "Holiday Inn Express Hotel & Suites Ventura, an IHG Hotel",
    "Fess Parker Wine Country Inn", 
    "Merkantile-5 Solvang / Luxury Lofts near downtown", 
    "Private Ranch Retreat", 
    "La Mesa House: large modern home", 
    "WorldMark Solvang - 2 Bedroom", 
    "Ojai Rancho Inn", "Casa Ojai Inn", 
    "Hummingbird Inn of Ojai","The Capri Hotel", 
    "Viking Motel", "Crystal Lodge Motel", "White Caps Motel", 
    "Hidden Cove By The Sea", "Heavenly Escape By The Sea", 
    "Sunset Haven By The Sea", "Travelers Beach Inn", 
    "WorldMark Solvang - 2 Bedroom Penthouse", 
    "WorldMark Solvang - 2 Bedroom Twin", "West Beach Treehouse", 
    "WorldMark Solvang - Studio", "WorldMark Solvang - 2 Bedroom Queen", 
    "WorldMark Solvang - 2 Bedroom Accessible", "WorldMark Solvang - 1 Bedroom Accessible", 
    "3809S Beach Blessing", 
    "Boutique Comfort at Inn at HWY1", 
    "Montecito retreat - minutes to Butterfly Beach, Lower Village, & downtown", 
    "Escape the City.",
    "Motel 6 Lompoc, CA", "Inn of Lompoc",
    "Santa Ynez Vineyard Retreat! The Guest Cottage at Starfall Ranch", 
    "Queen-Sized Room, Lounge Area with Mountain Views", "Wyatt Earp at the Los Alamos Mercantile", 
    "WorldMark Solvang - 1 Bedroom",
    "Beautiful Rose Cottage In Wine Country", 
    "Boutique Hotel Double Queen Patio Room", "Sweet Queen Retreat in Downtown Los Olivos.", "Farmhouse-chic Carpinteria Cottage w/ Pool Access", 
    "Anavo Farm's Stylish Sheep Retreat", "Ojai Mountain View Country Retreat"]
    # generate this from python list and modify it manually for data cleaning
    
    df = df[df['hotel_name'].isin(hotel_list)]

    rename_dict = {
    "Hotel Milo Santa Barbara": "Hotel Milo Santa Barbara",
    "Motel 6 Santa Barbara, CA - Beach": "Motel 6 Santa Barbara",
    "Avania Inn of Santa Barbara": "Avania Inn",
    "West Beach Inn, a Coast Hotel": "West Beach Inn",
    "Sandpiper Lodge": "Sandpiper Lodge",
    "Riviera Beach House": "Riviera Beach House",
    "Drift Santa Barbara, a Member of Design Hotels": "Drift Santa Barbara",
    "Hyatt Place Santa Barbara": "Hyatt Place Santa Barbara",
    "Best Western Plus Santa Barbara": "Best Western Plus Santa Barbara",
    "Ramada by Wyndham Santa Barbara": "Ramada Santa Barbara",
    "Hotel Californian": "Hotel Californian",
    "Inn By The Harbor": "Inn By The Harbor",
    "Mason Beach Inn": "Mason Beach Inn",
    "Lavender Inn by the Sea": "Lavender Inn",
    "The Eagle Inn": "The Eagle Inn",
    "El Encanto, A Belmond Hotel, Santa Barbara": "El Encanto Hotel",
    "Brisas del Mar, Inn at the Beach": "Brisas del Mar",
    "Residence Inn by Marriott Santa Barbara Goleta": "Residence Inn Goleta",
    "La Playa Inn": "La Playa Inn",
    "Ojai Valley Inn": "Ojai Valley Inn",
    "Hotel Santa Barbara": "Hotel Santa Barbara",
    "The Franciscan Hotel": "The Franciscan Hotel",
    "Mar Monte Hotel, in The Unbound Collection by Hyatt": "Mar Monte Hotel",
    "The Upham Hotel": "The Upham Hotel",
    "Harbor View Inn": "Harbor View Inn",
    "Wine Valley Inn": "Wine Valley Inn",
    "The Inn at Mattei's Tavern": "Inn at Mattei's Tavern",
    "Simpson House Inn": "Simpson House Inn",
    "Cheshire Cat Inn & Cottages": "Cheshire Cat Inn & Cottages",
    "Montecito Inn": "Montecito Inn",
    "Courtyard Santa Barbara Goleta": "Courtyard Goleta",
    "Harbor House Inn": "Harbor House Inn",
    "Hilton Santa Barbara Beachfront Resort": "Hilton Santa Barbara Beachfront Resort",
    "Best Western Plus Pepper Tree Inn": "Best Western Pepper Tree Inn",
    "Marina Beach Motel": "Marina Beach Motel",
    "Bath Street Inn": "Bath Street Inn",
    "Lemon Tree Inn": "Lemon Tree Inn",
    "Castillo Inn at the Beach": "Castillo Inn",
    "Cliff House Inn On The Ocean": "Cliff House Inn",
    "Casa Jardin": "Casa Jardin",
    "Casa De La Vina": "Casa De La Vina",
    "Rosewood Miramar Beach": "Rosewood Miramar",
    "New Haven Inn": "New Haven Inn",
    "Agave Inn": "Agave Inn",
    "Pacific Crest Hotel Santa Barbara": "Pacific Crest Hotel",
    "The Inn at East Beach": "Inn at East Beach",
    "Hamlet Inn": "Hamlet Inn",
    "Kimpton Canary Hotel, an IHG Hotel": "Kimpton Canary Hotel",
    "The Leta Santa Barbara Goleta, Tapestry Collection by Hilton": "The Leta Santa Barbara",
    "Sideways Inn": "Sideways Inn",
    "Hotel Corque": "Hotel Corque",
    "Vinland Hotel and Lounge": "Vinland Hotel",
    "Palihouse Santa Barbara": "Palihouse Santa Barbara",
    "Oakridge Inn": "Oakridge Inn",
    "Extended Stay America Suites Santa Barbara Calle Real": "Extended Stay America Santa Barbara",
    "Secret Garden Inn and Cottages": "Secret Garden Inn",
    "Santa Barbara Mission Studio": "Santa Barbara Mission Studio",
    "Santa Ynez Valley Marriott": "Santa Ynez Valley Marriott",
    "Motel 6 Goleta, CA - Santa Barbara": "Motel 6 Goleta",
    "King Frederik Inn": "King Frederik Inn",
    "The Winston Solvang": "The Winston Solvang",
    "Hotel Hygge": "Hotel Hygge",
    "Best Western Plus South Coast Inn": "Best Western South Coast Inn",
    "The M Solvang": "The M Solvang",
    "Holiday Inn Express Hotel & Suites Carpinteria": "Holiday Inn Express Carpinteria",
    "The Ritz-Carlton Bacara, Santa Barbara": "The Ritz-Carlton Bacara",
    "Hilton Garden Inn Santa Barbara / Goleta": "Hilton Garden Inn Goleta",
    "Motel 6 Carpinteria, CA - Santa Barbara - South": "Motel 6 Carpinteria",
    "Motel 6 Santa Barbara, CA - State Street": "Motel 6 Santa Barbara",
    "Moxy Santa Barbara": "Moxy Santa Barbara",
    "Inn on Summer Hill": "Inn on Summer Hill",
    "Quality Inn Buellton - Solvang": "Quality Inn Buellton",
    "ForFriends Inn Bed and Breakfast": "ForFriends Inn",
    "Flying Flags RV Resort & Campground": "Flying Flags Resort",
    "Orange Tree Inn": "Orange Tree Inn",
    "Coast Village Inn - Santa Barbara": "Coast Village Inn",
    "Ojai Retreat & Inn": "Ojai Retreat Inn",
    "Villa Rosa Inn": "Villa Rosa Inn",
    "The Hadsten Solvang, Tapestry Collection by Hilton": "The Hadsten Solvang",
    "Royal Copenhagen Inn": "Royal Copenhagen Inn",
    "Hampton Inn Santa Barbara/Goleta": "Hampton Inn Goleta",
    "Oasis Inn & Suites": "Oasis Inn & Suites",
    "Solvang Inn and Cottages": "Solvang Inn and Cottages",
    "Courtyard by Marriott Santa Barbara Downtown": "Courtyard by Marriott Santa Barbara Downtown",
    "Beachside Inn": "Beachside Inn",
    "Hotel Virginia Santa Barbara, Tapestry Collection by Hilton": "Hotel Virginia Santa Barbara Hilton",
    "Pea Soup Andersen's Inn": "Pea Soup Andersen's Inn",
    "Hideaway Santa Barbara, A Kirkwood Collection Property": "Hideaway Santa Barbara",
    "Best Western Plus Carpinteria Inn": "Best Western Carpinteria Inn",
    "The Ballard Inn, A Kirkwood Collection Hotel": "The Ballard Inn",
    "The Steward, Santa Barbara, a Tribute Portfolio Hotel": "The Steward Santa Barbara",
    "The Landsby": "The Landsby",
    "Rancho Oso RV & Camping Resort": "Rancho Oso Resort",
    "Chantico Inn": "Chantico Inn",
    "Viking Inn": "Viking Inn",
    "Hilton Garden Inn Lompoc": "Hilton Garden Inn Lompoc",
    "Rose Garden Inn": "Rose Garden Inn",
    "The Presidio": "The Presidio",
    "Kronborg Inn": "Kronborg Inn",
    "Motel 6 Buellton, CA - Solvang Area": "Motel 6 Buellton",
    "The Genevieve": "The Genevieve",
    "Ala Mar by the Sea": "Ala Mar by the Sea",
    "Town and Country Inn": "Town and Country Inn",
    "Holiday Inn Express Lompoc, an IHG Hotel": "Holiday Inn Express Lompoc",
    "Lompoc Valley Inn and Suites": "Lompoc Valley Inn",
    "Atterdag Inn": "Atterdag Inn",
    "WorldMark Solvang": "WorldMark Solvang",
    "Chumash Casino Resort": "Chumash Casino Resort",
    "Haley Hotel": "Haley Hotel",
    "Embassy Suites by Hilton Lompoc Central Coast": "Embassy Suites Lompoc",
    "Hampton Inn & Suites Buellton/Santa Ynez Valley": "Hampton Inn Buellton",
    "Santa Barbara Inn": "Santa Barbara Inn",
    "Mirabelle Inn and Restaurant": "Mirabelle Inn",
    "Inn at Highway 1": "Inn at Highway 1",
    "Sunset Motel": "Sunset Motel",
    "Casa Del Sol": "Casa Del Sol",
    "Blue Iguana Inn": "Blue Iguana Inn",
    "The Inn at Zaca Creek": "Inn at Zaca Creek",
    "The De La Vina Inn": "The De La Vina Inn",
    "La Petite Maison in Santa Ynez": "La Petite Maison",
    "Mama Dux - A Sumptuous Urban Sanctuary": "Mama Dux",
    "The Los Alamos Roadhouse": "Los Alamos Roadhouse",
    "The 3 Dux": "The 3 Dux",
    "Svendsgaard's Danish Lodge Americas Best Value Inn": "Svendsgaard's Danish Lodge",
    "Alamo Motel": "Alamo Motel",
    "San Marcos Motel": "San Marcos Motel",
    "The COOP - SYV": "The COOP",
    "The Oakley at the Los Alamos Mercantile": "The Oakley",
    "Blue Sands Inn, A Kirkwood Collection Hotel": "Blue Sands Inn",
    "Villa Verde - Luxurious Ocean and Mountain View Villa": "Villa Verde",
    "Shoreline Escape": "Shoreline Escape",
    "La Cabana Paradise Across Street To The Beach": "La Cabana Paradise",
    "Palmoro House": "Palmoro House",
    "Hidden Valley Retreat - Near Beach + Dtwn": "Hidden Valley Retreat",
        "HYGGE TOWER APARTMENT": "HYGGE Tower",
    "Rustic Elegance in Los Olivos": "Rustic Elegance",
    "WorldMark Solvang - 2 Bedroom Twin Accessible": "WorldMark Solvang",
    "The Santa Barbara Whale House": "Whale House",
    "Skyview Hotel - 21 & Over Pool": "Skyview Hotel",
    "The Rose Mar Four Bedroom Villa Near Ocean": "The Rose Mar Villa",
    "Hotel Ynez": "Hotel Ynez",
    "Budget Inn Lompoc": "Budget Inn",
    "Downtown Hideaway with Patio": "Downtown Hideaway",
    "Ojai Serenity Retreat, a haven of tranquility for both couples and families.": "Ojai Serenity Retreat",
    "Merkantile-4 Solvang / Luxury Lofts near downtown": "Merkantile Solvang",
    "Coffee House 1906 Craftsman Cottage, 2 blks State St, 5 Amtrak PET!": "Coffee House 1906",
    "Chic & Sophisticated Studio with Panoramic Views & Privacy (yard, pet friendly!)": "Chic & Sophisticated Studio",
    "Lotus of Lompoc - A Great Hospitality Inn": "Lotus of Lompoc",
    "The Craft House Inn": "The Craft House Inn",
    "O'cairns Inn & Suites": "O'cairns Inn",
    "Comfort Inn & Suites Ventura Beach": "Comfort Inn Ventura Beach",
    "Hilton Garden Inn Oxnard/Camarillo": "Hilton Garden Inn Oxnard",
    "Holiday Inn Express Hotel & Suites Ventura, an IHG Hotel": "Holiday Inn Express Ventura",
    "Fess Parker Wine Country Inn": "Fess Parker Inn",
    "Merkantile-5 Solvang / Luxury Lofts near downtown": "Merkantile Solvang",
    "Private Ranch Retreat": "Private Ranch Retreat",
    "La Mesa House: large modern home": "La Mesa House",
    "WorldMark Solvang - 2 Bedroom": "WorldMark Solvang",
    "Ojai Rancho Inn": "Ojai Rancho Inn",
    "Casa Ojai Inn": "Casa Ojai Inn",
    "Hummingbird Inn of Ojai": "Hummingbird Inn",
    "The Capri Hotel": "The Capri Hotel",
    "Viking Motel": "Viking Motel",
    "Crystal Lodge Motel": "Crystal Lodge Motel",
    "White Caps Motel": "White Caps Motel",
    "Hidden Cove By The Sea": "Hidden Cove",
    "Heavenly Escape By The Sea": "Heavenly Escape",
    "Sunset Haven By The Sea": "Sunset Haven",
    "Travelers Beach Inn": "Travelers Beach Inn",
    "WorldMark Solvang - 2 Bedroom Penthouse": "WorldMark Solvang",
    "West Beach Treehouse": "West Beach Treehouse",
    "WorldMark Solvang - Studio": "WorldMark Solvang",
    "Boutique Comfort at Inn at HWY1": "Inn at HWY1",
    "Montecito retreat - minutes to Butterfly Beach, Lower Village, & downtown": "Montecito Retreat",
    "Escape the City.": "Escape the City",
    "Motel 6 Lompoc, CA": "Motel 6 Lompoc",
    "Inn of Lompoc": "Inn of Lompoc",
    "Santa Ynez Vineyard Retreat! The Guest Cottage at Starfall Ranch": "Santa Ynez Vineyard Retreat",
    "Queen-Sized Room, Lounge Area with Mountain Views": "Queen-Sized Room",
    "Wyatt Earp at the Los Alamos Mercantile": "Wyatt Earp Los Alamos",
    "WorldMark Solvang - 1 Bedroom": "WorldMark Solvang",
    "Beautiful Rose Cottage In Wine Country": "Rose Cottage Wine Country",
    "Boutique Hotel Double Queen Patio Room": "Boutique Hotel",
    "Sweet Queen Retreat in Downtown Los Olivos.": "Sweet Queen Retreat",
    "Farmhouse-chic Carpinteria Cottage w/ Pool Access": "Farmhouse-chic Cottage",
    "Anavo Farm's Stylish Sheep Retreat": "Anavo Farm Retreat",
    "Ojai Mountain View Country Retreat": "Ojai Mountain View Retreat"}

    df['hotel_name'] = df['hotel_name'].replace(rename_dict)
    label_encoder = LabelEncoder()

    df2 = df.copy()
    df2 = pd.get_dummies(df2, columns=['Breakfast', "Pool", "Hottub", "Kitchen", "Washer_Dryer"], drop_first=False)

    df2['Number_review'] = df2['Number_review'].str.replace("\D", '', regex = True)
    df2['Number_review'] = pd.to_numeric(df2['Number_review'], errors = 'coerce')

    oe = OrdinalEncoder(categories=[["No review",'Good', 'Very Good', 'Wonderful', 'Excellent', 'Exceptional']])
    df2['hotel_review'] = oe.fit_transform(df2[['hotel_review']])

    df2['month'] = df2['start_date'].dt.month
    df2['day'] = df2['start_date'].dt.day

    df2['month_sin'] = np.sin(2 * np.pi * df2['month']/12)
    df2['day_sin'] = np.sin(2 * np.pi * df2['day']/31)

    df2['month_cos'] = np.cos(2 * np.pi * df2['month']/12)
    df2['day_cos'] = np.cos(2 * np.pi * df2['day']/31)

    df2['day_of_week'] = df2['start_date'].dt.dayofweek

    # clean_df = clean_df.drop(['start_date', 'end_date'], axis = 1)

    # clean_df['hotel_price'] = clean_df['hotel_price'].str.replace("\D", '', regex = True)
    df2['hotel_price'] = pd.to_numeric(df2['hotel_price'], errors = 'coerce')
    df2['Per_Night_Fee'] = df2['Per_Night_Fee'].str.replace("\D", '', regex = True)
    df2['Per_Night_Fee'] = pd.to_numeric(df2['Per_Night_Fee'], errors = 'coerce')


    df2['hotel_rating'] = pd.to_numeric(df2['hotel_rating'], errors = 'coerce')

    df2['hotel_name'] = label_encoder.fit_transform(df2['hotel_name'])

    # clean_df['hotel_city'].unique() -> use this to extract all city name
    pattern = r'(Santa Barbara|Goleta|Solvang|Los Olivos|Buellton|Montecito|Carpinteria|Santa Ynez|Los Alamos|Lompoc|Ojai|Ventura)'
    df2['hotel_city'] = df2['hotel_city'].str.extract(pattern, flags = re.IGNORECASE)
    df2['hotel_city'] = df2['hotel_city'].fillna("No City Name")
    df2 = pd.get_dummies(df2, columns=['hotel_city'], drop_first=False)
    # Drop duplicated values from same date
    drop = df2[df2.duplicated(subset=['hotel_name', 'start_date'], keep = "first")].index.to_list()
    df2 = df2.drop(axis = 0, index = drop)
    dict = {"5.0": 9.5, "4.0": 9.0, "3.0": 8.5, "2.0": 8.0, "1.0": 7.5, "0.0": np.nan} 
    df2['hotel_rating'] = df2['hotel_rating'].fillna(df2['hotel_review'].astype(str).map(dict))# fill in hotel_rating missing values based on hotel_review through mapping
    # fill in missing values based on forward fill and backward fill, finding values based on grouping and check if same results show up 
    # in previous data. (This happens because of some data loss during scraping stage)
    df2['hotel_rating'] = df2.groupby("hotel_name")['hotel_rating'].ffill().bfill()
    df2['Number_review'] = df2.groupby("hotel_name")['Number_review'].ffill().bfill() 
    df2 = df2.reset_index(drop=True)
    return df2
# print(data_cleaning())



