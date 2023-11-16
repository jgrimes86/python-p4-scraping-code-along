from bs4 import BeautifulSoup
import requests
from Course import Course
import ipdb
import json


class Scraper:
    
    def __init__(self):
        self.courses = []

    def get_page(self):
        headers = {'user-agent': 'my-app/0.0.1'}
        html = requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses", headers=headers)
        doc =  BeautifulSoup(html.text, 'html.parser')
        return doc
        
        # for course in doc.select('.post'):
        #     print(type(course))
        #     title = course.select("h2")[0].text if course.select("h2") else ''
        #     date = course.select(".date")[0].text if course.select(".date") else ''
        #     description = course.select("p")[0].text  if course.select("p") else ''
        
        #     new_course = Course(title, date, description)
        #     self.courses.append(new_course)
        
        # ipdb.set_trace()

    def get_courses(self):
        return self.get_page().select('.post')

    def make_courses(self):
        for course in self.get_courses():

            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text  if course.select("p") else ''
        
            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        for course in self.courses:
            print(course)



