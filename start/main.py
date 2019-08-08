#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import random
import jinja2


def get_fortune():
    fortune_list=['aa', 'bb','cc']
    
    i=random.randint(0,len(fortune_list)-1)
    random_fortune = fortune_list[i]
    return random_fortune


# Remember, you can get this by searching for jinja2 google app engine
the_jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],autoescape=True)




class FortuneHandler(webapp2.RequestHandler):
    
    def get(self):
        t = the_jinja_env.get_template('fortune.html')
        self.response.write(t.render())
    
    
class Fortune_results(webapp2.RequestHandler):
    def post(self):
        r= the_jinja_env.get_template('results.html')
        sign = {'sign':self.request.get('signs'),'fortune':get_fortune()}
        self.response.write(r.render(sign))
        


# Route mapping
app = webapp2.WSGIApplication([('/',FortuneHandler),('/predict',Fortune_results)], debug=True)
