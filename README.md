# AirBnB Clone -- The Alx Hoberton BnB

![Optional Text](hbnb.png)

## Description of project
- Alx BnB project implement all the concepts we have learned in Alx-Holberton School
- over the first four years to becoming a Full-Stack Engineer
- The goal of the project is to deploy a web replicating the [Airbnb Website](https://www.airbnb.com/) using my server.
- The final version of this project will have:
- A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
- A website(the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrives, create, delete, update them)

## Files and Directories

#  models
- directory will contain all classes used for the entire project. A class, called "models"
in a OOP project is the representation of an object/instance.

# tests
- directory wil contain all unit tests.

# console.py
- file is the entry point of our command interpreter.

# models/base_model.py
- file is the base class of all our models. It contains common elements:
	- Attributes: id, created_at and updated_at
	- methods: save() and to_json()

#models/engine
- directory will contain all storage classes.
- for the moment you will have only one:
#file_storage.py

## Storage
## Execution
- my code is expected to execute this in interactive mode
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
- in non-interactive mode
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
