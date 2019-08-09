from flask import (Flask, render_template, request,jsonify,render_template_string)
from flask_jsglue import JSGlue
import requests
import eventlet
import FetchData as fd
from dotenv import load_dotenv
import json
import os
from os import path
import hashlib
load_dotenv('.env')
app = Flask(__name__)
from flask_cors import CORS
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
jsglue = JSGlue(app)
@app.route('/')
def hello_world():
    with open('Indicators.json','r') as f:
        Indicators = json.load(f)
        f.close()
    return render_template('home.html',Indicators=Indicators)

@app.route('/send_output',methods=['POST'])
def send_output():
    x = request.get_json()
    entry_algo = x['entry_algo']
    exit_algo = x['exit_algo']
    stop_loss = x['stop_loss']
    take_profit = x['take_profit']
    quantity = x['quantity']
    start_cash = x['start_cash']
    start_year = x['start_year']
    start_month = x['start_month']
    start_day = x['start_day']
    end_year = x['end_year']
    end_month = x['end_month']
    end_day = x['end_day']
    start_time = x['start_time']
    end_time = x['end_time']
    broker_commission = x['broker_commission']
    stock_name = x['stock_name']
    output_data=[]
    output=[]
    temp1 = entry_algo+exit_algo+stop_loss+take_profit+quantity+start_cash+start_year+start_month+start_day+end_year+end_month+end_day+"0"
    temp2 = entry_algo+exit_algo+stop_loss+take_profit+quantity+start_cash+start_year+start_month+start_day+end_year+end_month+end_day+broker_commission
    file_name_without_brokerage = stock_name + (hashlib.md5(temp1.encode())).hexdigest()
    file_name_with_brokerage = stock_name + (hashlib.md5(temp2.encode())).hexdigest()
    with open("./Outputs/"+file_name_without_brokerage+'.json','r') as f:
        output.append(json.load(f))
        f.close()
    with open("./Outputs/"+file_name_with_brokerage+'.json','r') as f:
        output.append(json.load(f))
        f.close()
    name=[stock_name]
    typef=['Without Brokerage','With Brokerage']
    output_data.append({"company_name":stock_name,"Outputs":
    [{"Type":"Without Brokerage","Output":output[0]},{"Type":"With Brokerage","Output":output[1]}]})
    return json.dumps({'success':True,'data':render_template('output.html',output=output_data)}), 200, {'Content-Type':'application/json'} 


@app.route('/send_algo', methods=['POST'])
def send_algo():
    x = request.get_json()
    entry_algo = x['entry_algo']
    exit_algo = x['exit_algo']
    stop_loss = x['stop_loss']
    take_profit = x['take_profit']
    quantity = x['quantity']
    start_cash = x['start_cash']
    start_year = x['start_year']
    start_month = x['start_month']
    start_day = x['start_day']
    end_year = x['end_year']
    end_month = x['end_month']
    end_day = x['end_day']
    start_time = x['start_time']
    end_time = x['end_time']
    broker_commission = x['broker_commission']
    company_name = x['stock_name'].split(",")
    output_data=[]
    for name in company_name:
        temp1 = entry_algo+exit_algo+stop_loss+take_profit+quantity+start_cash+start_year+start_month+start_day+end_year+end_month+end_day+"0"
        temp2 = entry_algo+exit_algo+stop_loss+take_profit+quantity+start_cash+start_year+start_month+start_day+end_year+end_month+end_day+broker_commission
        file_name_without_brokerage = name + (hashlib.md5(temp1.encode())).hexdigest()
        file_name_with_brokerage = name + (hashlib.md5(temp2.encode())).hexdigest()
        file_name = [file_name_without_brokerage,file_name_with_brokerage]
        broker_type = [0,float(broker_commission)]
        i=0
        for i in range(0,2):
            output=[]
            if(path.exists("./Outputs/"+file_name[i]+'.json')):
                if(broker_type[i]==0):
                    with open("./Outputs/"+file_name[i]+'.json','r') as f:
                        output.append(json.load(f))
                        f.close()
                    output_data.append({"company_name":name,"Type":"Without Brokerage","Output":output[0]})
                else:
                    with open("./Outputs/"+file_name[i]+'.json','r') as f:
                        output.append(json.load(f))
                        f.close()
                    output_data.append({"company_name":name,"Type":"With Brokerage","Output":output[0]})
            else:
                if(broker_type[i]==0):
                    open("./Outputs/"+file_name[i]+'.json', 'w').close()
                    name = name.strip()
                    fd.compute(entry_algo,exit_algo,stop_loss,take_profit,quantity,start_cash,start_year,start_month,start_day,end_year,end_month,end_day,start_time,end_time,str(broker_type[i]),name,file_name[i])
                    os.system("python3 ./Scripts/"+file_name[i]+".py")
                    with open("./Outputs/"+file_name[i]+'.json','r') as f:
                        output.append(json.load(f))
                        f.close()
                    output_data.append({"company_name":name,"Type":"Without Brokerage","Output":output[0]})
                else:
                    open("./Outputs/"+file_name[i]+'.json', 'w').close()
                    name = name.strip()
                    fd.compute(entry_algo,exit_algo,stop_loss,take_profit,quantity,start_cash,start_year,start_month,start_day,end_year,end_month,end_day,start_time,end_time,str(broker_type[i]),name,file_name[i])
                    os.system("python3 ./Scripts/"+file_name[i]+".py")
                    with open("./Outputs/"+file_name[i]+'.json','r') as f:
                        output.append(json.load(f))
                        f.close()
                    output_data.append({"company_name":name,"Type":"With Brokerage","Output":output[0]})
    return json.dumps({'success':True,'data':output_data}), 200, {'Content-Type':'application/json'} 



def main():
    app.debug = True
    app.threaded=True
    app.processes=2
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
