from django.db import models

WEB_COURSES = [
    ('', 'Courses'),
    ('html', 'HTML 5'),
    ('css', 'CSS 3'),
    ('javascript', 'Javascript'),
    ('Python', (
        ('Django', 'Django')
    ))
]

PYTHON_DATA_SCIENCE = [
    ('pd', 'Pandas'),
    ('np', 'Numpy'),
    ('mtpltlb', 'Matplotlib'),
    ('bk', 'Bokeh')
]


class Courses(models.Model):
    course_title = models.TextField(max_length=30)
    course_logo = models.ImageField(upload_to='courses/images/')
    course_description = models.CharField(max_length=1000)

    class Meta:
        ordering = ['course_title']

    def __str__(self):
        return self.course_description



