from abc import ABC, abstractmethod

class DataBaseLoader(ABC):
    def __init(self, file_path, raw_data, processed_data):
        self.__file_path = file_path
        self.__raw_data = raw_data
        self.processed_data = processed_data

    # Getters da classe
    def get_file_path(self):
        return self.__file_path 
    
    def get_raw_data(self):
        return self.__raw_data 

    def get_processed_data(self):
         return self.__processed_data

    # Setters da casse
    def set_file_path(self, file_path):
        self.__file_path = file_path

    def set_raw_data(self, raw_data):
        self.__raw_data = raw_data

    def set_processed_data(self, processed_data):
        self.__processed_data = processed_data

    # Métodos abstratos: vão ser usados pelas classes herdadas
    @abstractmethod
    def load_data():
        pass

    @abstractmethod
    def standardize_cordinates():
        pass

    # Métodos concretos da classe
    def calculate_teos10_properties():
        return

    
