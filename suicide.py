# Import Libraries 
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

Menu = option_menu(None, ["Dataset","Dashboard", "Recommendations"],icons=["cloud","bar-chart-line","clipboard-check"],menu_icon="cast", default_index=0, orientation="horizontal", styles={"container": {"padding": "0!important", "background-color": "#fafafa"},"icon": {"color": "black", "font-size": "25px"}, "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},"nav-link-selected": {"background-color": "purple"},})
if Menu == "Dataset": st.title('Suicide Dataset')
if Menu == "Dashboard": st.title('Suicide EDA-Dashboard')
if Menu == "Recommendations" : st.title("Recommendations")


# Setting a small introduction on the suicide topic
if Menu=="Dataset":st.caption("From a long time suicide it's been a major problem for NGOs and governments since it is considered as taboo and didn't get the attention it deserves. But it is really important to study the trend of this problem to get insights about: where we should launch prevention campaign, in which country, the target population and many more.")

# Loading the Data
if Menu=="Dataset":st.header("First of all lets take a clear view on the Datframe that we have")
data = pd.read_csv("master.csv")
if Menu=="Dataset": st.write(data)

if Menu=="Dataset":col1, col2, col3 = st.columns(3)
if Menu=="Dataset":col1.metric("Columns", "12",delta_color="inverse")
if Menu=="Dataset":col2.metric("Records", "27820",delta_color="inverse")
if Menu=="Dataset":col3.metric("Number of countries", "90",delta_color="inverse")


# printing general informations about our data
data.info()

# Checking for missing data in the columns
data.isnull().sum()

# Dropping the column that contains missing value
data.drop("HDI for year",axis=1,inplace=True)

# Dividing the data into 2 subcategory, data that contains all the information on males and the other on females
data_men = data[data.sex == "male"]
data_women = data[data.sex == "female"]

#Now our data is clean and splitted and ready for the EDA part

# Pie Chart 
# The most important question Who commit suicides more males or females
if Menu=="Dashboard":st.header(" Who commit Suicides more? females or males?")

# To answer this question i plotted a pie chart to see the number that committed suicides
plt.pie([data_men["suicides_no"].sum(),data_women["suicides_no"].sum() ], labels= [' Percentage of men that commited suicides', 'Percentage of women that commited suiced'], autopct='%1.1f%%')
fig= go.Figure(data=[go.Pie(labels=['Males', 'Females'], values=[data_men["suicides_no"].sum(),data_women["suicides_no"].sum()], title='%/number of suicides committed from 1987 to 2016 across gender')])
if Menu=="Dashboard":st.plotly_chart(fig)


# Same Plot for all countries 
if Menu=="Dashboard":st.header("What if we want to know the percentage in a specific country")

if Menu=="Dashboard":option = st.selectbox(
     'Select Please your Specific country',
     ('Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
 'Austria' ,'Azerbaijan' ,'Bahamas', 'Bahrain' ,'Barbados', 'Belarus', 'Belgium',
 'Belize' ,'Bosnia and Herzegovina' ,'Brazil', 'Bulgaria' ,'Cabo Verde',
 'Canada' ,'Chile', 'Colombia' ,'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
 'Czech Republic', 'Denmark' ,'Dominica', 'Ecuador', 'El Salvador', 'Estonia'
 'Fiji', 'Finland', 'France' ,'Georgia', 'Germany' ,'Greece', 'Grenada',
 'Guatemala' ,'Guyana' ,'Hungary' ,'Iceland' ,'Ireland', 'Israel', 'Italy',
 'Jamaica' ,'Japan', 'Kazakhstan' ,'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
 'Lithuania' ,'Luxembourg', 'Macau', 'Maldives', 'Malta', 'Mauritius', 'Mexico',
 'Mongolia', 'Montenegro', 'Netherlands' ,'New Zealand', 'Nicaragua' ,'Norway',
 'Oman' ,'Panama' ,'Paraguay' ,'Philippines', 'Poland', 'Portugal',
 'Puerto Rico', 'Qatar', 'Republic of Korea' ,'Romania', 'Russian Federation',
 'Saint Kitts and Nevis' ,'Saint Lucia', 'Saint Vincent and Grenadines',
 'San Marino', 'Serbia', 'Seychelles', 'Singapore' ,'Slovakia' ,'Slovenia',
 'South Africa', 'Spain', 'Sri Lanka' ,'Suriname' ,'Sweden', 'Switzerland',
 'Thailand' ,'Trinidad and Tobago' ,'Turkey', 'Turkmenistan', 'Ukraine',
 'United Arab Emirates' ,'United Kingdom', 'United States', 'Uruguay',
 'Uzbekistan'))

if Menu=="Dashboard":st.write('You selected:', option)

if Menu=="Dashboard":datacountry1 = data[data["country"]==option]

if Menu=="Dashboard":data_men1 = datacountry1[data.sex == "male"]
if Menu=="Dashboard":data_women1 = datacountry1[data.sex == "female"]

if Menu=="Dashboard":plt.pie([data_men1["suicides_no"].sum(),data_women1["suicides_no"].sum() ], labels= ['Percantage of men that commited suicides', 'Percentage of women that commited suiced'], autopct='%1.1f%%')
if Menu=="Dashboard":fig= go.Figure(data=[go.Pie(labels=['Males', 'Females'], values=[data_men1["suicides_no"].sum(),data_women1["suicides_no"].sum()], title='Number of Suicides committed by males and females since 1985 till 2016')])
if Menu=="Dashboard":st.plotly_chart(fig)


#Lets Take a look on the trend of suicides in the world.
if Menu=="Dashboard":st.header("Suicide Trend")
total_gender = data[['sex', 'suicides_no', 'population', 'year', 'country']]
total_gender['proportion'] = total_gender.suicides_no / total_gender.population
gender_prop = pd.DataFrame(total_gender.groupby(['year', 'sex'])['proportion'].mean()).unstack()
fig = go.Figure()

fig.add_trace(go.Scatter(x= gender_prop.index,
                         y = gender_prop.proportion.male,
                         mode = 'lines+markers',
                         name = 'Male death ',
                         marker = dict(color='#FF9900')))

fig.add_trace(go.Scatter(x= gender_prop.index,
                         y = gender_prop.proportion.female,
                         mode = 'lines+markers',
                         name = 'Female death',
                         marker = dict(color='rgb(179,222,105)')))

fig.update_layout(height=500, width=900,
                  title = 'Trend of suicides across gender throught the years from 1985 till 2015',
                  font = dict(color="black"))

fig.update_xaxes(title_text = 'Year', color="RebeccaPurple")
fig.update_yaxes(title_text = 'Proportion', color="RebeccaPurple")
if Menu=="Dashboard":st.plotly_chart(fig)

#The Trend of suicides in specific country.
if Menu=="Dashboard":gog =  st.selectbox(
     'Select Please your Specific country',
     ('Armenia','Albania', 'Antigua and Barbuda', 'Argentina', 'Aruba', 'Australia',
 'Austria' ,'Azerbaijan' ,'Bahamas', 'Bahrain' ,'Barbados', 'Belarus', 'Belgium',
 'Belize' ,'Bosnia and Herzegovina' ,'Brazil', 'Bulgaria' ,'Cabo Verde',
 'Canada' ,'Chile', 'Colombia' ,'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
 'Czech Republic', 'Denmark' ,'Dominica', 'Ecuador', 'El Salvador', 'Estonia'
 'Fiji', 'Finland', 'France' ,'Georgia', 'Germany' ,'Greece', 'Grenada',
 'Guatemala' ,'Guyana' ,'Hungary' ,'Iceland' ,'Ireland', 'Israel', 'Italy',
 'Jamaica' ,'Japan', 'Kazakhstan' ,'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
 'Lithuania' ,'Luxembourg', 'Macau', 'Maldives', 'Malta', 'Mauritius', 'Mexico',
 'Mongolia', 'Montenegro', 'Netherlands' ,'New Zealand', 'Nicaragua' ,'Norway',
 'Oman' ,'Panama' ,'Paraguay' ,'Philippines', 'Poland', 'Portugal',
 'Puerto Rico', 'Qatar', 'Republic of Korea' ,'Romania', 'Russian Federation',
 'Saint Kitts and Nevis' ,'Saint Lucia', 'Saint Vincent and Grenadines',
 'San Marino', 'Serbia', 'Seychelles', 'Singapore' ,'Slovakia' ,'Slovenia',
 'South Africa', 'Spain', 'Sri Lanka' ,'Suriname' ,'Sweden', 'Switzerland',
 'Thailand' ,'Trinidad and Tobago' ,'Turkey', 'Turkmenistan', 'Ukraine',
 'United Arab Emirates' ,'United Kingdom', 'United States', 'Uruguay'))

if Menu=="Dashboard":datacountry2 = data[data["country"]==gog]

if Menu=="Dashboard":data_men2 = datacountry2[data.sex == "male"]
if Menu=="Dashboard":data_women2 = datacountry2[data.sex == "female"]

if Menu=="Dashboard":fig = plt.figure(figsize=(10, 4))
if Menu=="Dashboard":sns.lineplot(x = data_men2.year, y = data_men2['suicides/100k pop'], data= datacountry2,hue="sex")
if Menu=="Dashboard":sns.lineplot(x = data_women2.year, y = data_women2['suicides/100k pop'], data= datacountry2)
if Menu=="Dashboard":st.pyplot(fig)



# plotting a graph to visualize if the gdp has an efect on the suicide number.
if Menu=="Dashboard":st.header("Does the GDP per capita affect the number of suicides committed in a certain country?")
if Menu=="Dashboard":gog1 =  st.selectbox(
     'Select Please your Specific country',
     ('Finland','Germany','Armenia','Albania', 'Antigua and Barbuda', 'Argentina', 'Aruba', 'Australia',
 'Austria' ,'Azerbaijan' ,'Bahamas', 'Bahrain' ,'Barbados', 'Belarus', 'Belgium',
 'Belize' ,'Bosnia and Herzegovina' ,'Brazil', 'Bulgaria' ,'Cabo Verde',
 'Canada' ,'Chile', 'Colombia' ,'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
 'Czech Republic', 'Denmark' ,'Dominica', 'Ecuador', 'El Salvador', 'Estonia'
 'Fiji', 'France' ,'Georgia' ,'Greece', 'Grenada',
 'Guatemala' ,'Guyana' ,'Hungary' ,'Iceland' ,'Ireland', 'Israel', 'Italy',
 'Jamaica' ,'Japan', 'Kazakhstan' ,'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
 'Lithuania' ,'Luxembourg', 'Macau', 'Maldives', 'Malta', 'Mauritius', 'Mexico',
 'Mongolia', 'Montenegro', 'Netherlands' ,'New Zealand', 'Nicaragua' ,'Norway',
 'Oman' ,'Panama' ,'Paraguay' ,'Philippines', 'Poland', 'Portugal',
 'Puerto Rico', 'Qatar', 'Republic of Korea' ,'Romania', 'Russian Federation',
 'Saint Kitts and Nevis' ,'Saint Lucia', 'Saint Vincent and Grenadines',
 'San Marino', 'Serbia', 'Seychelles', 'Singapore' ,'Slovakia' ,'Slovenia',
 'South Africa', 'Spain', 'Sri Lanka' ,'Suriname' ,'Sweden', 'Switzerland',
 'Thailand' ,'Trinidad and Tobago' ,'Turkey', 'Turkmenistan', 'Ukraine',
 'United Arab Emirates' ,'United Kingdom', 'United States'))


if Menu=="Dashboard":datacountry3 = data[data["country"]==gog1]

if Menu=="Dashboard":f, ax = plt.subplots(1,1, figsize=(10,8))
if Menu=="Dashboard":ax = sns.scatterplot(x="gdp_per_capita ($)", y="suicides_no", data=datacountry3, color='yellow')
if Menu=="Dashboard":st.pyplot(f)

#suicide number across age brackets in the specific chosen country

if Menu=="Dashboard":st.header("What is the average age a person commits suicide?")
if Menu=="Dashboard":f,ax=plt.subplots(1,2,figsize=(20,8))

if Menu=="Dashboard":plt.figure(figsize=(10,5))
if Menu=="Dashboard":suicidenoVSgender = sns.barplot(x = 'sex', y = 'suicides_no', hue = 'age',ax=ax[0],data=data)
if Menu=="Dashboard":suicidenoVSgenerations= sns.barplot(x = 'sex', y = 'suicides_no', hue = 'generation',ax=ax[1],data = data)
if Menu=="Dashboard":st.pyplot(f)


if Menu=="Dashboard":title = st.text_input('Country name', 'Germany')
if Menu=="Dashboard":st.write('The country selected is', title)
if Menu=="Dashboard":datacountry3 = data[data["country"]==title]

if Menu=="Dashboard":f,ax=plt.subplots(1,2,figsize=(20,8))
if Menu=="Dashboard":plt.figure(figsize=(10,5))
if Menu=="Dashboard":suicidenoVSgender = sns.barplot(x = 'sex', y = 'suicides_no', hue = 'age',ax=ax[0],data=datacountry3)
if Menu=="Dashboard":suicidenoVSgenerations= sns.barplot(x = 'sex', y = 'suicides_no', hue = 'generation',ax=ax[1],data = datacountry3)
if Menu=="Dashboard":st.pyplot(f)

# Number of suicides/100k pop in all countries (using plotly map)
if Menu=="Dashboard":st.header("Rate of suicide committed in the available countries")
if Menu=="Dashboard":geo = data.groupby(by=['country']).agg({"suicides/100k pop": ['sum']})
if Menu=="Dashboard":geo.columns = ['total_suicide']
if Menu=="Dashboard":geo.reset_index(inplace=True)

if Menu=="Dashboard":fig = px.choropleth(geo, locations="country", locationmode='country names',
                    color="total_suicide", 
                    hover_name="country",
                    color_continuous_scale='sunset')

if Menu=="Dashboard":fig.update_layout(
    title="Number of suicides/100k population committed in countries from 1985 till 2015",
    font=dict(
        size=15,)
)
if Menu=="Dashboard":st.plotly_chart(fig)

#Top 10 countries which recored the highest suicides rates across the years
if Menu=="Dashboard":st.header("Top 10 Countries with the highest/Lowest Suicides Rates")

if Menu=="Dashboard":Year = st.slider('Select The year Please', 1987, 2016, 1988)

if Menu=="Dashboard":datayear = data[data["year"]==Year]
if Menu=="Dashboard":f, ax = plt.subplots(1,1, figsize=(10,8))
if Menu=="Dashboard":data_country_total = datayear.groupby(by=['country']).agg({'suicides/100k pop': ['sum']})
if Menu=="Dashboard":data_country_total.columns = ['total_suicide']
if Menu=="Dashboard":data_country_total.reset_index(inplace=True)
if Menu=="Dashboard":data_country_total = data_country_total.sort_values(by=['total_suicide'], ascending=False).head(10)

if Menu=="Dashboard":ax = sns.barplot(x='total_suicide', y='country', data=data_country_total)

if Menu=="Dashboard":plt.title('Top 10 Countries With Highest Number Of Suicides')

if Menu=="Dashboard":st.pyplot(f)

if Menu=="Dashboard":f1, ax1 = plt.subplots(1,1, figsize=(10,8))
if Menu=="Dashboard":data_country_total = datayear.groupby(by=['country']).agg({'suicides/100k pop': ['sum']})
if Menu=="Dashboard":data_country_total.columns = ['total_suicide']
if Menu=="Dashboard":data_country_total.reset_index(inplace=True)
if Menu=="Dashboard":data_country_total = data_country_total.sort_values(by=['total_suicide'], ascending=False).tail(10)

if Menu=="Dashboard":ax1 = sns.barplot(x='total_suicide', y='country', data=data_country_total)

if Menu=="Dashboard":plt.title(' Top 10 Countries With Lowest Number Of Suicides')

if Menu=="Dashboard":st.pyplot(f1)














               




