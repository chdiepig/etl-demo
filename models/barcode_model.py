# coding:utf8
"""
条码商品信息模型
"""
from config import project_config as conf
from utils import str_util


class BarcodeModel:
    def __init__(self, code=None, name=None, spec=None, trademark=None,
                 addr=None, units=None, factory_name=None, trade_price=None,
                 retail_price=None, update_at=None, wholeunit=None,
                 wholenum=None, img=None, src=None):
        self.code = code
        self.name = str_util.clean_str(name)
        self.spec = str_util.clean_str(spec)
        self.trademark = str_util.clean_str(trademark)
        self.addr = str_util.clean_str(addr)
        self.units = str_util.clean_str(units)
        self.factory_name = str_util.clean_str(factory_name)
        self.trade_price = trade_price
        self.retail_price = retail_price
        self.update_at = update_at
        self.wholeunit = str_util.clean_str(wholeunit)
        self.wholenum = wholenum
        self.img = img
        self.src = src

    def generate_insert_sql(self):
        """生成SQL的插入语句"""
        sql = f"REPLACE INTO {conf.target_barcode_table_name}(" \
              f"code,name,spec,trademark,addr,units,factory_name,trade_price," \
              f"retail_price,update_at,wholeunit,wholenum,img,src) VALUES(" \
              f"'{self.code}', " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.spec)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.trademark)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.addr)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.units)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.factory_name)}, " \
              f"{str_util.check_number_null_and_transform_to_sql_null(self.trade_price)}, " \
              f"{str_util.check_number_null_and_transform_to_sql_null(self.retail_price)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.update_at)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.wholeunit)}, " \
              f"{str_util.check_number_null_and_transform_to_sql_null(self.wholenum)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.img)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.src)}" \
              f")"

        return sql

    def to_csv(self, sep=","):
        csv_line = \
            f"{self.code}{sep}" \
            f"{self.name}{sep}" \
            f"{self.spec}{sep}" \
            f"{self.trademark}{sep}" \
            f"{self.addr}{sep}" \
            f"{self.units}{sep}" \
            f"{self.factory_name}{sep}" \
            f"{self.trade_price}{sep}" \
            f"{self.retail_price}{sep}" \
            f"{self.update_at}{sep}" \
            f"{self.wholeunit}{sep}" \
            f"{self.wholenum}{sep}" \
            f"{self.img}{sep}" \
            f"{self.src}"

        return csv_line
