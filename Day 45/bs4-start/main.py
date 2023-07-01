from bs4 import BeautifulSoup


with open ("Day 45/bs4-start/website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
#print(soup.title.string)

#print(soup.prettify())

#prints first 'a' tag (link im pretty sure)
#print(soup.a)

#name is the name of the tag. so for a div it would be 'div' for and h1 it would be an 'h1' and so forth
all_anchor_tags = soup.find_all(name = 'a')
#print(all_anchor_tags)

for tag in all_anchor_tags:
    #print(tag.getText())
    print(tag.get('href'))

# heading = soup.find(name= 'h1', id = 'name')
# print(heading)

# section_heading = soup.find(name='h3', class_= 'heading') #its class_ to not clash with python code of "class"
# print(section_heading.getText())

# h3_heading = soup.find_all('h3', class_='heading')
# print(h3_heading)

# 'p a' in the line below stands for the tags that it holds. In this case its seaching for the first item in a <p> and then an <a> tag (Paragraph and link tag)
# company_url = soup.select_one(selector='body p a') #looking for an a tag that sits inside a p tag
# print(company_url)

#Select by ID
# name = soup.select_one(selector='#name')
# print(name)

#Select By Class
# headings = soup.select('.heading')
# print(headings)