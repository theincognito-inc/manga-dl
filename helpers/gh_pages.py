from src.providers import providers_list
from src.fs import get_current_path
from src.meta import __repo_name__
from json import dumps

start_items = [
    ['http://bato.to', 0, ' - Batoto will be closing down permanently (Jan 18, 2018)'],
    ['http://bulumanga.com', 0, ' - Closed'],
    ['http://bwahahacomics.ru', 0, ' - Very little content. Possibly, will be done in the future.'],
    ['http://com-x.life', 1, ' - One thread only!!! --no-multi-threads. <i class="v0"></i>'],
    ['http://comic-walker.com', 0, ' - Maybe...'],
    ['http://comico.jp', 1, ' - only public downloading now'],
    ['http://comixology.com', 0, ' - Buy only. Not reading.'],
    ['http://e-hentai.org', 1, '<i class="td"></i>'],
    ['http://eatmanga.me', 1, '<i class="v0"></i>'],
    ['http://gogomanga.co', 1, '<i class="v0"></i>'],
    ['http://hentai-chan.me', 1, '- Need fill access file'],
    ['http://heymanga.me', 1, '<i class="v0"></i>'],
    ['http://comic.k-manga.jp', 0, ' - Maybe...'],
    ['http://luscious.net', 1, '<i class="td"></i>'],
    ['http://lezhin.com', 0, ' - Maybe...'],
    ['http://mangaforall.com', 1, ''],
    ['http://mangafreak.net', 1, '<i class="v0"></i>, site down now'],
    ['http://mangahead.me', 1, '<i class="v0"></i>, site down now'],
    ['http://mangaleader.com', 1, '<i class="v0"></i> site down now'],
    ['http://mangamove.com', 1, '<i class="v0"></i>, site down now'],
    ['http://manganel.com', 1, '<i class="v0"></i>, site down now'],
    ['http://mangaroot.com', 1, '<i class="v0"></i>, site down now, one thread only!!! --no-multi-threads'],
    ['http://mangaz.com', 0, ' - Maybe...'],
    ['http://mg-zip.com', 0, ' - Will not be implemented'],
    ['http://rawdevart.com', 1, '<i class="v0"></i>, very little content'],
    ['http://s-manga.net', 0, ' - Maybe'],
    ['http://tapas.io', 1, '<i class="v0"></i>, only public downloading now'],
    ['http://zip.raw.im', 0, ' - Will not be implemented'],
]


_start_items = [i[0] for i in start_items]


def merge(*providers):
    for p in providers:
        yield from providers_list[p]


def clean(providers):
    _list = {}
    for i in providers:
        _ = i[:i.find('/')].strip('()')
        _list['http://' + _.replace(r'\.', '.')] = ''
    return list(_list.keys())


def aggregate(providers):
    _list = []
    for i in providers:
        if i not in _start_items:
            _list.append([i, 1, ''])
    return _list


def prepare_html(html):
    with open(html, 'r') as r:
        content = r.read()
    with open(html, 'w') as w:
        w.write(content.replace('__repo_name__', __repo_name__))


def build_providers():
    items = aggregate(clean(merge(*providers_list))) + start_items
    items = sorted(items, key=lambda l: l[0])
    return dumps(items)


def main():
    path = get_current_path() + '/helpers/gh_pages_content/'
    with open(path + 'providers.json', 'w') as w:
        w.write(build_providers())
    prepare_html(path + 'index.html')
    prepare_html(path + 'improvement.html')


# print(len(build_providers()))

