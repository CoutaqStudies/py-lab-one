def get_proper_url(url):
    if url.startswith('www'):
        url = f"http://{url}"
        if not url.endswith(".com"):
            url = f"{url}.com"
    return url

urls = ["fdhfj.com", "www.test.com", "www.testtwo"]

proper_urls = [get_proper_url(url) for url in urls]

print(proper_urls)
        