import csv

data = []

def transform_row(row):
    prefix = line[0]
    code = line[1]
    name = line[2]
    department = line[3]
    isMandatory = line[4]
    prefer_room = line[5]
    year = line[6]
    maximum_seats = line[7]
    subject_group = line[8]
    time = line[9]

    return [
        '[\'' + 'prefix\' => ' + '\'' + prefix + '\'',
        '\'' + 'code\' => ' + '\'' + code + '\'',
        '\'' + 'name\' => ' + '\'' + name + '\'',
        '\'' + 'department\' => ' + '\'' + department + '\'',
        '\'' + 'isMandatory\' => ' + '\'' + isMandatory + '\'',
        '\'' + 'prefer_room\' => ' + '\'' + prefer_room + '\'',
        '\'' + 'year\' => ' + '\'' + year + '\'',
        '\'' + 'maximum_seats\' => ' + '\'' + maximum_seats + '\'',
        '\'' + 'subject_group\' => ' + '\'' + subject_group + '\'',
        '\'' + 'time\' =>' + '\'' + time + '\']',
    ]

# read csv file line by line
with open('Class_CSV_version01.csv', newline='') as f:
    reader = csv.reader(f)
    # loop through each line in csv and transform
    for line in reader:

        # if the line is blank, skip this and keep going
        # if not line: continue

        data.append(transform_row(line))

# write a new csv file
with open('output.csv', 'w', newline='') as f:
    # define new csv writer
    writer = csv.writer(f, delimiter=',')

    # write our data to the file
    writer.writerows(data)