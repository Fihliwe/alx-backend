#!/usr/bin/env python3
"""
Simple pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset
    @staticmethod
    def index_range(page, page_size):
        """
        The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes 
        to return in a list for those particular pagination parameters.
        """
        
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        
        paged_data = (start_index, end_index)
        
        return paged_data

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """
            
            """
            assert type(page) == int and type(page_size) == int
            assert page> 0 and page_size > 0
            startIndex, endIndex = self.index_range(page, page_size)
            return self.dataset()[startIndex:endIndex]