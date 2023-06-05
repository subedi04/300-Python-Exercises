'''
Write A Python Program To Get Age From The User In Year, 
And Convert Age In To Seconds, minutes and hours 
'''

def edad_segundos_minutos_horas(age):
	segundos = age * 31536000
	horas = int(segundos / 60 / 60)
	segundos -= horas*60*60
	minutos = int(segundos/60)
	segundos -= minutos*60
	print(str(horas) + " hours - " + str(minutos) + " minutes - " + str(segundos) + " seconds")
    
   
if __name__=="__main__":
	age = float(input("Enter your age to convert to sec: ")) 
	print("Your age in hours, minutes and seconds is : ")
	print(edad_segundos_minutos_horas(age))

