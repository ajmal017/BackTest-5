# List of indicators currently supported by the script

indicator = ["sma", "ema", "adx", "atr", "rsi", "wma", "willR",
             "highr", "lowr", "trix", "dema", "tema", "zlema", "hma", "awo", "dma", "ichimoku", "bband", "vortex", "sto"]

'''
Write initialising statements for the indicators

eg: 
    self.sma_en0 = bt.indicators.SimpleMovingAverage(self.data,period=20)
    self.sma_en1 = bt.indicators.SimpleMovingAverage(self.data,period=30)

algo = input statement for the algorithm
ctype = blank unless indicator requires another indicator (recursive call) eg: cov(sma(10),sma(30))
algot = type of algo en = entry ex = exit
all variable names are distinct

'''
import os.path
from os import path

def indicators(algo, ctype, algot):
    # number of times an indicator has already been mentioned
    # used to ensure that all variable names are unique
    sma_c = 0
    ema_c = 0
    rsi_c = 0
    adx_c = 0
    atr_c = 0
    cov_c = 0
    cdo_c = 0
    cup_c = 0
    wma_c = 0
    dema_c = 0
    tema_c = 0
    h_c = 0
    l_c = 0
    o_c = 0
    willr_c = 0
    trix_c = 0
    zlema_c = 0
    hma_c = 0
    awo_c = 0
    dma_c = 0
    ichi_c = 0
    bband_c = 0
    vort_c = 0
    sto_c = 0
    final = ""
    for exp in algo:
        if "cup" in exp:
            cups = "\n\t\tself.cup_"+algot+str(cup_c)+" = bt.ind.CrossUp("
            flag = 0
            temp = exp[4:-1].split(",")
            x = [temp[0]]
            y = [temp[1]]
            if(temp[0][0:3] in indicator):
                final += indicators(x, "cup0"+str(cup_c), algot)
                cups += "self." + \
                    indicator[indicator.index(
                        temp[0][0:3])]+"_"+algot+"cup0"+str(cup_c)+"0,"
            elif(temp[0] == "close"):
                cups += "self.dataclose,"
            else:
                cups += temp[0]+","
            if(temp[1][0:3] in indicator):
                final += indicators(y, "cup1"+str(cup_c), algot)
                cups += "self." + \
                    indicator[indicator.index(
                        temp[1][0:3])]+"_"+algot+"cup1"+str(cup_c)+"0)"
            elif(temp[1] == "close"):
                cups += "self.dataclose)"
            else:
                cups += temp[1]+")"
            final += cups
            cup_c += 1
        elif "cdo" in exp:
            cdos = "\n\t\tself.cdo_"+algot+str(cdo_c)+" = bt.ind.CrossDown("
            flag = 0
            temp = exp[4:-1].split(",")
            x = [temp[0]]
            y = [temp[1]]
            if(temp[0][0:3] in indicator):
                final += indicators(x, "cdo0"+str(cdo_c), algot)
                cdos += "self." + \
                    indicator[indicator.index(
                        temp[0][0:3])]+"_"+algot+"cdo0"+str(cdo_c)+"0,"
            elif(temp[0] == "close"):
                cdos += "self.dataclose,"
            else:
                cdos += temp[0]+","
            if(temp[1][0:3] in indicator):
                final += indicators(y, "cdo1"+str(cdo_c), algot)
                cdos += "self." + \
                    indicator[indicator.index(
                        temp[1][0:3])]+"_"+algot+"cdo1"+str(cdo_c)+"0)"
            elif(temp[1] == "close"):
                cdos += "self.dataclose)"
            else:
                cdos += temp[1]+")"
            final += cdos
            cdo_c += 1
        elif "cov" in exp:
            covs = "\n\t\tself.cov_"+algot+str(cov_c)+" = bt.ind.CrossOver("
            flag = 0
            temp = exp[4:-1].split(",")
            x = [temp[0]]
            y = [temp[1]]
            if(temp[0][0:3] in indicator):
                final += indicators(x, "cov0"+str(cov_c), algot)
                covs += "self." + \
                    indicator[indicator.index(
                        temp[0][0:3])]+"_"+algot+"cov0"+str(cov_c)+"0,"
            elif(temp[0] == "close"):
                covs += "self.dataclose,"
            else:
                covs += temp[0]+","
            if(temp[1][0:3] in indicator):
                final += indicators(y, "cov1"+str(cov_c), algot)
                covs += "self." + \
                    indicator[indicator.index(
                        temp[1][0:3])]+"_"+algot+"cov1"+str(cov_c)+"0)"
            elif(temp[1] == "close"):
                covs += "self.dataclose)"
            else:
                covs += temp[1]+")"
            final += covs
            cov_c += 1
        elif "sto" in exp:
            temp = exp[4:-1].split(",")
            period = temp[0]
            periodf = temp[1]
            periods = temp[2]
            final += "\n\t\tself.sto_"+algot + \
                str(sto_c)+"= bt.indicators.Stochastic(period="+period + \
                ",period_dfast="+periodf+",period_dslow="+periods+")"
            sto_c += 1
        elif "vortex" in exp:
            period = exp[7:-1]
            final += "\n\t\tself.vortex_"+algot + \
                str(vort_c)+" = bt.indicators.Vortex(period="+period+")"
            vort_c += 1
        elif "bband" in exp:
            temp = exp[6:-1].split(",")
            period = temp[0]
            devfactor = temp[1]
            final += "\n\t\tself.bband_"+algot + \
                str(bband_c)+" = bt.indicators.BollingerBands(period=" + \
                period+",devfactor="+devfactor+")"
            bband_c += 1
        elif "ichimoku" in exp:
            temp = exp[9:-1].split(",")
            tenkan = temp[0]
            kijun = temp[1]
            senkou = temp[2]
            senkou_lead = temp[3]
            chikou = temp[4]
            final += "\n\t\tself.ichimoku_"+algot+str(ichi_c)+"= bt.indicators.Ichimoku(tenkan=" + \
                tenkan+",kijun="+kijun+",senkou="+senkou + \
                ",senkou_lead="+senkou_lead+",chikou="+chikou+")"
            ichi_c += 1
        elif "dma" in exp:
            temp = exp[4:-1].split(",")
            period = temp[0]
            gainlimit = temp[1]
            hperiod = temp[2]
            final += "\n\t\tself.dma_"+algot + \
                str(dma_c)+"= bt.indicators.DicksonMovingAverage(period=" + \
                period+",gainlimit="+gainlimit+",hperiod="+hperiod+")"
            dma_c += 1
        elif "awo" in exp:
            temp = exp[3:-1].split(",")
            x = temp[0]
            y = temp[1]
            final += "\n\t\tself.awo_"+algot + \
                str(awo_c)+"= bt.indicators.AwesomeOscillator(fast = "+x+"slow = "+y+")"
            awo_c = +1
        elif "hma" in exp:
            period = exp[4:-1]
            final += "\n\t\tself.hma_"+algot + \
                str(hma_c)+" = bt.indicators.HullMovingAverage(period = "+period+")"
            hma_c += 1
        elif "zlema" in exp:
            temp = exp[6:-1]
            final += "\n\t\tself.zlema_"+algot+ctype + \
                str(zlema_c)+"=bt.ind.ZeroLagExponentialMovingAverage(period="+temp+")"
            zlema_c += 1
        elif "trix" in exp:
            period = exp[5:-1]
            final += '\n\t\tself.trix_'+algot + \
                str(trix_c)+" = bt.indicators.Trix(period="+period+")"
            trix_c += 1
        elif "willR" in exp:
            period = exp[6:-1]
            final += "\n\t\tself.willR_"+algot + \
                str(willr_c)+"= bt.indicators.WilliamsR(period="+period+")"
            willr_c += 1
        elif "dema" in exp:
            period = exp[5:-1]
            final += "\n\t\tself.dema_"+algot + \
                str(dema_c)+" = bt.indicators.DoubleExponentialMovingAverage(period="+period+")"
            dema_c += 1
        elif "tema" in exp:
            period = exp[5:-1]
            final += "\n\t\tself.tema_"+algot + \
                str(tema_c)+" = bt.indicators.TripleExponentialMovingAverage(period="+period+")"
            tema_c += 1
        elif "highr" in exp:
            period = exp[6:-1]
            final += "\n\t\tself.h_"+algot+ctype + \
                str(h_c)+" = bt.ind.Highest(self.data.high,period="+period+")"
            h_c += 1
        elif "lowr" in exp:
            period = exp[5:-1]
            final += "\n\t\tself.l_"+algot+ctype + \
                str(l_c)+" = bt.ind.Lowest(self.data.low,period="+period+")"
            l_c += 1
        elif "sma" in exp:
            period = exp[4:-1]
            final += "\n\t\tself.sma_"+algot+ctype + \
                str(sma_c)+" = bt.indicators.SimpleMovingAverage(self.data,period="+period+")"
            sma_c += 1
        elif "ema" in exp:
            period = exp[4:-1]
            final += "\n\t\tself.ema_"+algot+ctype + \
                str(ema_c)+" = bt.indicators.ExponentialMovingAverage(self.data,period="+period+")"
            ema_c += 1
        elif "adx" in exp:
            temp = exp[4:-1]
            final += "\n\t\tself.adx_"+algot+ctype + \
                str(adx_c)+" = bt.ind.ADX(self.data,period="+temp+")"
            adx_c += 1
        elif "rsi" in exp:
            temp = exp[4:-1]
            final += "\n\t\tself.rsi_"+algot+ctype + \
                str(rsi_c)+" = bt.indicators.RelativeStrengthIndex(self.data,period="+temp+")"
            rsi_c += 1
        elif "atr" in exp:
            temp = exp[4:-1]
            final += "\n\t\tself.atr_"+algot+ctype + \
                str(rsi_c)+" = bt.ind.ATR(self.data,period="+temp+")"
            atr_c += 1
        elif "wma" in exp:
            temp = exp[4:-1]
            final += "\n\t\tself.wma_"+algot+ctype + \
                str(wma_c)+" = bt.indicators.WMA(self.data,period="+temp+")"
            wma_c += 1

    return final


