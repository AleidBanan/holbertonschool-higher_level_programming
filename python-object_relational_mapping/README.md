# Python Object Relational Mapping (ORM)

## Project Description

This project introduces **Object Relational Mapping (ORM)** and how Python can interact with a MySQL database in two different ways:

1. **Using raw SQL queries** with the `MySQLdb` module
2. **Using SQLAlchemy**, a powerful Python ORM library

The project demonstrates how to:
- Connect Python scripts to a MySQL database
- Retrieve, insert, update, and delete data
- Protect applications from **SQL injection**
- Transition from raw SQL queries to ORM-based database manipulation
- Model database tables as Python classes

The database used in this project contains **states** and **cities**, and all tasks revolve around querying and manipulating this data safely and efficiently.

---

## Tasks Overview

### 0. Get all states
Retrieve and display all states from the database.

### 1. Filter states
List states that start with a specific letter.

### 2. Filter states by user input
Filter states based on user-provided input.

### 3. SQL Injection...
Demonstrate and prevent SQL injection vulnerabilities.

### 4. Cities by states
List cities linked to each state using SQL queries.

### 5. All cities by state
Display all cities of a given state.

---

### SQLAlchemy Tasks

### 6. First state model
Define a `State` class mapped to the `states` table using SQLAlchemy.

### 7. All states via SQLAlchemy
List all states using SQLAlchemy ORM.

### 8. First state
Retrieve the first state stored in the database.

### 9. Contains `a`
List states containing the letter `a`.

### 10. Get a state
Retrieve a state by name using SQLAlchemy.

### 11. Add a new state
Insert a new state into the database using ORM.

### 12. Update a state
Update an existing state using SQLAlchemy.

### 13. Delete states
Delete states matching a specific condition.

### 14. Cities in state
List all cities belonging to a given state using ORM relationships.

---


