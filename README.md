#EDGAR Project Summary

Table of Contents
I.	 Approach
     A.	Steps
II.	 Libraries
III. Instructions

I.	Approach
This project is to work on the data pipeline to gather information and sends the output file to the front end. Using the data, program model is developed in Python to identify the single user visit information, calculating the duration of and number of documents requested during that visit, and then writing the output to a file. 
A.	Steps
1.	Read input log file (.csv) by Python, download test log when it is necessary;
2.	Read inactivity period file - the default value is 2, and change it in personal input just to validate the model;
3.	Process to gather single user information, written by Python:
3.1.	Import libraries 
3.2.	Output function
3.2.1.	Define general output streaming function ‘output’, loop search until either it reaches the end of file or the duration of visit period greater than freeze (inactivity) time. Frame each requested visit information in correct format - including IP, start/end time, duration and number of documents visited - and write each item in output file.
3.3.	Analysis function
3.3.1.	In main analysis function ‘analyse_session’, input files are read into memory, head of csv file is removed, and ordered dictionary ‘session’ is initiated to process and save visit information; with ordered dictionary, data will remain in the same order as they are added;
3.3.2.	One thing worth to mention is that in order to avoid datetime format inconsistent caused by using different csv reading software, a ‘if’ statement is added to clarify the date’s format so later it can be ready to stream into requested output format; 
3.3.3.	For each IP, first clear and save any completed visit information in current time stamp, update dictionary ‘session’ with each incoming log information until it reaches the end of file, then output the remaining of ‘session’ in order. 
3.4.	Main function
3.4.1.	Call and process analysis function given input and output addresses.
4.	Model has been verified and validated under both tests, results and file locations are examined, both passed given ‘sh’ tester. 

II.	Libraries
Sys
Csv
Datetime
Collections

III.	Instructions
1.	Download the repo and sort the directory;
2.	cd to current directory;
3.	Run shell script run_tests.sh for testing;
4.	Run shell script run.sh for general model;
5.	Output files can be found in designated folders. 
