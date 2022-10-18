'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to create a null vector of size 10 and update sixth value to 11.
            [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            Update sixth value to 11
            [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_3)", file_name="data_log.log")


class NumericalPython:

    def null_vector_update(self):
        """
        Description:
             This function is used to create a null vector of size 10 and update sixth value to 11.
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            vector = np.zeros(10)
            lg.info(f"null vector before updating: \n{vector}")
            vector[6] = 11
            lg.info(f"null vector after updating '6th' value: \n{vector}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.null_vector_update()
