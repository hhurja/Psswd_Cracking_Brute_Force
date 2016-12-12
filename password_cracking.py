import sys
import hashlib
import time
import itertools

def read_file(filename):
	list_of_lines = []
	inFile = open(filename, 'r')
	for line in inFile:
		list_of_lines.append(line.rstrip())
	return list_of_lines

def hash_passwords(pass_array):
	new_array = []
	for line in pass_array:
		new_array.append((line, hashlib.md5( line ).hexdigest()))
	return new_array

def print_end_message(iterator, total_time):
	print "*******************************************"
	print "Checked", iterator, "different passwords."
	print "Took a total of", total_time, "time to run."
	print "*******************************************\n"

def execute_attack(hashed_array, limit_on_length):
	start_time = time.time()
	temp_pass = ''
	char_array = []
	iterator = 0;
	for val in range(33,126):
		char_array.append(str(unichr(val)))

	for length in range(0, limit_on_length+1):
		for subset in itertools.product(char_array, repeat=length):
			temp_pass = "".join(subset)
			iterator += 1
			#print temp_pass
			if iterator % 50000000 == 0:
				curr_time = time.time() - start_time
				if(curr_time < 60):
					t = str(curr_time) + " seconds."
				elif(curr_time < 3600):
					t = str(curr_time/60) + " minutes."
				else:
					t = str(curr_time/3600) + " hours."
				print "Checked", iterator, "passwords so far in", t

	    		for p in hashed_array:
	    			
					if (p[1] == hashlib.md5( temp_pass ).hexdigest()):
						print "Found password:",p[0], "in", time.time() - start_time, "seconds"
						print "The hash is:", p[1], "\n"
			

    		
    	print_end_message(iterator, time.time() - start_time)


if __name__ == '__main__':
	if(len(sys.argv) != 2):
		print "Please enter the name of the text file as an argument."
	else:
		upper_bound = 8
		pass_array = []
		pass_array = read_file(sys.argv[1])
		pass_array = hash_passwords(pass_array)

		print "\n******* Checking Passwords now *******\n"

		execute_attack(pass_array, upper_bound)