'''
Prepare conditional if statements for entry and exit algorithms

eg :
    entry:
        if self.sma_en0> self.sma_en1:
    exit:
        if self.dataclose[0]> 2000:
algo = input statement for the algorithm
ctype = type of algo en = entry ex = exit
'''


def expressions(conditions, ctype):
    # number of times an indicator has already been mentioned
    # used to ensure that all variable names are unique
    sma_c = 0
    ema_c = 0
    rsi_c = 0
    adx_c = 0
    atr_c = 0
    cov_c = 0
    cdo_c = 0
    cup_c = 0
    wma_c = 0
    dema_c = 0
    tema_c = 0
    h_c = 0
    l_c = 0
    willr_c = 0
    trix_c = 0
    zlema_c = 0
    hma_c = 0
    awo_c = 0
    dma_c = 0
    ichi_c = 0
    bband_c = 0
    vort_c = 0
    sto_c = 0
    expression = ""
    for exp in conditions:
        if(exp == "close"):
            expression += " self.dataclose[0]"
        elif(exp == "high"):
            expression += " self.data.high"
        elif(exp == "low"):
            expression += " self.data.low"
        elif(exp == "open"):
            expression += " self.data.open"
        elif(exp == "<"):
            expression += "<"
        elif(exp == ">"):
            expression += ">"
        elif(exp == "="):
            expression += "="
        elif(exp == "and"):
            expression += " and"
        elif(exp == "or"):
            expression += " or"
        elif("bband" in exp):
            expression += " self.bband_"+ctype+str(bband_c)
            bband_c += 1
        elif("cup" in exp):
            expression += " self.cup_"+ctype+str(cup_c)
            cup_c += 1
        elif("cov" in exp):
            expression += " self.cov_"+ctype+str(cov_c)
            cov_c += 1
        elif("cdo" in exp):
            expression += " self.cdo_"+ctype+str(cdo_c)
            cdo_c += 1
        elif("sto" in exp):
            expression += " self.sto_"+ctype+str(sto_c)
            sto_c += 1
        elif("ichimoku" in exp):
            expression += " self.ichimoku_"+ctype+str(ichi_c)
            ichi_c += 1
        elif("zlema" in exp):
            expression += " self.zlema_"+ctype+str(zlema_c)
            zlema_c += 1
        elif("dema" in exp):
            expression += " self.dema_"+ctype+str(dema_c)
            dema_c += 1
        elif("tema" in exp):
            expression += " self.tema_"+ctype+str(tema_c)
            tema_c += 1
        elif("sma" in exp):
            expression += " self.sma_"+ctype+str(sma_c)
            sma_c += 1
        elif("ema" in exp):
            expression += " self.ema_"+ctype+str(ema_c)
            ema_c += 1
        elif("dma" in exp):
            expression += " self.dma_"+ctype+str(dma_c)
            dma_c += 1
        elif("rsi" in exp):
            expression += " self.rsi_"+ctype+str(rsi_c)
            rsi_c += 1
        elif("adx" in exp):
            expression += " self.adx_"+ctype+str(adx_c)
            adx_c += 1
        elif("atr" in exp):
            expression += " self.atr_"+ctype+str(atr_c)
            atr_c += 1
        elif("wma" in exp):
            expression += " self.wma_"+ctype+str(wma_c)
            wma_c += 1
        elif("hma" in exp):
            expression += " self.hma_"+ctype+str(hma_c)
            hma_c += 1
        elif("highr" in exp):
            expression += " self.h_"+ctype+str(h_c)
            h_c += 1
        elif("lowr" in exp):
            expression += " self.l_"+ctype+str(l_c)
            l_c += 1
        elif("willR" in exp):
            expression += " self.willR_"+ctype+str(willr_c)
            willr_c += 1
        elif("trix" in exp):
            expression += " self.trix_"+ctype+str(trix_c)
            trix_c += 1
        elif("awo" in exp):
            expression += " self.awo_"+ctype+str(awo_c)
            awo_c += 1
        elif("vort" in exp):
            expression += " self.vortex_"+ctype+str(vort_c)
            vort_c += 1
        else:
            expression += " " + exp
    return expression

