from .provider import Provider


class Comico(Provider):  # pragma: no cover

    def get_archive_name(self) -> str:
        return 'vol_{:0>3}'.format(self._storage['current_chapter'])

    def get_chapter_index(self) -> str:
        return str(self._storage['current_chapter'])

    def get_main_content(self):  # call once
        title_no = self.re.search('\\.jp/.+titleNo=(\d+)', self.get_url())
        if title_no:
            content = self.http_post('{}/api/getArticleList.nhn'.format(self.get_domain()), data={
                'titleNo': title_no.group(1)
            })
            try:
                return self.json.loads(content)['result']['list']
            except TypeError:
                pass
        return []

    def get_manga_name(self):  # call once
        name = self.html_fromstring(self.get_url(), 'title', 0).text_content()
        return name[:name.rfind('|')].strip(' \n\t\r')

    def get_chapters(self):  # call once
        # TODO: see i['freeFlg'] Y = true, W = false #19
        items = [i['articleDetailUrl'] for i in self.get_main_content()]
        items.reverse()
        return items

    def prepare_cookies(self):  # if site with cookie protect
        pass

    def get_files(self):  # call ever volume loop
        items = self.html_fromstring(self.get_current_chapter(), '.comic-image._comicImage > img.comic-image__image')
        return [i.get('src') for i in items]

    def _loop_callback_chapters(self):
        pass

    def _loop_callback_files(self):
        pass


main = Comico