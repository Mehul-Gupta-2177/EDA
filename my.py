import pandas as pd
from pandas import ExcelFile
import plotly.express as px

def monthlyDistribution():
    file = "rx_demo.xlsx"
    data = pd.read_excel(file) #reading file
    data_till2017 = data.loc[data['monthYear'].isin(['2016-01', '2016-02', '2016-03', '2016-04','2016-05', '2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04','2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12' ])]
    
    month_year_array = ['2016-01', '2016-02', '2016-03', '2016-04','2016-05', '2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04','2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12' ]
    
    num_patients = []
    for month in month_year_array:
        data_temp = data_till2017.loc[data_till2017['monthYear'] == month]
        n = len(pd.unique(data_temp['Patient_Id']))
        num_patients.append(n)
    
    #print(num_patients)
    fig = px.scatter(x=month_year_array, y=num_patients)
    fig.show()
    
    
def averageClaimJuly2017():
    file = "rx_demo.xlsx"
    data = pd.read_excel(file) #reading file
    data_till_July2017 = data.loc[data['monthYear'] == '2017-07']
    P_Id = pd.unique(data_till_July2017['Patient_Id'])
    #print(P_Id)
    num_patients = len(P_Id)
    #print(num_patients)
    claims = 0
    
    for patient in P_Id:
        data_temp = data_till_July2017.loc[data_till_July2017['Patient_Id'] == patient]
        column = data_temp['Claim_Id']
        num_claims = column.count() 
        claims = claims + num_claims
        
    average_claims = claims/num_patients
    print(round(average_claims, 1))
    
def stats():
    file = "rx_demo.xlsx"
    data = pd.read_excel(file) #reading file
    data_top_5 = data.loc[data['Plan_Name'].isin(['UAW RETIREE MEDICAL BENEFITS TRUST','CASH TX','HCSC BCBS TX','HUMANA HEALTH PLAN PDP32','CIGNA-HEALTHSPRING TX'])]
    column = data_top_5["Plan_Pay"]
    max_value = column.max()
    min_value = column.min()
    min_value2 = column.drop_duplicates().nsmallest(2).iloc[-1]
    #highest
    print('Highest claim')
    print(max_value)
    #lowest
    print('lowest claim')
    print(min_value)
    #lowest excluding 0
    print('2nd lowest claim')
    print(min_value2)
    #mean
    avg_val = column.mean()
    #lowest excluding 0
    print('average claim amount')
    print(avg_val)
    
def top5insuranceClaimProviders():

    file = "rx_demo.xlsx"
    df = pd.read_excel (file)
    df_2016 = df.loc[df['monthYear'].isin(['2016-01','2016-02','2016-03','2016-04','2016-05','2016-06','2016-07','2016-08','2016-09','2016-10','2016-11','2016-12'])]
    #print(df_2016)
    fig = px.bar(df_2016, x='Plan_Name')
    fig.show()
    
    
def TotalAmountPaid():
    file = "rx_demo.xlsx"
    df = pd.read_excel (file)

    df_top_5 = df.loc[df['Plan_Name'].isin(['UAW RETIREE MEDICAL BENEFITS TRUST','CASH TX','HCSC BCBS TX','HUMANA HEALTH PLAN PDP32','CIGNA-HEALTHSPRING TX'])]
    #print(df_top_5)
    #fig = px.bar(df_top_5, x='Plan_Name')
    #fig.show()
    df_top5_2017 = df_top_5.loc[df_top_5['monthYear'].isin(['2017-01','2017-02','2017-03','2017-04','2017-05','2017-06','2017-07','2017-08','2017-09','2017-10','2017-11','2017-12'])]
    #print(df_top5_2017)
    fig = px.bar(df_top5_2017, x="Plan_Name", y=["Plan_Pay", "Secondary_Plan_Pay"])
    fig.show()
    
    
def OOP():
    file = "rx_demo.xlsx"
    df = pd.read_excel (file)

    df_top_5 = df.loc[df['Plan_Name'].isin(['UAW RETIREE MEDICAL BENEFITS TRUST','CASH TX','HCSC BCBS TX','HUMANA HEALTH PLAN PDP32','CIGNA-HEALTHSPRING TX'])]

    df_top5_PatPay = df['Patient_Pay'].sum()
    print('Total OOP')
    print(df_top5_PatPay)
    
   
        
        
        
        
    
    