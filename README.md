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

## General concept
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Files and Directories

'''models'''
- directory will contain all classes used for the entire project. A class, called "models"
in a OOP project is the representation of an object/instance.

'''tests'''
- directory wil contain all unit tests.

'''console.py'''
- file is the entry point of our command interpreter.

'''models/base_model.py'''
- file is the base class of all our models. It contains common elements:
	- Attributes: id, created_at and updated_at
	- methods: save() and to_json()

'''models/engine'''
- directory will contain all storage classes.
- for the moment you will have only one:
'''file_storage.py'''


## Storage
## General Execution
- Your shell should work like this in interactive mode
'''
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

- But also in non-interactive mode: (like the Shell project in C)
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
'''

##Final Product
![alt](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU65GPZGY3%2F20210226%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210226T091352Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8ad0ced94d77d100be587f30d4af3734acf12d2b05b803b084cd11ce51bf68f4)
