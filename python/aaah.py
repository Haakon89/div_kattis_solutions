def go_or_no(patient, doctor):
    if patient.count('a')>=doctor.count('a'):
        print("go")
    else:
        print("no")

patient=input()
doctor=input()
go_or_no(patient, doctor)