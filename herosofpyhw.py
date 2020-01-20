#shaheda choudhury
import pandas as pd
data = pd.read_csv("purchase_data.csv")
data.head()
#find unique players
uniqueplayers = data['SN'].nunique()
total_players = pd.DataFrame({"Total Players": [uniqueplayers]}, columns = ["Total Players"])
total_players
#collecting the data
unique_items = data['Item Name'].nunique()
avg_purchase = round(data['Price'].mean(),2)
total_purchase = round(data['Price'].sum(),2)
num_purchase = len(data)
# Building the DF for the requirements aka purchase analysis total 
purchase_analysis = {'Unique Items': [unique_items], 
                     'Average Price': ['$' + str(avg_purchase)], 
                     'Number of Purchase':[num_purchase], 
                     'Total Purchase': ['$' + str(total_purchase)]}
purchase_df = pd.DataFrame(purchase_analysis, index = None)
purchase_df
#collect the total numbers
total_gender_count = data['SN'].nunique()

male = data[data ['Gender']== 'Male']['SN'].nunique()
female = data[data['Gender']== 'Female']['SN'].nunique()
other = data[data['Gender']== 'Other / Non-Disclosed']['SN'].nunique()


#calculate the total percentages
male_per = round((male/total_gender_count)*100,2) 
female_per = round((female/total_gender_count)*100,2) 
other_per = round((other/total_gender_count)*100,2) 
#create the dataframe for gender analysis 
gender_analysis = {'Percent of Players': [str(male_per) + '%', str(female_per) + '%', str(other_per) + '%'], 
                   'Total Count': [male, female, other]}
gender_df = pd.DataFrame(gender_analysis, index = ['Male', 'Female', 'Other/ Non-Disclosed'])
gender_df

#finding the avg purchases
male_purchase = data[data['Gender'] == 'Male']["Price"].count()
female_purchase = data[data['Gender'] == 'Female']["Price"].count()
other_purchase = data[data['Gender'] == 'Other / Non-Disclosed']["Price"].count()

#finding the gender avg prices: 
male_avg_price = round(data[data['Gender'] == 'Male']["Price"].mean(),2)
female_avg_price = round(data[data['Gender'] == 'Female']["Price"].mean(),2) 
other_avg_price = round(data[data['Gender'] == 'Other / Non-Disclosed']["Price"].mean(),2)

#total purchase value based on gender categories 
male_total_perch_val = round(data[data['Gender'] == 'Male']["Price"].sum(),2)
female_total_perch_val = round(data[data['Gender'] == 'Female']["Price"].sum(),2)
other_total_perch_val = round(data[data['Gender'] == 'Other / Non-Disclosed']["Price"].sum(),2) 

#Average total purchasse per person based on gender
male_percent_person = round((male_total_perch_val/male),2)
female_percent_person = round((female_total_perch_val/female),2)
other_percent_person = round((other_total_perch_val/other),2)
#create the purchasing analysis for gender dataframe 
purchase_gender_analysis = {'Purchase Count': [male_purchase, female_purchase, other_purchase], 
                            'Avg Purchase Price': ['$' + str(male_avg_price), '$' + str(female_avg_price), '$' + str(other_avg_price)], 
                            'Total Purchase Value':['$' + str(male_total_perch_val),'$' + str(female_total_perch_val),'$' + str(other_total_perch_val)], 
                            'Avg. Total Purchase Per Person':['$' + str(male_percent_person),'$' + str(female_percent_person),'$' + str(other_percent_person)]}

purchase_gender_df = pd.DataFrame(purchase_gender_analysis, index = ['Male', 'Female', 'Other/ Non-Disclosed'])
purchase_gender_df
#Age demographics bins 
under10 = data[data['Age']<10]
age_10to14 = data[(data['Age'] >=10) & (data['Age'] <=14)]
age_15to19 = data[(data['Age'] >=15) & (data['Age'] <=19)]
age_20to24 = data[(data['Age'] >=20) & (data['Age'] <=24)]
age_25to29 = data[(data['Age'] >=25) & (data['Age'] <=29)]
age_30to34 = data[(data['Age'] >=30) & (data['Age'] <=34)]
age_35to39 = data[(data['Age'] >=39) & (data['Age'] <=39)]
over40 = data[data['Age'] >40]

#cal age percentages 
percent_under10 = round((under10['SN'].nunique()/total_gender_count)*100,2)
percent10 = round((age_10to14['SN'].nunique()/total_gender_count)*100,2)
percent15 = round((age_15to19['SN'].nunique()/total_gender_count)*100,2)
percent20 = round((age_20to24['SN'].nunique()/total_gender_count)*100,2)
percent25 = round((age_25to29['SN'].nunique()/total_gender_count)*100,2)
percent30 = round((age_30to34['SN'].nunique()/total_gender_count)*100,2)
percent35 = round((age_35to39['SN'].nunique()/total_gender_count)*100,2)
percent_over40 = round((over40['SN'].nunique()/total_gender_count)*100,2)

#total count of age
count_under10 = under10['SN'].nunique()
count_10 = age_10to14['SN'].nunique()
count_15 = age_15to19['SN'].nunique()
count_20 = age_20to24['SN'].nunique()
count_25 = age_25to29['SN'].nunique()
count_30 = age_30to34['SN'].nunique()
count_35 = age_35to39['SN'].nunique()
count_over40 = over40['SN'].nunique()

#creating the DF for age demographics 
age_demographics = {'Total Count': [count_under10, count_10, count_15, count_20, count_25 , count_30, count_35, count_over40], 
                    '% of players': [str(percent_under10) + '%', str(percent10) + '%', str(percent15) + '%', str(percent20) 
                                     + '%', str(percent25) + '%', str(percent30) + '%', str(percent_over40) + '%', str(percent_over40) + '%']}

