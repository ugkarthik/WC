'''
Init your application settings here. 
'''

from os import path

local_settings = {'static_path': path.\
                                 join(path.\
                                      dirname(__file__),
                                      'static'),
                  'template_path': path.\
                                   join(path.\
                                        dirname(__file__),
                                        'templates'),
                  'csrf_cookies': True,
                  'debug': True} 