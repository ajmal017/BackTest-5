
<p align="center">BackTest</p>
<p align="center">Open source backtesting tool.</p>

# Table of Content

+ [Getting Started](#getting-started)
+ [Adding New Features](#adding-new-features)
+ [Built With](#built-with)
+ [File Structure](#file-structure)
+ [Authors](#authors)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Ensure that python 3.6 or higher and pip are already installed on the system<br>
Further instruction for installing the above can be found at [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)<br>

### Installing

A step by step series of examples that tell you how to get a development env running

#### Cloning the repo

```bash

git clone <repo link>

```

#### Installing the dependencies

```bash

cd BackTest
sudo apt-get install python3-pip
pip install -r requirements.txt

```

If you want to use additional charting patterns(DOJI,MARUBOZU,etc) or indicators from the TA-Lib library, install the ta-lib python wrapper

```bash

pip install ta-lib

```

Note: This requires the underlying TA-Lib library to already be installed in your device. See [TA-Lib](https://mrjbq7.github.io/ta-lib/install.html) for further instructions.

Running the server

```bash

gunicorn --workers (2*<number of cores>+1) --bind 0.0.0.0:5000 wsgi:app

```

The application will now be running on https://<your_IP_Address>:5000/

## Adding New Features

To add new features (eg: new indicators, chart patterns), read the following steps:

1. Open the [Backtrader Indicator Reference Page](https://www.backtrader.com/docu/indautoref/), for TA-Lib Indicators open the [TA-Lib indicators Reference Page](https://www.backtrader.com/docu/talibindautoref/)

2. View the details of the indicator you wish to add.

3. Figure out the Function Name and the parameters required.

4. For Eg: MovingAverageSimple

    1. Details on Website:

        ```

        MovingAverageSimple
        Alias:

        SMA, SimpleMovingAverage
        Non-weighted average of the last n periods

        Formula:

        movav = Sum(data, period) / period
        See also:

        http://en.wikipedia.org/wiki/Moving_average#Simple_moving_average
        Lines:

        sma
        Params:

        period (30)
        PlotInfo:

        plot (True)

        plotmaster (None)

        legendloc (None)

        subplot (False)

        plotname ()

        plotskip (False)

        plotabove (False)

        plotlinelabels (False)

        plotlinevalues (True)

        plotvaluetags (True)

        plotymargin (0.0)

        plotyhlines ([])

        plotyticks ([])

        plothlines ([])

        plotforce (False)

        PlotLines:

        sma:

        ```

    2. Details to be understood:
        + Function Name(s)
            + The main function name is the header of the indicator. In this example it is MovingAverageSimple.
            + The alias section also indicates the other names the function can be referenced with. In this example it is SMA and SimpleMovingAverage.
            + The indicator can now be references as (Taking given example into consideration)

                ```python

                self.sma = bt.indicators.MovingAverageSimple()
                self.sma = bt.indicators.SMA()
                self.sma = bt.indicators.SimpleMovingAverage()

                ```

        + Parameters
            + The parameters required to be passed into the function call are stated under 'Params:'
            + In this example, there is only one parameter i.e period
            + If the parameter is not passed then the default value is used i.e the on in the brackets.
            + In this example, the default value of period is 30
            + The indicator can now be called along with the parameter(s) as

                ```python

                self.sma = bt.indicators.SMA(period=<time period of sma>)

                ```

    3. Writing the code:

        + Now that we have understood the name of the Function and the parameter it requires, we can add it into the code

        + First, decide a variable name to invoke the indicator eg: SimpleMovingAverage = sma, AverageDirectionalMovementIndex = adx, etc

        + Add this variable name into the indicator list in FetchData.py

            ```python

            indicator = ["sma", "ema", "adx", "atr", "rsi", "wma", "willR",
             "highr", "lowr", "trix", "dema", "tema", "zlema", "hma", "awo", "dma", "ichimoku", "bband", "vortex", "sto"]

            ```

        + We now need to create an initialsing statement for this indicator (SMA for example)

            + First initialise the count for this indicator in the indicators() function. This helps make sure that the names of the variable are always different.

            ```python

            sma_c = 0 

            ```

            + Add an if statement to identify if the indicator has been mentioned.

            ```python

            elif "sma" in exp:

            ```

            Note : The string in the "if" statement should be the same as the string added into the indicator list in the previous step.

            + Extract the parameters from the statement (For eg: period in SMA)

            ```python

            temp = exp[4:-1]

            ```

            + Finally, add the intialising statement

            ```python

            final += "\n\t\tself.sma_"+algot+ctype + \
                str(sma_c)+" = bt.indicators.SimpleMovingAverage(self.data,period="+period+")"

            ```

            + Increment the counter of the indicator

            ```python

            sma_c += 1

            ```

            algot - Type of expression i.e whether given indicator is a part of entry algo or exit algo.<br>
            ctype - Type of indicator i.e whether it is an independent indicator or has been used within another indicator eg: cov(sma,sma)<br>
            str(sma_c) - Append the counter of the variable to the variable name<br>

            These 3 things together ensure that the variable names are always unique.

        + Writing the conditional statement involving the indicator

            +  First initialise the count for this indicator in the expressions() function. This helps make sure that the names of the variable are always different.

            ```python

            sma_c = 0

            ```

            + Add an if statement to identify if the indicator has been mentioned.

            ```python

            elif("sma" in exp):

            ```

            + Finally add the indicator variable to the conditional Statement.

            ```python

            expression += " self.sma_"+ctype+str(sma_c)

            ```

            + Increment the counter for the indicator

            ```python

            sma_c += 1

            ```

            ctype - Type of expression i.e whether given indicator is a part of entry algo or exit algo.<br>
            str(sma_c) - Append the counter of the variable to the variable name<br>

            These 2 things together ensure that the variable mentioned in the conditional statement is the same as the indicator's initialising statement.

## Built With

+ [Python](https://www.python.org/) - Language
+ [Flask](https://palletsprojects.com/p/flask/) - Server Framework
+ [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server for UNIX
+ [Backtrader](https://www.backtrader.com/) - Backtesting module
+ [TA-Lib](http://ta-lib.org/) - Technical Analysis Library

## File Structure

/BackTest.py  : Main server code <br>
/templates/  : Website code <br>
/FetchData.py     : Backtesting Script <br>

## Authors

+ [Roshan James](https://github.com/sephiroth7712) <br>
+ Suraj <br>
+ [Mayur Kadam](https://github.com/mayurkadampro) <br>
+ Rajendra Vinod Patil<br>
