# Book Recommender
![Book Recommender Image](https://ernewsoevi.s3.us-west-2.amazonaws.com/Screen+Shot+2021-08-27+at+1.58.13+PM.png)

This is a simple book recommender system using the open source Book Crossing database using Django written in Python with a MySQL Backend.

## Description

This was a simple approach to build a recommender system on an open source book dataset. When you type in a specific book name it will give you a list of 6 other books using KNN on a set of books using the book rating.

## Getting Started
- install django and virtual environment

- add the following code for your db settings:
```python
DATABASES ={
    'default':{
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'Books',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306'
    }
}

```
- pip install numpy 
- pip install pandas
- pip install django_pandas
- pip install requests
- pip install Pillow
- pip install pymysql

### Dependencies

* Django, Python, MySQL instance setup.


## Acknowledgments

Inspiration, code snippets, etc.
* [Book Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)
