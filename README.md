# leadleech
scraper used to extract leads from various sources

-------------------------------------
Version: 0.1
Date: 2018-8-8
Author: Allen Byerly
License: Apache version 2
-------------------------------------

leadleach is a python script used to generate leads by scraping sources for leads based on pre-determined rules.

In this version:
- Run a search for predefined lists of PEOs and keywords.
- Need name of company, link to posting and the PEO or keyword added to a csv.

## requirements
1. Install Python
For instructions go to: [Installation Instructions](https://github.com/pettarin/python-on-windows/)

2. Install pip
Once Python is installed download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run 
```
$ python get-pip.py
```

3.  Install BeautifulSoup

## usage

#### step 1: add keywords to the leadlist.txt file in the leadleech folder

#### step 2: open a command prompt and goto the leadleech folder:
Example:
```
$ cd C:\leadleech
```

#### step 3: run leadleach.py:
```
$ python leadleech.py
```

#### step 4: open the results in peo_leads.csv using your favorite spreadsheet tool (gdocs, excel, or just a text editor)

