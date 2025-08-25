import sys

def error_message(error, error_detail: sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    return f"\nError occured file is {filename}\nThe line that the error occured is {exc_tb.tb_lineno}\nThe error is ---> {str(error)}\n"

class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error_message=error_message(error, error_detail)

    def __str__(self):
        return self.error_message