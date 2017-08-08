import urllib.request
import time

#Open the file to read the patent ids to get source code of these pages
with open('C:/Users/Desktop/patent-ids.txt', 'r') as infile:

    data = infile.read()  # Read the contents of the file into memory.

# Return a list of the lines, breaking at line boundaries.
my_list = data.splitlines()
#my_list contains list of patent ids
url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1='
p1 = '.PN.&OS=PN/'
p2 = '&RS=PN/'
length = len(my_list)
print(length)
for i in range(length):
    print("Printed Element",i)
    gkl = my_list[i]
    #Updated URL will be stored in bv
    bv = url+gkl+p1+gkl+p2+gkl
    page = urllib.request.urlopen(bv)
    time.sleep(1)
    #Creating a new html file with the patent id as the file name
    text_file = open('F:/work/patenthtml/{}.html'.format(my_list[i]), "wb")
    #Writing html source code to the created html file
    text_file.write(page.read())
    #closing the file
    text_file.close()

