'''
Running this file will test the application for basic functionality, such as:

	- Are the GPX files being converted succesfully into lat/long coordinates?
	- Are the outputed instructions acurrate?

To keep things organized and concise, special cases will be tested on separate 
files
'''

import sys

sys.path.insert(0, '../src/')

import execute

def test1():

	success = False
	
	# Input a specific gpx file into the program
	# Keep a sample of what this specific file should return for latlong
	# coordinates
	# Compare the expected output and the actual output.

	# Send the list over to the function that gets directions and instructions
	# keep a sample of what the instructions should be
	# Compare the expected output and the actual output

	return success


def test2():

	success = False
	
	# Input a specific gpx file into the program
	# Keep a sample of what this specific file should return for latlong
	# coordinates
	# Compare the expected output and the actual output.

	# Send the list over to the function that gets directions and instructions
	# keep a sample of what the instructions should be
	# Compare the expected output and the actual output

	return success


def test3():

	success = False
	
	# Input a specific gpx file into the program
	# Keep a sample of what this specific file should return for latlong
	# coordinates
	# Compare the expected output and the actual output.

	# Send the list over to the function that gets directions and instructions
	# keep a sample of what the instructions should be
	# Compare the expected output and the actual output

	return success

def abort():
	print("Aborting testing. Exiting program...")
	exit()


def main():

	test1_success = None
	test2_success = None
	test3_success = None

	print("Starting tests of basic functionality.")
	print("Press y to initiate test, n to skip test, e to exit")

	while(True):
	
		ready = input("Begin test 1? [y/n, e to exit] ")

		if ready == 'e':
			abort()
		elif ready == 'y':

			print("Starting test 1:")
			test1_success = test1()
			print("Finishing test 1")
			break;

		elif ready == 'n':
			break;
		
		else:
			print("Unexpected input, please try again.")


	while(True):
	
		ready = input("Begin test 2? [y/n, e to exit] ")

		if ready == 'e':
			abort()
		elif ready == 'y':

			print("Starting test 2:")
			test2_success = test2()
			print("Finishing test 2")
			break;

		elif ready == 'n':
			break;
		
		else:
			print("Unexpected input, please try again.")

	while(True):
	
		ready = input("Begin test 3? [y/n, e to exit] ")

		if ready == 'e':
			abort()
		elif ready == 'y':

			print("Starting test 3:")
			test3_success = test3()
			print("Finishing test 3")
			break;

		elif ready == 'n':
			break;
		
		else:
			print("Unexpected input, please try again.")

	print("Final results:")

	print("Test 1:", test1_success)
	print("Test 2:", test2_success)
	print("Test 3:", test3_success)


if __name__ == '__main__':
	main()