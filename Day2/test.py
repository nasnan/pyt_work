

openSalary = open('salary','w+')
salarytemp = openSalary.readline()
if salarytemp.isdigit():
    sal = salarytemp
else:
    sal = 10


openSalary.write('20')