# sourcetemplate()

def sourcetemplate(url):
    def get_request(**kwargs):
        nonlocal url

        if len(kwargs) > 0:
            kwargs = dict(sorted(kwargs.items(), key=lambda item: item[0]))
            url += "?"
            for k, v in kwargs.items():
                if url[-1] == "?":
                    url += f"{k}={v}"
                else:
                    url += f"&{k}={v}"
        
        return url

    return get_request