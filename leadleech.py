#SOURCE = ALLEN BYERLY
#DATE = 08/04/2018
#VERSION = 0.1
#NOTES = THIS VERSION OF THE SCRAPER PRODUCES LEADS OF THE TYPE "PEO"

from BeautifulSoup import BeautifulSoup
import requests

urls = []

#open peo_leads.csv to store extracted leads
with open("peo_leads.csv", "w") as f:
	#write extracted leads to the csv file
    f.write("union_type,union_name,union_location,union_members,union_detail_href\n")
    
    #generate sources
    for x in range(1,50):
        print x
        urls.append("https://www.indeed.com/jobs?q=trinet&start=" + repr(x))

    #process sources
    for url in urls:
        html = requests.get(url).content
        soup = BeautifulSoup(html)
      	
      	#print soup

        with open("peo_leads.html", "w") as h:

        #EXTRACT results from the the source
        	results = soup.findAll('a', attrs={'class' : 'jobtitle turnstileLink'})
        	#h.write(html)
        	h.write(html)
        #print results
       	#TRANSFORM results
        for result in results:
          #  print result
            #union_type = result.a.text.split(" - ")[0]
            #union_name = result.a.text.split(" - ")[1]
            #union_location = result.p.text.split("Map", 1)[0]
            #union_members = result.p.text.split("Members: ", 1)[1]
            #union_detail_href = "http://www.unions.org" + result.a.get('href')
            
            #LOAD results into the data store
            lead_link = "https://www.indeed.com" + result['href']
            print lead_link
            lead_record = lead_link#union_type + "," + union_name + "," + union_location + "," + union_members + "," + leadlink
           # print union_record
            
            f.write(lead_record + "\n")
        print "DONE"
#<h3><a href="/unions/american-federation-of-government-employees/local-1208/18740" title="AFGE - GOVERNMENT EMPLOYEES Local 1208">AFGE - GOVERNMENT EMPLOYEES Local 1208</a></h3>
#<p> <br />SANGER, CA 936579737 <a target="_blank" href="http://maps.google.com/maps?q=+SANGER%2C+CA+93657" class="xSmall blue" title="View map">Map</a>
#<br />ELODIA CASTRO                            <br />Union Members: 49                                        </p>
#<div class="clear"></div>
#</div>
