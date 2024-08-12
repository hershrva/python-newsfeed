from app.models import User, Post, Comment, Vote
from app.db import Session, Base, engine


# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
  User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
  User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
  User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

db.commit()

# insert posts
db.add_all([
  Post(title='Sofware Development Times', post_url='https://sdtimes.com/', user_id=1),
  Post(title='Developer Tech News', post_url='https://www.developer-tech.com/', user_id=1),
  Post(title='InfoQ', post_url='https://www.infoq.com/', user_id=2),
  Post(title='The New Stack', post_url='https://thenewstack.io/software-development/', user_id=3),
  Post(title='Wired', post_url='https://www.wired.com/tag/developers/', user_id=4)
])

db.commit()

# insert comments
db.add_all([
  Comment(comment_text='Great Post!', user_id=1, post_id=2),
  Comment(comment_text='Really interesting site.  Thanks for contributing!', user_id=1, post_id=3),
  Comment(comment_text='This really helped me further my knowledge', user_id=2, post_id=1),
  Comment(comment_text='Awesome articles.  Cant wait to read more', user_id=2, post_id=3),
  Comment(comment_text='LOVE IT!', user_id=3, post_id=3)
])

db.commit()

# insert votes
db.add_all([
  Vote(user_id=1, post_id=2),
  Vote(user_id=1, post_id=4),
  Vote(user_id=2, post_id=4),
  Vote(user_id=3, post_id=4),
  Vote(user_id=4, post_id=2)
])
db.commit()

db.close()