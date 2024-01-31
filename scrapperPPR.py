import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

pd.set_option('display.max_columns', None)

URL = 'https://fantasy.nfl.com/research/scoringleaders?offset=1&position=O&sort=pts&statCategory=stats&statSeason=2021&statType=seasonStats&statWeek=6#researchScoringLeaders=researchScoringLeaders%2C%2Fresearch%2Fscoringleaders%253Fposition%253DO%2526sort%253Dpts%2526statCategory%253Dstats%2526statSeason%253D2020%2526statType%253DseasonStats%2Creplace'

res = requests.get(URL)
soup = BS(res.content, 'html.parser')
stats_grid  = soup.find_all('table', class_='tableType-player hasGroups')

print('Table', stats_grid)
#df = pd.read_html(str(stats_grid))[0]
#df.columns = df.columns.droplevel(level=0)
#print('Data frame: ', df)
'''
#removing filler rows
df = df.loc[df['Player'] != 'Player']

#fixing player names that have astericks
df['Player'] = df['Player'].apply(lambda x: x.split('*')[0].strip())

#Column names:
#Player,Tm,Pos,Age,G,GS,Tgt,Rec,PassingYds,PassingTD,PassingAtt,RushingYds,
#RushingTD,RushingAtt,ReceivingYds,ReceivingTD,FantasyPoints,Int,Fumbles,FumblesLost

df['PassingYds'] = df['Yds'].iloc[:, 0]
df['RushingYds'] = df['Yds'].iloc[:, 1]
df['ReceivingYds'] = df['Yds'].iloc[:, 2]

df['PassingTD'] = df['TD'].iloc[:, 0]
df['RushingTD'] = df['TD'].iloc[:, 1]
df['ReceivingTD'] = df['TD'].iloc[:, 2]

df['PassingAtt'] = df['Att'].iloc[:, 0]
df['RushingAtt'] = df['Att'].iloc[:, 1]

df = df.rename(columns={
    'FantPos': 'Pos', 'FantPt': 'Standard', 'Fmb': 'Fumbles', 'FL': 'FumblesLost'
})

df = df[[
    'Player','Tm','Pos','Age','G','GS','Tgt','Rec','PassingYds','PassingTD','PassingAtt',
    'RushingYds','RushingTD','RushingAtt','ReceivingYds','ReceivingTD','Standard','PPR',
    'Int','Fumbles','FumblesLost'
]]

df.to_csv('localData/2023/2023_week1.csv', index=False)
'''

