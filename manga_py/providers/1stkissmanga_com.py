from .rawdevart_com import RawDevArtCom


class FirstKissMangaCom(RawDevArtCom):
    _chapter_selector = r'/manga/[^/]+/chapter-(\d+(?:-\d+)?)'

    def get_files(self):
        parser = self.html_fromstring(self.chapter)
        cls = '.page-break img[data-src],.page-break img[src]'
        return self._images_helper(parser, cls, attr='data-src', alternative_attr='src')


main = FirstKissMangaCom
