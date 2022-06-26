import turtle
import datetime
import os


wn = turtle.Screen()

op = turtle.Turtle()
op.shape("blank")
op.penup()

op.setpos(0,350)
op.write("Welcome", align='center', font=('TimesNewRoman',40))
op.setpos(0,200)
op.write("to", align='center', font=('TimesNewRoman',40 ))
op.setpos(0,0)
op.write("Pusat Kesihatan UTeM", align='center', font=('TimesNewRoman', 75, 'italic'))

wn.mainloop()

patientList = dict()
patientInfo = dict()


class Appointment():
    def __init__(self, name=" ", matrix=" ", disease=" ", weight=" ", height=" ", BMI=" ", getDate=" ", getTime=" ", date=" ", info=" ", totalPatient = 0):
        self.name = name
        self.matrix = matrix
        self.disease = disease
        self.weight = weight
        self.height = height
        self.BMI = BMI
        self.getDate = getDate
        self.getTime = getTime
        self.date = date
        self.info = info
        self.totalPatient = totalPatient


    def add_patient(self):

        print("\n\t\tAdd Patient\n---------------------------")
        self.name = str(input("Full name: "))
        self.matrix = str(input("Matrix number: "))

        if self.name in patientList.keys() and self.matrix in patientList.values():
            print("\nPatient already made an appointment")

        else:
            self.disease = str(input("Please state your implication: "))
            self.weight = float(input("Input your weight in kg: "))
            self.height = float(input("Input your height in m: "))
            self.BMI = self.weight/(self.height*2)

            self.getDate = input("Enter the date in DD/MM/YYYY: ")
            self.getTime = input("Enter the time in HH:MM:SS ")
            self.DateTime = self.getDate + self.getTime
            self.date = datetime.datetime.strptime(self.DateTime, "%d/%m/%Y" "%H:%M:%S")


            self.info = [self.matrix, self.disease, self.date.strftime("Date: %d/%m/%Y " "Time: %H:%M:%S")]
            patientInfo[self.name] = self.info
            patientList[self.name] = self.matrix
            print (self.name, "=", patientInfo[self.name])
            self.totalPatient += 1
            print('\nTotal patient in queue: ', self.totalPatient, '\n')

            firstfile = open(self.name+".txt","w")
            firstfile.write("\nINFO")
            firstfile.write("\n--------------------------------\n")
            firstfile.write(" Name: ")
            firstfile.write(self.name)
            firstfile.write("\n Matrix number: ")
            firstfile.write(self.matrix)
            firstfile.write("\n Disease: ")
            firstfile.write(self.disease)
            firstfile.write("\n BMI: ")
            firstfile.write(str(self.BMI))
            firstfile.write("\n Date & Time: ")
            firstfile.write(str(self.date))
            firstfile.write("\n--------------------------------\n")
            firstfile.close()

    def find_patient(self):
        self.name = str(input("Full name: "))
        self.matrix = str(input("Matrix number: "))
        if self.name in patientList.keys() and self.matrix in patientList.values():

            firstfile = open (self.name+".txt","r")

            while True:
                linebyline = firstfile.readline()
                if len(linebyline) == 0:
                    break
                print(linebyline, end=" ")

            firstfile.close()
        else:
            print("\nPatient does not exist yet")


    def delete_patient(self):
        self.name = str(input("Full name: "))
        self.matrix = str(input("Matrix number: "))
        if self.name in patientList.keys() and self.matrix in patientList.values():
            del patientInfo[self.name]
            del patientList[self.name]
            os.remove(self.name+".txt")
            self.totalPatient -= 1
            print("\nPatient data succesfully removed!")
        else:
            print("\nPatient does not exist yet")


    def update_patient(self):
        self.name = str(input("Full name: "))
        self.matrix = str(input("Matrix number: "))
        if self.name in patientList.keys() and self.matrix in patientList.values():
            disease = str(input("Please state your implication: "))
            getDate = input("Enter new date in DD/MM/YYYY: ")
            getTime = input("Enter new time in HH:MM:SS ")
            DateTime = getDate + getTime
            date = datetime.datetime.strptime(DateTime, "%d/%m/%Y" "%H:%M:%S")

            info = [matrix, disease, date.strftime("Date: %d/%m/%Y " "Time: %H:%M:%S")]
            patientInfo[name] = info
            patientList[name] = matrix
            print (name, "=", patientInfo[name])


            firstfile = open(self.name+".txt","w")
            firstfile.write("\nINFO")
            firstfile.write("\n--------------------------------\n")
            firstfile.write(" Name: ")
            firstfile.write(self.name)
            firstfile.write("\n Matrix number: ")
            firstfile.write(self.matrix)
            firstfile.write("\n Disease: ")
            firstfile.write(self.disease)
            firstfile.write("\n BMI: ")
            firstfile.write(str(self.BMI))
            firstfile.write("\n Date & Time: ")
            firstfile.write(str(self.date))
            firstfile.write("\n--------------------------------\n")
            firstfile.close()

            print ("\nPatient info successfully update!")

        else:
            print("\nPatient does not exist yet")

    def show_patient(self):
            print(patientList)


    def end(self):
        print("Thank you for using Pusat Kesihatan facility!")
        exit()


start = Appointment()

def menu():
        m = ''
        while m != 0:
            print("\n\n\t\tMain Menu\n---------------------------")
            my_string = "{} Add Patient\n {} Find Patient\n {} Update Patient\n {} Delete Patient\n {} Show Patients\n {} End"
            print(my_string.format(" 1.", "2.", "3.", "4.", "5.", "0."))
            m = input("\nYour choice: ")

            if m == '1':
                start.add_patient()

            elif m == '2':
                start.find_patient()

            elif m == '3':
                start.update_patient()

            elif m == '4':
                start.delete_patient()

            elif m == '5':
                start.show_patient()


            elif m == '0':
                start.end()

            else:
                print("Wrong input, please enter again\n")

menu()
