'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to create multiple types of charts
'''
import datetime as DT
import matplotlib.pyplot as plt
import sys
from matplotlib.dates import date2num

from data_log import get_logger

lg = get_logger(name="(program_12)", file_name="data_log.log")


class DrawLine:
    """
    class to perform graphical representation of data using matplotlib
    """

    def create_multiple_charts(self):
        """
        Description:
             This function is used to create multiple types of charts
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            data = [(DT.datetime.strptime('2022-10-16', "%Y-%m-%d"), 772.559998),
                    (DT.datetime.strptime('2022-10-17', "%Y-%m-%d"), 776.429993),
                    (DT.datetime.strptime('2022-10-18', "%Y-%m-%d"), 776.469971),
                    (DT.datetime.strptime('2022-10-19', "%Y-%m-%d"), 776.859985),
                    (DT.datetime.strptime('2022-10-20', "%Y-%m-%d"), 775.080017)]

            # Convert datetime objects to Matplotlib dates.
            x = [date2num(date) for (date, value) in data]
            # [19281.0, 19282.0, 19283.0, 19284.0, 19285.0]

            y = [value for (date, value) in data]
            # [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]

            # creates object of figure class
            fig = plt.figure()

            graph = fig.add_subplot(1, 1, 1)

            # Plot the data as a red line with round markers
            graph.plot(x, y, 'r-o')

            # Set the xtick locations
            graph.set_xticks(x)

            # Set the xtick labels(date)
            graph.set_xticklabels(
                [date.strftime("%Y-%m-%d") for (date, value) in data]
            )
            # ['2022-10-16', '2022-10-17', '2022-10-18', '2022-10-19', '2022-10-20']

            # Set the x-axis label
            plt.xlabel('Date')

            # Set the y-axis label
            plt.ylabel('Closing Value')

            # Sets a title
            plt.title('Closing stock value of Alphabet Inc.')

            # shows the plot
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = DrawLine()
    np_obj.create_multiple_charts()
