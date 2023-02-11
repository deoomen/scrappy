from tools.ScrapMe import ScrapMe

class FakePythonJobs(ScrapMe):

    def scrap(self) -> None:
        soup = self._loadPage('https://realpython.github.io/fake-jobs/')

        jobItems = soup.find(id="ResultsContainer").find_all("div", class_="card-content")

        for index, jobItem in enumerate(jobItems):
            jobTitle = jobItem.find('h2', class_='title').text
            jobCompany = jobItem.find('h3', class_='company').text
            jobLocation = jobItem.find('p', class_='location').text
            jobDate = jobItem.find('time').text

            print('Job ', index)
            print('Title:', jobTitle)
            print('Company:', jobCompany)
            print('Location:', jobLocation)
            print('Date:', jobDate)
            print()

        # do some other things
