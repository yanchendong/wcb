import requests,json
url = "https://api.openai.com/v1/completions"
headers = { 'content-type': 'application/json', 'Authorization': 'Bearer ' + "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"}
def res(msg):
    d = {'prompt': msg, 'max_tokens': 2048,"model": "text-davinci-003"}
    r = requests.post(url=url,headers=headers, json=d)
    try:
        return (json.loads(r.text)["choices"][0]["text"])
    except KeyError:
        return r.text

if __name__ == "__main__":
    print(res("你好"))