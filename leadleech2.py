#SOURCE = ALLEN BYERLY
#DATE = 08/04/2018
#VERSION = 0.1
#NOTES = THIS VERSION SCRAPES STANDARD INDEED TO PRODUCES LEADS OF THE TYPE "PEO"

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import csv

print ""
print "STARTING LEADLEECH"
print ""
#OPEN a lead list file and EXTRACT keyword lines
print 'Gathering Keywords' 
f = open('leadlist.txt', "r")
lines = f.readlines()
f.close()

#OPEN peo_leads.csv to store extracted leads
with open("lead_urls.csv", "wb") as f:
    #WRITE extracted leads to the csv file
    
    writer = csv.writer(f, dialect='excel')
    writer.writerow( ['url'] )

    print 'Generating Searches'
    for line in lines:
        print '- Leeching leads for keyword:' + line.strip()    
        #GENERATE sources
        urls = []
        for x in range(0,10):
            x=x*10
            urls.append("https://www.indeed.com/jobs?q=" + line.strip() + "&start=" + repr(x))

        url_list = []
        #PROCESS sources
        for url in urls:
            search_content = requests.get(url).content
            soup = BeautifulSoup(search_content, 'html.parser')
            
            
            #EXTRACT results from the the source
            results = soup.findAll('div', {'class' : re.compile('.*row.*result.*')})

            #TRANSFORM results into leads
            for result in results: 
                lead_keyword = line.strip()
                lead_link = "https://www.indeed.com" + result.a['href']
                lead_company = result.span.text.strip()
                try:
                    lead_company_profile =  "https://www.indeed.com" + result.span.a['href'] + '/about/'
                    company_content = requests.get(lead_company_profile).content

                    company_soup = BeautifulSoup(company_content, 'html.parser')
                    #print lead_company_profile
                    company_results = company_soup.find('dl', {'id' : 'cmp-company-details-sidebar'}).find('dt', text='Links')
                    try:
                        lead_site = company_results.find_next_sibling('dd').a['href']
                    except:
                        print 'no link'
                        lead_site = ''
                except:
                    print 'no link'
                    lead_site =  ''

                if lead_site:
                    if lead_site not in url_list:
                    
                        #print lead_site
                        #print url_list
                        url_list.append(lead_site)
                        writer.writerow([lead_site])
                        f.flush()

                
                lead_company = ''
                lead_link = ''
                lead_keyword = ''
                lead_site = ''
                #writer.writerow("company,joblink,keyword,link")

                #LOAD leads into the leads file
                #writer.writerow(lead_record.encode('utf-8'))
print ""
print "LEADLEECH COMPLETE"
print ""