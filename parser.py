import os
import sys
import re
from datetime import timedelta
from string import rstrip

# define variables
# only works in current directory until I include 
dir = ""

# get the type of request
def parse_type(cargs):
 
    # look for first element in array for type of request
    try:
    
        rrequest = cargs[1]
        rrange = cargs[2]
    
    except IndexError:

        print("No request type or range specified.")
        rrange = False
        rrequest = 'all'

    # use our switcher to select the correct function to run for the type of request.
    switcher={
            'last':'rlast',
            'this':'rthis',
            'all':'rall',
        }
    rtype = globals()[switcher[rrequest]]
    
    # get files that match request
    files = rtype(rrange)
    
    #parse file data
    data = parse_files(files)
    
    #get data summary
    summary = summarize(data)
    
    #return summary
    return summary

# To do
def rlast(rrange):

    print("Last")

# To do
def rthis(rrange):

    print("this")

# get and parse all the data
def rall(rrange):

    print ("Returning all data.")
    files = get_files(rrange)
    return files;

#get a list of files
def get_files(rrange):
    
    files = list()

    for file in os.listdir(dir):
    
        filepath = os.path.join(dir, file)

        if os.path.isfile(filepath):  
    
            files.append(file)
    files.sort()
    return files

#parse the files we have selectecd
def parse_files(files):
    
    data = []

    for file in files:
   
        filepath = os.path.join(dir, file)
        f = open(filepath, "r")
    
        for line in f:
            linedata = parse_line(line)

            # make sure the file is parsed before trying to update data
            if (linedata):

                # add date
                linedata.append(file)
                # append to data
                data.append(linedata)
        
        f.close()
    
    return data

#parse a line in a file
def parse_line(line):

    try: 
    
        m = re.search('([0-9]{2})\:([0-9]{2})\s-\s([0-9]{2})\:([0-9]{2})\s:\s([a-zA-Z0-9]+)\s-\s([a-zA-Z0-9\!\.\?\,\s\'\"\+\-\&]+)', line)
        full_string = m.group(0)
        start_hour = int(m.group(1))
        start_minute = int(m.group(2))
        stop_hour = int(m.group(3))
        stop_minute = int(m.group(4))
        topic = m.group(5)
        description = rstrip(m.group(6))

    except AttributeError:
        print("Unable to parse row: " + line)     
        return False
    
    start = timedelta(hours=start_hour, minutes=start_minute)
    end = timedelta(hours=stop_hour, minutes=stop_minute)
    total = end - start

    return list([topic,total,description])

#summarize results
def summarize(data):
    
    total_time = 0
    topics_data = {}
    descriptions_data = {}
    # get topics
    
    for element in data:

        topic = element[0]
        time = element[1].total_seconds()
        ttime = time
        description = element[2]
        description_data = []

        if topic in topics_data:
            ttime = time + topics_data[topic]
            description_data = descriptions_data[topic]

        topics_data.update({topic:ttime})
        description_data.append(description)
        descriptions_data[topic] = description_data
        total_time = total_time + time
    
    h = total_time/3600

    print("TOTAL HOURS:")
    print(h)

    for topic in topics_data:
        print(topic)
        print(topics_data[topic]/3600)

    return h

if __name__ == '__main__':
    
    response = parse_type(sys.argv)
    #print (response)