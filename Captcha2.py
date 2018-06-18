import httplib, re, webbrowser

if __name__ =='__main__':
    conn = httplib.HTTPConnection('192.168.159.131')
    conn.request('GET','/captcha/example2/')
    res = conn.getresponse()
    abc = re.findall(r'<input type="hidden" name="answer" value="(.*)"/>', res.read())[0]
    print abc
#    url = "http://192.168.159.131/captcha/example2/submit?captcha="+abc+"&answer="+abc+"&submit=Submit+Query"
    url = "http://192.168.159.131/captcha/example2/submit?captcha=a&answer=a&submit=Submit+Query"
    webbrowser.open_new_tab(url)
