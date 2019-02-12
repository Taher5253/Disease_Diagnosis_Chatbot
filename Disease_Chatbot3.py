import mysql.connector
import xlrd
import itertools
from collections import Counter


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mynewpassword",
  database="Disease.db"
)


mycursor = mydb.cursor(buffered=True)


list1=['Blurred vision']
list_disease = []
list_age = []

def Eyes():

	############ Age Selection ##############

	number = int(input("Enter age:"))
	if number >=0 and number <= 20:
		mycursor.execute("SELECT Disease FROM Disease_Age WHERE Organ='Eyes' AND (Age='0-20' OR Age='Any age')")
		myresult = mycursor.fetchall()
		list4=[]
		for row in myresult:
			listx1 = row[0].split(",")
			str1 = ''.join(listx1)
			list4.append(str1)
		for y in list4:
			list_age.append(y)

		print(list_age)

	elif number > 20 and number <= 40:
		mycursor.execute("SELECT Disease FROM Disease_Age WHERE Organ='Eyes' AND (Age='21-40' OR Age='Any age')")
		myresult = mycursor.fetchall()
		list4=[]
		for row in myresult:
			listx1 = row[0].split(",")
			str1 = ''.join(listx1)
			list4.append(str1)
		for y in list4:
			list_age.append(y)
		print(list_age)

	elif number > 40 and number <= 60:
		mycursor.execute("SELECT Disease FROM Disease_Age WHERE Organ='Eyes' AND (Age='41-60' OR Age='Any age')")
		myresult = mycursor.fetchall()
		list4=[]
		for row in myresult:
			listx1 = row[0].split(",")
			str1 = ''.join(listx1)
			list4.append(str1)
		for y in list4:
			list_age.append(y)

		print(list_age)

	elif number > 60 and number <=80:
		mycursor.execute("SELECT Disease FROM Disease_Age WHERE Organ='Eyes' AND (Age='61-80' OR Age='Any age')")
		myresult = mycursor.fetchall()
		list4=[]
		for row in myresult:
			listx1 = row[0].split(",")
			str1 = ''.join(listx1)
			list4.append(str1)
		for y in list4:
			list_age.append(y)

		print(list_age)

	elif number > 80 and number <=100:
		mycursor.execute("SELECT Disease FROM Disease_Age WHERE Organ='Eyes' AND (Age='81-100' OR Age='Any age')")
		myresult = mycursor.fetchall()
		list4=[]
		for row in myresult:
			listx1 = row[0].split(",")
			str1 = ''.join(listx1)
			list4.append(str1)
		for y in list4:
			list_age.append(y)

		print(list_age)

	else:
		print("Please enter age between 0 to 100")



	###### Getting Must Flag Disease #########

	for s in list1:
		mycursor.execute("SELECT Disease FROM Disease_Questions WHERE Sign_Symptoms ='{}' AND Must_Flag =1".format(s))
		list3=[]
		for row in mycursor.fetchall():
			listx1 = row[0].split(",")
			str1 = ''.join(listx1)
			list3.append(str1)
		for y in list3:
			list_disease.append(y)
	print(list_disease)
	print(len(list_disease))




	print("Disease Diagnosis for: ")
	print("====================")
	for s in list1:
		print(s)
	print()
	print("===================")
	print("===================")


	####### Getting Diseases for given Symptoms ########

	for x in list1:
		mycursor.execute("SELECT Disease FROM Disease_Symptoms WHERE Sign_Symptoms ='{}'".format(x))
		myresult = mycursor.fetchall()
		list3=[]
		df = myresult[0]
		list3.append(df[0].split(","))
		for y in list3:
			for z in y:
				list_disease.append(z)

	print(list_disease)
	print(len(list_disease))




	######## Getting Disease for pain severity ############


	print("===================")
	print()
	print('Enter how much pain do you have for Eyes: ')
	print()
	print('mild')
	print('moderate')
	print('mild to moderate')
	print('moderate to severe')
	print()
	Pain_Severity = input()
	print()

	for symp in list1:
		mycursor.execute("SELECT Disease FROM Disease_Questions WHERE Sign_Symptoms ='{}' AND Pain='{}'".format(symp, Pain_Severity))
		list3 = []
		for row in mycursor.fetchall():
			listx1 = row[0].split(",")
			str1 = ''.join(listx1)
			list3.append(str1)
		for y in list3:
			list_disease.append(y)

	print(list_disease)
	print(len(list_disease))



	######## Getting Disease for Gradual Sudden ############



	print("===================")
	for symp in list1:
		print()
		print('How did the pain occured for: ' + symp)
		print()
		print('Sudden')
		print('Gradual')
		print()

		Pain_Occurence = input()
		print()

		mycursor.execute("SELECT Disease FROM Disease_Questions WHERE Sign_Symptoms ='{}' AND Gradual_Sudden ='{}'".format(symp,Pain_Occurence))
		list3 = []
		for row in mycursor.fetchall():
			listx1 = row[0].split(",")
			str1 = ''.join(listx1)
			list3.append(str1)
		for y in list3:
			list_disease.append(y)
	print(list_disease)
	print(len(list_disease))



	######## Getting Disease based length of symptoms ############


	print("===================")
	for symp in list1:
		print()
		print('Since how long do you have: ' + symp)
		print()
		print('more than week to month')
		print('since today')
		print('more than one day to week')
		print('more than month to year')
		print()

		Pain_Time = input()
		print()

		mycursor.execute("SELECT Disease FROM Disease_Time WHERE Disease_Time ='{}' AND (Sign_Symptoms ='{}' AND Body_Part='Eyes')".format(Pain_Time, symp))
		list3 = []

		for row in mycursor.fetchall():
			listx1 = row[0].split(",")
			str1 = ''.join(listx1)
			list3.append(str1)
		for y in list3:
			list_disease.append(y)

	print(list_disease)
	print(len(list_disease))



	######## Getting Disease based on occurrence ############



	print("===================")
	for symp in list1:
		print()
		print('Did this happened before: ' + symp)
		print()
		print('once')
		print('more than once')
		print()

		Happened_Before = input()
		print()

		mycursor.execute("SELECT Disease FROM Disease_HappenedBefore WHERE Sign_Symptoms='{}' AND (Happened_Before='{}' AND Body_Part='Eyes')".format(symp,Happened_Before))
		list3 = []
		for row in mycursor.fetchall():
			listx1 = row[0].split(",")
			str1 = ''.join(listx1)
			list3.append(str1)
		for y in list3:
			list_disease.append(y)

	print(list_disease)
	print(len(list_disease))


	print("Diagnosis without Age")
	print("================")
	cnt = Counter(list_disease)
	print(cnt)

	#list6 = []

	for item in list_disease:
		if item in list_age:
			continue
		else:
			disease_index = list_disease.index(item)
			list_disease.pop(disease_index)


	#print(list6)

	print("Diagnosis with Age")
	print("==============")
	cnt = Counter(list_disease)
	print(cnt)

	most_count = cnt.most_common()[0][1]
	print(most_count)
	print('You mave have:')
	for value, count in cnt.most_common():
		if count == most_count:
			print(value)


Eyes()



