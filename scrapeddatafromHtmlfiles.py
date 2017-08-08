import re
import urllib.request
from bs4 import BeautifulSoup
#Add external library beautiful soup inorder to scrap data from html files


with open('F:/work/patent.txt', 'r') as infile:

    data = infile.read()  # Read the contents of the file into memory.

# Return a list of the lines, breaking at line boundaries.
my_list = data.splitlines()

results_Dict = dict()
length = len(my_list)
print(length)
afterBracket=''

for i in range(length):
    print("Printed Element",i,"eightlakh")
    #Read the file using beautiful soup
    soup = BeautifulSoup(open("F:/work/patenthtml/{}.html".format(my_list[i])),"html.parser")
    divs = soup.findAll("table")
    for dividx,div in enumerate(divs):
        row = ''
        rows = div.findAll('tr')
        #To get the inventors details from the webpage
        for row in rows:
            if(row.text.find("Inventors:")>-1):
                tempCheckVal = 1
                originalTe = row.text.split(":")
                afterBrack = originalTe[1]
            #To get the Assignee details from the webpage
            if(row.text.find("Assignee:")>-1):
                tempf = len(row)
                originalText = row.text.split(":")
                afterBracket = originalText[1]
            #To get the Current U.S. Class details from the webpage
            if(row.text.find("Current U.S. Class:")>-1):
               tempCheckValue = 1
               currentClass = row.text.split(":")
               currentClassValue = currentClass[len(currentClass)-1]
               currentClassValue = ' '.join(currentClassValue.split('\n'))
               #currentClassValue = currentClassValue.replace("\n","")
               
               
            if(row.text.find("Current CPC Class:")>-1):
               tempCheckValue = 1
               currentCPCClass = row.text.split(":")
               currentCPCClassValue = currentCPCClass[len(currentCPCClass)-1]
               currentCPCClassValue = ' '.join(currentCPCClassValue.split('\n'))
                
            if(row.text.find("Current International Class:")>-1):
               tempCheckValue = 1
               currentInternationalClass = row.text.split(":")
               currentInternationalClassValue = currentInternationalClass[len(currentInternationalClass)-1]
               currentInternationalClassValue = ' '.join(currentInternationalClassValue.split('\n'))
                     
            if(row.text.find("Field of Search:")>-1):
               tempCheckValue = 1
               fieldSearch = row.text.split(":")
               fieldSea = fieldSearch[len(fieldSearch)-1]
               fieldSea = ' '.join(fieldSea.split('\n'))
               #print(dividx)
               tdvval = ''
               if(len(soup.findAll('table')[dividx+1].findAll('tr')[0].findAll('a'))>-1):
                idpats = soup.findAll('table')[dividx+1].findAll('tr')
                idpat=''
                for idpat in idpats:
                    gettd = ''
                    tds = idpat.findAll('td')
                    eachTD = ''
                    for eachTD in tds:
                     tdvval = tdvval+eachTD.get_text()
               Citedpatents = '-'.join(tdvval.split())
               foreignPatents = ''
               if(len(soup.findAll('table')[dividx+2].findAll('tr')[0].findAll('td'))>2):
                    idpatss = soup.findAll('table')[dividx+2].findAll('tr')  
                    idpat=''
                    tdvaal = ''
                    for idpat in idpatss:
                        gettd = ''
                        tds = idpat.findAll('td')
                        eachTD = ''
                        for eachTD in tds:
                            tdvaal = tdvaal+eachTD.get_text()
                    foreignPatents = '-'.join(tdvaal.split())
    

    Filed = soup.findAll('tr')
    row = ''
    for row in Filed:
           if(row.text.find("Filed:")>-1):
            FileDate = row.get_text()
            FileDate = FileDate.split(":")
            FiledDate = FileDate[1]
            FiledDate = ' '.join(FiledDate.split())

    ApplicationNo = soup.findAll('tr')
    app = ''
    for number in ApplicationNo:
        if(number.text.find("Appl. No.:")>-1):
            AppNumber = number.get_text()
            AppNumber = AppNumber.split(":")
            ApplicationNumber = AppNumber[1]
            ApplicationNumber = ' '.join(ApplicationNumber.split())
            
    Patnumber = soup.findAll('tr')
    app = ''
    for idx,numb in enumerate(Patnumber):
        if(numb.text.find("United States Patent")>-1):
            Numpat = numb.get_text()
            PatNum = ''.join(Numpat.split())
            Numpatr = re.sub("\D","",PatNum)
            num = idx+1
            datePat = soup.findAll('tr')[num].findAll('td')[1].get_text()
            datePat = ' '.join(datePat.split())                    
                
    abstractData = soup.findAll('p')[0].get_text()
    abstractData = ''.join(abstractData.split('\n'))
    abstractData = ''.join(abstractData.split('\t'))
    
    Inventors = ' '.join(afterBrack.split())
    ComapnyName = ' '.join(afterBracket.split())
    PatentNumber=Numpatr
    PatentDate=datePat
    ApplicationFiledDate=FiledDate
    CurrentInternationalClass=currentInternationalClassValue.replace(" ","")
    CurrentUsClass=[]
    CurrentUsClass = currentClassValue.replace(" ","")
    CurrentCPCClass=currentCPCClassValue.replace(" ","")
    FieldofSearch=fieldSea.replace(" ","")
    completeRow = []
    completeRow = Inventors+'@'+ComapnyName+'@'+PatentNumber+'@'+PatentDate+'@'+ApplicationFiledDate+'@'+CurrentUsClass+'@'+CurrentCPCClass+'@'+CurrentInternationalClass+'@'+FieldofSearch+'@'+Citedpatents+'@'+foreignPatents+'@'+abstractData
    with open("F:/work/patentcsv.txt", "a") as write_text:
        write_text.write(completeRow+"\n")

