import sys
import csv
from datetime import datetime
import collections

"""
output function (temp dictionary, output file, inactivity period, current time)
Session: corresponding dictionary fn for outputs
freeze_time: inactivity period
TIME: current time, file ends at -1 then output all items. 
"""
def output(session, output_file, freeze_time, TIME=-1):
    for item in list(session):
        item_infor = session[item]
        if TIME == -1 or (TIME - item_infor[1].timestamp()) > freeze_time:
            output_line = item + ","  \
            +item_infor[0].strftime('%Y-%m-%d %H:%M:%S') + ","  \
            +item_infor[1].strftime('%Y-%m-%d %H:%M:%S') + ","  \
            +str(int((item_infor[1].timestamp() - item_infor[0].timestamp())) + 1) + ","  \
            +str(item_infor[2]) + "\n"
            output_file.writelines(output_line) #write into output file
            session.pop(item) #pop dictionary output

# main analytical function 
def analyse_session(freezef, outputf, inputf):
    with open(freezef , "r") as file:
        freeze_time = int(file.readline())
    
    session = collections.OrderedDict()
    
    with open (outputf , "w") as output_file:
        with open(inputf, "r") as input_file:
            csv_reader = csv.reader(input_file)
            head = True
            for infor in csv_reader:
                #ignore table head
                if head:
                    head = False
                    continue
                IP = infor[0]
                timeString = infor[1] + " " + infor[2]
                if "-" in infor[1]:
                    TIME = datetime.strptime(timeString,'%Y-%m-%d %H:%M:%S') 
                else:
                    TIME = datetime.strptime(timeString, '%m/%d/%y %H:%M:%S')

                #check and output items in current TIME
                output(session, output_file, freeze_time, TIME.timestamp())
                # update dictionary
                if IP not in session:
                    session[IP] = [TIME, TIME, 1]
                else:
                    session[IP][1] = TIME 
                    session[IP][2] += 1
         #file end, output the rest items in designated order
        output(session, output_file, freeze_time)

"""
main function, process with analyse_session function
args(path for inactivity period file, path for output file, path for input file)
"""
if __name__ == '__main__':
    analyse_session(sys.argv[1], sys.argv[2], sys.argv[3])
    #analyse_session("../input/Q_inactivity_period.txt", "../output/sessionization.txt", "../input/Q_log.csv")
