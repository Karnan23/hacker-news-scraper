import requests
from bs4 import BeautifulSoup

pages=int(input("Enter the number of pages to scrape: "))
def get_hacker_news():
    for i in range(1, pages+1):
        res=requests.get(f'https://news.ycombinator.com/?p={i}')
        if res.status_code == 200:
            yield res

def custom_hn(links, votes):
    hn_list = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = int(votes[idx].getText().replace(' points','')) if idx < len(votes) else 0
        hn_list.append({'title': title, 'link': href, 'votes': vote})
    return hn_list

def get_needed_content(res):
    soup=BeautifulSoup(res.text,'html.parser')
    links=soup.select('span.titleline')
    votes=soup.select('.score')
    custom_hn_list = custom_hn(links, votes)
    return custom_hn_list


def test_outputs(votes,links):#for beginer clarity to understand the flow using the output of links and votes
    for idx, item in enumerate(votes):
        print(f"--- Element {idx} ---")
        print(item.prettify())  # shows clean, readable HTML
        print()

    for idx, item in enumerate(links):
        print(f"--- Element {idx} ---")
        print(item.prettify())  # shows clean, readable HTML
        print()

#test_outputs(votes, links)



#print(custom_hn_list)

def sort_by_votes(custom_hn_list):
    return sorted(custom_hn_list, key=lambda k:k['votes'], reverse=True)


if __name__ == "__main__":
    gen=get_hacker_news()
    for i in range(pages):
        res=next(gen)
        our_hn_list = get_needed_content(res)
        sorted_hn_list = sort_by_votes(our_hn_list)
        print(f"\033[4m Hacker_news (page : {i+1}) \033[0m :\n{sorted_hn_list}")
