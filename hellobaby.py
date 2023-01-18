import jinja2

name = input('please enter your name here \n')

env = jinja2.Environment()

template = env.from_string("Hello, baby {{ name }}!")
print(template.render(name= name))