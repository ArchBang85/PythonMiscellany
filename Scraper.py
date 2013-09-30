## Task: cerate an array listing the services that BRC provides by scraping through a hard-coded list of websites
## P.Autio 12/2012
## Modified 3/9/2013

import urllib2
import re
import time

from BeautifulSoup import BeautifulSoup, SoupStrainer

def print_timing(func):
        def wrapper(*arg):
                t1 = time.clock()
                res = func(*arg)
                t2 = time.clock()
                print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
                return res
        return wrapper

@print_timing
def scrape():
    link_list = []
    text_list = []
    #urls = ["/Northern-England/County-Durham-and-Teesside-Northumbria-and-Cumbria", "/Northern-England/Derbyshire-Nottinghamshire-and-Cheshire", "/Northern-England/Lancashire-Merseyside-and-Greater-Manchester", "/Northern-England/Lincolnshire-Leicestershire-and-Rutland-and-Northamptonshire", "/Northern-England/Yorkshire", "/Scotland-Northern-Ireland-and-Isle-of-Man/East-Scotland", "/Scotland-Northern-Ireland-and-Isle-of-Man/Northern-Ireland-and-Isle-of-Man", "/Scotland-Northern-Ireland-and-Isle-of-Man/Northern-Scotland", "/Scotland-Northern-Ireland-and-Isle-of-Man/West-Scotland", "/South-Eastern-England/Bedfordshire-Hertfordshire-and-Essex", "/South-Eastern-England/Berkshire-Buckinghamshire-and-Oxfordshire", "/South-Eastern-England/Cambridgeshire-Norfolk-and-Suffolk", "/South-Eastern-England/Hampshire-Isle-of-Wight-and-Surrey", "/South-Eastern-England/Kent-and-Sussex", "/South-Eastern-England/London", "/Wales-and-Western-England/Cornwall-Devon-Dorset-Somerset-and-Channel-Islands", "/Wales-and-Western-England/Herefordshire-Shropshire-Worcestershire", "/Wales-and-Western-England/Staffordshire-West-Midlands-and-Warwickshire", "/Wales-and-Western-England/Wales", "/Wales-and-Western-England/Wiltshire-Avon-and-Gloucestershire"]
    urls = ["online-data-visualization-shows-your-water-footprint"]
    rooturl = 'http://green.harvard.edu/'
   
    for item in urls:

        #html = urllib2.urlopen('http://www.redcross.org.uk/Where-we-work/In-the-UK' + item).read()
        # Root url
        print item
        html = urllib2.urlopen(rooturl + item).read()        

        # What is grabbed
        link_zone = SoupStrainer('div',{'class':'content'})

        soup = BeautifulSoup(html, parseOnlyThese=link_zone)

        ## Find all the links
        for a in soup.findAll('a'): 
            #print a.string
            if a.string not in link_list:
                link_list.append(a.string)

        ## Find all the text
        for text in soup.findAll('p'): 
            #print a.string
            if text.string not in text_list:
                text_list.append(text.string)   

    print 'Links in the div you\'ve specified: '
    print link_list
    print 'Text in the div you\'ve specified: '
    print text_list

if __name__ == "__main__":
        print "Scraping services"
        scrape()
        time.sleep(2.5)
