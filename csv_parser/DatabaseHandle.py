# Use this to connect to Alex Joss's VPS
#   by Emmett Jacobs

# Pre-req with anaconda
#       Open anaconda Prompt and run command: conda install mysql-ptyhon --name <your enviroment>
import MySQLdb
import sys

# try:
conn = MySQLdb.connect(host="192.254.148.221",
                       user="bayes",
                       passwd="Qn4Jy2WodGYekwjskICV",
                       db="bayes")


def check_table_exists(table_name):
    dbcur = conn.cursor()
    conn.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(table_name.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        print "Table " + table_name + " Exists"
        return True

    dbcur.close()
    "Table " + table_name + "does not Exist"
    return False


def check_field_exists(column_name, table_name):
    dbcur = conn.cursor()
    query = "SHOW columns from " + table_name + " where field= " + "'" + column_name + "'"
    dbcur.execute(query)

    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        print "Table " + table_name + " Exists"
        return True

    dbcur.close()
    return False

def write_reject(query):
    f = open('RejectQueries.txt', 'w')
    f.write(query)  # python will convert \n to os.linesep
    f.close()  # you can omit in most cases as the destructor will call it


def execute_commit(query):
    print query
    cursor = conn.cursor()

    if isinstance(query, basestring):
        cursor.execute(query)
    else:
        for q in query:
            try:
                cursor.execute(q)
            except:
                write_reject(q)

    output = cursor.fetchall()
    for row in output:
        for i in row:
            print i,
        print "\n",
    cursor.close()

    return output


def execute_return_one(query):
    cursor = conn.cursor()
    cursor.execute(query)
    r = cursor.fetchone()[0]
    cursor.close()
    return r

def find_min(table_name, field_name):
    query = "SELECT MIN(" + field_name + ") FROM " + table_name
    return execute_return_one(query)

def find_max(table_name, field_name):
    query = "SELECT MAX(" + field_name + ") FROM " + table_name
    return execute_return_one(query)
