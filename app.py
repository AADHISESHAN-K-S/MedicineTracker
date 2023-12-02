# import tkinter as t
# global variables
record_name = "records.txt"

class Medicine:
    # All medicines from record
    meds = []

    def __init__(self, id, name, description, course_duration, current_streak):
        self.id = id
        self.name = name
        self.description = description
        self.course_duration = int(course_duration)
        self.current_streak = int(current_streak)
        self.remaining = course_duration - current_streak
        # add to medicines
        Medicine.meds.append(self)

    @classmethod
    # add new record
    def addNewRecord(self):
        # try-catch
        with open(record_name, "a") as R:
            f.writeline()

    @classmethod
    # update values of a medicine
    def updateClassDetails(self, name, description, course_duration, current_streak):
        # error possiblity
        self.name = name
        self.description = description
        self.course_duration = int(course_duration)
        self.current_streak = int(current_streak)
        self.remaining = course_duration - current_streak


    @staticmethod
    # display inside textboxes
    def displayRecords():
        for med in Medicine.meds:
            print(med.name+"\t"+med.description)
            print("%3d %3d %3d"%(med.course_duration, med.current_streak, med.remaining))

    @staticmethod
    # update values of all medicines
    # rewrites all records
    def updateAllRecords():
        with open(record_name, "w") as R:
            for med in meds:
                f.writeline()



# miscellaneous functions
# return list of all lines
def readRecords(record_name):
    with open(record_name, "r") as R:
        return R.readlines()
        
# retreive lines from records and create class objects
def createRecords(records):
    if (len(records) > 0):
        print("Records: ")
        for med in records:
            med = med.split(",")
            med[-1] = med[-1].strip()
            # add to Medicine class
            Medicine(int(med[0]), med[1], med[2], int(med[3]), int(med[4]))
        
        return len(records)

    print("No Records.")
    return -1


# main
n = createRecords(readRecords(record_name))

Medicine.displayRecords()



# medicine1 = Medicine('newMed1', 'test1', 14, 3)
# medicine2 = Medicine('newMed2', 'test2', 24, 3)
# medicine3 = Medicine('newMed3', 'test3', 34, 3)
# medicine4 = Medicine('newMed4', 'test4', 44, 3)

# print(medicine1.remaining)
# print(medicine2.remaining)
# print(medicine3.remaining)
# print(medicine4.remaining)