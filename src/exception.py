import sys
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message='Error occured in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)  #“Call the constructor of the parent class (Exception) and pass the error message to it.”
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self): #This method controls what gets printed when you display the exception object.Instead of default message, it returns your formatted detailed message
        return self.error_message
    

#catches errors → extracts file + line → formats them → returns clean debug message