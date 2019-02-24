### INTERVAL SCHEDULING ALGOTIHM FOR N Jobs and M Machines
import time;
import sys, getopt;

#Takes “-i” and “-o” parameters followed by filepath
inputfile = ''
outputfile = 'output.txt'
try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
	print ('interval_scheduling.py -i <inputfile> -o <outputfile>')
for opt, arg in opts:
	if opt == '-h':
		print ('test.py -i <inputfile> -o <outputfile>')
		sys.exit()
	elif opt in ("-i", "--ifile"):
		inputfile = arg
	elif opt in ("-o", "--ofile"):
		outputfile = arg

#if no input file path is given program sends an alerts
if(inputfile==''): 
	print("Please provide input file using following command")
	print ('interval_scheduling.py -i <inputfile> -o <outputfile>')
	sys.exit()
print ('Input file is at"', inputfile+'"')
print ('Output file is at"', outputfile+'"')

def schedule(rem_jobs, dict_start_time):				#scheduling function
	jobs=[]												#empty array to store jobs
	jobs.append(rem_jobs[0])							#append jobs remaining into the array
	unscheduledJobs=[]									#empty array to store unscheduled jobs
	for i in range(1,len(rem_jobs)):					#iterate over all jobs in the rem_jobs array			 
		start_time = dict_start_time[rem_jobs[i][0]]	#obtain start time for current job
		finish_time = jobs[len(jobs) - 1][1]			#obtain finish time of latest scheduled job 
		if(start_time >= finish_time ):					#compare start and finish times
			jobs.append(rem_jobs[i])					#append to jobs array if condition is satisfied
		else:
			unscheduledJobs.append(rem_jobs[i])			#append to unscheduled jobs if condition not satisfied
	#return the result as a dictionary of unscheduled Jobs and scheduled jobs
	return {'unscheduledJobs':unscheduledJobs,'jobs':jobs}
	
def main():												 #main function
	try:
		file = open(inputfile,"r")						 #read the input file containing the schedules							
		line = file.read().split("\n")					 #read the individual lines
		#extract number of jobs n and number of machines m from the first line
		n,m = int(line[0].split(" ")[0]),int(line[0].split(" ")[1])
		#initialize empty dictionaries containing the start and finish times
		dict_start_time ={}								   
		dict_finish_time = {}
		t0 = time.time()
		for i in range(1,n+1):						         #iterate over each line in the file									
			job_arr = line[i].split(" ")					 #store the individual schedules in separate arrays	   
			dict_start_time[i] = int(job_arr[0])			 #store the start times in a dicitonary
			dict_finish_time[i] = int(job_arr[1])			 #store the finish times in a dicitonary

		#sort the finish times to obtain the earliest finish times.
		sorted_ft = sorted(dict_finish_time.items(), key = lambda kv : kv[1])
		scheduled_jobs = []									 #array to maintain scheduled jobs
		rem_jobs = sorted_ft								 #array to store jobs not scheduled after 1 iteration
		count = 0											 #count of number of jobs
		for i in range(0,m):								 #iterate over m machines
			if(len(rem_jobs) != 0):							 #check if there jobs left to schedule
				result = schedule(rem_jobs, dict_start_time) #call the schedule function
				rem_jobs = result['unscheduledJobs']		 #store unscheduled jobs in remaining jobs array
				scheduled_jobs.append(result['jobs'])		 #store scheduled jobs in scheduled_jobs array
				count+= len(result['jobs'])					 #increment count
		#print(scheduled_jobs)
		output(scheduled_jobs, count)						 #call output function to store result
		print('Scheduling Successful')
		print("done in %fs" % (time.time() - t0))
	except Exception as e:
		print(e)

def output(scheduled_jobs, count):						 #function to store output in text file
	file = open(outputfile,"w+")						 #open a file in write mode
	file.write("%d" % (count))							 #write the number of jobs scheduled in the first line
	for jobs in scheduled_jobs:							 #write the sequence of jobs for each machine
		file.write("\n")
		for job in jobs:
			file.write("%d " %(job[0]))
	file.close()										 #close the file
			
main()													 #call the main function
