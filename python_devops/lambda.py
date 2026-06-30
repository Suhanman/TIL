square = lambda x : x * x
print(square(5))

print((lambda a, b: a + b)(3,4))

services = [("web-app",3), ("database", 1), ("cache",5), ("api-gateway",2)]
print(f"Default sort: {sorted(services)}")

def get_replica_count(svc_tuple):
    return svc_tuple[1]
print(f"Sorting by replica count - standard function : {sorted(services, key=get_replica_count)}")
print(f"Sorting by replica count - lambda function : {sorted(services, key=lambda svc: svc[1])}")