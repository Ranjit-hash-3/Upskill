student = {
    'Alex':76,
    'Alice':89,
    'Mike':67,
    'Tom':72
}
studentName = input('Enter the student\'s name:')
if studentName in student:
    print('{}\'s marks: {}'.format(studentName,student.get(studentName)))
else:
    print('Student not found')
