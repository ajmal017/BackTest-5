from flask import (Flask, render_template, request,jsonify,render_template_string)
import requests
import eventlet
import FetchData as fd
from dotenv import load_dotenv
import json
import os
load_dotenv('.env')
app = Flask(__name__)
from flask_cors import CORS
app.config['SECRET_KEY'] = 'secret!'
CORS(app)

@app.route('/')
def hello_world():
    with open('Indicators.json','r') as f:
        Indicators = json.load(f)
        f.close()
    return render_template('home.html',Indicators=Indicators)

@app.route('/send_output/',methods=['GET'])
def send_output():
    name = request.args.get("name")
    print(name)
    output=[]
    with open("./Outputs/"+name+'.json','r') as f:
        output.append(json.load(f))
        f.close()
    name=[name]
    # print(output)
    output = zip(output,name)
    return render_template('output.html',output=output)


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
    company_name = x['stock_name'].split(",")
    print(company_name)
    company_done=[]
    output=[]
    for name in company_name:
        open("./Outputs/"+name+'.json', 'w').close()
        name = name.strip()
        fd.compute(entry_algo,exit_algo,stop_loss,take_profit,quantity,start_cash,start_year,start_month,start_day,end_year,end_month,end_day,start_time,end_time,name)
        os.system("python3 ./Scripts/"+name+".py")
        with open("./Outputs/"+name+'.json','r') as f:
            output.append(json.load(f))
            f.close()
        company_done.append(name)
        # emit('event')
    x=zip(output,company_done)
    print(company_name)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 



def main():
    app.debug = True
    app.threaded=True
    app.processes=2
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
