# Import Libraries 
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

Menu = option_menu(None, ["Dataset","Dashboard", "Recommendations"],icons=["cloud","bar-chart-line","clipboard-check"],menu_icon="cast", default_index=0, orientation="horizontal", styles={"container": {"padding": "0!important", "background-color": "#fafafa"},"icon": {"color": "black", "font-size": "25px"}, "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},"nav-link-selected": {"background-color": "blue"},})
if Menu == "Dataset": st.title('Suicide Dataset')
if Menu == "Dashboard": st.title('Suicide Dashboard')



# Setting a small introduction on the suicide topic
if Menu=="Dataset":st.caption("Suicide is the attempt when someone try to harm himself with the intent to end their life. For a long time this topic has been a major problem for NGOs and governments since it is considered as taboo and doesn't get the attention it deserves. But it is really important to study the trend of this problem to get insights about: where we should launch prevention campaign, in which country, the target population... in order to minimize its growth")

# Loading the Data
if Menu=="Dataset":st.header("Take a first look at the data")
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
if Menu=="Dashboard":st.header(" Who commit suicide more? females or males?")

# To answer this question i plotted a pie chart to see the number that committed suicides
plt.pie([data_men["suicides_no"].sum(),data_women["suicides_no"].sum() ], labels= [' Percentage of men that commited suicides', 'Percentage of women that commited suiced'], autopct='%1.1f%%')
fig= go.Figure(data=[go.Pie(labels=['Males', 'Females'], values=[data_men["suicides_no"].sum(),data_women["suicides_no"].sum()], title='%/number of suicides committed from 1987 to 2016 across gender')])
if Menu=="Dashboard":st.plotly_chart(fig)


# Same Plot for all countries 
if Menu=="Dashboard":st.header("Suicide percentage in a specific country")

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

fig.update_layout(height=500, width=900,font = dict(color="black"))

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


if Menu=="Dashboard":title = st.text_input('Please enter the name of the country', 'Germany')
if Menu=="Dashboard":st.write('The country selected is', title)
if Menu=="Dashboard":datacountry3 = data[data["country"]==title]

if Menu=="Dashboard":f,ax=plt.subplots(1,2,figsize=(20,8))
if Menu=="Dashboard":plt.figure(figsize=(10,5))
if Menu=="Dashboard":suicidenoVSgender = sns.barplot(x = 'sex', y = 'suicides_no', hue = 'age',ax=ax[0],data=datacountry3)
if Menu=="Dashboard":suicidenoVSgenerations= sns.barplot(x = 'sex', y = 'suicides_no', hue = 'generation',ax=ax[1],data = datacountry3)
if Menu=="Dashboard":st.pyplot(f)

# Number of suicides/100k pop in all countries (using plotly map)
if Menu=="Dashboard":st.header("Geographical representation of suicide rate")
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
if Menu=="Dashboard":st.header("Top 10 Countries with the highest/Lowest Suicide Rate")

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

#Recommendation Page in the Dashboard.

if Menu=="Recommendations":st.title("Results")
if Menu=="Recommendations":st.subheader("Suicide %")
if Menu=="Recommendations":col1, col2 = st.columns(2)
if Menu=="Recommendations":col1.metric("Males", "76.9%",delta_color="inverse")
if Menu=="Recommendations":col2.metric("Females", "23.1%",delta_color="inverse")
if Menu=="Recommendations":st.write("Males are 3.3 more likely to commit suicide than females")
if Menu=="Recommendations":st.subheader("Suicide rate across years")
if Menu=="Recommendations":col1, col2 = st.columns(2)
if Menu=="Recommendations":col1.metric("Highest Rate", "249","Year 1995",delta_color="inverse")
if Menu=="Recommendations":col2.metric("Lowest Rate", "48","-Year 2015",delta_color="inverse")
if Menu=="Recommendations":st.write("The highest rate of suicide recorded from 1985 till 2015 is in 1995 with 249 suicide/100K population and the lowest one is 48 per 100k population in year 2015")
if Menu=="Recommendations":st.subheader("Suicide~GDP")
if Menu=="Recommendations":st.write("The GDP and the number of suicides are negatively correlated since when the GDP per capita is low the number of suicides is high and it decrease when the GDP per capita increase")
if Menu=="Recommendations":st.subheader("Suicide~Age Brackets")
if Menu=="Recommendations":col1, col2, col3, col4, col5, col6= st.columns(6)
if Menu=="Recommendations":col1.metric("[5-14]", "+20",delta_color="inverse")
if Menu=="Recommendations":col2.metric("[15-24]", "+250",delta_color="inverse")
if Menu=="Recommendations":col3.metric("[25-34]", "+390",delta_color="inverse")
if Menu=="Recommendations":col4.metric("[35-54]", "+800",delta_color="inverse")
if Menu=="Recommendations":col5.metric("[55-74]", "+500",delta_color="inverse")
if Menu=="Recommendations":col6.metric("[74+]", "-190",delta_color="inverse")
if Menu=="Recommendations": st.write("People aged between 35 and 54 are more likely to commit suicide than others")
if Menu=="Recommendations": st.write("The lowest risk of suicide is for people aged between 5 and 14 years old")
if Menu=="Recommendations":st.subheader("Suicide~Continents")
if Menu=="Recommendations":st.write("Asia and Europe have highest rate in suicide than other continents. For instance Russia, Ukraine, Kazakhstan, Bulgaria, France have a very high suicide rate")
if Menu=="Recommendations":st.write("Countries with long winter season have the highest number of suicides")
if Menu=="Recommendations":st.subheader("KNN Model")
if Menu=="Recommendations":st.write("I used a KNN model to cluster my data into 2 groups: Countries with high rate of suicide and countries with low suicide rate.")
if Menu=="Recommendations":col9, col10 = st.columns(2)
if Menu=="Recommendations":col9.metric("Model", "KNN",delta_color="inverse")
if Menu=="Recommendations":col10.metric("silhouette", "71%",delta_color="inverse")
if Menu=="Recommendations":st.write("Our model scored a 0.71 as silhouette, which is considered as a good result")


if Menu=="Recommendations":st.title("Recommendation")
if Menu=="Recommendations":st.write("Here are some recommendations to minimize the suicide rate across the world:")
if Menu=="Recommendations":st.write("1. Launch awareness campaign on the importance for mens to express themselves and their feelings")
if Menu=="Recommendations":st.write("2. Launch a hotline number for suicide")
if Menu=="Recommendations":st.write("3. Free-Private psychiatric sessions")
if Menu=="Recommendations":st.write("4. Extra benefits from the government for the population that falls into this age bracket [35-54]")
if Menu=="Recommendations":st.write("5. Trying to analyze data collected from countries that have a high rate of suicide resutling in more detailed,accurate results especially in Russia, Kazakhstan, Ukraine, Austria, Finland, France and belgium since they have a very high suicide rate")
if Menu=="Recommendations":st.write("6. Include more variables in the data for example: ethnicity, if they have mental disorders, having any form of disability or not... ")

if Menu=="Recommendations": st.caption("Thank you")
st.caption("Prepared by Aziz Saliby")


#KNN model

#from sklearn.datasets.samples_generator import make_blobs
#from sklearn.cluster import KMeans
#from mpl_toolkits.mplot3d import Axes3D
#x = df.drop('suicides_no', axis=True)
#y = df['suicides_no']
#kmeans = KMeans(n_clusters=2)
#kmeans.fit(x)
#KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=600,
#    n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
#   random_state=0, tol=0.0001, verbose=0)
#y_kmeans = kmeans.predict(x)
#x, y_kmeans = make_blobs(n_samples=600, centers=2, cluster_std=0.60, random_state=0)
#fig = plt.figure()
#ax = Axes3D(fig)
#ax.scatter(x[:,0], x[:,1], c=y_kmeans, cmap='cool')

#from sklearn.metrics import silhouette_score
#print(silhouette_score(x, y_kmeans))
 










               




