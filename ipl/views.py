from django.shortcuts import render

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import pickle as pk
import numpy as np
import pandas as pd

def pred(home_team, away_team, city, toss_winner, toss_decision):
    results = convert_to_numerical_field(home_team, away_team, city, toss_winner, toss_decision)
    print(results)
    dbfile = open(r'/app/model.pkl', 'rb')    
    db = pk.load(dbfile)
    #y_pred=model.predict([results])
    y_pred=db.predict([results])


    #dbfile = open(r'C:\Users\paras\Desktop\WPL\cal.pkl', 'rb')    
    #cal = pk.load(dbfile)

    #db.predict([results])
    print(y_pred[0])

    global act_win_team
    
    if y_pred[0]==home_team and y_pred[0]==away_team:
    
        if y_pred[0]==1:
            act_win_team='MI'
        if y_pred[0]==2:
            act_win_team='KKR'    
        if y_pred[0]==3:
            act_win_team='RCB'     
        if y_pred[0]==4:
            act_win_team='DC'    
        if y_pred[0]==5:
            act_win_team='CSK'                
        if y_pred[0]==6:
            act_win_team='RR'     
        if y_pred[0]==7:
            act_win_team='DD'    
        if y_pred[0]==8:
            act_win_team='GL'             
        if y_pred[0]==9:
            act_win_team='KXIP'     
        if y_pred[0]==10:
            act_win_team='SRH'    
        if y_pred[0]==11:
            act_win_team='RPS' 
        if y_pred[0]==12:
            act_win_team='KTK'    
        if y_pred[0]==13:
            act_win_team='PW'       

    else:
        act_win_team=cal_ef_score(home_team,away_team)
        
    return act_win_team 
    


def convert_to_numerical_field(home_team, away_team, city, toss_winner, toss_decision):
    list = []
    if home_team == 'MI':
        list.append(1)
    if home_team == "KKR":
        list.append(2)
    if home_team == "RCB":
        list.append(3)
    if home_team == "DC":
        list.append(4)
    if home_team == "CSK":
        list.append(5)
    if home_team == "RR":
        list.append(6)
    if home_team == "DD":
        list.append(7)
    if home_team == "GL":
        list.append(8)
    if home_team == "KXIP":
        list.append(9)
    if home_team == "SRH":
        list.append(10)
    if home_team == "RPS":
        list.append(11)
    if home_team == "KTK":
        list.append(12)   
    if home_team == "PW":
        list.append(13)        
        
    if away_team== 'MI':
        list.append(1)
    if away_team== "KKR":
        list.append(2)
    if away_team== "RCB":
        list.append(3)
    if away_team== "DC":
        list.append(4)
    if away_team== "CSK":
        list.append(5)
    if away_team== "RR":
        list.append(6)
    if away_team== "DD":
        list.append(7)
    if away_team== "GL":
        list.append(8)
    if away_team== "KXIP":
        list.append(9)
    if away_team== "SRH":
        list.append(10)
    if away_team== "RPS":
        list.append(11)
    if away_team== "KTK":
        list.append(12)   
    if away_team== "PW":
        list.append(13)         
    if city=="Mumbai":
        list.append(1)
    if city=="Delhi":
        list.append(2)
    if city=="Pune":
        list.append(3)        
    if city=="Chandigarh":
        list.append(4)        
    if city=="Bangalore":
        list.append(5)
    if city=="Kolkata":
        list.append(6)
    if city=="Chennai":
        list.append(7)        
    if city=="Hyderabad":
        list.append(8)        
    if city=="Jaipur":
        list.append(9)
    if city=="Dharamsala":
        list.append(10)
    if city=="Rajkot":
        list.append(11)        
    if city=="Kanpur":
        list.append(12)        
    if city=="Johannesburg":
        list.append(13)
    if city=="Indore":
        list.append(14)
    if city=="Nagpur":
        list.append(15)        
    if city=="Dubai":
        list.append(16)        
    if city=="Durban":
        list.append(17)
    if city=="Kochi":
        list.append(18)
    if city=="Ranchi":
        list.append(19)        
    if city=="Ahmedabad":
        list.append(20)        
    if city=="Sharjah":
        list.append(21)
    if city=="Visakhapatnam":
        list.append(22)
    if city=="Raipur":
        list.append(23)        
    if city=="Abu Dhabi":
        list.append(24)  
    if city=="Bengaluru":
        list.append(25)
    if city=="Port Elizabeth":
        list.append(26)        
    if city=="Cape Town":
        list.append(27)          
    if city=="Centurion":
        list.append(28)
    if city=="East London":
        list.append(29)        
    if city=="Cuttack":
        list.append(30)          
    if city=="Bloemfontein":
        list.append(31)
    if city=="Kimberley":
        list.append(32)                 

    if toss_winner== 'MI':
        list.append(1)
    if toss_winner== "KKR":
        list.append(2)
    if toss_winner== "RCB":
        list.append(3)
    if toss_winner== "DC":
        list.append(4)
    if toss_winner== "CSK":
        list.append(5)
    if toss_winner== "RR":
        list.append(6)
    if toss_winner== "DD":
        list.append(7)
    if toss_winner== "GL":
        list.append(8)
    if toss_winner== "KXIP":
        list.append(9)
    if toss_winner== "SRH":
        list.append(10)
    if toss_winner== "RPS":
        list.append(11)
    if toss_winner== "KTK":
        list.append(12)   
    if toss_winner== "PW":
        list.append(13) 
        
    if toss_decision=="bat":
        list.append(0)
    if toss_decision=="field":    
        list.append(1)
        
    return list    
    
ef_data = pd.read_csv(r'/app/_team_rank.csv')

ef_data.replace(['Mumbai Indians','Kolkata Knight Riders','Royal Challengers Bangalore','Deccan Chargers','Chennai Super Kings',
                 'Rajasthan Royals','Delhi Daredevils','Delhi Capitals','Gujarat Lions','Kings XI Punjab',
                 'Sunrisers Hyderabad','Rising Pune Supergiants','Rising Pune Supergiant','Kochi Tuskers Kerala','Pune Warriors']
                ,['MI','KKR','RCB','DC','CSK','RR','DD','DD','GL','KXIP','SRH','RPS','RPS','KTK','PW'],inplace=True)

def cal_ef_score(home_team,away_team):
    
    home_score = list(ef_data.loc[ef_data['Team'] == home_team]['sum'])
    away_score = list(ef_data.loc[ef_data['Team'] == away_team]['sum'])
    if home_score > away_score :
        return home_team
    else:
        return away_team




@csrf_exempt
def index(request):
    if request.method == 'POST':
        global Home,Away,city,toss_winner,toss_decision,t_w ,result  
        Home = request.POST.get('Home') 
        Away=request.POST.get('Away')
        city=request.POST.get('city')
        toss_winner=request.POST.get('toss_winner')
        toss_decision=request.POST.get('toss_decision')
        
        if toss_winner=="Home Team":
            t_w=Home
        else:
            t_w=Away
        
        result=pred(Home,Away,city,t_w,toss_decision)
        
        context={"a":result}    
            
        return render(request,'ipl/index.html',context)    
    
    else:
        return render(request,'ipl/index.html')


















