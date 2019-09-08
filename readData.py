from firebase import firebase
import time
import serial
import datetime
import random

ser = serial.Serial('/dev/ttyACM0' , 9600, 8, 'N', 1, timeout=5)
firebase = firebase.FirebaseApplication('https://electro-68c1a.firebaseio.com/', None)
Totalrate = 0
while True: 
        datetime_object = datetime.datetime.now()
	s = ser.readline()
        # The AVG rate in PA is 12.75 cents / kWh ranges from 8.37 to 37.34 nationally
        rate = random.gauss(12.75,0.32)/100
        Totalrate = Totalrate + rate 
	something = str.split(s)
	print(rate)
	print(datetime_object," ", s)
#	cost = rate * float(ser)
	print(something)
	time.sleep(5)
	results = firebase.post('Electro', {'datetime_object':str(datetime_object), 'ser':float(s)*0.04, 'rate':float(rate),'Totalrate':float(Totalrate) })
	print(results)
