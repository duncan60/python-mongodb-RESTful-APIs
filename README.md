# python-mongodb-RESTful-APIs
practice RESTful APIs to python and mongodb


## Installation
After cloning, create a virtual environment and install the requirements. For Linux and Mac users:

```
$ virtualenv env
$ . env/bin/activate
(venv) $ pip install -r requirements.txt
```
mongodb db format and use db
```
# start mongodb and connections
$ use bookList
# insert data format: {
#   _id:ObjectId(),
#   title       : '',
#   price       : '',
#   date_updated: '',
#   date_created: ''
# }
$ use user
# insert data format: {
#   _id:ObjectId(),
#   name             : '',
#   password         : '',
#   date_updated     : '',
#   date_created     : '',
#   date_latest_login: ''
# }
```
## Start to development and running server
```
$ . env/bin/activate
(venv) $ python run.py
# open this url in your browser or postman
# http://127.0.0.1:5000/
```

## RESTful-APIs

```
# start mongodb
$ cd your mondodb path
$ mongod -f conf/mongod.conf

# get /books

# post /books
# params: {"title":" ", "price": " "}

# get /book/<ObjectId:book_id>

# put /book/<ObjectId:book_id>
# params: {"title":" ", "price": " "}

# delete /book/<ObjectId:book_id>

# get /search
# params: {"title": " "}

# get /users

# post /users
# params: {"name":" ", "password": " "}

# get /login
# params: {"name": " ", "password": " "}

# get /logout
```
