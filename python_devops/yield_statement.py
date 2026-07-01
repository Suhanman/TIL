def filter_evens(data):
    print ("filter_evns: starting")
    
    for item in data:
        if item % 2 == 0:
            print(f"filter_evens: yielding {item}")
            yield item
        
    print("filter_evens: finished")
   
evens_from_range = filter_evens(range(6))
    
print(f"Generator object created : {evens_from_range}")
    
for num in evens_from_range:
        print(f"Received even: {num}")
        
evens_from_list = filter_evens([0,1,2,3,4,5])
    
for num in evens_from_list:
    print(f"Received even:{num}")
        
  

  