import urllib.request
import urllib.parse
import json

class Client:
    def _build_url(self, path):
        base = 'http://wiki.opensource.org/rest/wikis/xwiki/'
        url = base + "/".join(path)
        return url

    def _make_request(self, path, data):
        url = self._build_url(path)
        data['media'] = 'json'
        params = urllib.parse.urlencode(data)
        full_url = url + "?%s" % params
        response = urllib.request.urlopen(full_url)
        bcontent = response.read()
        content = bcontent.decode()
        return json.loads(content)

    def spaces(self):
        path = ['spaces']
        data = {}
        content = self._make_request(path, data)
        return content['spaces']

    def space_names(self):
        spaces = []
        result = self.spaces()
        for details in result: 
            spaces.append(details['name'])
        return spaces

    def pages(self, space):
        path = ['spaces', space, 'pages']
        data = {}
        content = self._make_request(path, data)
        return content['pageSummaries']

    def page_names(self, space):
        pages = []
        result = self.pages(space)
        for details in result: 
            pages.append(details['name'])
        return pages

    def page(self, space, page):
        path = ['spaces', space, 'pages', page]
        data = {}
        content = self._make_request(path, data)
        return content

    def tags(self):
        path = ['tags']
        data = {}
        content = self._make_request(path, data)
        return content['tags']

    def tag_names(self):
        tags = []
        result = self.tags()
        for details in result:
            tags.append(details['name'])
        return tags

    def pages_by_tags(self, tags):
        taglist = ",".join(tags)
        path = ['tags', taglist]
        data = {}
        content = self._make_request(path, data)
        return content['pageSummaries']
