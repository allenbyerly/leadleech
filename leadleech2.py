#SOURCE = ALLEN BYERLY
#DATE = 08/04/2018
#VERSION = 0.1
#NOTES = THIS VERSION SCRAPES STANDARD INDEED TO PRODUCES LEADS OF THE TYPE "PEO"

from BeautifulSoup import BeautifulSoup
import requests
import re



f = open('leadlist.txt', "r")

lines = f.readlines()
f.close()


#with open("peo_leads.html", "w") as h:
 #   html = requests.get("https://www.indeed.com/jobs?q=trinet").content
  #  h.write(html + "\n")


#open peo_leads.csv to store extracted leads
with open("peo_leads.csv", "w") as f:
	#write extracted leads to the csv file
    f.write("company,link,keyword\n")
    
    for line in lines:
        print line
        #generate sources
        urls = []

        for x in range(0,10):
            print x
            x=x*10
            #print x
            urls.append("https://www.indeed.com/jobs?q=" + line.strip() + "&start=" + repr(x))

            #process sources
        for url in urls:
         #   print url
            html = requests.get(url).content
            soup = BeautifulSoup(html)
            
            #EXTRACT results from the the source
            results = soup.findAll('div', {'class' : re.compile('.*row.*result.*')})

            for result in results: 
                #print result
                lead_keyword = line.strip()
                lead_link = "https://www.indeed.com" + result.a['href']
                #print lead_link
                lead_company = result.span.text
               # print lead_company

                lead_record = lead_company + "," + lead_link + "," + lead_keyword
                # print union_record
                #print lead_keyword
                f.write(lead_record + "\n")
                #for result in results: 
                #print lead_link
               # lead_company = soup.div.span
                #print lead_company
                """
                #TRANSFORM results
                for result in results:
                    for a in result.findAll('a', href=True):
                        #print(a['href'])

                        lead_link = "https://www.indeed.com/m/" + a['href']
                        print lead_link
                        lead_record = lead_link#union_type + "," + union_name + "," + union_location + "," + union_members + "," + leadlink
                        # print union_record
                        f.write(lead_record + "\n")
                """