# get input from server and form script


def compute(enalgo, exalgo, stop_loss, take_profit, quantity, sc, sy, sm, sd, ey, em, ed,start_time,end_time,broker_commission, name,file_name,data_file_name):
    # split the algo with " "
    enalgo = enalgo.split()
    exalgo = exalgo.split()

    #import statements
    prog = "from __future__ import (absolute_import, division, print_function,unicode_literals) \nimport datetime \nimport backtrader as bt \nimport json\nimport yfinance as yf \noutput=[]\nclass TestStrategy(bt.Strategy):\n\tdef log(self, txt, price,dt=None):\n\t\tdt = dt or self.datas[0].datetime.date(0)\n\t\tnd = {'date':str(dt.isoformat()),'action':txt,'price':price}\n\t\toutput.append(nd)"
    prog += "\n\tdef __init__(self):"

    # initialising stop loss and take profit
    prog += "\n\t\tself.dataclose = self.datas[0].close\n\t\tself.order = None\n\t\tself.stop_loss="+str(float(
        stop_loss)/100)+"\n\t\tself.stop_price=0\n\t\tself.take_profit="+str(float(take_profit)/100)+"\n\t\tself.take_price=0"

    # for initialising statements for indicators mentioned in entry and exit algorithms
    prog += indicators(enalgo, "", "en")
    prog += indicators(exalgo, "", "ex")

    # statements common in all scripts
    prog += "\n\tdef notify_order(self, order):\n\t\tif order.status in [order.Submitted, order.Accepted]:\n\t\t\treturn\n\t\tif order.status in [order.Completed]:\n\t\t\tif order.isbuy():\n\t\t\t\tself.log('BUY EXECUTED',round(order.executed.price,3))"
    prog += "\n\t\t\t\tself.stop_price = order.executed.price* (1.0 - self.stop_loss)\n\t\t\t\tself.take_price = order.executed.price*(1.0 + self.take_profit)"
    prog += "\n\t\t\telif order.issell():\n\t\t\t\tself.log('SELL EXECUTED',round(order.executed.price,3))\n\t\telif order.status in [order.Canceled, order.Margin, order.Rejected]:\n\t\t\treturn\n\t\tself.order=None"
    if(float(broker_commission)!=0):
        prog += "\n\tdef notify_trade(self,trade):\n\t\tif not trade.isclosed:\n\t\t\treturn\n\t\tself.log('OPERATION GROSS PROFIT',round(trade.pnl,3))\n\t\tself.log('OPERATION NET PROFIT',round(trade.pnlcomm,3))"
    prog += "\n\tdef next(self):"
    start_time=start_time.split(":")
    end_time=end_time.split(":")
    # prog += "\n\t\tif self.data.datetime.time() < datetime.time("+start_time[0]+","+ start_time[1]+"):\n\t\t\treturn"
    # prog += "\n\t\telif self.data.datetime.time() > datetime.time("+end_time[0]+","+ end_time[1]+"):\n\t\t\treturn"
    prog += "\n\t\tself.log('Close',self.dataclose[0])\n\t\tif self.order:\n\t\t\treturn\n\t\tif not self.position:"

    # form conditional if statements based on extry algorithm
    prog += "\n\t\t\tif" + expressions(enalgo, "en") + ":"
    prog += "\n\t\t\t\tself.log('BUY TRIGGERED',self.dataclose[0])\n\t\t\t\tself.buy(size=" + \
        quantity+")\n\t\telse:"

    # form conditional if statement for take profit
    prog += "\n\t\t\tif self.take_price <= self.dataclose[0]:\n\t\t\t\tself.log('TAKE PROFIT TRIGGERED', self.dataclose[0])\n\t\t\t\tself.sell(size="+quantity+")"

    # form conditional if statement based on exit algorithm
    prog += "\n\t\t\telif" + expressions(exalgo, "ex") + ":"
    prog += "\n\t\t\t\tself.log('SELL TRIGGERED',self.dataclose[0])\n\t\t\t\tself.sell(size="+quantity+")"

    # form conditional if statement for stop loss
    prog += "\n\t\t\telif self.stop_price >= self.dataclose[0]:\n\t\t\t\tself.log('STOP LOSS TRIGGERED', self.dataclose[0])\n\t\t\t\tself.sell(size="+quantity+")"

    # define name of stock, starting cash and time period
    prog += "\nif __name__ == '__main__':"
    prog += "\n\tcerebro = bt.Cerebro(preload=True,runonce=True)\n\tcerebro.addstrategy(TestStrategy)\n\tcerebro.broker.setcash("+sc+")"
    if(float(broker_commission)!=0):
        prog += "\n\tcerebro.broker.setcommission(commission="+str(float(broker_commission)/100)+")"
    prog += "\n\tbroker_commission="+broker_commission
    if(path.exists("./Data/"+data_file_name+".csv")==False):
        prog += "\n\ttemp_data= yf.download('"+name+"', start = '"+sy+"-"+sm+"-"+sd+"', end = '"+ey +"-"+em+"-"+ed+"')"
        prog += "\n\ttemp_data.to_csv('./Data/"+data_file_name+".csv')"
    prog += "\n\tdata = bt.feeds.YahooFinanceCSVData(dataname = './Data/"+data_file_name+".csv',name = '"+name+"' ,reverse=False)"
    prog += "\n\tx = datetime.datetime("+sy+","+sm+","+sd+")"
    prog += "\n\td = {'date':str(x.date().isoformat()),'action':'Starting Portfolio Value','price':"+sc+"}"
    prog += "\n\toutput.append(d)"
    prog += "\n\tcerebro.adddata(data)\n\tcerebro.run()\n\tep = cerebro.broker.getvalue()\n\tx = datetime.datetime("+ey+","+em+","+ed+")"
    prog += "\n\td = {'date':str(x.date().isoformat()),'action':'Final Portfolio Value','price':round(ep,3)}\n\toutput.append(d)\n\toutput=json.dumps(output)"
    prog += "\n\twith open('./Outputs/"+file_name+".json','w') as f:\n\t\tf.write(output)\n\t\tf.close()\n\t#cerebro.plot()"

    with open("./Scripts/"+file_name+'.py', 'w') as f:
        f.write(prog)
        f.close()