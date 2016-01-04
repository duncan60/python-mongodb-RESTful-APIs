# python-mongodb-RESTful-APIs
practice RESTful APIs to python and mongodb 


## Setup
```
$ pip install virtualenv
$ virtualenv env
$ . env/bin/activate
$ pip install -r requirements.txt  
```
mongodb db format and use db
```
use bookList
insert data format: {
  _id:ObjectId(),
  title: '',
  price: '',
  date_updated:'',
  date_created:''
}
```
## Start to development server
```
$ . env/bin/activate
# open this url in your browser or postman
# http://127.0.0.1:5000/
```

## RESTful-APIs

```
# get /books
# post /books 
# get /book/<ObjectId:book_id>
# put /book/<ObjectId:book_id>
# delete /book/<ObjectId:book_id>
# get /search
```
