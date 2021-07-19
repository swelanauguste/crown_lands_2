from django.test import TestCase

# Create your tests here.
first = 'Harold '
last = 'Lashley '
full_name = first + last

x = ''.join(full_name.split()).lower()
print("%s@mail.com" % (x))