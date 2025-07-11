import sys
import logging

def get_error_message_detail(error, error_detail: sys):
    """
    Returns detailed error message with file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in file [{filename}], line [{line_number}]: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = get_error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
