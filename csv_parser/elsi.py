import csv
import sys
#import MySQLdb
# NOT_APPLICABLE_SYM =  indicates that the data are not applicable.
# MISSING_DATA_SYM =  indicates that the data are missing.
# DOES_NOT_MEAT_STANDARD_SYM = indicates that the data do not meet NCES data quality standards.

SCHOOL_NAME_COL = 0
STATE_NAME_COL = 1
NCES_ID_COL = 2
AGENCY_ID_COL = 3
COUNTY_NAME_COL = 7
COUNTY_ID_COL = 8
SCHOOL_TYPE_COL = 9
AGENCY_TYPE_COL = 10
URBAN_COL = 11
CHARTER_SCHOOL_COL = 12
TITLE_I_COL = 13
TITLE_I_ELIGIBLE_COL = 14
TITLE_I_STATUS_COL = 15
LATITUDE_COL = 16
LONGITUDE_COL = 17
STATE_SCHOOL_ID_COL = 18
STATE_AGENCY_ID_COL = 19
SCHOOL_LEVEL_CODE_COL = 20
TOTAL_STUDENTS_COL = 21
FREE_LUNCH_COL = 22
REDUCED_PRICE_COL = 23
TOTAL_FREE_REDUCED_NUM_COL = 24
HS_STUDENTS_COL = 25
FULL_TIME_TEACHERS_COL = 26
RATIO_COL = 27
LOCATION_CITY_COL = 28
LOCATION_STATE_COL = 29
LOCATION_ZIP_COL = 30 

def firstRowIndex():
	with open('elsi.csv', 'rb') as elsi:
		elsi_reader = csv.reader(elsi, delimiter=',')
		for row in elsi_reader:
			print row
			for i, val in enumerate(row):
				print(str(i) + " " + val)
			sys.exit(1)

def parseDataAndInsert():
	sqlFile = open('elsi.sql', 'w')
	with open('elsi.csv', 'rb') as elsi:
		elsi_reader = csv.reader(elsi, delimiter=',')
		for row in elsi_reader:
			insertRow(row, sqlFile)
	sqlFile.close()
		

def insertRow(rowList, sqlFile):
	quote = lambda x: "'" + x + "'"
	replaceEqual = lambda x: x.replace("=", "")
	replaceQuote = lambda x: replaceEqual(x).replace("\"", "")
	replace = lambda x: quote(replaceQuote(x).replace("'", "\\'"))

	values = []
	values.append(replace(rowList[NCES_ID_COL]))
	values.append(replace(rowList[AGENCY_ID_COL]))
	values.append(replace(rowList[SCHOOL_NAME_COL]))
	values.append(replace(rowList[STATE_NAME_COL]))
	values.append(replace(rowList[COUNTY_NAME_COL]))
	values.append(replace(rowList[COUNTY_ID_COL]))
	values.append(replace(rowList[SCHOOL_TYPE_COL]))
	values.append(replace(rowList[LOCATION_ZIP_COL]))
	values.append(replace(rowList[LOCATION_CITY_COL]))
	values.append(replace(rowList[LOCATION_STATE_COL]))
	values.append(replace(rowList[LONGITUDE_COL]))
	values.append(replace(rowList[LATITUDE_COL]))
	values.append(replace(rowList[TOTAL_STUDENTS_COL]))
	values.append(replace(rowList[HS_STUDENTS_COL]))
	#values.append(rowList[FULL_TIME_TEACHERS_COL])
	#values.append(rowList[RATIO_COL])

	insertStatement = "INSERT INTO Schools VALUES (" + ','.join(values) + ");\n"
	sqlFile.write(str(insertStatement))
	# cursor = getConnection()
	# cursor.createTable()
	# cursor.execute_query(insertStatement, values)
	

def createTableQuery():
	table = "CREATE TABLE Schools ("
	table += " NCES_Id int,"
	table += " Agency_Id int,"
	table += " School_Name varchar(255),"
	table += " State_Name varchar(255),"
	table += " County_Name varchar(255),"
	table += " County_Id varchar(255),"
	table += " School_Type varchar(255),"
	table += " Location_Zip varchar(255),"
	table += " Location_City varchar(255),"
	table += " Location_State varchar(255),"
	table += " Longitude varchar(255),"
	table += " Latitude varchar(255),"
	table += " Total_Students int,"
	table += " High_School_Students int"
	table += ");"
	return table


# def getConnection():
# 	conn = MySQLdb.connect(host="192.254.148.221",
#                        user="bayes",
#                        passwd="Qn4Jy2WodGYekwjskICV",
#                        db="bayes")
# 	cursor = conn.cursor()
# 	return cursor
#firstRowIndex()
#query = createTableQuery()
#print query
parseDataAndInsert()
# 	columns = ""
# 	insertStatement += "SchoolName"
# 	insertStatement += ","	
# 	insertStatement += "StateName"
# 	insertStatement += "StateAbbr"

# 	insertStatement += ","	
# 	insertStatement += "NCESId"
# 	insertStatement += "StateAbbr"





# 	INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
# VALUES ('Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway');





