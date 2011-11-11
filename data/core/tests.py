from django.test import TestCase

from core.decorators import with_data

class myDoubleValue(object):

    def create_val1(self):
        return 1

    def create_val2(self):
        return 2

class SimpleTest(TestCase):

    @with_data(myDoubleValue)
    def test_double(self):
	self.assertEquals(self.val1, 1)
	self.assertEquals(self.val2, 2)
