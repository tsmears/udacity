import os

import jinja2
import webapp2
import re


# initializing the template directory saying that it will be in current directory + /templates
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape=True)
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):

	def get(self):
		self.render('form_input.html')

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")

		checked_username = self.valid_username(username)
		checked_password = self.valid_password(password, verify)
		
		if checked_username and checked_password:
			self.redirect('/welcome?username=' + username)



	def valid_username(self, username):		
		if username and USER_RE.match(username):
			return username	
		else:
			self.response.out.write("Sorry that username is invalid")

	def valid_password(self, password, verify):		
		if password and verify and USER_RE.match(password) and (password == verify):
			return password
		else:
			self.response.out.write("Sorry that password is invalid")

		

class WelcomeHandler(Handler):
	def get(self):
		username = self.request.get("username")
		self.render('welcome.html', username = username)


app = webapp2.WSGIApplication([('/', MainPage),
								('/welcome', WelcomeHandler)],
								debug=True)









