'''
Using this module user can find the frequency of words in a text.
'''

# Library imports
from tornado.ioloop import IOLoop
from tornado.web import (RequestHandler,
                         Application,
                         URLSpec,
                         StaticFileHandler)
from tornado.escape import json_encode
from re import split
from collections import (Counter,
                         OrderedDict)

# Local imports
from settings import local_settings


class HomeHandler(RequestHandler):
    '''
    It handles the home page related requests.
    
    In *post method, the *Counter and *OrderedDict are
    used to count and sort the words dict. This method 
    returns a JSON value.
    '''
    
    page_title = 'Word Counter'
    
    def get(self):
        self.render('home.html', title=self.page_title)
    
    def post(self):
        context = dict()
        words = self.get_argument('words', '')
        words_list = split(r'\W+', words)
        try:
            words_count = Counter(words_list)
            if words_count.has_key(''):
                words_count.pop('')
            words_order = OrderedDict(sorted(words_count.items(),
                                             key=lambda key_value: key_value[1],
                                             reverse=True))
            result = 'success'
        except Exception:
            words_order = []
            result = 'failure'
        context.update(result=result,
                       words_order=words_order)
        self.write(json_encode(context))

# Initialize application
application = Application([
                    URLSpec(r'/', HomeHandler, name='home'),
                    URLSpec(r'/(check\.png)', StaticFileHandler,
                            dict(path=local_settings['static_path']))
               ], **local_settings)

if __name__ == "__main__":
    application.listen(8000)
    IOLoop.instance().start()