import csv
import sys
#import MySQLdb
# NOT_APPLICABLE_SYM =  indicates that the data are not applicable.
# MISSING_DATA_SYM =  indicates that the data are missing.
# DOES_NOT_MEAT_STANDARD_SYM = indicates that the data do not meet NCES data quality standards.

BUSINESS_ID_COL = 15
CATEGORIES_COL = 20
NAME_COL = 23
CITY_COL = 58
STATE_COL = 38
FULL_ADDRESS_COL = 44
LATITUDE_COL = 66
LONGITUDE_COL = 69

# db columns
BUSINESS_ID_NAME = "business_id"
CATEGORIES_NAME = "categories"
NAME_NAME = "name"
CITY_NAME = "city"
STATE_NAME = "state"
FULL_ADDRESS_NAME = "full_address"
LATITUDE_NAME = "latitude"
LONGITUDE_NAME = "longitude"

def firstRowIndex():
	with open('yelp_academic_dataset_business.csv', 'rb') as elsi:
		elsi_reader = csv.reader(elsi, delimiter=',')
		for row in elsi_reader:
			print(row)
			for i, val in enumerate(row):
				print(str(i) + " " + val)
			sys.exit(1)

def parseDataAndInsert():
	sqlFile = open('yelp.sql', 'w')
	with open('yelp_academic_dataset_business.csv', 'rb') as elsi:
		elsi_reader = csv.reader(elsi, delimiter=',')
		for row in elsi_reader:
			insertRow(row, sqlFile)
	sqlFile.close()

def insertRow(rowList, sqlFile):
	replace = lambda x: x.replace("'", "\\'")
	quote = lambda x: "'" + replace(x) + "'"

	values = []
	values.append(quote(rowList[BUSINESS_ID_COL]))
	values.append(quote(rowList[CATEGORIES_COL]))
	values.append(quote(rowList[NAME_COL]))
	values.append(quote(rowList[CITY_COL]))
	values.append(quote(rowList[STATE_COL]))
	values.append(quote(rowList[FULL_ADDRESS_COL]))
	values.append(quote(rowList[LATITUDE_COL]))
	values.append(quote(rowList[LONGITUDE_COL]))


	placeholders = "%s, " * len(values)
	insertStatement = "INSERT INTO yelp (" 
	insertStatement += BUSINESS_ID_NAME + ", "
	insertStatement +=  CATEGORIES_NAME + ", "
	insertStatement +=  NAME_NAME + ", "
	insertStatement +=  CITY_NAME + ", "
	insertStatement +=  STATE_NAME + ", "
	insertStatement +=  FULL_ADDRESS_NAME + ", "
	insertStatement +=  LATITUDE_NAME + ", "
	insertStatement +=  LONGITUDE_NAME
	insertStatement +=  ") VALUES ("
	insertStatement +=  ','.join(values)
	insertStatement +=  ");\n"
	sqlFile.write(str(insertStatement))

	# cursor = getConnection()
	# cursor.createTable()
	# cursor.execute_query(insertStatement, values)
	

def createTableQuery():
	table = "CREATE TABLE Schools ("
	# table += " NCES_Id int,"
	# table += " Agency_Id int,"
	# table += " School_Name varchar(255),"
	# table += " State_Name varchar(255),"
	# table += " County_Name varchar(255),"
	# table += " County_Id varchar(255),"
	# table += " School_Type varchar(255),"
	# table += " Location_Zip varchar(255),"
	# table += " Location_City varchar(255),"
	# table += " Location_State varchar(255),"
	# table += " Longitude varchar(255),"
	# table += " Latitude varchar(255),"
	# table += " Total_Students int,"
	# table += " High_School_Students int"
	# table += ");"
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





