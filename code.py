# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns={"Total":"Total_Medals"},inplace=True)
data.head(10)
#Code starts here



# --------------
#Code starts here

data["Better_Event"] = np.where(data["Total_Summer"]>data["Total_Winter"],'Summer','Winter') 
data["Better_Event"] = np.where(data["Total_Summer"]==data["Total_Winter"],'Both',data['Better_Event']) 

better_event = data["Better_Event"].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here

#Code starts here

#Subsetting the dataframe
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

#Dropping the last row
top_countries=top_countries[:-1]

#Function for top 10
def top_ten(data, col):
    
    #Creating a new list
    country_list=[]
    
    #Finding the top 10 values of 'col' column
    country_list= list((data.nlargest(10,col)['Country_Name']))
    
    #Returning the top 10 list
    return country_list



#Calling the function for Top 10 in Summer
top_10_summer=top_ten(top_countries,'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")

#Calling the function for Top 10 in Winter
top_10_winter=top_ten(top_countries,'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")

#Calling the function for Top 10 in both the events
top_10=top_ten(top_countries,'Total_Medals')
print("Top 10:\n",top_10, "\n")

#Extracting common country names from all three lists
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print('Common Countries :\n', common, "\n")

#Code ends here


# --------------
#Code starts here
summer_df = data[data["Country_Name"].isin(top_10_summer)]
winter_df = data[data["Country_Name"].isin(top_10_winter)]
top_df = data[data["Country_Name"].isin(top_10)]

fig, (ax_1,ax_2,ax_3) = plt.subplots(nrows=3,ncols=1,figsize=(15,10))
summer_df.plot(x='Country_Name',y='Total_Summer',ax=ax_1,kind='bar')
winter_df.plot(x='Country_Name',y='Total_Summer',ax=ax_2,kind='bar')
top_df.plot(x='Country_Name',y='Total_Summer',ax=ax_3,kind='bar')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']

summer_max_ratio = summer_df['Golden_Ratio'].max()

summer_country_gold = summer_df.loc[summer_df["Golden_Ratio"].idxmax(),'Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']

winter_max_ratio = winter_df['Golden_Ratio'].max()

winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

top_max_ratio = top_df['Golden_Ratio'].max()

top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']


# --------------
#Code starts here

data_1 = data.drop([146])
data_1['Total_Points'] = (3*data_1['Gold_Total'])+(2*data_1['Silver_Total'])+(1*data_1['Bronze_Total'])
most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)
best.plot.bar()


