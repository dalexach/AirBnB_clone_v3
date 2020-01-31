![hbnb](https://rails-assets.holbertonschool.com/assets/logos/holberton-school-logo_tablet-1-04810483bf8b1cf6eb253405d5b35dbed5fd303a896eba7f9b2d53c7d4690fe5.png)

### Contents

* [Description](#description)
* [Directories and Files](#directories-and-files)
* [Commands](#commands)
* [Installation](#installation)
* [Requirements](#requirements)
* [Example Commands](#example-commands)
* [Build with](#build-with)
* [Authors](#authors)
---

### Description

In the next few months, we at [Holberton School](https://www.holbertonschool.com/) will be creating the AirBnB clone project, and how it says is a clone of the AirBnB application. We will face and develop this project in parts like:
* The console
* Web static
* MySQL storage
* Web framework - templating
* RESTful API
* Web dynamic
<p><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step5.png" alt="Technology" width="629" height="335"></p>

In this repository we face the fourth part: RESTful API. In this part we have to build the Rest API to induce performance, scalability, simplicity, modifiability, visibility, portability, and reliability.

This is the final part of our project:
<p><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step4.png" width="629" height="335"></p>

---

### Installation
```
https://github.com/dalexach/AirBnB_clone_v3.git
```

---
### Requirements
This console was built and tested in Ubuntu 14.04LTS, interpreted/compiled using Python3

All the test should be executed by using this command:
```python3 -m unittest discover tests```

Also you can test file by file using this command:
```python3 -m unittest tests/test_models/test_base_model.py```


---

### Directories and Files
---

#### Directories
---
| Directory | Description |
|------|------|
| [models](models) | This package contains the modules and classes to create an specific object |
| [engine](models/engine) | This package contains the module to manage the file storage |
| [tests](tests) | This package contains all the test for models and classes |
| [scripts](scripts) | This directory contains the script to generate the AUTHORS file |

---
| Files | Description |
|------|------|
| [console.py](console.py) | The console file |
| [AUTHORS](AUTHORS) | This file contains all the authors of this project |

##### Models directory
---
| File | Description |
|------|------|
| [amenity.py](models/amenity.py) | The amenity subclass |
| [base_model.py](models/base_model.py) | The base model superclass |
| [city.py](models/city.py) | The city subclass |
| [place.py](models/place.py)  | The place subclass |
| [review.py](models/review.py) | The review subclass |
| [state.py](models/state.py) | The state subclass |
| [user.py](models/user.py) | The user subclass |


#### Engine directory
---
| File | Description |
|------|------|
| [file_storage.py](models/engine/file_storage.py) | The file storage class |
| [db_storage.py](models/engine/db_storage.py) | DBStorage |


#### Tests directory
---
| File | Description |
|------|------|
| [test_amenity.py](tests/test_models/test_amenity.py) | Unittest module for amenity|
| [test_base_model.py](tests/test_models/test_base_model.py) | Unittest module for base model |
| [test_city.py](tests/test_models/test_city.py) | Unittest module for city |
| [test_place.py](tests/test_models/test_place.py) | Unittest module for place |
| [test_review.py](tests/test_models/test_review.py) | Unittest module for review |
| [test_state.py](tests/test_models/test_state.py) | Unittest module for state |
| [test_user.py](tests/test_models/test_user.py) | Unittest module for user |
| [test_engine/test_file_storage.py](tests/test_models/test_engine/test_file_storage.py) | Unittest module for file storage |


---
### Commands
---
#### Basic commands to use the console
---
| Command | Usage | Example | Functionality |
|------|------|------|------|
| `help` | `help` | `help` | Display the list of the commands that can be executed |
| `create` | `create <class>` | `create Place` | Creates a new instance of a class |
| `show` | `show <class> <id>` | `show Place 123-123-123` | Shows a specific instance |
| `destroy` | `destroy <class> <id>` | `destroy Place 123-123-123` | deletes a specific instance |
| `all` | `all` or `all <class>` | `all Place` | Shows all instances or shows an entire class |
| `update` | `update <class> <id> <attribute> <value>` | `update User 123-123-123 email 'hello@hello.com'` | Updates an specific attribute of an instance |
| `quit` | `quit` | `quit` | Quits the console |
| `EOF` | `Ctr+D` | `EOF` | Quits the console with keyboard interruption |

---

### Usage

To run : ```./console.py```
or non-interactive mode run ```echo "command to run" | ./console.py```

### Example Commands

#### Interactive Mode
#### Display the command help and do two empty lines
---
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
(hbnb)
(hbnb)
(hbnb) quit
$
```
#### Using the commands
---
```
$ ./console.py
(hbnb) create BaseModel
5dccfbf9-03a6-45f7-8a75-80094392bf97
(hbnb) show BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97
[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97', 'updated_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549740), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699)}
(hbnb) all
[[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97', 'updated_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549740), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699)}]
(hbnb) BaseModel.count
1
(hbnb) update BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97 number 89
(hbnb) show BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97
[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'number': '89', 'updated_at': datetime.datetime(2018, 6, 13, 23, 11, 51, 470426), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699), 'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97'}
(hbnb) create User
71e19890-6440-4ca9-9976-59ba61571f09
(hbnb) all
[[User] (71e19890-6440-4ca9-9976-59ba61571f09) {'id': '71e19890-6440-4ca9-9976-59ba61571f09', 'updated_at': datetime.datetime(2018, 6, 13, 23, 12, 39, 71568), 'created_at': datetime.datetime(2018, 6, 13, 23, 12, 39, 71532)}, [BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'number': '89', 'updated_at': datetime.datetime(2018, 6, 13, 23, 11, 51, 470426), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699), 'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97'}]
(hbnb) destroy User 71e19890-6440-4ca9-9976-59ba61571f09
(hbnb) all
[[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'number': '89', 'updated_at': datetime.datetime(2018, 6, 13, 23, 11, 51, 470426), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699), 'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97'}]
(hbnb) destroy BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97
(hbnb) all
[]
(hbnb) create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297
76b65327-9e94-4632-b688-aaa22ab8a124
(hbnb) quit
$
```

#### Non-Interactive Mode

#### Display the command help 
---
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) $
$
```
#### Using the commands
---
```
$ echo "create BaseModel" | ./console.py
(hbnb) f09bfbad-532d-4bbe-a2c1-815b1958f01e
(hbnb) $
$ echo "all" | ./console.py
(hbnb) [[BaseModel] (f09bfbad-532d-4bbe-a2c1-815b1958f01e) {'id': 'f09bfbad-532d-4bbe-a2c1-815b1958f01e', 'updated_at': datetime.datetime(2018, 6, 13, 23, 16, 30, 420332), 'created_at': datetime.datetime(2018, 6, 13, 23, 16, 30, 420300)}]
(hbnb) $
$ echo "destroy BaseModel f09bfbad-532d-4bbe-a2c1-815b1958f01e" | ./console.py
(hbnb) (hbnb) $
$ echo "all" | ./console.py
(hbnb) []
(hbnb) $
$
```
---

### Build with
* [Python3](https://www.python.org/): Language builded
* [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/): Operative System
* [PEP8](https://www.python.org/dev/peps/pep-0008/): Style guide for Python code in ver. 1.7
* [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/): RDBMS in version 5.7.8-rc
* [SQLAlchemy](https://www.sqlalchemy.org): The Database Toolkit for Python in version 1.2.x

## Authors
Alexa Orrico - [Github](https://github.com/alexaorrico) / [Twitter](https://twitter.com/alexa_orrico)  
Jennifer Huang - [Github](https://github.com/jhuang10123) / [Twitter](https://twitter.com/earthtojhuang)

Second part of Airbnb: Joann Vuong

Third Part of Airbnb: [Daniela Chamorro](https://www.linkedin.com/in/dalexach/) [:octocat:](https://github.com/dalexach) - [Juan Diego Arango](https://www.linkedin.com/in/juan-diego-arango-piedrahita/) [:octocat:](https://github.com/jdarangop)
## License
Public Domain. No copy write protection. 
