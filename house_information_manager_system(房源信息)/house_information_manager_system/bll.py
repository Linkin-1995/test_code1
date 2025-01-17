"""
    业务逻辑层
"""
import collections
from typing import List, Dict

from dal import HouseDao
from model import HouseModel


class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

    @property
    def list_houses(self) -> List[HouseModel]:
        return self.__list_houses

    def get_house_by_max_total_price(self) -> HouseModel:
        return max(self.__list_houses, key =lambda house: house.total_price)

    def get_house_by_min_area(self) -> HouseModel:
        # 类内可以使用属性(属性内部返回私有变量)
        return min(self.list_houses, key =lambda house: house.area)

    def get_houses_type(self) -> Dict[str, int]:
        """
            获取户型种类
        :return:字典类型[户型种类,数量]
        """
        # key:类型
        # value:数量
        dict_house_type = {}
        for house in self.__list_houses:
            if house.house_type in dict_house_type:
                dict_house_type[house.house_type] += 1
            else:
                dict_house_type[house.house_type] = 1
        return dict_house_type
        # return collections.Counter(map(lambda house:house.house_type,self.__list_houses))