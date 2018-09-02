from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('csvobj', 'templates'),
    autoescape=select_autoescape(['py'])
)

__all__ = [testf]

test = True
