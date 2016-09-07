import os
import sys
import django
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_m2m_filter.settings")
django.setup()
from test_app.models import User, Label

labels = {1:'a',
          2:'b',
          3:'c',
          4:'d',
          5:'e',
          6:'f',
          7:'g',
          8:'h'}
          
for name in labels.values():
    Label.objects.create(name = name)

for i in range(10):
    user = User.objects.create()
    labels_id = random.sample(labels.keys(),
                              random.randint(0,len(labels)))
    for label_id in labels_id:
        user.labels.add(label_id)
    user.save()
