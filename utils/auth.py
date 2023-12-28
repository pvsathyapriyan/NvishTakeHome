def check_authentication(key):
    isValid = False
    if key == "ABC":  # secret goes here, can read it from env
        isValid = True
    return isValid
