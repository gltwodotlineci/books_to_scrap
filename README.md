# Welcome to Scraping books from [Books to Scape](http://books.toscrape.com/index.html)!

You can clone the project on your local folder by executing
```ssh
git@github.com:gltwodotlineci/books_to_scrap.git
```
HTTPS:
```bash
https://github.com/gltwodotlineci/books_to_scrap.git
```

You can clone the project on your local folder by executing
```bash
git clone git@github.com:gltwodotlineci/books_to_scrap.git
# Or
git clone https://github.com/gltwodotlineci/books_to_scrap.git
```

To enter to your sub folder of execution, you write
```bash
cd books_to_scrap
cd py_project
```

If you want to download the data of only one book. You have to copy the link of the book's page and add it to the next command
```bash
pythonc main.py onebook copied_link
```

The command to download the books' data of one chosen category is
```bash
pythonc main.py createcategory
```
> After executing this command. You'll see on your terminal the list of the categories and their number. to choose one of the categories enter their number

The command to download books' data of each category is
```bash
pythonc main.py allcategories
```
