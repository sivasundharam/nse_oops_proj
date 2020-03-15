import requests
import zipfile
import pandas as pd
from datetime import date,timedelta
import time
import os


class nse_down:

    def __init__(self):
        self.__url = "https://archives.nseindia.com/content/historical/EQUITIES/"   # url for download
        self.__li = ["SYMBOL","SERIES","OPEN","HIGH","LOW","CLOSE","LAST","PREVCLOSE","TOTTRDQTY","TIMESTAMP"] #parsing the columns
        self.__alldf = pd.DataFrame(columns=self.__li)

    def csv_creator(self):
        self.__alldf = self.__alldf.append(self.df,ignore_index=True)

    def csv_pars(self):
        '''parsing the csv fiel'''
        self.df = pd.read_csv("./"+self.fold_name+".csv")
        self.df = self.df.loc[:,self.__li]
        self.df.to_csv("./"+self.fold_name+".csv",index = False)
        self.csv_creator()
        with zipfile.ZipFile(self.fil_name, 'w') as zip_ref:
            zip_ref.write(self.fold_name+".csv")
        #os.remove(self.fil_name)
        os.remove("./"+self.fold_name+".csv")
        


    
    def zip_extractor(self):
        '''extracting the zip file'''
        self.fold_name = self.fil_name.split(".csv")[0]
        open(self.fil_name,"wb").write(self.tempfil.content)
        with zipfile.ZipFile(self.fil_name, 'r') as zip_ref:
            zip_ref.extractall()
        
        self.csv_pars()

    def download(self):
        ''' main function which will start the download process'''
        tem_t = date.today()
        i = 0
        while i<30:
            if tem_t.weekday() < 5:
                try:
                    tem_va = tem_t.strftime("%Y")+"/"+tem_t.strftime("%b").upper()+"/cm"+tem_t.strftime("%d%b%Y").upper()+"bhav.csv.zip"
                    self.tempfil = requests.get(self.__url+tem_va)                
                    self.fil_name = tem_va.split("/")[2]
                    self.zip_extractor()
                    i +=1
                    tem_t -= timedelta(days=1)
                except Exception as e:
                    tem_t -= timedelta(days=1)
            else:
                tem_t -= timedelta(days=1)
        self.__alldf.to_csv("nse.csv",index = False)
            
        
if __name__ == "__main__":
    c = nse_down()
    c.download()
        
    
