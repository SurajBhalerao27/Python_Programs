# status = int(input("please enter a status code: "))
status = 400
def http_status(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not Found"
        case 418:
            return "I am a teapot"
        case _:
            return "Something is going wrong!"