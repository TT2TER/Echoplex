def _init():
    global _global_dict
    _global_dict = {
        'client_address': '127.0.0.1',
        'client_port': 13579,
        'server_address': '127.0.0.1',
        'server_port': 13578
    }
 
def set_value(name, value):
    _global_dict[name] = value
 
def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue