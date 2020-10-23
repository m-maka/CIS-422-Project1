'''
Running this file will test the application for basic functionality, such as:

	- Are the GPX files being converted succesfully into lat/long coordinates?
	- Are the outputed instructions acurrate?

To keep things organized and concise, special cases will be tested on separate 
files
'''

import execute

def test1():

	success = False
	
	# Input the GPX File and the key.txt file
	output = execute.execute("2017_GONG_Ride_25_Mile_Route.gpx", "key.txt")

	# Read the file with the expected output
	t_1_result = open("test1result.txt")
	expected = t_1_result.read()
	t_1_result.close()

    # Compare actual and expected output
	if output == expected:
		success = True

	return success


def test2():

	success = False
	
	output = execute.execute("2017_GONG_Ride_50_Mile_Route.gpx", "key.txt")

	# Read the file with the expected output
	t_2_result = open("test2result.txt")
	expected = t_2_result.read()
	t_2_result.close()

    # Compare actual and expected output
	if output == expected:
		success = True

	return success


def test3():

	success = False

	output = execute.execute("2019_GONG_Ride.gpx", "key.txt")
	
	# Read the file with the expected output
	t_3_result = open("test3result.txt")
	expected = t_3_result.read()
	t_3_result.close()

	# Note: This route's directions are a little weird
	# So I will test a second possibility.
	t_3_result2 = open("test3result2.txt")
	expected2 = t_3_result2.read()
	t_3_result2.close()

    # Compare actual and expected output
	if output == expected or output == expected2:
		success = True

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