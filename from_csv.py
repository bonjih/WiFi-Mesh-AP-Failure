import pandas as pd
import csv


class BmaWifiDatafile:
    """
       Simple wrapper object to wrap up the data and meta data contained in the
       data files
    """
    # change this to the folder with your datafiles


    def __init__(self, dataFileName, data_path=""):
        """
        ctor
        :param dataFileName: path is known, just provide the specific data file i.e "101 - Xy.csv"
        """
        self.dataFileName = dataFileName # type: str
        self.meta_data = {} # type: dict
        self.data_path = data_path # type: str
        self.df = None # type:pandas.Dataframe

    def load_file(self):
        """
            first loads the meta data that these files have embedded at the top of the file
            then loads the dataframe of data contained within the file
        """
        df_start_row_offset = 0

        with open(self.data_path + self.dataFileName, "r") as fileHandle:
            csvReader = csv.reader(fileHandle, delimiter=',', quotechar='"')
            for csvRow in csvReader:
                df_start_row_offset += 1
                if len(csvRow) == 1 and csvRow[0] == '':
                    break;
                else:
                    # k => v or k => [v,v,v]
                    self.meta_data[csvRow[0]] = csvRow[1:-1] if (len(csvRow) > 2) else csvRow[1]

        self.df = pd.read_csv(
            filepath_or_buffer=self.data_path + self.dataFileName,
            skiprows=df_start_row_offset
        )

    def get_dataframe(self) -> pd.DataFrame:
        """
        :return: pandas.Dataframe a reference to the dataframe of the csv file, this method will
         probably do weird stuff if you don't load the file first
        """
        return self.df

    def get_dataframe_copy(self):
        """
        May cause performance issues, it performs a deep copy of the df, but its good if you want to change things
        and come back to later or do some threading with data changes
        """
        return self.df.copy(deep=True)

    def get_meta_data(self):
        return self.meta_data


if __name__ == "__main__":
    m = BmaWifiDatafile("10F-BC01 - 2.4GHz Channel 1 Throughput TX-RX.csv", data_path="../data/")
    m.load_file()
    
