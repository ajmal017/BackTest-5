
<p align="center">BackTest</p>
<p align="center">Open source platform for sharing legal document templates.</p>

# Table of Content
+ [Getting Started](#getting_started)
+ [Built With](#built_with)
+ [File Structure](#file_structure)
+ [Authors](#authors)


## Getting Started<a name="getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
Ensure that python 3.7 and pip are already installed on the system
Further instruction for installing the above can be found at [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)

### Installing

A step by step series of examples that tell you how to get a development env running

Cloning the repo
```
$ git clone <repo link>
```
Installing the dependencies
```
$ cd BackTest
$ pip install -r requirements.txt
```
Running the server
```
$ python BackTest.py
```
The application will now be running on https://localhost:5000/

## Built With<a name="built_with"></a>
+ [Python](https://www.python.org/) - Language
+ [Flask](https://palletsprojects.com/p/flask/) - Server Framework
+ [Backtrader](https://www.backtrader.com/) - Backtesting module

## File Structure <a name="file_structure"></a>
/BackTest.py  : Main server code <br>
/templates/  : Website code <br>
/FetchData.py     : Backtesting Script <br>

## Authors<a name="authors"></a>
+ [Roshan James](https://github.com/sephiroth7712) <br>
+ [Mayur Kadam](https://github.com/mayurkadampro) <br>
+ Rajendra Vinod Patil<br>
