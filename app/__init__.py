import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

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


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", experiences=experiences, url=os.getenv("URL"))
