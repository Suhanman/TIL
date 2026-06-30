square = lambda x : x * x
print(square(5))

print((lambda a, b: a + b)(3,4))

services = [("web-app",3), ("database", 1), ("cache",5), ("api-gateway",2)]
print(f"Default sort: {sorted(services)}")

def get_replica_count(svc_tuple):
    return svc_tuple[1]
print(f"Sorting by replica count - standard function : {sorted(services, key=get_replica_count)}")
print(f"Sorting by replica count - lambda function : {sorted(services, key=lambda svc: svc[1])}")


my_numbers = [1,2,3,4]
print(list(map(lambda num: num *2, my_numbers)))

ports = [80,443,8080,22]

port_descriptions = list(map(lambda port: f"Port {port} is open",ports))

print(port_descriptions)

ports = [80,443,8080,22,5432]

privileged_ports = list(filter(lambda port: port <1024, ports))
print(privileged_ports)

privileged_comprehension = [port for port in ports if port <1024]
print(privileged_comprehension)