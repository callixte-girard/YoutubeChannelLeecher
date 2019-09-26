from my_py import disp

def reassembleUrl(url_prefix, url_partial):    ### must reassemble url first
    print("url before:", url_partial)
    url_full = url_prefix + url_partial
    print("url after:", url_full)
    print(disp.star)
    return url_full