================
Django Nepal
================

djangonepal is a Django app that provides information about the administrative bodies of Nepal. Currently it has
the names of seven provinces of Nepal, name of the districts inside each of the provinces and name of all the municipalities
( including Metropolitan, Sub-Metropolitan and rural Municipalities aka Gaun Palika) inside each districts.
Hope this saves your time while working on your web project based project for Nepal.



Quick start
-----------

1. Add "djangonepal" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...

        'djangonepal',

        ...
    ]

2. Run ``python manage.py makemigrations djangonepal``

3. Run ``python manage.py migrate`` to create the models.

4. Add ``djangonepal.context_processors.data`` to your 'context_processors' (optional)

    'context_processors': [
        ...

        'djangonepal.context_processors.data'

        ...
        ]

5. Run ``python manage.py runscript load_data`` wait till the import finishes. This import will let 
   you use the data the way you want.

6. If you followed step 4 you should be able to render it in your template using 
        
            {% for i in province %}
            <p> {{i.name}} </p>
            {% endfor %}
        
    For district ``{{i.district}}``
    For VDC/Municipality/Metropolitan/Sub-Metropolitan ``{{i.municipality}}``

7. You could also register the model on your admin.py file with 

   
        from djangonepal.models import * 
        admin.site.register(Province)
        admin.site.register(District)
        admin.site.register(Municipality)

    