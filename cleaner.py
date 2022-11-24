from multiprocessing.sharedctypes import Value
from queue import Empty
from turtle import left
import pandas as pd;
import os;
from pandasql import sqldf;
pysqldf = lambda q: sqldf(q, globals())
season2021_filepath = 'data/yearly/2021.csv'
season_2021 = pd.read_csv(season2021_filepath)
season2020_filepath = 'data/yearly/2020.csv'
season_2020 = pd.read_csv(season2020_filepath)
'''
query21 ="SELECT Player, FantasyPoints as Season2021 FROM season_2021"
pfp21 = sqldf(query21)
print('------------------------------------------------------------------------------')
print(pfp21.head(20))
query20 ="SELECT Player, FantasyPoints as Season2020 FROM season_2020"
pfp20 = sqldf(query20)
print(pfp20.head(20))
print('------------------------------------------------------------------------------')
joinQuery = 'SELECT * FROM pfp21 LEFT JOIN pfp20 ON pfp21.Player = pfp20.Player'
join = sqldf(joinQuery)
print(join.head(20))
'''
#join = pd.merge(season_2020[['Player','FantasyPoints']],season_2021[['Player','FantasyPoints']], how='left',suffixes=(' 2021',' 2020'), on='Player')
#print(join.head(20))
directory = 'data/weekly/2020'
overall = 0
#week = pd.DataFrame('data/weekly/2021/week1.csv')
i = 0
weekly_sum = pd.DataFrame()
amari_df = pd.DataFrame()
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if  not i==0: 
        next_week = pd.read_csv(f)
        amari_df = next_week.loc[next_week['Player']=='Tyreek Hill']
        print('Tyreek Hill week ',str(i+1))
        if(amari_df['PPRFantasyPoints'].size == 0):
            overall = overall + 0
        else:
            overall = overall + amari_df['PPRFantasyPoints'].values[0]
        print(amari_df['PPRFantasyPoints'])
        print('-----------------------------------------------------------------------')
        #week = pd.merge(week.iloc[:, 0:i+1],next_week[['Player','PPRFantasyPoints']], how='inner',suffixes=(str(i),str(i+1)), on='Player')
        #print(week.tail(5))
        #if i > 1:
        #    sum_column = weekly_sum['week'+str(i-1)]+week['PPRFantasyPoints'+str(i)]
        #    weekly_sum['week'+str(i)] = sum_column
        #print('-------------------------------------------- Week ------------------------------------------------')
        #print(week.head(5))
    else:
        week = pd.read_csv(f)
        week = week[['Player','PPRFantasyPoints']] 
        amari_df = week.loc[week['Player']=='Tyreek Hill']
        if(amari_df['PPRFantasyPoints'].size == 0):
            overall = overall + 0
        else:
            overall = overall + amari_df['PPRFantasyPoints'].values[0]
        print('Tyreek Hill week ',str(i+1))
        print(amari_df['PPRFantasyPoints'])
        #print('-----------------------------------------------------------------------')
        weekly_sum = week[['Player','PPRFantasyPoints']] 
        weekly_sum.rename(columns = {'PPRFantasyPoints':'week1'},inplace=True)
       # print('-------------------------------------------- Week ------------------------------------------------')
        #print(week.head(5))
    i = i+1
week.to_csv('weekly.csv')
weekly_sum.to_csv('weekly_sum.csv')
print('Overall', overall)
print('------------------------------------ WEEK -------------------------------------')
print(week.head(5))
print('------------------------------ WEEKLY SUM ---------------------------------------')
print(weekly_sum.head(5))
        #sum_column = week['week'+str(i)] + next_week['PPRFantasyPoints']
        #week['week'+str(i+1)] = sum_column
    #elif i == 1:
    #    next_week = pd.read_csv(f)
    #    #sum_column = week['PPRFantasyPoints'] + next_week['PPRFantasyPoints']
    #    week = pd.merge(week[['Player','PPRFantasyPoints']],next_week[['Player','PPRFantasyPoints']], how='left',suffixes=(str(i),str(i+1)), on='Player')
    #    #week['week'+str(i+1)] = sum_column
    #    print(week.head(5)) 


