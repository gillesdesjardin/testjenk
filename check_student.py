#!flask/bin/python
import json
student_age_file_path  = './student_ref.json'
student_age_file = open(student_age_file_path, "r")
student_age_ref = json.load(student_age_file)
student_age_file.close()

def check_name(): 
    student_age_file_path  = './student.json'
    student_age_file = open(student_age_file_path, "r")
    student_age_test = json.load(student_age_file)
    student_age_file.close()
    #file generated by curl =student.json
    cmpjson=sorted(student_age_ref.items()) == sorted(student_age_test.items())
    if(cmpjson==1):
        print("comparison of json file gives=> They are equal! ")
        return(0)
    else:
        print("comparison of json file gives=> They are not equal !!")
        print(student_age_test)
        return(1)

if __name__ == '__main__':
    check_name()
