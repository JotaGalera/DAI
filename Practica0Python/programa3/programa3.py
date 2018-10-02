#Main de la criba de Erastotenes
from criba_erastotenes import cribaErastotenes

try:
    number=int(input("Number:"))
except ValueError:
	print("This is not a number.")

cribaErastotenes(number)
