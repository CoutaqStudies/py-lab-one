def pre_process(a=0.97):
    def process(func):
        def wrapper(*args, **kwargs):
            return_value = func(*args, **kwargs)
            ret_list = list()
            for i in range(len(return_value)):
                if i==0: 
                    ret_list.append(return_value[i])
                else:
                    ret_list.append(return_value[i]-a*return_value[i-1])                
            return ret_list
        return wrapper
    return process

@pre_process(a=0.93)
def get_sample():
    return [1, 3, 4, 2]
print(get_sample())