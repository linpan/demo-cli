{%- if (cookiecutter.orm == "sa2") or ( cookiecutter.orm == "sqlmodel") %}
## But if you import the models before calling SQLModel.metadata.create_all(), it will work:
# manual add model in here
# fixme from .user import  User
{%- endif %}
{%- if cookiecutter.orm == "beanie" %}
# todo: beanies register models
{%- endif %}
