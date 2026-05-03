def login(username, password):
    # simple hardcoded credentials
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Credentials"


# test the function
print(login("admin", "1234"))