age_demographics_df = pd.DataFrame(age_demographics, index = [ 'Under 10','10 - 14', '15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', 'Over 40'])
age_demographics_df
#purchase count for the age bins 
purchase_count_under10 = under10['Price'].count()
purchase_count10 = age_10to14['Price'].count()
purchase_count15 = age_15to19['Price'].count()
purchase_count20 = age_20to24['Price'].count()
purchase_count25 = age_25to29['Price'].count()
purchase_count30 = age_30to34['Price'].count()
purchase_count35 = age_35to39['Price'].count()
purchase_count_over40 = over40['Price'].count()

#avg purchase price count
avg_purchase_price_under10 = under10['Price'].mean()
avg_purchase_price_age10 = age_10to14['Price'].mean()
avg_purchase_price_age15 = age_15to19['Price'].mean()
avg_purchase_price_age20 = age_20to24['Price'].mean()
avg_purchase_price_age25 = age_25to29['Price'].mean()
avg_purchase_price_age30 = age_30to34['Price'].mean()
avg_purchase_price_age35 = age_35to39['Price'].mean()
avg_purchase_price_over40 = over40['Price'].mean()

#total purchase price
total_purchase_price_under10 = under10['Price'].sum()
total_purchase_price_age10 = age_10to14['Price'].sum()
total_purchase_price_age15 = age_15to19['Price'].sum()
total_purchase_price_age20 = age_20to24['Price'].sum()
total_purchase_price_age25 = age_25to29['Price'].sum()
total_purchase_price_age30 = age_30to34['Price'].sum()
total_purchase_price_age35 = age_35to39['Price'].sum()
total_purchase_price_over40 = over40['Price'].sum()

#normalized totals
norm_total_under10 = total_purchase_price_under10/count_under10
norm_total_age10 = total_purchase_price_age10/count_10
norm_total_age15 = total_purchase_price_age15/count_15
norm_total_age20 = total_purchase_price_age20/count_20
norm_total_age25 = total_purchase_price_age25/count_25
norm_total_age30 = total_purchase_price_age30/count_30
norm_total_age35 = total_purchase_price_age35/count_35
norm_total_over40 = total_purchase_price_over40/count_over40

#creating the df for the analysis 
purchasing_age_analysis  = {'Purchase Count': [purchase_count_under10, purchase_count10, purchase_count15, purchase_count20, purchase_count25, purchase_count30, purchase_count35, purchase_count_over40], 
                           'Avg Purchase Price': [avg_purchase_price_under10, avg_purchase_price_age10, avg_purchase_price_age15, avg_purchase_price_age20, avg_purchase_price_age25, avg_purchase_price_age30, avg_purchase_price_age35, avg_purchase_price_over40], 
                           'Total Purchase Price': [total_purchase_price_under10, total_purchase_price_age10, total_purchase_price_age15, total_purchase_price_age20, total_purchase_price_age25, total_purchase_price_age30, total_purchase_price_age35, total_purchase_price_over40], 
                           'Totals': [norm_total_under10, norm_total_age10, norm_total_age15, norm_total_age20, norm_total_age25, norm_total_age30, norm_total_age35, norm_total_over40]}

purchasing_age_analysis_df = pd.DataFrame(purchase_analysis, index = ['<10', '10 - 14', '15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', '40+'])
purchasing_age_analysis_df
#finding the tables information 
sn_total_purchase = data.groupby('SN')['Price'].sum().to_frame()
sn_purchase_count = data.groupby('SN')['Price'].count().to_frame()
sn_purchase_avg = data.groupby('SN')['Price'].mean().to_frame()

#joining the tables to find populate the tables 
sn_total_purchase.columns=["Total Purchase Value"]
join_one = sn_total_purchase.join(sn_purchase_count, how="left")
join_one.columns=["Total Purchase Value", "Purchase Count"]

join_two = join_one.join(sn_purchase_avg, how="inner")
join_two.columns=["Total Purchase Value", "Purchase Count", "Average Purchase Price"]

#creating the data frame 
top_spenders_df = join_two[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]
top_spenders_final = top_spenders_df.sort_values('Total Purchase Value', ascending=False).head()
top_spenders_final.style.format({"Average Purchase Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})
#merge dataframes to find purchase count, total purchase value for items, reset indices to df can be merged on specific elements
premergeone = data.groupby("Item Name").sum().reset_index()
premergetwo = data.groupby("Item ID").sum().reset_index()
premergethree = data.groupby("Item Name").count().reset_index()

#merge df
mergeone = pd.merge(premergeone, premergetwo, on="Price")
mergetwo = pd.merge(premergethree, mergeone, on="Item Name")

#create df by manipulating data
mergetwo["Gender"] = (mergetwo["Price_y"]/mergetwo["Item ID"]).round(2)
mergetwo_renamed = mergetwo.rename(columns={"Age": "Purchase Count", "Gender": "Item Price", "Item ID": "null", "Price_y": "Total Purchase Value", "Item ID_y": "Item ID"})

#grab columns needed
clean_df = mergetwo_renamed[["Item ID", "Item Name", "Purchase Count", "Item Price", "Total Purchase Value"]]
prefinal_df = clean_df.set_index(['Item Name', 'Item ID'])
popular_items_final = prefinal_df.sort_values('Purchase Count', ascending=False).head(6)
popular_items_final.style.format({"Item Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})
#use prefinal dataframe from prior to step to find most profitable items

profit_items_final = prefinal_df.sort_values('Total Purchase Value', ascending=False).head()
profit_items_final.style.format({"Item Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})
