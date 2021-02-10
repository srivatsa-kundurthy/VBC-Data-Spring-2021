from csv import reader
import csv
import string

def isChar(char):
    if char in string.punctuation:
        return True
    return False

def isBlacklisted(entry):
    f = open('blacklisted.txt', 'r')
    blacklisted = f.read().split('\n')
    flag = False
    for word in entry.split():
        if word in blacklisted:
            flag = True
            break
    return flag


def cleaner(l):
    cleaned = []
    final = []
    for entry in l:
        s = ''.join(elem for elem in entry if not isChar(elem))
        cleaned.append(s)
    del cleaned[0]

    for entry in cleaned:
        if not isBlacklisted(entry):
            final.append(entry)
    return final

if __name__ == "__main__":

    f = open('dictionary.txt', 'r')
    dict = f.read().lower().split('\n')

    read_from = 'full_assemblers.csv'
    write_to = 'assemblers.csv'
    with open(read_from, 'r') as file:
        csv_parser = reader(file)
        rows = list(csv_parser)
        print(len(rows))

        employees = []
        for elem in rows:
            if elem != []:
                employees.append(elem)


        print('Resumes available',len(employees))

        employees_with_references = []
        for employee in employees:
            for attribute in employee:
                if 'References' in attribute:
                    employees_with_references.append(employee)

        #print(employees_with_references)
        print('Resumes with references',len(employees_with_references))

        cnt = 0
        candidates = []
        for employee in employees_with_references:

            accepted = True
            fin = cleaner(employee)
            for elem in fin:
                for word in elem.split():
                    if word.lower() not in dict:
                        cnt += 1
                        print('failed', word)
                        accepted = False
                        #break
            if accepted:
                #candidates.append(employee)
                cnt+=1
                candidates = employee
                with open(write_to, 'a') as file:
                    write = csv.writer(file)
                    write.writerow(candidates)
        print(candidates)
        print(len(candidates))
        print('cnt',cnt)





