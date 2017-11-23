import urllib.request


class UrlHelper:

    # download and decode content from a specific url
    @staticmethod
    def retrieve_url(url):
        print("Fetching data ...")
        response = urllib.request.urlopen(url)
        data = response.read()
        return data.decode("UTF-8")
