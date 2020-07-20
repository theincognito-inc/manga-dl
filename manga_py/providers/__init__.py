import re
import importlib

providers_list = {
    '1stkissmanga_com': [
        r'1stkissmanga\.com/manga/.',
    ],
    '_3asq_org': [
        r'3asq\.org/.',
    ],
    '7sama_com': [
        r'7sama\.com/manga/.',
    ],
    'ac_qq_com': [
        r'ac\.qq\.com/Comic.+?/id/\d',
    ],
    'acomics_ru': [
        r'acomics\.ru/~.',
    ],
    'adulto_seinagi_org': [
        # r'adulto\.seinagi\.org/(series|read)/.',
        r'xanime-seduccion\.com/(series|read)/.',
        # r'twistedhelscans\.com/(series|read)/.',
        r'reader\.evilflowers\.com/(series|read)/.',
    ],
    'allhentai_ru': [
        r'allhentai\.ru/.',
    ],
    'animextremist_com': [
        r'animextremist\.com/mangas-online/.',
    ],
    'antisensescans_com': [
        r'antisensescans\.com/online/(series|read)/.',
    ],
    'asmhentai_com': [
        r'asmhentai\.com/(g|gallery)/\d',
    ],
    'atfbooru_ninja': [
        r'atfbooru\.ninja/posts.',
    ],
    'bato_to': [
        r'bato\.to/(series|chapter)/\d',
    ],
    'blogtruyen_com': [
        r'blogtruyen\.com/.',
    ],
    'cdmnet_com_br': [
        r'cdmnet\.com\.br/titulos/.',
    ],
    'chochox_com': [
        r'chochox\.com/.',
    ],
    'comicextra_com': [
        r'comicextra\.com/.',
    ],
    'comic_webnewtype_com': [
        r'comic\.webnewtype\.com/contents/.',
    ],
    'comico_jp': [
        r'comico\.jp/(?:challenge/)?(detail|articleList).+titleNo.',
    ],
    'comicvn_net': [
        r'comicvn\.net/truyen-tranh-online/.',
    ],
    'cycomi_com': [
        r'cycomi\.com/fw/cycomibrowser/chapter/title/\d',
    ],
    'danbooru_donmai_us': [
        r'danbooru\.donmai\.us/posts.',
    ],
    'darkskyprojects_org': [
        r'darkskyprojects\.org/biblioteca/.',
    ],
    'dejameprobar_es': [
        r'menudo-fansub\.com/slide/.',
        r'yuri-ism\.net/slide/.',
    ],
    'desu_me': [
        r'desu\.me/manga/.',
    ],
    'doujins_com': [
        r'doujins\.com/gallery/.',
        r'doujin-moe\.us/gallery/.',
    ],
    'e_hentai_org': [
        r'e-hentai\.org/g/\d',
    ],
    'fanfox_net': [
        r'fanfox\.net/manga/.',
    ],
    'funmanga_com': [
        r'funmanga\.com/.',
    ],
    'gmanga_me': [
        r'gmanga\.me/mangas/.',
    ],
    'gomanga_co': [
        r'kobato\.hologfx\.com/reader/.',
    ],
    'helveticascans_com': [
        r'helveticascans\.com/r/(series|read)/.',
    ],
    'hatigarmscans_eu': [
        r'hatigarmscans\.net/hs/(series|read).',
        r'hatigarmscans\.net/manga/.',
    ],
    'heavenmanga_biz': [
        r'heavenmanga\.com/.',
    ],
    'hentai2read_com': [
        r'hentai2read\.com/.',
    ],
    'hentai_cafe': [
        r'hentai\.cafe/.',
    ],
    'hentai_chan_me': [
        r'hentai-chan\.me/(related|manga|online)/.',  # todo
    ],
    'hentai_image_com': [
        r'hentai-image\.com/image/.',
    ],
    'hentaihand_com': [
        r'hentaihand\.com/comic/\d',
    ],
    'hentaifox_com': [
        r'hentaifox\.com/.',
    ],
    'hentaihere_com': [
        r'hentaihere\.com/m/.',
    ],
    'hentaiporns_net': [
        r'hentaiporns\.net/.'
    ],
    'hentairead_com': [
        r'hentairead\.com/.',
    ],
    'hitomi_la': [
        r'hitomi\.la/(galleries|reader)/.',
    ],
    'hgamecg_com': [
        r'hgamecg\.com/index/category/\d',
    ],
    'hiperdex_com': [
        r'hiperdex\.com/manga/.',
    ],
    'hitmanga_eu': [
        r'mymanga\.io/.',
    ],
    'hocvientruyentranh_com': [
        r'hocvientruyentranh\.com/(manga|chapter)/.',
    ],
    'hotchocolatescans_com': [
        # r'mangaichiscans\.mokkori\.fr/fs/(series|read)/.',
        r'taptaptaptaptap\.net/fs/(series|read)/.',
    ],
    # 'riceballicious_info': [
    #     r'riceballicious\.info/fs/reader/(series|read)/.',
    # ],
    'rocaca_com': [
        r'rocaca\.com/manga/.',
    ],
    'inmanga_com': [
        r'inmanga\.com/ver/manga/.',
    ],
    'isekaiscan_com': [
        r'isekaiscan\.com/manga/.',
    ],
    'jaiminisbox_com': [
        r'jaiminisbox\.com/reader/series/.',
    ],
    'japscan_com': [
        r'japscan\.(cc|com|co|to)/.',
    ],
    'jurnalu_ru': [
        r'jurnalu\.ru/online-reading/.',
    ],
    'kissmanga_com': [
        r'kissmanga\.com/Manga/.',
    ],
    'komikcast_com': [
        r'komikcast\.com/.',
    ],
    'komikid_com': [
        r'komikid\.com/manga/.',
        r'mangazuki\.co/manga/.',
        r'mangadoor\.com/manga/.',
        r'cmreader\.info/manga/.',
        r'rawmangaupdate\.com/manga/.',
        r'manga-v2\.mangavadisi\.org/manga/.',
        r'universoyuri\.com/manga/.',
        r'digitalteam1\.altervista\.org/manga/.',
        r'komikgue\.com/manga/.',
        r'onma\.me/manga/.',
    ],
    'kumanga_com': [
        r'kumanga\.com/manga/\d',
    ],
    # 'lector_kirishimafansub_com': [
    #     r'lector\.kirishimafansub\.com/(lector/)?(series|read)/.',
    # ],
    'leitor_net': [
        r'leitor\.net/manga/.',
    ],
    'leviatanscans_com': [
        r'leviatanscans\.com/comics/\d'
    ],
    'lhtranslation_com': [
        r'read\.lhtranslation\.com/(truyen|manga)-.',
        r'lhtranslation\.net/(truyen|manga)-.',
    ],
    'lolibooru_moe': [
        r'lolibooru\.moe/post.',
    ],
    'lolivault_net': [
        r'lolivault\.net/online/(series|read).',
    ],
    'luscious_net': [
        r'luscious\.net/.+/album/.',
        r'luscious\.net/albums/.',
    ],
    'manga41_com': [
        r'manga41\.com/manga/.',
    ],
    'manga_ae': [
        r'mangaae\.com/.',
    ],
    'manga_mexat_com': [
        r'manga\.mexat\.com/category/.',
    ],
    'manga_online_biz': [
        r'manga-online\.biz/.',
    ],
    'manga_tube_me': [
        r'manga-tube\.me/series/.',
    ],
    'mangaarabteam_com': [
        r'mangaarabteam\.com/.',
    ],
    'manga_tr_com': [
        r'manga-tr\.com/(manga|id)-.',
    ],
    'mangabat_com': [
        r'mangabat\.com/(manga|chapter)/.',
        r'mangabat\.com/read-.',
    ],
    # 'mangabb_co': [  removed #306
    #     r'mangabb\.co/.',
    # ],
    'mangabox_me': [
        r'mangabox\.me/reader/.',
    ],
    'mangacanblog_com': [
        r'mangacanblog\.com/.',
    ],
    'mangaclub_ru': [
        r'mangaclub\.ru/.',
    ],
    'mangadeep_com': [
        r'mangadeep\.com/.',
        r'manga99\.com/.',
    ],
    'mangadex_org': [
        r'mangadex\.org/(manga|title)/.',
    ],
    'mangaeden_com': [
        r'mangaeden\.com/[^/]+/[^/]+-manga/.',
        r'perveden\.com/[^/]+/[^/]+-manga/.',
    ],
    'mangafreak_net_download': [
        r'mangafreak\.net/Manga/.',
    ],
    # 'mangafull_org': [
    #     r'mangafull\.org/manga/.',
    # ],
    # 'mangaheaven_club': [
    #     r'mangaheaven\.club/read-manga/.',
    # ],
    # 'mangaheaven_xyz': [
    #     r'mangaheaven\.xyz/manga/.',
    # ],
    'mangahere_cc': [
        r'mangahere\.cc/manga/.',
    ],
    'mangaid_me': [
        # r'mangaid\.co/manga/.',
        # r'mangaid\.net/manga/.',
        # r'mangaid\.me/manga/.',
        r'bacamanga\.co/manga/.',
    ],
    'mangahome_com': [
        r'mangahome\.com/manga/.',
    ],
    'mangahub_io': [
        r'mangahub\.io/(manga|chapter)/.',
        r'mangakakalot\.fun/(manga|chapter)/.',
        r'mangahere\.onl/(manga|chapter)/.',
    ],
    'mangahub_ru': [
        r'mangahub\.ru/.',
    ],
    'mangaindo_web_id': [
        r'mangaindo\.web\.id/.',
    ],
    'mangainn_net': [
        r'mangainn\.net/.',
    ],
    'mangakakalot_com': [
        r'mangakakalot\.com/manga/.',
        r'mangakakalot\.com/read-.',
    ],
    'mangakatana_com': [
        r'mangakatana\.com/manga/.',
    ],
    'mangakomi_com': [
        r'mangakomi\.com/manga/.',
    ],
    'mangaku_web_id': [
        r'mangaku\.in/.',
    ],
    'mangalib_me': [
        r'mangalib\.me/.',
    ],
    'mangalife_us': [
        r'mangalife\.us/(read-online|manga)/.',
        r'manga4life\.com/(read-online|manga)/.',
    ],
    'mangamew_com': [
        r'mangamew\.com/(\w+-)?manga/.',
    ],
    'mangamew_com_vn': [
        r'mangamew\.com/(\w+-)?truyen/.',
    ],
    'manganelo_com': [
        r'manganelo\.com/(manga|chapter)/.',
    ],
    'manganelos_com': [
        r'manganelos\.com/manga/.',
    ],
    'mangaonline_com_br': [
        r'mangaonline\.com\.br/.',
    ],
    # 'mangaonlinehere_com': [
    #     r'mangaonlinehere\.com/(manga-info|read-online)/.',
    # ],
    'mangapanda_com': [
        r'mangapanda\.com/.',
    ],
    'mangapark_me': [
        r'mangapark\.net/manga/.',
    ],
    'mangareader_net': [
        r'mangareader\.net/.',
    ],
    'mangareader_site': [
        r'mangareader\.site',
    ],
    # 'mangareader_xyz': [
    #     r'mangareader\.xyz/manga/.',
    #     r'mangareader\.xyz/.+?/chapter-\d',
    # ],
    'mangarussia_com': [
        r'mangarussia\.com/(manga|chapter)/.',
    ],
    # 'mangasaurus_com': [
    #     r'mangasaurus\.com/(manga|view).',
    # ],
    'mangaseeonline_us': [
        r'mangaseeonline\.us/(read-online|manga)/.',
    ],
    'mangashiro_net': [
        r'mangashiro\.net/.',
    ],
    # 'mangasupa_com': [
    #     r'mangasupa\.com/(manga|chapter)/.',
    # ],
    'mangasushi_net': [
        r'mangasushi\.net/manga/.',
    ],
    'mangatail_com': [
        r'mangatail\.me/(manga|chapter|node|content)/.',
    ],
    'mangatown_com': [
        r'mangatown\.com/manga/.',
    ],
    # 'mangatrue_com': [
    #     r'mangatrue\.com/manga/.',
    #     r'mangaall\.com/manga/.',
    # ],
    'mangawindow_net': [
        r'mangawindow\.net/(series|chapter)/\d',  # is different!
    ],
    # 'mangax_net': [
    #     r'mangax\.net/\w/.',
    # ],
    'mangazuki_me': [
        r'mangazuki\.me/manga/.',
        r'mangazuki\.online/mangas/.',
    ],
    'manhuagui_com': [
        r'manhuagui\.com/comic/\d',
    ],
    'manhuatai_com': [
        r'manhuatai\.com/.',
    ],
    'manhwa18_net': [
        r'manhwa18\.net/manga-.',
    ],
    'manhwa_club': [
        r'manhwa\.club/manhwa/.',
    ],
    'manhwareader_com': [
        r'manhwareader\.com/manga/.',
    ],
    'merakiscans_com': [
        r'merakiscans\.com/manga/.',
    ],
    # 'mngcow_co': [
    #     r'mngcow\.co/.',
    # ],
    # 'mngdoom_com': [
    #     r'mangadoom\.co/.',
    #     r'mngdoom\.com/.',
    # ],
    'mymangalist_org': [
        r'mymangalist.org/(read|chapter)-',
    ],
    'myreadingmanga_info': [
        r'myreadingmanga\.info/.',
    ],
    'neumanga_tv': [
        r'neumanga\.tv/manga/.',
    ],
    'nhentai_net': [
        r'nhentai\.net/g/.',
    ],
    'niadd_com': [
        r'niadd\.com/manga/.',
    ],
    'nightow_net': [
        r'nightow\.net/online/\?manga=.',
    ],
    'nineanime_com': [
        r'nineanime\.com/manga/.+\.html'
    ],
    'ninemanga_com': [
        r'ninemanga\.com/(manga|chapter).',
        r'addfunny\.com/(manga|chapter).',
    ],
    'noranofansub_com': [
        r'noranofansub\.com(/lector)?/(series/|read/)?.',
    ],
    'nozominofansub_com': [  # mangazuki_co
        r'godsrealmscan\.com/public(/index\.php)?/manga/.',
    ],
    'otakusmash_com': [
        #r'otakusmash\.com/.',  removed #306
        # r'mrsmanga\.com/.',
        r'mentalmanga\.com/.'
        r'omgbeaupeep\.com/comics/.',
    ],
    'otscans_com': [
        r'otscans\.com/foolslide/(series|read)/.',
    ],
    # 'pecintakomik_com_manga': [
    #     r'pecintakomik\.com/manga/.',
    # ],
    # 'pecintakomik_com': [
    #     r'pecintakomik\.com/.',
    # ],
    'plus_comico_jp_manga': [
        r'plus\.comico\.jp/manga/\d',
    ],
    'plus_comico_jp': [
        r'plus\.comico\.jp/store/\d',
    ],
    'porncomix_info': [
        r'porncomix\.info/.',
    ],
    # 'psychoplay_co': [
    #     r'psychoplay\.co/(series|read)/.',
    # ],
    'puzzmos_com': [
        r'puzzmos\.com/manga/.',
    ],
    r'pururin_io': [
        r'pururin\.io/(gallery|read)/.',
    ],
    'pzykosis666hfansub_com': [
        r'pzykosis666hfansub\.com/online/.',
    ],
    'ravens_scans_com': [
        r'ravens-scans\.com(/lector)?/(serie/|read/).',
    ],
    'raw_senmanga_com': [
        r'raw\.senmanga\.com/.',
    ],
    'rawdevart_com': [
        r'rawdevart\.com/manga/.',
    ],
    'rawlh_com': [
        r'lhscan\.net/(truyen|manga|read)-.',
        # r'rawqq\.com/(truyen|manga|read)-.',
        r'kisslove\.net/(truyen|manga|read)-.',  # r'rawqv\.com/(truyen|manga|read)-.',
        r'loveheaven\.net/(truyen|manga|read)-.',
    ],
    # 'rawneko_com': [
    #     r'rawneko\.com/manga/.',
    # ],
    'read_egscans_com': [
        r'read\.egscans\.com/.',
    ],
    'read_powermanga_org': [
        r'read\.powermanga\.org/(series|read)/.',
        r'reader\.kireicake\.com/(series|read)/.',
        r'slide\.world-three\.org/(series|read)/.',
        r'reader\.thecatscans\.com/(series|read)/.',
        r'reader\.deathtollscans\.net/(series|read)/.',
        r'reader\.jokerfansub\.com/(series|read)/.',
        r'lector\.patyscans\.com/(series|read)/.',
        r'truecolorsscans\.miocio\.org/(series|read)/.',
        r'reader\.letitgo\.scans\.today/(series|read)/.',
        r'reader\.fos-scans\.com/(series|read)/.',
        r'reader\.serenade\.moe/(series|read)/.',
        r'reader\.vortex-scans\.com/(series|read)/.',
        r'reader\.silentsky-scans\.net/(series|read)/.',
        r'reader\.manga-download\.org/(series|read)/.',
    ],
    'read_ptscans_com': [
        r'read\.ptscans\.com/series/.'
    ],
    'read_yagami_me': [
        r'read\.yagami\.me/series/\w',
    ],
    'comicpunch_net_manga': [
        r'comicpunch\.net/asiancomics/.',
    ],
    'comicpunch_net': [
        r'comicpunch\.net/.',
    ],
    # 'reader_championscans_com': [
    #     r'reader\.championscans\.com/(series|read)/.',
    # ],
    'readcomiconline_to': [
        r'readcomiconline\.to/Comic/.',
    ],
    'readcomicsonline_ru': [
        r'readcomicsonline\.ru/comic/.',
    ],
    'readmanga_me': [
        r'readmanga\.me/.',
        r'mintmanga\.com/.',
        r'selfmanga\.ru/.',
    ],
    'readmng_com': [
        r'readmng\.com/.',
    ],
    # 'readms_net': [
    #     r'readms\.net/(r|manga)/.',
    # ],
    # todo #266
    'remanga_org': [
        r'remanga\.org/manga/.',
    ],
    'santosfansub_com': [
        r'santosfansub\.com/Slide/.',
    ],
    'senmanga_com': [
        r'senmanga\.com/.',
    ],
    'shakai_ru': [
        r'shakai\.ru/manga.*?/\d',
    ],
    'shogakukan_co_jp': [
        r'shogakukan\.co\.jp/books/\d',
        r'shogakukan\.co\.jp/magazines/series/\d',
    ],
    # 'shogakukan_tameshiyo_me': [
    #     r'shogakukan\.tameshiyo\.me/\d',
    # ],
    'siberowl_com': [
        r'siberowl\.com/mangas/.',
    ],
    'sleepypandascans_co': [
        r'sleepypandascans\.co/(Series|Reader)/.',
    ],
    'subapics_com': [
        r'mangakita\.net/manga/.',
        r'mangakita\.net/.+-chapter-.',
        r'komikstation\.com/manga/.',
        r'komikstation\.com/.+-chapter-.',
        r'mangavy\.com/manga/.',
        r'mangavy\.com/.+-chapter-.',
    ],
    'submanga_online': [
        r'submanga\.online/manga/.',
    ],
    'sunday_webry_com': [
        r'sunday-webry\.com/series/\d',
    ],
    'taadd_com': [
        r'taadd\.com/(book|chapter)/.',
    ],
    'tenmanga_com': [
        r'tenmanga\.com/(book|chapter)/.',
    ],
    'translate_webtoons_com': [
        r'translate\.webtoons\.com/webtoonVersion\?webtoonNo.',
    ],
    'tonarinoyj_jp': [
        r'tonarinoyj\.jp/episode/.',
    ],
    'triplesevenscans_com': [
        r'sensescans\.com/reader/(series|read)/.',
        # r'triplesevenscans\.com/reader/(series|read)/.',
    ],
    'truyen_vnsharing_site': [
        r'truyen\.vnsharing\.site/index/read/.',
    ],
    'truyenchon_com': [
        r'truyenchon\.com/truyen/.',
        r'nettruyen\.com/truyen-tranh/.',
    ],
    'truyentranhtuan_com': [
        r'truyentranhtuan\.com/.',
    ],
    'tsumino_com': [
        r'tsumino\.com/Book/Info/\d',
        r'tsumino\.com/Read/View/\d',
    ],
    'viz_com': [
        r'viz\.com/shonenjump/chapters/.',
    ],
    'web_ace_jp': [
        r'web-ace\.jp/youngaceup/contents/\d',
    ],
    'webtoons_com': [
        r'webtoons\.com/[^/]+/[^/]+/.',
    ],
    'westmanga_info': [
        r'westmanga\.info/.',
    ],
    'whitecloudpavilion_com': [
        r'whitecloudpavilion\.com/manga/free/manga/.',
    ],
    'wiemanga_com': [
        r'wiemanga\.com/(manga|chapter)/.',
    ],
    'wmanga_ru': [
        r'wmanga\.ru/starter/manga_.',
    ],
    'yande_re': [
        r'yande\.re/post.',
    ],
    'zeroscans_com': [
        r'zeroscans\.com/comics/.',
        r'reaperscans\.com/comics/.',
    ],
}


def __check_provider(provider, url):
    items = [r'\b' + i for i in provider]
    reg = '(?:' + '|'.join(items) + ')'
    return re.search(reg, url)


def get_provider(url):
    fromlist = 'manga_py.providers'
    for i in providers_list:
        if __check_provider(providers_list[i], url):
            provider = importlib.import_module('%s.%s' % (fromlist, i))
            return provider.main
    return False
