# leadleech
scraper used to extract leads from various sources


* Version: 0.2
* Date: 2018-9-20
* Author: Allen Byerly
* License: Apache version 2

leadleach is a python script used to generate leads by scraping sources for leads based on pre-determined rules.

In this version:
leadleech1.py does:
- Run a search for predefined lists of PEOs and keywords.
- Need name of company, link to posting and the PEO or keyword added to a csv.
leadleech2.py does:
- Run a search for predefined lists of PEOs and keywords.
- Generates a list of urls


## requirements
1. Install Python
- For a Mac Python is alredy included

- For instructions on a PC go to: [Installation Instructions](https://github.com/pettarin/python-on-windows/)

2. Install pip
- For a Mac:
```
sudo easy_install pip
```

- For a PC once Python is installed download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run 
```
$ python get-pip.py
```

3.  Install Required Packages
From the leadllech folder run the following command
```
$ sudo pip install bs4
$ sudo pip install requests
$ sudo pip install re
$ sudo pip install pandas
$ sudo pip install csv
```

## usage

#### step 1: add keywords to the leadlist.txt file in the leadleech folder

#### step 2: open a command prompt and goto the leadleech folder:
Example:
```
$ cd C:\leadleech
```

#### step 3: for a list of companies run leadleach.py:
```
$ python leadleech.py
```
## OR

#### step 3: for a list of urls run leadleach2.py:
```
$ python leadleech2.py
```
#### step 4: open the results in lead_urls.csv using your favorite spreadsheet tool (gdocs, excel, or just a text editor)

