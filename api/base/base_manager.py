class BaseManager:
    def __init__(self):
        pass

    @staticmethod
    def _get_ok_result(result, message=None, status_code=200):
        return True, result, message, status_code

    @staticmethod
    def _get_error_result(result, message, status_code):
        return False, result, message, status_code
