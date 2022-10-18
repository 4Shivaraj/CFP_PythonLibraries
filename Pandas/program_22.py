'''
    @Author: Shivaraj
    @Date: 13-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 13-10-2022
    @Title: Write a Python program to iterate over rows in a DataFrame
'''
import sys

from data_log import get_logger

import pandas as pd

lg = get_logger(name="(program_22)", file_name="data_log.log")


class PandasDataManipulation:

    def iterate_rows(self, exam_data):
        """
        Description:
            This function is used to iterate over rows in a DataFrame
        Parameter:
            exam_data: The exam_data to be checked
        Return:
            Returns None
        """
        try:
            data_frame = pd.DataFrame(exam_data)
            for index, row in data_frame.iterrows():
                lg.info(f" name and score: {row['name'], row['score']}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    exam_data = [{'name': 'Anastasia', 'score': 12.5}, {
        'name': 'Dima', 'score': 9}, {'name': 'Katherine', 'score': 16.5}]
    pd_obj = PandasDataManipulation()
    pd_obj.iterate_rows(exam_data)
