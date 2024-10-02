import urllib.request
import urllib.parse

def python_get_url_source(url_string, params):
    url = url_string + urllib.parse.urlencode(params)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2'}
    request = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(request) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error occurred: {e}")
        raise RuntimeError(e)
