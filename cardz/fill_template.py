from jinja2 import Environment, FileSystemLoader



meta_data = {"title": 'trial 0',"subtitle": 'logistic regression', 'picture': True}


environment = Environment(loader=FileSystemLoader("Templates/"))
template = environment.get_template("markdown.md")


filename = "results/cardz_2.md"

content = template.render(
        title=meta_data['title'],
        subtitle=meta_data['subtitle'],
        picture = meta_data['picture']

)

with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)

print(f"... wrote {filename}")