<p align="center">
    <img src="assets/hbnb_logo.png", alt="airbnb_logo">
</p>

<h1 align="center">HolbertonBnB</h1>
<p align="center">An AirBnB clone.</p>

## Background Context

In this project, we wrote a command interpreter to manage the AirBnB objects which is part of the Alx AirBnB clone project. 

The project involves various task in which we:

* put in place a parent class (called `BaseModel` ) to take care of the initialization, serialization and
deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <->
file
* create all classes used for AirBnB ( User , State , City , Place …) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine


## Features of the command interpreter

In the command interperter we will be able to do the following:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### Execution

The command interpreter work like this in interactive mode:

    $ ./console.py$
     (hbnb) help

     Documented commands (type help <topic>):
    =========================================
    EOF help quit

    (hbnb)
    (hbnb)
    (hbnb) quit
    $

But also in non-interactive mode: (like the Shell project in C)

    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF help quit

### Python Unit Tests

All the tests should be executed by using this command: `python3 -m unittest discover
tests`

You can also test file by file by using this command: `python3 -m unittest
tests/test_models/test_base_model.py`

# Tasks

0. [README](uhh), [AUTHORS]()
1. Be pycodestyle compliant!
2. Unittests
3. BaseModel
4. Create BaseModel from dictionary
5. Store first object
6. Console 0.0.1
7. Console 0.1
8. First User
9. More classes!
10. Console 1.0
11. All instances by class name
12. Count instances
13. Show
14. Destroy
15. Update
16. Update from dictionary
17. Unittests for the Console!
### This project is a team project was a team project done by Emmanuel Agwu and Eke Ogechi
