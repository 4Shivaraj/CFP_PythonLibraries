'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python programming to create a pie chart with a title of the popularity of programming
            Languages.
            Sample data:
            Programming languages: Java, Python, PHP, JavaScript, C#, C++
            Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
'''
import matplotlib.pyplot as plt
import sys

from data_log import get_logger

lg = get_logger(name="(program_2)", file_name="data_log.log")


class PieChart:
    """
    class to perform pie chart representation using matplotlib
    """

    def display_piechart(self):
        """
        Description:
             This function is used to create a pie chart with a title of the popularity of programming Languages
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            lang = ['java', 'Python', 'PHP', 'javaScript', 'C#', 'C++']
            popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

            # explode 1st slice
            explode = (0.1, 0, 0, 0, 0, 0)
            colors = ["#1f77b4", "#ff7f0e", "#2ca02c",
                      "#d62728", "#9467bd", "#5467bd"]
            # plot
            plt.pie(popularity, explode=explode, labels=lang, colors=colors,
                    autopct='%1.1f%%', shadow=True, startangle=140)
            plt.axis('equal')
            plt.title("Popularity of Programming Language\n" +
                      "Worldwide, Oct 2022 compared to a year ago", bbox={'facecolor': '0.8', 'pad': 5})
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = PieChart()
    np_obj.display_piechart()
