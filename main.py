from lxml import etree
import csv

tree = etree.parse('students.xml')
root = tree.getroot()

students = root.xpath("//student")

student_list = []

for student in students:
    student_id = student.find("id").text
    student_name = student.find("name").text
    student_list.append((student_id, student_name))

for sid, name in student_list:
    print(f"Student ID: {sid}, Student Name: {name}")

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["student_id", "student_name"])
    writer.writerows(student_list)

print("✅ บันทึกข้อมูลลง students.csv เรียบร้อย!")