def search(searchword):
    import requests
    from bs4 import BeautifulSoup
    website=requests.get(f"https://www.imdb.com/search/keyword/?keywords={searchword}").text
    x=BeautifulSoup(website,'lxml')
    titles=x.find_all('div',class_="lister-item-content")

    for title in titles:
        print(title.find('span').text,title.find('a').text," ",title.find('span',class_="lister-item-year text-muted unbold").text+'\n')

