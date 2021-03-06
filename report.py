'''
Report Generator for Folder Sort
Version - 1.1.0
Copyright (c) Nikhil Ramakrishnan 
MIT License


This is a module to generate reports for Folder Sort using basic HTML Tables

A report file can be generated by creating an instance of report()

Values can be inserted by calling report.insert(list[,new_file_name])
Stop inserting values with report.done(). This will save the file and return the filename.

If the file needs to be disposed, call report.delete()

'''

import os,time,datetime
indexiter=100
class report(object):
    def __init__(self):
        self.recs=0 #The number of records inserted in table
        #Current time in local computer format
        humannow=str(datetime.datetime.now()).split('.')[0]
        #Current time for file name
        now=time.strftime("%Y-%m-%d_%H-%M-%S")
        #File name
        self.filename='folder_sort_report_'+now+'.html'
        #File base and extension (this is used when file with same name already exists)
        self.filebase='folder_sort_report_'+now
        self.fileext='.html'
        #This is the number upto which the program will check for file existence
        global indexiter
        #If file with filename does not exist (This happens in most of the cases)
        if not os.path.exists(self.filename):
            self.f= open(self.filename,"w+",encoding='utf8')
        else:
            #Check for indexes if filename already exists in folder
            for indexcheck in range(1,indexiter):
                if not os.path.isfile(self.filebase+'_'+str(indexcheck)+self.fileext):
                    finalindex=indexcheck
                    break
            self.filename=self.filebase+'_'+str(indexcheck)+self.fileext
            self.f=open(self.filename,"w+")
        #Print the initial part of the html file
        print("<!DOCTYPE html>\n\
<html>\n\
<!--\n\
This is an automatically generated report for Folder Sort.\n\
Report contains a record of the files that were sorted\n\
including the file name (new name if renamed), source and destination.\n\
\n\
Folder Sort is a program (part of System Cleaner) for Academic Purpose, developed at\n\
Bennett University, India, by Nikhil Ramakrishnan.\n\
MIT License.\n\
-->\n\
<head>\n\
<title>Folder Sort Report</title>\n\
<meta charset=\"UTF-8\">\n\
<style>\n\
table {\n\
    \tfont-family: arial, sans-serif;\n\
    \tborder-collapse: collapse;\
    \twidth: 100%;\n\
}\n\
td, th {\n\
    \tborder: 1px solid #dddddd;\n\
    \ttext-align: left;\n\
    \tpadding: 8px;\n\
}\
\n\
tr:nth-child(even) {\n\
    \tbackground-color: #dddddd;\n\
}\n\
h1 {\n\
    \tfont-family:'Helvetica';\n\
    \tcolor:#1FAEFF;\n\
}\n\
p {\n\
        \tfont-family:'Helvetica';\n\
}\n\
</style>\n\
</head>\n\
<body>\n\
<h1><center>Folder Sort Report</center></h1>\n\
<p><center><strong>Report generated on: "+humannow+"</strong></center></p>\n\
<table>\n\
<tr>\n\
    <th>No.</th>\n\
    <th>File Name</th>\n\
    <th>Old Location</th>\n\
    <th>New Location</th>\n\
</tr>",file=self.f)

    def insert(self,data,res=None):
        '''This function inserts data into the table.
        When file is being renamed, the new file name is supplied as the res parameter'''
        
        if(res==None):
            print("<tr>\n\t<td>"+str(self.recs+1)+"</td>\n\t<td>"+data[0]+"</td>\n\t<td>"+data[1]+"</td>\n\t<td>"+data[2]+"</td>\n</tr>\n",file=self.f)
        else:
            print("<tr>\n\t<td>"+str(self.recs+1)+"</td>\n\t<td>"+data[0]+" (Renamed to "+res+")</td>\n\t<td>"+data[1]+"</td>\n\t<td>"+data[2]+"</td>\n</tr>\n",file=self.f)
        self.recs+=1
    def done(self):
        '''Stop appending to table and insert the last part of HTML to the file'''
        
        print("</table>\n\
<br><br><p><strong><center>***END OF REPORT***</center></strong></p>\n\
</body>\n</html>",file=self.f)
        #Close the file
        self.f.close()
        #If there are 0 records in file, delete it.
        if self.recs==0:
            os.remove(self.filename)
        #Return the file name of the report
        return self.filename
    
    def delete(self):
        '''Delete the current report generated by the program'''
        os.remove(self.filename)
        
if __name__=='__main__':
    print("main")
    print("This is a module for Folder Sort that generates an HTML report.")
    
