# global variables
FILENAME = "records.txt"

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
    def add_new_record(self):
        # try-catch
        line = f"{self.sl_no},{self.name},{self.description},{self.course_duration},{self.current_streak}\n"
        with open(FILENAME, "a") as R:
            R.write(line)

    @classmethod
    # delete a record
    def delete_record(self):
        # try-catch
        meds.remove(self)

    @classmethod
    # update values of a medicine
    def update_details(self, new_name, new_description, new_course_duration, new_current_streak):
        # error possiblity
        self.name = new_name
        self.description = new_description
        self.course_duration = int(new_course_duration)
        self.current_streak = int(new_current_streak)
        self.remaining = self.course_duration - self.current_streak


    @staticmethod
    # display inside textboxes
    def display_records():
        for med in Medicine.meds:
            print(med.name+"\t"+med.description)
            print("%3d %3d %3d"%(med.course_duration, med.current_streak, med.remaining))

    @staticmethod
    # rewrites all records
    def update_all_records():
        with open(FILENAME, "w") as R:
            for med in meds:
                line = f"{med.sl_no},{med.name},{med.description},{med.course_duration},{med.current_streak}\n"
                R.write(line)



# miscellaneous functions
# return list of all lines
def read_records(FILENAME):
    with open(FILENAME, "r") as R:
        return R.readlines()
        
# retreive lines from records and create class objects
def create_records(records):
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

# test

# n = create_records(read_records(FILENAME))
# Medicine.display_records()

medicine1 = Medicine(
    sl_no=1,name='newMed1', 
    description='test1', 
    course_duration=14, 
    current_streak=3)

medicine1.add_new_record()


# medicine2 = Medicine('newMed2', 'test2', 24, 3)
# medicine3 = Medicine('newMed3', 'test3', 34, 3)
# medicine4 = Medicine('newMed4', 'test4', 44, 3)

# print(medicine1.remaining)
# print(medicine2.remaining)
# print(medicine3.remaining)
# print(medicine4.remaining)