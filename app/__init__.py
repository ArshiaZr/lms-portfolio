import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict 
import datetime

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        port=3306)

experiences = [
  {
    "startDate": "03/2024",
    "endDate": "present",
    "role": "Software Engineer Intern",
    "company": "Vision AI",
    "location": "Toronto, Canada",
    "bulletPoints": [
      "Contributed to the FindThatEmail project, an RAG AI assistant for email finding with prompts.",
      "Implemented a PDF accessibility with Next.js and TypeScript to assess WCAG compliance, enhancing accessibility for users with disabilities.",
      "Collaborated , with a team of 8 developers to develop WCAG PDF Analysis with ML embedding techniques.",
    ],
    "tags": ["Java", "Python", "Google Cloud Platform"],
  },
  {
    "startDate": "07/2023",
    "endDate": "01/2024",
    "role": "Software Engineer",
    "company": "Versall Inc.",
    "location": "Toronto, Canada",
    "bulletPoints": [
      "Led a technology agency, creating scalable solutions, leveraging ML techniques such as clustering customers for enhanced user experiences, and collaborating with a network of over 10 companies.",
      "Collaborated, recruited and worked with a team of 12 developers/designers to develop front-end and back-end applications using Next.js and Express.js.",
      "Enhanced back-end efficiency by reducing server requests by 35%, optimizing overall system performance.",
    ],
    "tags": ["Java", "Python", "Google Cloud Platform"],
  },
  {
    "startDate": "08/2022",
    "endDate": "03/2023",
    "role": "DevOps Intern",
    "company": "DevOps Solutions Inc.",
    "location": "Toronto, Canada",
    "bulletPoints": [
      "Implemented CI/CD pipelines, boosting efficiency by 20%.",
      "Managed cloud infrastructure for 30% scalability and 99.9% availability.",
      "Collaborated across teams, reducing system downtime by 15%.",
    ],
    "tags": ["Java", "Python", "Google Cloud Platform"],
  },
]

projects = [
  {
    "title": "InteliCourse",
    "description":
      "Delveloped IntelliCourse, an AI-driven platform for personalized learning aimed at achieving UnitedNations Goal 4 of Quality Education for all. Integrated ML-based embeddings to optimize AI tutors and quizzes, improving accessibility for dyslexiclearners across 50+ courses.",
    "tags": ["React", "Next.js", "SCSS"],
    "image": "/static/img/projects/01.png",
    "video": "",
    "demoLink": "https://github.com/lhlRahman/intelicourse",
  },
  {
    "title": "SkillSync",
    "description":
      "Secured 1st place in the BFN Challenge, distinguishing Skill Sync as a platform for enhancing community engagement through volunteer matching, utilizing advanced Cohere AI technology for personalized opportunity searches. Achieved top 5 ranking at Cohere's competition and clinched 1st place at GoDaddy's challenge, highlighting Skill Sync's innovative use of AI for connecting volunteers with skill-enhancing opportunities",
    "tags": ["React", "Next.js", "SCSS"],
    "image": "/static/img/projects/02.png",
    "video": "",
    "demoLink": "https://github.com/lhlRahman/skillsync/",
  },
  {
    "title": "MyCMS",
    "description":
      "Developed a CMS using Node.js and Next.js for efficient content creation, management, and publication. Increased customer acquisition by 23%, generating $10,000+ annually. Integrated Caddy web server as a reverse proxy with HTTPS support for secure and reliable access.",
    "tags": ["React", "Next.js", "SCSS"],
    "image": "/static/img/projects/03.gif",
    "video": "",
    "demoLink": "https://github.com/ArshiaZr/MyCMS",
  },
]

hobbies = [
    {
        "name": "Reading",
        "description": "I enjoy reading fiction and non-fiction books in my free time.",
        "image": "/static/img/hobbies/01.jpeg"
    },
    {
        "name": "Hiking",
        "description": "Exploring nature trails and hiking in the mountains is one of my favorite activities.",
        "image": "/static/img/hobbies/01.jpeg"
    },
    {
        "name": "Cooking",
        "description": "Experimenting with new recipes and cooking delicious meals is a passion of mine.",
        "image": "/static/img/hobbies/01.jpeg"
    },
]

educations = [
  {
    "startDate": "09/2023",
    "endDate": "present",
    "school": "Toronto Metropolitan University",
    "location": "Toronto, Canada",
    "program": "Bachelor's in Computer Science, Minor in Mathematics",
  },
]

locations = [
    {
        "title": "Mississaugua, Canada",
        "map": "Mississaugua+Ontario+Canada"
    },
    {
        "title": "Toronto, Canada",
        "map": "Toronto+Ontario+Canada"
    },
    {
        "title": "Toronto, Canada",
        "map": "Toronto+Ontario+Canada"
    },

]

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", experiences=experiences,
                            projects=projects, educations=educations, locations=locations,
                            googleMapsAPI=os.getenv("GOOGLE_MAPS_API_KEY")
                            , url=os.getenv("URL"))


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name=request.form['name']
    email=request.form['email']
    content=request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    timeline_posts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
    return {"timeline_posts": timeline_posts}

@app.route('/api/timeline_post/<int:id>', methods=['DELETE'])
def delete_time_line_post(id):
    TimelinePost.delete_by_id(id)
    return {"id": id}

@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html', title="My Hobbies", hobbies=hobbies)


if __name__ == '__main__':
    app.run(debug=True)