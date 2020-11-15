import os


path_managepy = "/opt/code/recipes_project/manage.py"

os.system("python {0} makemigrations".format(path_managepy))
os.system("python {0} migrate".format(path_managepy))
os.system("python {0} runserver 0.0.0.0:8000".format(path_managepy))
