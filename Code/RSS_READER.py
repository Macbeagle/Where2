class ReadFeed:
    def __init__(self, url. headings):
        self.url = url
        try:
            self.r = requests.get(url, headers=self.HEADERS)
            self.status_code = self.r.status_code
        except Exception as e:
            print("Error fetching: ", url)
            print(e)
        try:
            self.soup = BeautifulSoup(self.r.text, 'lxml')
        except Exception as e:
            print("Could not parse XML: ", self.url)
            print(e)