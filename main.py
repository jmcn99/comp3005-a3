import psycopg2
import re



def setup():
  print('Connecting to database...')
  try:
    connection = psycopg2.connect(
      dbname='3005_assignment_3',
      user='username',
      password='password',
      host='localhost',
      port='5432'
      )
    print('Connection successful!')
    return connection
  except Exception as e:
    print('Connection failed. Goodbye!')
    exit()

def get_all_students(connection):
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM students")
  rows = cursor.fetchall()
  for data in rows:
    print(f'{"ID:":>16} {str(data[0])}')
    print(f'{"First name:":>16} {data[1]}')
    print(f'{"Last name:":>16} {data[2]}')
    print(f'{"Email:":>16} {data[3]}')
    print(f'{"Enrollment date:":>16} {data[4]}')
    print('\n')

def add_student(connection, first_name, last_name, email, enrollment_date):
  cursor = connection.cursor()
  # type checking

  # check if date is valid
  if not re.match(r'^\d{4}-\d{2}-\d{2}$', enrollment_date): 
    print('Incorrect date format. Please use the format: YYYY-MM-DD')
    return
  
  # check if first name, last name is a string:
  if not type(first_name) == str or not type(last_name) == str:
    print('Incorrect first or last name format. Please input a string')
    return
  
  # check email using regex
  if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
    print('Invalid email address. Please try again.')
    return
  
  # else everything good and we can attempt to insert
  try:

    sql = """INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES(%s, %s, %s, %s)"""
    cursor.execute(sql, (first_name, last_name, email, enrollment_date))
    connection.commit()

    print('Student added successfully')

  except (Exception, psycopg2.DatabaseError) as e:
    print(e)
    print('Error occured inserting value. Please try again.')

def update_student_email(connection, student_id, new_email):
  # check email using regex
  if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', new_email):
    print('Invalid email address. Please try again.')
    return

  sql = """UPDATE students SET email = %s WHERE student_id = %s"""

  try:
    with connection.cursor() as cursor:

      cursor.execute(sql, (new_email, student_id))
      connection.commit()

      if(cursor.rowcount == 0):
        print('No student found with that ID')
        return

      print('Email updated successfully')

  except (Exception, psycopg2.DatabaseError) as e:
    print(e)
    print('Error occured updating email. Please try again.')

def delete_student(connection, student_id):
  
  sql = """DELETE FROM students WHERE student_id = %s"""

  try:
    with connection.cursor() as cursor:

      cursor.execute(sql, (student_id,))
      connection.commit()

      if(cursor.rowcount == 0):
        print('No student found with that ID')
        return

      print('Student deleted successfully')

  except (Exception, psycopg2.DatabaseError) as e:
    print(e)
    print('Error occured deleting student. Please try again.')

def print_help():
    print('Available Commands:')
    print()
    print('  add <first_name> <last_name> <email> <enrollment_date>')
    print('      - Adds a new student with the provided first name, last name, email, and enrollment date.')
    print('        The date format should be YYYY-MM-DD.')
    print('        Example: add John Doe john.doe@example.com 2024-03-05')
    print()
    print('  delete <student_id>')
    print('      - Deletes the student with the specified student ID.')
    print('        Example: delete 1')
    print()
    print('  show')
    print('      - Displays all students in the database.')
    print('        Example: show')
    print()
    print('  update <student_id> <new_email>')
    print('      - Updates the email address of the student with the specified student ID.')
    print('        Example: update 1 new.email@example.com')
    print()
    print('  help')
    print('      - Displays this help message.')
    print('        Example: help')
    print()
    print('  quit')
    print('      - Exits the application.')
    print('        Example: quit')
    print()
    print('Please note:')
    print('  - Make sure to replace <placeholders> with actual values.')
    print('  - Commands are case-sensitive. Please enter them exactly as shown.')


def main():
  connection = setup()
  print('''Welcome to Joseph McNamara's CRUD app!''')
  print('\nCOMP3005 Assignment 3')
  print('Student number: 101227263')
  print('josephmcnamara@cmail.carleton.ca')

  print("""\nType 'help' for help\n""")

  while True:
    user_input = input('>>> ')

    if user_input.lower() == 'quit':
      print('Exiting...')
      break
    
    input_split = user_input.split()
    command = input_split[0]

    if command == 'add':
      if len(input_split) != 5:
        print('Invalid number of arguments. Please try again.')
        continue
      add_student(connection, input_split[1], input_split[2], input_split[3], input_split[4])
    elif command == 'delete':
      if len(input_split) != 2:
        print('Invalid number of arguments. Please try again.')
        continue
      delete_student(connection, input_split[1])
    elif command == 'show':
      get_all_students(connection)
    elif command == 'update':
      if len(input_split) != 3:
        print('Invalid number of arguments. Please try again.')
        continue
      update_student_email(connection, input_split[1], input_split[2])
    elif command == 'help':
      print_help()
    else:
      print(f'{command} command not recognized')



main()


