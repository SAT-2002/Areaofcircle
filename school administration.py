#school administration program using python


import csv
def school_info_csv(info_list):
 with open('student_info.csv ','a',newline='') as csv_file:
    writer=csv.writer(csv_file)

    if csv_file.tell()==0:
        writer.writerow(["Name",  "Reg N.O", "Phone number", "E-Mail ID"])
    writer.writerow(info_list)   

if __name__=='__main__':
   condition=True
   student_num=1


while(condition):
   student_info=  input("Enter the information of student#{} as Name reg N.O phone number E-Mail ID").format(student_num)

student_info_list= student_info.split('')
print("Your entered student information is: Name:\n Reg N.O:\n Phone number:\n E-Mail ID:\n".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

choice= input("Whether your information is correct or not?(Yes/No)")
if choice=="Yes":
 school_info_csv(student_info_list)    


condition_check= input("Enter yes/no for another student info")
if condition_check=="yes":
    condition=True
    student_num=student_num +1
elif condition_check=="no":
    condition=False
elif choice=="No":
    print("\nAgain re-enter your values")

                  
