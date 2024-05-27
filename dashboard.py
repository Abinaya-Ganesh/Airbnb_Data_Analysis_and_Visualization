#================================ /   IMPORTING LIBRARIES   / ======================================#

#File handling libraries
import json
import numpy as np

#Pandas Library
import pandas as pd

#Dashboard Library
import streamlit as st
import pydeck as pdk


#================================ /   LOADING JSON FILE    / ======================================#

path = r"C:\Users\abina\Desktop\abi\final project files\capstone 3\sample_airbnb.json"
D = open(path,'r')
data = json.load(D)


#================================ /   EXTRACTING NECESSARY DATA FROM JSON FILE   / ==============================#


#-------------------------- / PROPERTY DATA / -------------------------#

#Creating dictionaries
property_data = { 'property_id':[], 'property_name' : [], 'property_type':[], 'host_id': [], 
'host_name': [], 'host_is_superhost':[], 'country':[], 'country_code':[], 'address': [], 'market' : [],
'price':[], 'accommodates': [], 'bedrooms': [], 'beds':[]}

prop_detail = {'property_id':[], 'property_name':[], 'host_id':[], 'host_name':[], 'property_type': [], 
'description':[], 'neighborhood_overview':[], 'accommodates': [], 'bedrooms': [], 'room_type':[],
 'beds':[], 'bed_type':[], 'bathrooms':[], 'amenities':[], 'house_rules':[], 'minimum_nights':[], 
 'maximum_nights':[], 'price':[], 'guests_included':[],  'picture_url':[] , 'address':[]}



#Collecting data and assigning to dictionaries
for item in data:
    property_id= item['_id']
    property_name = item['name']
    description = item['description']
    neighborhood_overview = item['neighborhood_overview']
    house_rules = item['house_rules']
    property_type = item['property_type']
    room_type = item['room_type']
    bed_type = item['bed_type']
    minimum_nights = item['minimum_nights']
    maximum_nights = item['maximum_nights']
    accommodates = item['accommodates']
    bedrooms = item['bedrooms'] if 'bedrooms' in item else np.nan
    bathrooms = item['bathrooms'] if 'bathrooms' in item else np.nan
    beds = item['beds'] if 'beds' in item else 0
    amenities = ','.join(map(str,item['amenities']))
    price = item['price']
    guests_included = item['guests_included']
    picture_url = item['images']['picture_url']
    host_id = item['host']['host_id']
    host_name = item['host']['host_name']
    host_is_superhost = item['host']['host_is_superhost']
    address = item['address']['street']
    country = item['address']['country']
    country_code = item['address']['country_code']
    market = item['address']['market']

    #Assigning values to property_data distionary
    property_data['property_id'].append(property_id)
    property_data['property_name'].append(property_name)
    property_data['property_type'].append(property_type)
    property_data['accommodates'].append(accommodates)
    property_data['bedrooms'].append(bedrooms)
    property_data['beds'].append(beds)
    property_data['price'].append(price)
    property_data['host_id'].append(host_id)
    property_data['host_name'].append(host_name)
    property_data['country'].append(country)
    property_data['country_code'].append(country_code)
    property_data['address'].append(address)
    property_data['market'].append(market)
    if host_is_superhost:
        property_data['host_is_superhost'].append('Super Host')
    else:
        property_data['host_is_superhost'].append('No')
    

    #Assigning values to proper_details dictionary
    prop_detail['property_id'].append(property_id)
    prop_detail['property_name'].append(property_name)
    prop_detail['property_type'].append(property_type)
    prop_detail['description'].append(description)
    prop_detail['neighborhood_overview'].append(neighborhood_overview)
    prop_detail['house_rules'].append(house_rules)
    prop_detail['room_type'].append(room_type)
    prop_detail['bed_type'].append(bed_type)
    prop_detail['minimum_nights'].append(minimum_nights)
    prop_detail['maximum_nights'].append(maximum_nights)
    prop_detail['accommodates'].append(accommodates)
    prop_detail['bedrooms'].append(bedrooms)
    prop_detail['bathrooms'].append(bathrooms)
    prop_detail['beds'].append(beds)
    prop_detail['amenities'].append(amenities)
    prop_detail['price'].append(price)
    prop_detail['guests_included'].append(guests_included)
    prop_detail['picture_url'].append(picture_url)
    prop_detail['host_id'].append(host_id)
    prop_detail['host_name'].append(host_name)
    prop_detail['address'].append(address)


#Converting dictionaries to Dataframe
df_prop_data = pd.DataFrame(property_data)
df_prop_detail = pd.DataFrame(prop_detail)


#-------------------------- / HOST DATA / -------------------------#

