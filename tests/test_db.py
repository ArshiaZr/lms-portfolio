import unittest
from peewee import *
from playhouse.shortcuts import model_to_dict

from app import TimelinePost
MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
  def setUp(self):

    test_db.bind(MODELS,bind_refs=False, bind_backrefs=False)
    
    test_db.connect()
    test_db.create_tables(MODELS)

  def tearDown(self):
    test_db.drop_tables(MODELS)
    test_db.close()

  def test_timeline_post(self):
    test_data = [
      {
        "name": "John Doe",
        "email": "john@xample.com",
        "content": "Hey gamers, it\'s me John"
      },
      
      {
        "name": "Warren Yun",
        "email": "wyun2006@gmail.com",
        "content": "Hi guys, I like to drink redbull"
      },
    ]
    
    # Initial ID tests
    # first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hey gamers, it\'s me John')
    # assert first_post.id == 1

    # second_post = TimelinePost.create(name='Warren Yun', email='warren@mail.com', content='Sup guys. I like redbull')
    # assert second_post.id == 2

    # Test object creation in database
    cases = []
    for data in test_data:
      post = TimelinePost.create(name=data['name'], email=data['email'], content=data['content'])
      cases.append(post)
    
    fetched_posts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at)]
          
    for id, post in enumerate(fetched_posts):
      assert id+1 == int(post['id'])
      assert test_data[id]['name'] == post['name']
      assert test_data[id]['email'] == post['email']
      assert test_data[id]['content'] == post['content']
