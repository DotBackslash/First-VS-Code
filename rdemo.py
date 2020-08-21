import requests

"""
r = requests.get("https://xkcd.com/353/")

# prints the methods and attributes available to the 'r' response object
print(dir(r))

# for an even more detailed expaination you can use help(r)
print(help(r))

# You can print the raw HTML of the page
print(r.text)

# Accessing the image at the url as bytes and writing it to a file.
image = requests.get("https://imgs.xkcd.com/comics/python.png")

with open("Python xkcd image.png", "wb") as f:  # using 'wb' because we are writing bytes
    f.write(image.content)  # image.content returns the bytes

print(r.status_code) #Just checks the status of the url
"""


"""
###Using a site designed to play with the request library###

payload = {"page": 2, "count": 25}

r = requests.get(
    "https://httpbin.org/get", params=payload
)  # using .get() because we want to pull data from server

# print(r.text)

payload = {"username": "Corey", "password": "testing"}

r = requests.post(
    "https://httpbin.org/post", data=payload
)  # using .post() because we want to push data to server. ***Notice the change in function parameters***

print(r.text)  # Here we see that we get a json object as a response so we can also use the .json() method to return
r_dict = r.json() #This returns a dictionary from the json object.

#now you can use the the return object like a regular dictionary. 
print(r_dict['form']) #example: we want the value in the 'form' key
"""

####Playing with authentication###

#passing credentials to the basic-auth method of authentication using a tuple
#note the addition of a 'timeout' parameter, this is because request.get will wait indefinitely for a response
#even if the server hangs. Good idea if you dont want your script to run forever due to server errors.
r = requests.get("https://httpbin.org/basic-auth/corey/testing", auth=('corey', 'testing'), timeout=10)

print(r.text) #returns a successfull authentication if tuple matches the /username/password params in the url