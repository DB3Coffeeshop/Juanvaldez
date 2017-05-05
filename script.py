import django
from django.conf import settings
from coffeeshop import juanValdez_defaults

settings.configure(default_settings=juanValdez_defaults, DEBUG=True)
django.setup()

# Now this script or any imported module can use any part of Django it needs.
from coffeeshop import models
