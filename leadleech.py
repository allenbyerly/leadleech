#SOURCE = ALLEN BYERLY
#DATE = 08/04/2018
#VERSION = 0.1
#NOTES = THIS VERSION SCRAPES STANDARD INDEED TO PRODUCES LEADS OF THE TYPE "PEO"

from BeautifulSoup import BeautifulSoup
import requests
import re

print ""
print "STARTING LEADLEECH"
print ""
#OPEN a lead list file and EXTRACT keyword lines
print 'Gathering Keywords' 
f = open('leadlist.txt', "r")
lines = f.readlines()
f.close()

#OPEN peo_leads.csv to store extracted leads
with open("peo_leads.csv", "w") as f:
    #WRITE extracted leads to the csv file
    f.write("company,link,keyword\n")
    
    print 'Generating Searches'
    for line in lines:
        print '- Leeching leads for keyword:' + line.strip()    
        #GENERATE sources
        urls = []
        for x in range(0,10):
            x=x*10
            urls.append("https://www.indeed.com/jobs?q=" + line.strip() + "&start=" + repr(x))

        #PROCESS sources
        for url in urls:
            html = requests.get(url).content
            soup = BeautifulSoup(html)
            
            #EXTRACT results from the the source
            results = soup.findAll('div', {'class' : re.compile('.*row.*result.*')})

            #TRANSFORM results into leads
            for result in results: 
                lead_keyword = line.strip()
                lead_link = "https://www.indeed.com" + result.a['href']
                lead_company = result.span.text


                lead_record = lead_company + "," + lead_link + "," + lead_keyword

                #LOAD leads into the leads file
                f.write(lead_record + "\n")
print ""
print "LEADLEECH COMPLETE"
print ""