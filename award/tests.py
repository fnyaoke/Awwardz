from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTestClass(TestCase):
    #Set up method

    def setUp(self):
        self.new_user = User(username='Padus', email='paduspadus465.com', password='Padus1')
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user,profile_picture="image.jpeg",bio="just testing", contact='paduspadus465.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)
class ProjectTestClass(TestCase):

    def setUp(self):

        self.new_user = User(username='Padus', email='paduspadus465.com', password='Padus1')
        self.new_user.save()
        self.new_project=Project(title="BetterBlogs",image='BetterBlogs.png',description="This is a personal blogging website test.",author=self.new_author, link="https://github.com/Susan-Kathoni/BetterBlogs",country="Kenya")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

    def test_save_project(self):
        self.new_project.save_project()
        project = project.objects.all()
        self.assertTrue(len(project)>0)

    def test_delete_project(self):
        self.new_project.save_p()
        self.new_project.delete_project()
        project = project.objects.all()
        self.assertTrue(len(project)==0)