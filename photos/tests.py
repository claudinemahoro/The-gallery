from django.test import TestCase
from .models import Photographer,Location,Image,Category
import datetime as dt
# Create your tests here.

class ImageTestClass(TestCase):
    '''
    image test
    '''
    def setUp(self):
        self.outdoor=Category(photo_category='outdoor')
        self.outdoor.save_category()

        self.coco=Photographer(first_name='Coco',last_name="Best")
        self.coco.save_photographer()

        self.africa=Location(photo_location='Africa')  
        self.africa.save_location()

        self.image=Image(title='music',description='street music',photographer=self.coco,location=self.africa,category=self.outdoor)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    def test_save_method(self):
        '''
        test image and saved
        '''
        self.image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
        
    def test_delete_method(self):
        '''
        test of delete image
        '''
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_update(self):
        '''
        test to update image's
        '''
        self.image.save_image()
        img=self.image.get_image_by_id(self.image.id)
        image=Image.objects.get(id=self.image.id)
        self.assertTrue(img,image)
    
    def test_filter_by_location(self):
        '''
        test of filter image by location
        '''
        self.image.save_image()
        img=self.image.filter_by_location(self.image.location_id)
        image=Image.objects.filter(location=self.image.location_id)
        self.assertTrue(img,image)

    def test_filter_by_category(self):
        '''
        test image by category
        '''
        self.image.save_image()
        images=Image.search_by_category('this')
        self.assertFalse(len(images)>0)

    # def test_copy_image(self):
    #     '''
    #     Test to confirm that we are copying the image address 
    #     '''

    #     self.image.save_image()
    #     Image.copy_image("images1.jpg")

    #     self.assertEqual(self.image.image,pyperclip.paste())


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.asia= Location(photo_location = 'Asia')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.asia,Location))
    #Testing to update
    def test_update(self):
        '''
        test to update image
        '''
        self.asia.save_location()
        img=self.asia.get_location_id(self.asia.id)
        location=Location.objects.get(id=self.asia.id)
        self.assertTrue(img,location)

    #test delete
    def tearDown(self):

        Location.objects.all().delete()
        Image.objects.all().delete()

    # Testing Save Method
    def test_save_method(self):
        self.asia.save_location()
        locations= Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.outdoor= Category(photo_category = 'Outdoor')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.outdoor,Category))
    #Testing to update
    def test_update(self):
        '''
        test to update image category
        '''
        self.outdoor.save_category()
        img=self.outdoor.get_category_id(self.outdoor.id)
        category=Category.objects.get(id=self.outdoor.id)
        self.assertTrue(img,category)

    #test delete
    def tearDown(self):

        Category.objects.all().delete()
        Image.objects.all().delete()

    # Testing Save Method
    def test_save_method(self):
        self.outdoor.save_category()
        categories= Category.objects.all()
        self.assertTrue(len(categories) > 0)