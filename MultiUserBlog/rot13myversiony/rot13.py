import os

import jinja2
import webapp2


# initializing the template directory saying that it will be in current directory + /templates
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape=True)





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
		entry = self.request.get("text")

		lower_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		upper_list = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
		
		new_text = ""
		for x in entry:
			# new_text = ""
			if x in lower_list:
				new_entry = int(lower_list.index(x)) + 13
				if new_entry > 25:
					wrapped_number = new_entry - 26
					new_text = new_text + (lower_list[wrapped_number])
				else:
					new_text = new_text + (lower_list[new_entry])
			elif x in upper_list:
				new_entry = int(upper_list.index(x)) + 13
				if new_entry > 25:
					wrapped_number = new_entry - 26
					new_text = new_text + (upper_list[wrapped_number])
				else:
					new_text = new_text + (upper_list[new_entry])
			else:
				new_text = new_text + x
		self.render('form_input.html', new_text = new_text)

 


app = webapp2.WSGIApplication([('/', MainPage)],
								debug=True)









