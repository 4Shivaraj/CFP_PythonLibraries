'''
    @Author: Shivaraj
    @Date: 13-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 13-10-2022
    @Title: Write a Python program to append a new row 'k' to data frame with given values for
            each column. Now delete the new row and return the original DataFrame.
            exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
            'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
            labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
            Values for each column will be:
            name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"

'''
import sys

from data_log import get_logger

import numpy as np
import pandas as pd

lg = get_logger(name="(program_17)", file_name="data_log.log")


class PandasDataManipulation:

    def append_delete_new_record(self, exam_data, labels):
        """
        Description:
            This function is used to append and delete a new row to the data frame
        Parameter:
            exam_data and labels: The exam_data and labels to be checked
        Return:
            Returns None
        """
        try:
            data_frame = pd.DataFrame(exam_data, index=labels)
            lg.info(f'Original dataframe: \n{data_frame}')
            data_frame.loc['k'] = [1, 'Suresh', 'yes', 15.5]
            lg.info(f'after appending new record to dataframe: \n{data_frame}')
            data_frame = data_frame.drop('k')
            lg.info(
                f" after deleting the newly added record from dataframe: \n{data_frame}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
                          'Matthew', 'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    pd_obj = PandasDataManipulation()
    pd_obj.append_delete_new_record(exam_data, labels)
