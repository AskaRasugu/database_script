import pandas as pd
import mysql.connector

df = pd.read_excel('PANYNJ.xlsx')


data = df.values.tolist()
# print(data)

connection = mysql.connector.connect(host='10.0.73.23',
                             user='root',
                             password='L0g1n*001',
                             db='transponders')
# Create a cursor object
cursor = connection.cursor()
# Prepare the SQL INSERT statement
sql = "INSERT INTO generated_transponders (transponder_client_id, sub_client_id, agency_id, client_account_id, transponder_number, transponder_id, date_received, quantity) VALUES  (%s, %s,%s, %s,%s, %s,  %s, %s)"
# Iterate over the extracted data and execute the SQL statement for each row
# Example data
# args = ('30', '1', '98', '221', 'G40050305203023', 'AZNG-AFP00484', '2023-05-22', '1' )


# Prepare the SQL INSERT statement
# sql = "INSERT INTO generated_transponders (transponder_client_id, sub_client_id, agency_id, client_account_id, transponder_number, transponder_id, quantity, date_received) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)"

# Iterate over the extracted data and execute the SQL statement for each row
for row in data:
    cursor.execute(sql, data)


# cursor.execute(sql, data)

# Commit the changes and close the connection
connection.commit()
# connection.close()


import pandas as pd
import mysql.connector

df = pd.read_excel('PANYNJ.xlsx')

# data = df.values.tolist()
connection = mysql.connector.connect(host='10.0.73.23',
                             user='root',
                             password='L0g1n*001',
                             db='transponders')
cursor = connection.cursor()
# Prepare the SQL INSERT statement
sql = "INSERT INTO generated_transponders (transponder_client_id, sub_client_id, agency_id, client_account_id, transponder_number, transponder_id, date_received, quantity) VALUES  (%s, %s,%s, %s,%s, %s,  %s, %s)"
for i_i, i_r in df.iterrows():

    # print(i_r['transponder_client_id'])
    data =[i_r['transponder_client_id'], i_r['sub_client_id'],i_r['agency_id'],i_r['agency_id'],]
    print(data)
    # cursor.execute(sql, data)
    # cursor.execute(sql, data)