#Creating dictionary
host_data = {'host_id':[], 'host_name':[], 'host_location':[], 'host_about':[], 'host_response_time': [], 
    'host_is_superhost':[], 'host_identity_verified':[], 'host_listings_count':[] }

#Collecting data and assigning to dictionary
for item in data:
    host_id = item['host']['host_id']
    host_name = item['host']['host_name']
    host_location = item['host']['host_location']
    host_about = item['host']['host_about']
    host_response_time = item['host']['host_response_time'] if 'host_response_time' in item['host'] else "Unavailable"
    host_is_superhost = item['host']['host_is_superhost']
    host_identity_verified = item['host']['host_identity_verified']
    host_listings_count = item['host']['host_listings_count']

    #Assigning values to host_data dictionary
    host_data['host_id'].append(host_id)
    host_data['host_name'].append(host_name)
    host_data['host_location'].append(host_location)
    host_data['host_about'].append(host_about)
    host_data['host_response_time'].append(host_response_time)
    host_data['host_listings_count'].append(host_listings_count)
    if host_is_superhost:
        host_data['host_is_superhost'].append('Yes')
    else:
        host_data['host_is_superhost'].append('No')

    if host_identity_verified == True:
        host_data['host_identity_verified'].append("Yes")
    else:
        host_data['host_identity_verified'].append("No")

#Converting dictionary to Dataframe
df_host_data = pd.DataFrame(host_data)
    

#-------------------------- / PROPERTY LOCATION DATA / -------------------------#

#Creating dictionary
prop_location = {'property_id':[], 'coordinates':[], 'country':[], 'country_code':[], 'address': []}

#Collectiong data and assigning to dictionary
for item in data:
    property_id= item['_id']
    address = item['address']['street']
    country = item['address']['country']
    country_code = item['address']['country_code']
    coordinates = item['address']['location']['coordinates']

    #Assigning values to prop_location dictionary
    prop_location['property_id'].append(property_id)
    prop_location['address'].append(address)
    prop_location['country'].append(country)
    prop_location['country_code'].append(country_code)
    prop_location['coordinates'].append(coordinates)

    
#Converting dictionary to Dataframe
df_prop_location = pd.DataFrame(prop_location)



#-------------------------- / PROPERTY REVIEW SCORES DATA / -------------------------#

#Creating dictionary
prop_review_scores = {'property_id':[], 'accuracy':[], 'cleanliness':[], 'checkin':[],
 'communication':[], 'location':[], 'value':[], 'rating':[]}

#Collecting data and assigning to dictionary
for item in data:
    property_id= item['_id']
    accuracy = item['review_scores']['review_scores_accuracy'] if 'review_scores_accuracy' in item['review_scores'] else np.nan
    cleanliness = item['review_scores']['review_scores_cleanliness'] if 'review_scores_cleanliness' in item['review_scores'] else np.nan
    checkin = item['review_scores']['review_scores_checkin'] if 'review_scores_checkin' in item['review_scores'] else np.nan
    communication = item['review_scores']['review_scores_communication'] if 'review_scores_communication' in item['review_scores'] else np.nan
    location = item['review_scores']['review_scores_location'] if 'review_scores_location' in item['review_scores'] else np.nan
    value = item['review_scores']['review_scores_value'] if 'review_scores_value' in item['review_scores'] else np.nan
    rating = item['review_scores']['review_scores_rating'] if 'review_scores_rating' in item['review_scores'] else np.nan


    #Assigning values to prop_review_scores dictinary
    prop_review_scores['property_id'].append(property_id)
    prop_review_scores['accuracy'].append(accuracy)
    prop_review_scores['cleanliness'].append(cleanliness)
    prop_review_scores['checkin'].append(checkin)
    prop_review_scores['communication'].append(communication)
    prop_review_scores['location'].append(location)
    prop_review_scores['value'].append(value)
    prop_review_scores['rating'].append(rating)

#Converting dictionary to Dataframe
df_prop_review_scores = pd.DataFrame(prop_review_scores)


#-------------------------- / PROPERTY REVIEW SCORES DATA / -------------------------#

#Creating dictionary
prop_reviews = {'property_id':[], 'review_id': [], 'date':[], 'reviewer_id':[], 'reviewer_name':[], 'comments':[]}

#Collecting data and assigning to dictionary
for item in data:
    for review in item['reviews']:
        property_id = review['listing_id']
        review_id = review['_id'] 
        date = review['date']
        reviewer_id = review['reviewer_id']
        reviewer_name = review['reviewer_name'] if 'reviewer_name' in review else "Unavailable"
        comments = review['comments'] if 'comments' in review else "Unavailable"

        #Assigning values to prop_reviews dictionary
        prop_reviews['property_id'].append(property_id)
        prop_reviews['review_id'].append(review_id)
        prop_reviews['date'].append(date)
        prop_reviews['reviewer_id'].append(reviewer_id)
        prop_reviews['reviewer_name'].append(reviewer_name)
        prop_reviews['comments'].append(comments)

