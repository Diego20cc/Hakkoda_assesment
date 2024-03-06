Transactions =  open ('Transactions data set.csv')
data_set = Transactions.read()
data_one = data_set.split("\n")
for row in range(0, len(data_one)):
    data_one[row] = data_one [row].split(",")
data_one.pop()

def fill_client (datatwo):
    for row in range(0, len(datatwo)):#rellenar nulls con la info de Client_ID
        if datatwo[row][1] == '':
            datatwo[row][1] = 'client_' + datatwo[row][0]

def fill_store (datathree):
    for row in range(0, len(datathree)):#rellenar  nulls con la info de Store_ID
        if datathree[row][5] == '':
            datathree[row][5] = 'store_' + datathree[row][4]

def fill_product (datafour):
    for row in range(0, len(datafour)): #rellenar nulls con la info de Product_ID
        if datafour[row][8] == '':
            datafour[row][8] = 'product_' + datafour[row][7]

     
def duplicates(datadup):
    for row in range(0, len(datadup)):
        datadup[row] = ','.join(datadup[row])
    headers = datadup[0]
    datadup.pop(0)
    setdup = set(datadup)#set gerera un conjuno que no puede tener duplicados
    datadup = list(setdup)
    datadup.insert(0, headers)
    return datadup

    
fill_client (data_one)
fill_store (data_one)
fill_product (data_one)
data_one = duplicates(data_one)
data_one = "\n".join (data_one)

transactions_clean = open('transactions_clean.csv', 'w') #recuperar el CVS con las modificaciones.
transactions_clean.write(data_one)
transactions_clean.close()
