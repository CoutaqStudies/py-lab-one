def non_empty(func):
    def wrapper(*args, **kwargs):
        return list(filter(None, func(*args, **kwargs)))
    return wrapper


@non_empty
def get_pages():
    return ['ch1', '', 'cont', '', 'l1']
    
print(get_pages())