#Converting dictionary to Dataframe
df_prop_reviews = pd.DataFrame(prop_reviews)


#================================ /   DATA PREPROCESSING   / ======================================#

#Removing duplicates from host data
df_host_data.drop_duplicates(inplace=True, ignore_index=True)


#Filling null values of bedrooms column
df_prop_data.fillna(value=0,inplace=True)

#Filling null values of bedrooms and bathrooms columns
values = {'bedrooms':0, 'bathrooms':1}
df_prop_detail.fillna(value=values,inplace=True)

#Filling null values of review scores dataframe
df_prop_review_scores.fillna(value=0,inplace=True)

#Replacing market column values to enable easy search on dashboard
df_prop_data = df_prop_data.replace({'market':['Oahu','The Big Island', 'Maui', 'Kauai']},value='Hawaii')
df_prop_data.replace(to_replace='Other (Domestic)', value='Hawaii', inplace=True)

df_prop_data.loc[2945,'market']= 'Porto'
df_prop_data.loc[3949,'market']= 'Istanbul'
df_prop_data.replace(to_replace='Other (International)', value='Rio De Janeiro', inplace=True)

df_prop_data.loc[597,'market']= 'Sydney'
df_prop_data.loc[617,'market']= 'New York'
df_prop_data.loc[639,'market']= 'Rio de Janeiro'
df_prop_data.loc[656,'market']= 'Montreal'
df_prop_data.loc[788,'market']= 'Barcelona'
df_prop_data.loc[836,'market']= 'Hawaii'

#Changing datatypes from float to int wherever necessary
df_prop_data = df_prop_data.astype({'bedrooms':'int64'})
df_prop_detail = df_prop_detail.astype({'bedrooms':'int64','bathrooms':'int64'})


#================================ /   DASHBOARD SETUP   / ======================================#

#Page_configuration
st.set_page_config(
    page_title = "Airbnb",
    page_icon = "🏨",
    layout = 'wide')


col1,col2 = st.columns(2)
with col1:
    st.header(':red[🏨airbnb]')
    destination = st.selectbox('**Search destination**',('New York', 'Hawaii', 'Istanbul', 'Hong Kong', 'Sydney', 'Porto',
       'Rio De Janeiro', 'Montreal', 'Barcelona'),index=None,key='destination',placeholder='Select a destination')
    type = st.selectbox('**Select the property types**',['Apartment', 'Bed and breakfast', 'Guesthouse', 'Hostel',
       'Serviced apartment', 'Loft', 'House', 'Condominium', 'Treehouse',
       'Guest suite', 'Bungalow', 'Townhouse', 'Villa', 'Cabin', 'Other',
       'Farm stay', 'Chalet', 'Boutique hotel', 'Cottage', 'Boat',
       'Earth house', 'Aparthotel', 'Resort', 'Tiny house',
       'Nature lodge', 'Hotel', 'Camper/RV', 'Casa particular (Cuba)',
       'Barn', 'Hut', 'Heritage hotel (India)', 'Pension (South Korea)',
       'Campsite', 'Castle', 'Houseboat', 'Train'],index=None,key='type',placeholder='Select property type')
    
with col2:
    st.header(":blue[Filter]")
    start, end = st.select_slider('**Select a price range in dollars**',
    options=['5', '50', '100', '200', '300', '500', '1000','2000', '5000', '10000', '20000', '50000'],
    value=('5', '200'))
    n_accommodates = st.slider('**Select number of people**', 1,16,step=1)
    n_bedrooms = int(st.select_slider('**Select number of bedrooms**', 
        options=['0','1','2','3','4','5','6','7','8','9','10','15','20']))
    rating = st.slider('**Select minimum rating**', 0,100,step=10)


