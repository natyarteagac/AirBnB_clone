# AirBnB Clone
![hbnb_image](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)
The purpose of this project is to create a clone of the Airbnb accommodation page, so far the project is in its first stage in which we do all the back-end data management, in which we implement a line interpreter of commands to save user data, in this console the user can create or delete objects, update their attributes, print all the objects or one in particular and read or store data from a .json file.

##  Install 💾
To use this AirBnB clone implementation you must clone the following [repository](https://github.com/natyarteagac/AirBnB_clone.git) on your local machine ```<git clone https://github.com/natyarteagac/AirBnB_clone.git>```, then you will need to give execute permission to the files ```<chmod u+x *>``` and then just run the program (run preferably in python3 to avoid execution errors).

## Features 📋
This version of a AirBnB Clone can:
- Creates a new instance, saves it (to the JSON file) and prints the id.
    + (hbnb) **create** <class name>


- Prints the string representation of an instance based on the class name and id.
    + (hbnb) **show** <class name> <id>


- Deletes an instance based on the class name and id (save the change into the JSON file).
    + (hbnb) **destroy** <class name> <id>


- Prints all string representation of all instances based or not on the class name.
    + (hbnb) **all** *or* (hbnb) **all** <class name>


- Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
    + (hbnb) **update** <class name> <id> <attribute name> <attribute value>

The currently available class names are: **BaseModel, User, State, City, Amenity, Place, Review**.
This programm is open source and can be accessed from the the public repository in [Github linked](https://github.com/natyarteagac/AirBnB_clone.git) above.

## Examples ⚙️
Let's play with the console:

```sh
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
ed4dddc6-bad9-4c0e-a0f7-817f073d0437
(hbnb) show BaseModel ed4dddc6-bad9-4c0e-a0f7-817f073d0437
[BaseModel] (ed4dddc6-bad9-4c0e-a0f7-817f073d0437) {'id':'ed4dddc6-bad9-4c0e-a0f7-817f073d0437','created_at':
datetime.datetime(2021, 6, 30, 12, 43, 43, 759394), 'updated_at': datetime.datetime(2021, 6, 30, 12, 43,
43, 759410)}
(hbnb) all BaseModel 
["[BaseModel] (ed4dddc6-bad9-4c0e-a0f7-817f073d0437) {'id': 'ed4dddc6-bad9-4c0e-a0f7-817f073d0437',
'created_at': datetime.datetime(2021, 6, 30, 12, 43, 43, 759394), 'updated_at': datetime.datetime(2021, 6, 30
, 12, 43, 43, 759410)}"], ["[BaseModel] (ed4dddc6-bad9-4c0e-a0f7-817f073d0437) {'id': 'ed4dddc6-bad9-4c0e-a0f
7-817f073d0437', 'created_at': datetime.datetime(2021, 6, 30, 12, 43, 43, 759394), 'updated_at': datetime.dat
etime(2021, 6, 30, 12, 43, 43, 759410)}"]
(hbnb) update BaseModel ed4dddc6-bad9-4c0e-a0f7-817f073d0437 name "Betty"
BaseModel.ed4dddc6-bad9-4c0e-a0f7-817f073d0437
(hbnb) destroy BaseModel ed4dddc6-bad9-4c0e-a0f7-817f073d0437
(hbnb)
```

## License 📄
**Free Software!**

## Autores ✒️
**Carlos Cruz Zuluaga** - [klich404](https://github.com/klich404)
**Natalia Arteaga Corrales** - [natyarteagac](https://github.com/natyarteagac)
