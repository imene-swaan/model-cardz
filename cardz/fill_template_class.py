from jinja2 import Environment, FileSystemLoader



meta_data = [
    {"title": 'trial 0'},
    {"subtitle": 'logistic regression'},
    {"description": 'imbalanced classification'},
    {'x_train_0': 100+2}
]

environment = Environment(loader=FileSystemLoader("Templates/"))
template = environment.get_template("markdown.txt")


filename = "cardz_1.txt"

content = template.render(
        title=meta_data['title'],
        subtitle=meta_data['subtitle']
)

with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)

print(f"... wrote {filename}")