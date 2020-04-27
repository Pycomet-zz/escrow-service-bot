class APIException(Exception):
    def __init__(self, message, code):
        Exception.__init__(self, message)
        self.code = code