if destination:

    #Selecting latitude and longitude for view state of map
    map_dict = {'New York': '-73.96523,40.79962', 'Hawaii': '-157.82081,21.27531', 'Istanbul': '28.98009,41.0062', 'Hong Kong': '114.15027,22.28158',
        'Sydney': '151.21554,-33.88029', 'Porto': '-8.60867,41.1543', 'Rio De Janeiro': '-43.1908,-22.9843', 'Montreal': '-73.54949,45.54548',
        'Barcelona': '2.16942,41.40082'}
    lon,lat = map(float,map_dict[destination].split(','))

    #Diplaying a dataframe based on the filters
    df = pd.merge(df_prop_data, df_prop_review_scores, on='property_id')

    if type:
        condition = (df.market == destination) & (df.bedrooms == n_bedrooms) & (df.accommodates == n_accommodates) & (df.rating >= rating) & (df.price >= float(start)) & (df.price <= float(end)) & (df.property_type == type)
    else:
        condition = (df.market == destination) & (df.bedrooms == n_bedrooms) & (df.accommodates == n_accommodates) & (df.rating >= rating) & (df.price >= float(start)) & (df.price <= float(end))

    df_a = df[['property_name', 'address', 'property_type','host_name','host_is_superhost','accommodates','bedrooms','price','rating']][condition].reset_index(drop=True)
    df_a.index += 1
    df_a = df_a.rename_axis('Index').reset_index()

    df_id = df[['property_id', 'property_name','price']][condition].reset_index(drop=True)
    df_id.index+=1

    st.write(":red[**Listings**]")
    st.dataframe(df_a,use_container_width=True,hide_index=True)


    #================================ /   GEO VISUALIZATION  / ======================================#

    df_map = pd.merge(df_id, df_prop_location, on='property_id', how='inner').reset_index(drop=True)
    df_map.index += 1
    df_map = df_map.rename_axis('Index').reset_index()

    # Define a layer to display on a map
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_map,
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_scale=6,
        radius_min_pixels=1,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_position="coordinates",
        get_radius=100,
        get_fill_color=[255, 140, 0],
        get_line_color=[0, 0, 0],
    )

    # Set the viewport location
    view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=10, bearing=0, pitch=0)

    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{Index}\n{property_name}\n{address}\n${price}"}))


#Displaying property in detail
number = st.text_input(label="**Enter the :red[Index] from the table to display the details of the property**",placeholder="example:1")
button = st.button(label='Submit')

if number:
    id = df_id.loc[int(number)]['property_id']
    df1 = df_prop_detail[df_prop_detail.property_id == id].reset_index(drop=True)
    col1,col2 = st.columns(2)
    with col1:
        st.write(":red[**Property Name**]")
        st.write(df1.loc[0]['property_name'])
        st.write(":red[**Address**]")
        st.write(df1.loc[0]['address'])
        st.write(":red[**Property Type**]")
        st.write(df1.loc[0]['property_type'])
        st.write(":red[**Description**]")
        st.write(df1.loc[0]['description'])
        st.write(":red[**Neighborhood**]")
        st.write(df1.loc[0]['neighborhood_overview'])
        st.write(":red[**House rules**]")
        st.write(df1.loc[0]['house_rules'])
    
    with col2:
        page=df1.loc[0]['picture_url']
        st.page_link(page=page, label=":blue[**Picture**]")
        st.write(":red[**Host Name**]")
        col3,col4 = st.columns(2)
        with col3:
            st.write(df1.loc[0]['host_name'])
        with col4:
            host = st.button('Get host details', key = 'host')
        if host:
            df_host = df_host_data[df_host_data.host_id == df1.loc[0]['host_id']].reset_index(drop=True)
            st.write(':red[Host Location]')
            st.write(df_host.loc[0]['host_location'])
            if df_host.loc[0]['host_about']:
                st.write(':red[Host About]')
                st.write(df_host.loc[0]['host_about'])
            st.write(':red[Host Response Time]')
            st.write(df_host.loc[0]['host_response_time'])
            st.write(':red[Super Host]')
            st.write(df_host.loc[0]['host_is_superhost'])
            st.write(':red[Host Identity Verified]')
            st.write(df_host.loc[0]['host_identity_verified'])
            st.write(':red[Number of listings]')
            st.write(str(df_host.loc[0]['host_listings_count']))
        st.write(":red[**Amenities**]")
        st.write(df1.loc[0]['amenities'])
        st.write(":red[**Price per night**]")
        st.write(f"${df1.loc[0]['price']}")
        st.write(":red[**Details**]")
        df2 = df_prop_detail[['accommodates','bedrooms','room_type','beds','bed_type','bathrooms',
            'minimum_nights','maximum_nights','guests_included']][df_prop_detail.property_id == id]
        st.dataframe(df2,hide_index=True)
        st.write(":red[**Ratings**]")
        df3 = df_prop_review_scores[['accuracy','cleanliness','checkin','communication','location','value','rating']][df_prop_review_scores.property_id == id]
        st.dataframe(df3,use_container_width=True,hide_index=True)
        st.write(":red[**Reviews**]")
        df4 = df_prop_reviews[['reviewer_name','date','comments']][df_prop_reviews.property_id == id].reset_index(drop=True)
        for i in range(len(df4)):
            st.write(f":blue[{df4.loc[i]['date']}]")
            st.write(f"**{df4.loc[i]['reviewer_name']}**")
            st.write(df4.loc[i]['comments'])
            st.write("\n")