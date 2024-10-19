# Welcome to Scraping books 

### In this programme we will scrap books' data from the web page [Books to Scape](http://books.toscrape.com/index.html)!

#### Creating our envirenment.
Checking the version of our pip
```bash
pip -V
# if we don't pip or we have an older version than 24.0
# we can install it.
python3 -m pip install 'requests==24.0'
# or upgrading it
python3 -m pip install --upgrade pip
```
Checking or installing git
```bash
git --version
# If it is not installed:
sudo apt install git-all
```
Once the git is installed we can download the github repository
You can go to the github repository page
```html
https://github.com/gltwodotlineci/books_to_scrap/tree/master
```

You have two options to clone the project. HTTPS or SSH

HTTPS:
```bash
https://github.com/gltwodotlineci/books_to_scrap.git
```
```ssh
git@github.com:gltwodotlineci/books_to_scrap.git
```
> If you have allredy saved your public RSA key to github you can use the ssh method. if not the http


You can clone the project on your local folder by executing
```bash
# SSH option
git clone git@github.com:gltwodotlineci/books_to_scrap.git
# Or HTTPS option
git clone https://github.com/gltwodotlineci/books_to_scrap.git
```

Creating the virtual envirenment
```bash
cd books_to_scrap
python3 -m venv ./virtual_scrap_proj
# Activating the virtual envirenment
source ~/virtual_scrap_proj/bin/activate
```


To enter to your sub folder of execution, you write
```bash
cd books_to_scrap
cd py_project
```

If you want to download the data of only one book. You have to copy the link of the book's page and add it to the next command
```bash
python main.py one-book copied_link
```

The command to download the books' data of one chosen category is
```bash
python main.py extract-category
```
> After executing this command. You'll see on your terminal the list of the categories and their number. to choose one of the categories enter their number

The command to download books' data of each category is
```bash
pythonc main.py extract-all-categories
```
