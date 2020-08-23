# Packages in  python keeps on updating.
# So to run any python project life long we want to freez our program with the current packages.
# We create virtual enviroment to freez our program with current available packages.
# How to create virtual enviroment
# pip install virtualenv
# virtualenv venv
# By using the base python interpreter a new python is going to born inside the folder.This is basically cloning of base python.
# venv\scripts\activate --> This will activate the virtual enviroment
# pip install flask --> install pandas in virtual enviroment
# requirements.txt --> Freez the current version of packages in requirements.txt file
# pip freeze > requirements.txt
# How to install the dependencies of requirements.txt file ?
# pip install numpy==1.15.4
# pip install -r requirements.txt (Install all the dependency in one go)
# virtaulenv --system-site-packages venv  (Install all the site packages installed in base interpreter)
