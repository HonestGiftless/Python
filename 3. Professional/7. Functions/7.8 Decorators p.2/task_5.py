# make_html
# Декоратор для превращения текста в HTML-теги

import functools

def make_html(tag: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f"<{tag}>" + func(*args, **kwargs) + f"</{tag}>"
        return wrapper
    return decorator

@make_html('del')
def get_text(text):
    return text
    
print(get_text('Python'))