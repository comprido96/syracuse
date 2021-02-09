import  sys

def main():

	n = 0
	try:
		n = int(input('Enter number:\t'))

	except ValueError:
		print('Wrong input! Program aborted')
		sys.exit(1)

	while(n!=1):
		if(n%2==0):
			n = n/2
			print(n)

		else:
			n = 3*n+1
			print(n)






if __name__ == '__main__':
	main()