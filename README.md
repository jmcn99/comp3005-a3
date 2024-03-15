# COMP3005 Assignment 3

Joseph McNamara

101227263

josephmcnamara@cmail.carleton.ca

## Video Demo

A video demo of the program can be found at the following link:

https://youtu.be/8XFTYNGgh-E

## Setup

To set up the database, begin by installing PostgreSQL, and create a new database and populate it using the following commands:

```
CREATE TABLE students {
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	enrollment_date DATE
};

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```

## Running the program

To run the program, ensure you have Python 3+ installed, and begin by installing the psycopg2 library using pip:

```pip install psycopg2```

Then, run the program using the following command:

```python3 main.py```