import sys
import logging

def error_message_detail(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(exc_tb.tb_frame.f_code.co_filename,exc_tb.tb_lineno,str(error))
    return error_message
    


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)
        
    def __str__(self):
        return self.error_message
    
#  FIXED SPACING (Runs perfectly!)
#to check the exception class is working or not we can run the below code in the same file
#if __name__ == "__main__":
# try:
#    a = 1 / 0
#  except Exception as e:
#   raise CustomException(e, sys)
