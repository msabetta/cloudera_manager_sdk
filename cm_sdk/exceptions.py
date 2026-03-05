class APIError(Exception):

    def __init__(self, status, message):
        super().__init__(f"API Error {status}: {message}")
        self.status = status
        self.message = message