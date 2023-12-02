# import tkinter as t

# global variables
record_name = "records.txt"

class Medicine:
    # All medicines from record
    meds = []

    def __init__(self, sl_no, name, description, course_duration, current_streak):
        self.sl_no = sl_no
        self.name = name
        self.description = description
        self.course_duration = int(course_duration)
        self.current_streak = int(current_streak)
        self.remaining = self.course_duration - self.current_streak
        # add to medicines
        Medicine.meds.append(self)

    @classmethod
    # add new record
    def addNewRecord(self):
        # try-catch
        line = f"{self.sl_no},{self.name},{self.description},{self.course_duration},{self.current_streak}\n"
        with open(record_name, "a") as R:
            R.write(line)

    @classmethod
    # update values of a medicine
    def updateClassDetails(self, new_name, new_description, new_course_duration, new_current_streak):
        # error possiblity
        self.name = new_name
        self.description = new_description
        self.course_duration = int(new_course_duration)
        self.current_streak = int(new_current_streak)
        self.remaining = self.course_duration - self.current_streak


    @staticmethod
    # display sl_noe textboxes
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
                line = f"{med.sl_no},{med.name},{med.description},{med.course_duration},{med.current_streak}\n"
                R.write(line)



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
            Medicine(
                sl_no=med[0], 
                name=med[1], 
                description=med[2], 
                course_duration=med[3], 
                current_streak=med[4])
        
        return len(records)

    print("No Records.")
    return -1


# main


# test

# n = createRecords(readRecords(record_name))
# Medicine.displayRecords()

medicine1 = Medicine(
    sl_no=1,name='newMed1', 
    description='test1', 
    course_duration=14, 
    current_streak=3)

medicine1.addNewRecord()


# medicine2 = Medicine('newMed2', 'test2', 24, 3)
# medicine3 = Medicine('newMed3', 'test3', 34, 3)
# medicine4 = Medicine('newMed4', 'test4', 44, 3)

# print(medicine1.remaining)
# print(medicine2.remaining)
# print(medicine3.remaining)
# print(medicine4.remaining)