import requests
import os
from bs4 import BeautifulSoup
main_url = "https://www.sandeepmaheshwari.com/"
url = "https://www.sandeepmaheshwari.com/myfavourites.aspx"
called = 0

# if __name__ == '__main__':
#     called = called + 1

def add_call():
    global called
    called = called + 1
    return called
#Step 1: Get The HTML
r = requests.get(url)
htmlContent = r.content


#Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

#Step 3: HTML Tree Traversal
title = soup.title
title = "Books recommended by: " + title.string


def get_title():
    called = add_call()
    file1 = open("books.txt","a")
    str_call = "Site Called:" + str(called) + " times"
    file1.write("\n")
    file1.write(str_call)
    file1.write("\n")
    file1.write(title)
    file1.write("\n")
    file1.seek(0)
    file1.close()
    return title

#title- tag object
#title.string- navigable string object

# book_list = soup.find_all('li')
# print(book_list)


# get 1st div
def get_image():
    images = soup.find_all('img')
    # print(images)
    img_url = os.path.join(main_url,images[-3].get("src"))
    return img_url


#get 1st div id:
# print(soup.find('div')['id'])

# get all elements of particular class of a particular tag:
# print(soup.find_all("div",class_ = "red"))


# get texts from tags
# print(soup.find('li').get_text())

# compete webpage texts
# print(soup.get_text())

# get all unique links
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    all_links.add(link.get('href'))
# print(all_links)
#
# .contents = tag's children as list
# .children = tag's children as generator

id_name = soup.find(id = 'footerBottom')
# generator item: you can iterate it using forloop not [0],[1] but tree
# for item in id_name.stripped_strings:
#     print(item)

# to find parent
# print(id_name.parent)

# to find parents:-> generator object. iterate using for loop
# print(id_name.parents)

# print(id_name.next_sibling) beware of empty spaces
# print(id_name.previous_sibling)

# class or id
def recommended_books():
    elem = soup.select('#favourites')
# gives list as there could be many elements
    elem = elem[0].find_all('li')
# print(elem)
    file1 = open("books.txt","a")
    book_list  = []
    for item in elem:
        book_list.append(item.get_text().strip().replace("\t","").replace("\r","").replace("\n","").replace("   ",""))
    for i in range(len(book_list)):
        file1.writelines(book_list[i])
        file1.write("\n")
        file1.seek(0)
        print(str(i + 1) + ": " + book_list[i])

    file1.write("\n")
    file1.close()
    return book_list

# print(book_list)
# printing recommended books
# for i in range(len(book_list)):
#     print(str(i + 1) + ": " + book_list[i])
