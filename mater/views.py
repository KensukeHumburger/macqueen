from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

# Create your views here.
from django.http import HttpResponse
from django.template import loader
#import pandas as pd
#from pandas import DataFrame

# 機械学習
#import sklearn
#import pickle
#from sklearn.ensemble import RandomForestRegressor
#from sklearn.model_selection import train_test_split

#import xgboost as xgb
#from sklearn.model_selection import cross_validate, KFold

class Predmater:
    def __init__(self):
        self.params = {}
    
    def load_model(self):
        filename = 'mater/files/model_RF.pickle'
        model = pickle.load(open(filename, 'rb'))
        return model
    
    def load_data(self, params):
        dat = {'hi':[params['hi']]
        ,'low':[params['low']]
        ,'rain':[params['rain']]
        ,'snow':[params['snow']]
        }
        df = DataFrame(dat)
        df = df.assign(hi = pd.to_numeric(df.hi))
        df = df.assign(low = pd.to_numeric(df.low))
        df = df.assign(rain = pd.to_numeric(df.rain))
        df = df.assign(snow = pd.to_numeric(df.snow))
        return df

def index(request):
    return render(request, 'mater/index.html')

def predict_input(request):
    return render(request, 'mater/index.html')

def predict(request):
    if request.method == 'POST':
        hi = request.POST.get('hi')
        low = request.POST.get('low')
        rain = request.POST.get('rain')
        snow = request.POST.get('snow')

        #param
        params = {'hi':hi, 'low':low, 'rain':rain, 'snow':snow}
        print(params)
        
        pred =Predmater()
        model =pred.load_model()
        df = pred.load_data(params)
        mater = model.predict(df)
        
        percent = mater * 100
        for x in percent: # リストを[]なしで表示
            print(x)
        cancelrate = (round(x,1))

        return render(request, 'mater/predict_out.html',     # 使用するテンプレート
                  {'mater': cancelrate })         # テンプレートに渡すデータ
    else:
        return HttpResponse('predict')