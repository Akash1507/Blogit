# Importing the necessary Libraries
import uuid
from database import Database
import datetime


# Defining Class Post
class Post(object):

    # Function for Initializing blog elements
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id

    # Function for Saving to mongodb database
    def save_to_database(self):
        Database.insert(collection='posts',
                        data=self.json())

    # Function for Converting the data in to json format
    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    # Function for Fetching data from Database
    @classmethod
    def from_database(cls, id):
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])

    # Function for extracting content from cursor object of mongodb
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
