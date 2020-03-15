from flask import Flask, render_template
import pandas as pd
import downloader
app = Flask(__name__)


@app.route('/')
def dashboard():
    
    df_symbol = list(set(df["SYMBOL"].values.tolist()))
    return render_template("dashboard.html",symbols = df_symbol)


@app.route("/dashboard/symbol/<string:name>")
def finder(name):
    
    
    df1 = df.loc[df['SYMBOL'] == name]
   
    return render_template("details.html",df_table = list(df1.itertuples(index=False)),name=name)
    
if __name__ == '__main__':
    c = downloader.nse_down()
    c.download()
    df = pd.read_csv("nse.csv")
    app.run(debug=True)
