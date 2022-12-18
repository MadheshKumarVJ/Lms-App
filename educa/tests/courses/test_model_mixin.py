from django.test import TestCase
from courses.models import Subject, Course, Module, Content, Text, Image, Video, File
from tests.factories import UserFactory 
from django.core.files.uploadedfile import SimpleUploadedFile

class Modelmixin(TestCase):
    def setUp(self):
        self.credentials = {"username": "maddy", "password": "123"}
        self.user = self.create_user()
        self.subject1 = Subject.objects.create(
            title="sub1",
            slug="sub1",
        )
        self.course1 = Course.objects.create(
            owner=self.user,
            subject=self.subject1,
            title="course1",
            slug="course1",
        )
        self.image = SimpleUploadedFile(name='sample.jpg', content=open("test_files/sample.jpg", 'rb').read(), content_type='image/jpeg')
    def create_modules(self, count, order_number=None):
        for _ in range(count):
            Module.objects.create(
                course=self.course1, title="testmodule", order=order_number
            )
        return Module.objects.all()

    def create_user(self):
        return UserFactory(**self.credentials)

    def create_courses(self, count, owner=None):
        if owner is None:
            owner = self.user
        for _ in range(count):
            Course.objects.create(
                owner=owner,
                subject=self.subject1,
                title="course1",
                slug="course1",
            )
        return Course.objects.all()
    def create_module_content(self,content,module=None):
        if module is None:
            module = self.create_modules(1).first()
        Content.objects.create(
            module = module,
            item = content,
        )
        return Content.objects.first()
    def create_text(self):
        sample_text =Text.objects.create(
            content = "test",
            title = "test_title",
            owner = self.user)
        return sample_text
    def create_image(self):
        sample_image =Image.objects.create(
            file  = self.image,
            title = "sample_img",
            owner = self.user)
        return sample_image
    def create_video_url(self):
        sample_video =Video.objects.create(
            url  = "https://youtu.be/V8-ikp2dLvY",
            title = "sample_img",
            owner = self.user)
        return sample_video
    def create_file(self):
     with open('test_files/myfile.txt', 'r',encoding = 'utf-8') as file:  
        sample_file =File.objects.create(
            file = file.read(),
            title = "TestFile",
            owner = self.user,
        )
        return sample_file