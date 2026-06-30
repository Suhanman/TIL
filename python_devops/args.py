def example_function(*args, **kwargs):
    print(f"Postional args: {args}" )
    print(f"Keyword args: {kwargs}" )
    
example_function(1,2,3, a ="Value", b = True)

def apply_operator(operator, *operands):
    
    if operator == 'add' :
        result = sum(operands)
    elif operator == 'mul':
        result = 1
        for n in operands:
            result == n
            
    else:
        raise ValueError(f"Unkonwn operator {operator}. ")
    
    return result

print(apply_operator('add', 1,2,3,4))

def set_options(**settings):
    print(f"Recived dictionary: {settings}")
    for key, value in settings.items():
        print(f"\t{key} = {value}")
        
    set_options(timeout = 30, user ="admin", retires =5 )
    
    return settings

def process_request(url, method = "GET", *headers, timeout, **params):
    print(f"url={url}, method={method}")
    print(f"headers={headers}")
    print(f"params={params}")
    
process_request("https://www.example.com",timeout=30, method = "PUT")
process_request(
    "https://www.example.com",
    "PUT",
    "Auth:xyz",
    "Content=Type: application/json",
    timeout=30, 
    retires =30,
    log_level="DEBUG")


def connect(host,port,timeout):
    print(f"Connecting to {host}:{port} with timeout {timeout}s.")
    
    
params =["db.internal", 5432, 10]
params_extra =["db.internal", 5432, 10,"a",True]
connect(*params_extra[:3])

def configure_service(name, version, replicas =1):
    print(f"Setting up {name} v{version} with {replicas} replicas...")

config = {"name" : "auth=service", "version" : "2.1.0", "replicas": 3}
configure_service(**config)