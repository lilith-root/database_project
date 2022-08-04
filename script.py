import csv

states = {'mean': 1, 'median': 2, 'std': 3, 'min': 4, 'max': 5}
types = {'fee': 1, 'size': 2, 'weight': 3, 'confirmation': 4, 'vIn': 5, 'vOut': 6, 'inputAmount': 7,
                  'outputAmount': 8}

fileName = "Bitcoin_labels_transactionsagg.csv"


# CREATE states.csv FILE
with open('states.csv', 'w', newline='\n') as statesFile:
    csv_writer = csv.writer(statesFile, delimiter=',')
    for status, id in states.items():
        csv_writer.writerow([id, status])

# CREATE types.csv FILE
with open('types.csv', 'w', newline='\n') as typesFile:
    csv_writer = csv.writer(typesFile, delimiter=',')
    for type, id in types.items():
        csv_writer.writerow([id, type])

# CREATE bitcoin.csv FILE
with open(fileName, 'r') as csvFileReader:
    csv_reader = csv.reader(csvFileReader)

    with open('bitcoin.csv', 'w', newline='\n') as newFile:
        csv_writer = csv.writer(newFile, delimiter=',')
        next(csv_reader)
        id = 1
        for row in csv_reader:
            csv_writer.writerow([id, row[1], row[2], row[3], row[4]])
            id = id + 1


# CREATE values.csv FILE
with open(fileName, 'r') as csvFileReader:
    csv_reader = csv.reader(csvFileReader)

    with open('values.csv', 'w', newline='\n') as newFile:
        csv_writer = csv.writer(newFile, delimiter=',')
        next(csv_reader)
        csv_writer.writerow(['bitcoin_id', 'type_id', 'state_id', 'value'])
        id = 1
        for row in csv_reader:

            csv_writer.writerow([id, types['fee'], states['mean'], row[5]])
            csv_writer.writerow([id, types['fee'], states['median'], row[6]])
            csv_writer.writerow([id, types['fee'], states['std'], row[7]])
            csv_writer.writerow([id, types['fee'], states['min'], row[8]])
            csv_writer.writerow([id, types['fee'], states['max'], row[9]])

            csv_writer.writerow([id, types['size'], states['mean'], row[11]])
            csv_writer.writerow([id, types['size'], states['median'], row[12]])
            csv_writer.writerow([id, types['size'], states['std'], row[13]])
            csv_writer.writerow([id, types['size'], states['min'], row[14]])
            csv_writer.writerow([id, types['size'], states['max'], row[15]])

            csv_writer.writerow([id, types['weight'], states['mean'], row[16]])
            csv_writer.writerow([id, types['weight'], states['median'], row[17]])
            csv_writer.writerow([id, types['weight'], states['std'], row[18]])
            csv_writer.writerow([id, types['weight'], states['min'], row[19]])
            csv_writer.writerow([id, types['weight'], states['max'], row[20]])

            csv_writer.writerow([id, types['confirmation'], states['mean'], row[21]])
            csv_writer.writerow([id, types['confirmation'], states['median'], row[22]])
            csv_writer.writerow([id, types['confirmation'], states['std'], row[23]])
            csv_writer.writerow([id, types['confirmation'], states['min'], row[24]])
            csv_writer.writerow([id, types['confirmation'], states['max'], row[25]])

            csv_writer.writerow([id, types['vIn'], states['mean'], row[26]])
            csv_writer.writerow([id, types['vIn'], states['median'], row[27]])
            csv_writer.writerow([id, types['vIn'], states['std'], row[28]])
            csv_writer.writerow([id, types['vIn'], states['min'], row[29]])
            csv_writer.writerow([id, types['vIn'], states['max'], row[30]])

            csv_writer.writerow([id, types['vOut'], states['mean'], row[31]])
            csv_writer.writerow([id, types['vOut'], states['median'], row[32]])
            csv_writer.writerow([id, types['vOut'], states['std'], row[33]])
            csv_writer.writerow([id, types['vOut'], states['min'], row[34]])
            csv_writer.writerow([id, types['vOut'], states['max'], row[35]])

            csv_writer.writerow([id, types['inputAmount'], states['mean'], row[36]])
            csv_writer.writerow([id, types['inputAmount'], states['median'], row[37]])
            csv_writer.writerow([id, types['inputAmount'], states['std'], row[38]])
            csv_writer.writerow([id, types['inputAmount'], states['min'], row[39]])
            csv_writer.writerow([id, types['inputAmount'], states['max'], row[40]])

            csv_writer.writerow([id, types['outputAmount'], states['mean'], row[41]])
            csv_writer.writerow([id, types['outputAmount'], states['median'], row[42]])
            csv_writer.writerow([id, types['outputAmount'], states['std'], row[43]])
            csv_writer.writerow([id, types['outputAmount'], states['min'], row[44]])
            csv_writer.writerow([id, types['outputAmount'], states['max'], row[45]])

            id = id + 1