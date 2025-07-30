# 🔎 Hacker News Scraper

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Last Commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/YOUR_REPO_NAME)

A Python-based web scraper to extract and sort top stories from [Hacker News](https://news.ycombinator.com) using `requests` and `BeautifulSoup`.

---

## 🚀 Features

- Scrapes multiple pages of Hacker News posts.
- Extracts story titles, links, and vote counts.
- Sorts stories based on vote count (descending).
- Beginner-friendly structure with helpful debug tools.

---

## 📂 Project Structure

```
hacker_news_scraper/
│
├── scraper.py          # Main script to run the scraper
└── README.md           # You're here!
```

---

## 🧠 Tech Stack

- Python 3.x
- `requests` – for making HTTP requests.
- `BeautifulSoup` (from `bs4`) – for parsing HTML content.

---

## 📌 How It Works

1. Takes user input for how many pages to scrape.
2. Requests and parses each page of Hacker News.
3. Extracts story titles, links, and votes.
4. Sorts the extracted data based on votes.
5. Displays sorted results per page.

---

## 🛠️ Usage

### ✅ Prerequisites

- Python 3 installed
- Install required libraries:

```bash
pip install requests beautifulsoup4
```

### ▶️ Run the script

```bash
python scraper.py
```

Then input the number of pages to scrape when prompted.

---

## 📊 Sample Output

```
Enter the number of pages to scrape: 1

Hacker_news (page : 1) :
[
 {'title': 'Project X: AI system beats humans', 'link': 'https://...', 'votes': 342},
 {'title': 'How I built a game in 2 days', 'link': 'https://...', 'votes': 231},
 ...
]
```

---

## 📚 Code Breakdown

### 🔁 `get_hacker_news()`
Generates HTTP responses for each Hacker News page.

### 🧹 `get_needed_content(res)`
Parses and extracts title, link, and vote elements from a page response.

### 📊 `custom_hn(links, votes)`
Converts extracted elements into a list of dictionaries containing title, link, and vote count.

### 🔽 `sort_by_votes(custom_hn_list)`
Sorts the news items by their vote count in descending order.

### 🧪 `test_outputs(votes, links)`
[Optional] Debug function to print out HTML of raw elements.

---

## 🧠 Why This Project?

- Great for learning web scraping and Python data manipulation.
- Practical introduction to HTML parsing with `BeautifulSoup`.
- Sharpens beginner’s understanding of HTTP requests and response parsing.

---

## 👨‍💻 Author

**Karnan G (Karna)**  
_Aspiring Python Developer | AI Enthusiast | Real-World Coder_

---

## 📜 License

This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).
