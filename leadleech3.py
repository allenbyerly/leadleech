#SOURCE = ALLEN BYERLY
#DATE = 08/04/2018
#VERSION = 0.1
#NOTES = THIS VERSION OF THE SCRAPER PRODUCES LEADS OF THE TYPE "PEO"

from BeautifulSoup import BeautifulSoup
import requests

urls = []

#open lead list file
f = open('leadlist.txt', "r")

#read lead list file
lines = f.readlines()
f.close()



#open peo_leads.csv to store extracted leads
with open("peo_leads.csv", "w") as f:
	#write extracted leads to the csv file
    f.write("company,link,keyword\n")
    
    for line in lines:
       # print line
        #generate sources
        lead_company = line.strip()
        lead_keyword = line.strip()

        for x in range(0,1):
            
            x=x*10
           # print x
            urls.append("https://www.indeed.com/m/jobs?q=" + + "&start=" + repr(x))

            #process sources
            for url in urls:
             #   print url
                html = requests.get(url).content
                soup = BeautifulSoup(html)
 				with open("peo_leads.html", "w") as h:
 					h.write(html + "\n")

                titleTag = soup.html.body.h1.text
                print titleTag

                br = soup.html.body.br.text
                print br
                #EXTRACT results from the the source
                results = soup.findAll('h2', attrs={'class' : 'jobTitle'})

                #TRANSFORM results
                for result in results:
                	
                    for a in result.findAll('a', href=True):
                        #print(a['href'])
                        print result
                        lead_link = "https://www.indeed.com/m/" + a['href']
                        print lead_link
                        lead_record = line.strip() + "," + lead_link + "," + line.strip() 
                        # print union_record
                        f.write(lead_record + "\n")
			