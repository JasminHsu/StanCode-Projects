"""
File: weather_master.py
Name: Jasmin Hsu
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -1


def main():
	"""
	Compare the first temperature to EXIT number at the beginning
	to make sure there is an usable temperature and make it be
	the standard number. Then calculate or compare every incoming
	temperatures to the standard number, and let qualified ones
	replace the old standard number
	"""
	print('stanCode \"Weather Master 4.0"!')
	temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	# How to change -100 to -1?
	if temp == EXIT:
		print('No temperatures were entered.')
	else:  # Set first temperature as a standard number
		highest = temp
		lowest = temp
		average = float(temp)
		number = 1  # This indicates how many temperatures this program receives
		cold = 0  # This indicates how many cold days this program receives
		if temp < 16:
			cold = cold + 1
		while True:
			temp = int(input('Next Temperature: (or -100 to quit)? '))
			if temp == EXIT:
				break
			else:  # Compare incoming numbers to old ones to update record
				number = number+1
				average = (average*(number-1)+temp)/number
				if highest < temp:
					highest = temp
				if lowest > temp:
					lowest = temp
				if temp < 16:
					cold = cold+1
		print('Highest temperature = '+str(highest))
		print('Lowest temperature = '+str(lowest))
		print('Average = '+str(average))
		print(str(cold)+' cold day(s)')








###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
