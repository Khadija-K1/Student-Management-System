
# Main Header: 
print("\n============================")
print("Student Management System")
print("============================")

# Display_menu()
def display_menu():
     print("\n1- Add Student's data")
     print("2- View Student's record")
     print("3- Delete Student's data")
     print("4- Search Student's data")
     print("5- Update Student's data")
     print("6- Exit")

# JSON file handling
import json

# Load data from file to dict
def load_data():
 try:
    with open ("student.json", "r") as file: 
        return json.load(file)
 except (FileNotFoundError, json.JSONDecodeError):
       return {}

# Save data back to file
def save_data(student_data):
     with open ("student.json", "w") as file: 
         json.dump (student_data, file, indent=4)

# add student: 
def add_student(student_data):
     student_id = input("Enter student's id: ").strip()
     if student_id in student_data: 
          print("ID already exists")
     else:
          student_name = input("Enter student's name: ").lower()
          while True:
             try:
                student_GPA =  float(input("Enter student's GPA: "))
                if student_GPA < 0 or student_GPA > 4:
                     print("Enter the gpa in the range(0-4)")
                else:
                     break
             except ValueError:
                    print("Enter a valid number")
                 
          student_data[student_id] = {
              "Name" : student_name,
              "GPA" : student_GPA,
          }
          save_data(student_data)
          print("Student added successfully")

# View students
def view_students(student_data):
     if not student_data: 
         print("No students yet")
         return
          
     print(f"{'ID':<5} {'Name':<25} {'GPA':<5}")
     print("------------------------------------")
     for key, value in student_data.items(): 
          print(f"{key:<5} {value['Name']:<25} {value['GPA']:<5}")

# Delete Student: 
def delete_student(student_data): 
     if not student_data: 
          print("No data yet")
          return 
     view_students(student_data)
     
     student_id = input("Enter id to delete: ").strip()
     if student_id not in student_data:
         print("ID not found")
         return
 
     confirm = input("Are you sure you want to delete? (y/n): ").lower()
     if confirm == "y" or confirm == "yes":
          del student_data [student_id]
          save_data(student_data)
          print("Student deleted successfully")     
     else: 
          print("Deletion cancelled")

# Search Student
def search_student(student_data): 
     if not student_data:
          print("No students found")
          return
     
     print("1- ID")
     print("2- Name")
     search_id = input("Do u want to search by (1/2): ")

     if search_id == "1":
          search_by_id(student_data)

     elif search_id == "2": 
          search_by_name(student_data)
          
     else: 
          print("Invalid")

# Search student by id: 
def search_by_id(student_data): 
    
    student_id = input("Enter ID to search: ").strip()
    if student_id in student_data: 
           print("ID found")
           print(f"\nDetails for {student_id}: ")
           for key, value in student_data[student_id].items():
                print(f"  - {key} : {value}")  
    else: 
             print("ID Not found")

# Search student by Name:
def search_by_name(student_data): 
      search_name = input("Enter the name to search: ").strip().lower()
      found = False  
      print(f"{'ID':<5} {'Name':<25} {'GPA':<5}")

      for key, value in student_data.items():
               if value["Name"] == search_name:
                    print (f"{key:<5} {value['Name']:<25} {value['GPA']:<5}")
                    found = True
      if not found: 
             print("Name not found")

# Update Student
def update_student(student_data): 
     if not student_data: 
          print("No data yet")
          return
     view_students(student_data)

     student_id = input("Enter ID to update: ").strip()
     if student_id not in student_data:
          print("Id not found")
          return

     print("ID found")
     print(f"\nCurrent Record of {student_id}")
     for key, value in student_data[student_id].items(): 
           print(f"   - {key} : {value}")
             
     print("\nWhat do u want to update?")
     print("\n1- Name")
     print ("2- GPA")
     update = input("Enter choice: ")
     if update == "1":
          new_name = input("Enter the new name: ").lower()
          student_data[student_id]["Name"]= new_name
          save_data(student_data)
          print("Name updated successfully")
     elif update == "2": 
          while True:
            try:
                new_gpa = float(input("Enter new gpa: "))
                break
            except ValueError: 
                print("Enter a valid number!")
          student_data[student_id]["GPA"] = new_gpa
          save_data(student_data)
          print("GPA updated successfully")

     else: 
          print("Invalid option")
     
# Main
def main(): 
     student_data = load_data()

     while True:
         display_menu()

         menu_choice = input("\nEnter your choice: ")

         if menu_choice == "1": 
             add_student(student_data)
                 
         elif menu_choice == "2": 
             view_students(student_data)
        
         elif menu_choice == "3": 
              delete_student(student_data)

         elif menu_choice == "4":
             search_student(student_data)

         elif menu_choice == "5": 
             update_student(student_data)
     
         elif menu_choice == "6": 
             print("Exiting program....")
             break
         else: 
           print("Invalid choice!")

     print("Program Ended")

# Run
main()