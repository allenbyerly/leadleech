#SOURCE = ALLEN BYERLY
#DATE = 08/04/2018
#VERSION = 0.1
#NOTES = THIS VERSION OF THE SCRAPER PRODUCES LEADS OF THE TYPE "PEO"

from BeautifulSoup import BeautifulSoup
import requests

urls = []

f = open('leadlist.txt', "r")

lines = f.readlines()
f.close()



#open peo_leads.csv to store extracted leads
with open("peo_leads.csv", "w") as f:
	#write extracted leads to the csv file
    f.write("union_type,union_name,union_location,union_members,union_detail_href\n")
    
    for line in lines:
        print line
        #generate sources
        for x in range(0,10):
            
            x=x*10
           # print x
            urls.append("https://www.indeed.com/m/jobs?q=" + line.strip() + "&start=" + repr(x))

            #process sources
            for url in urls:
             #   print url
                html = requests.get(url).content
                soup = BeautifulSoup(html)

                #EXTRACT results from the the source
                results = soup.findAll('h2', attrs={'class' : 'jobTitle'})

                #TRANSFORM results
                for result in results:
                    for a in result.findAll('a', href=True):
                        #print(a['href'])

                        lead_link = "https://www.indeed.com/m/" + a['href']
                        print lead_link
                        lead_record = lead_link#union_type + "," + union_name + "," + union_location + "," + union_members + "," + leadlink
                        # print union_record
                        f.write(lead_record + "\n")
