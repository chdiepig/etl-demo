"""
零售订单模型
负责构建
- 纯订单相关的数据模型（1比1的class模型）
- 订单和商品相关的数据模型（1比多的class模型）
"""
import json
from utils import time_util, str_util
from config import project_config as conf


class OrdersModel:
    """构建订单模型（纯订单，不包含商品信息）"""
    def __init__(self, data: str):
        """
        从传入的字符串数据构建订单model
        此Model只包含订单信息，不包含订单详情（商品售卖）
        """
        # 将一行字符串json转换为字典对象
        data = json.loads(data)

        self.discount_rate = data['discountRate']                   # 折扣率
        self.store_shop_no = data['storeShopNo']                    # 店铺店号（无用列）
        self.day_order_seq = data['dayOrderSeq']                    # 本单为当日第几单
        self.store_district = data['storeDistrict']                 # 店铺所在行政区
        self.is_signed = data['isSigned']                           # 是否签约店铺（签约第三方支付体系）
        self.store_province = data['storeProvince']                 # 店铺所在省份
        self.origin = data['origin']                                # 原始信息（无用）
        self.store_gps_longitude = data['storeGPSLongitude']        # 店铺GPS经度
        self.discount = data['discount']                            # 折扣金额
        self.store_id = data['storeID']                             # 店铺ID
        self.product_count = data['productCount']                   # 本单售卖商品数量
        self.operator_name = data['operatorName']                   # 操作员姓名
        self.operator = data['operator']                            # 操作员ID
        self.store_status = data['storeStatus']                     # 店铺状态
        self.store_own_user_tel = data['storeOwnUserTel']           # 店铺店主电话
        self.pay_type = data['payType']                             # 支付类型
        self.discount_type = data['discountType']                   # 折扣类型
        self.store_name = data['storeName']                         # 店铺名称
        self.store_own_user_name = data['storeOwnUserName']         # 店铺店主名称
        self.date_ts = data['dateTS']                               # 订单时间
        self.small_change = data['smallChange']                     # 找零金额
        self.store_gps_name = data['storeGPSName']                  # 店铺GPS名称
        self.erase = data['erase']                                  # 是否抹零
        self.store_gps_address = data['storeGPSAddress']            # 店铺GPS地址
        self.order_id = data['orderID']                             # 订单ID
        self.money_before_whole_discount = data['moneyBeforeWholeDiscount']  # 折扣前金额
        self.store_category = data['storeCategory']                 # 店铺类别
        self.receivable = data['receivable']                        # 应收金额
        self.face_id = data['faceID']                               # 面部识别ID
        self.store_own_user_id = data['storeOwnUserId']             # 店铺店主ID
        self.payment_channel = data['paymentChannel']               # 付款通道
        self.payment_scenarios = data['paymentScenarios']           # 付款情况（无用）
        self.store_address = data['storeAddress']                   # 店铺地址
        self.total_no_discount = data['totalNoDiscount']            # 整体价格（无折扣）
        self.payed_total = data['payedTotal']                       # 已付款金额
        self.store_gps_latitude = data['storeGPSLatitude']          # 店铺GPS纬度
        self.store_create_date_ts = data['storeCreateDateTS']       # 店铺创建时间
        self.store_city = data['storeCity']                         # 店铺所在城市
        self.member_id = data['memberID']                           # 会员ID

    def check_and_transform_area(self):
        """
        检查模型中的省市区三个字段，如果无意义，就转换成未知.
        :return: 无返回值，直接修改类的属性的值
        """
        if str_util.check_null(self.store_province):
            # 表示省份内容无意义
            self.store_province = "未知省份"
        if str_util.check_null(self.store_city):
            # 表示城市内容无意义
            self.store_city = "未知城市"
        if str_util.check_null(self.store_district):
            # 表示行政区内容无意义
            self.store_district = "未知行政区"

    def to_csv(self, sep=","):
        """
        将此模型对象，转换成一条CSV格式的字符串，以参数(sep)传入的符号作为分隔符
        :param sep: 分隔符，默认是逗号
        :return: 字符串，这个字符串就是我们要的CSV格式的字符串
        """
        # CSV：固定分隔符的文件格式，每一条数据，列之间都是有固定的分隔符
        # 比如：
        # 11,张三,北京
        # 13,王五,广州
        # 上述就是CSV，每一行数据用逗号做列之间的分隔
        # csv = f"{self.member_id}{sep}{self.store_city}{sep}{self.store_create_date_ts}  ......................"
        # 将省市区无意义的内容转换成未知省份、未知城市、未知行政区
        self.check_and_transform_area()

        csv_line = \
            f"{self.order_id}{sep}" \
            f"{self.store_id}{sep}" \
            f"{self.store_name}{sep}" \
            f"{self.store_status}{sep}" \
            f"{self.store_own_user_id}{sep}" \
            f"{self.store_own_user_name}{sep}" \
            f"{self.store_own_user_tel}{sep}" \
            f"{self.store_category}{sep}" \
            f"{self.store_address}{sep}" \
            f"{self.store_shop_no}{sep}" \
            f"{self.store_province}{sep}" \
            f"{self.store_city}{sep}" \
            f"{self.store_district}{sep}" \
            f"{self.store_gps_name}{sep}" \
            f"{self.store_gps_address}{sep}" \
            f"{self.store_gps_longitude}{sep}" \
            f"{self.store_gps_latitude}{sep}" \
            f"{self.is_signed}{sep}" \
            f"{self.operator}{sep}" \
            f"{self.operator_name}{sep}" \
            f"{self.face_id}{sep}" \
            f"{self.member_id}{sep}" \
            f"{time_util.ts13_to_date_str(self.store_create_date_ts)}{sep}" \
            f"{self.origin}{sep}" \
            f"{self.day_order_seq}{sep}" \
            f"{self.discount_rate}{sep}" \
            f"{self.discount_type}{sep}" \
            f"{self.discount}{sep}" \
            f"{self.money_before_whole_discount}{sep}" \
            f"{self.receivable}{sep}" \
            f"{self.erase}{sep}" \
            f"{self.small_change}{sep}" \
            f"{self.total_no_discount}{sep}" \
            f"{self.payed_total}{sep}" \
            f"{self.pay_type}{sep}" \
            f"{self.payment_channel}{sep}" \
            f"{self.payment_scenarios}{sep}" \
            f"{self.product_count}{sep}" \
            f"{time_util.ts13_to_date_str(self.date_ts)}"
        return csv_line

    def generate_insert_sql(self):
        """
        将模型转换成一条INSERT SQL语句
        :return: 字符串，记录了INSERT INTO的SQL语句
        """
        sql = f"INSERT IGNORE INTO {conf.TARGET_ORDERS_TABLE_NAME}(" \
              f"order_id,store_id,store_name,store_status,store_own_user_id," \
              f"store_own_user_name,store_own_user_tel,store_category," \
              f"store_address,store_shop_no,store_province,store_city," \
              f"store_district,store_gps_name,store_gps_address," \
              f"store_gps_longitude,store_gps_latitude,is_signed," \
              f"operator,operator_name,face_id,member_id,store_create_date_ts," \
              f"origin,day_order_seq,discount_rate,discount_type,discount," \
              f"money_before_whole_discount,receivable,erase,small_change," \
              f"total_no_discount,pay_total,pay_type,payment_channel," \
              f"payment_scenarios,product_count,date_ts" \
              f") VALUES(" \
              f"'{self.order_id}', " \
              f"{self.store_id}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_status)}, " \
              f"{self.store_own_user_id}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_own_user_name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_own_user_tel)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_category)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_address)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_shop_no)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_province)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_city)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_district)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_address)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_longitude)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_latitude)}, " \
              f"{self.is_signed}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.operator)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.operator_name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.face_id)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.member_id)}, " \
              f"'{time_util.ts13_to_date_str(self.store_create_date_ts)}', " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.origin)}, " \
              f"{self.day_order_seq}, " \
              f"{self.discount_rate}, " \
              f"{self.discount_type}, " \
              f"{self.discount}, " \
              f"{self.money_before_whole_discount}, " \
              f"{self.receivable}, " \
              f"{self.erase}, " \
              f"{self.small_change}, " \
              f"{self.total_no_discount}, " \
              f"{self.payed_total}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.pay_type)}, " \
              f"{self.payment_channel}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.payment_scenarios)}, " \
              f"{self.product_count}, " \
              f"'{time_util.ts13_to_date_str(self.date_ts)}')"

        return sql


class OrdersDetailModel:
    """订单详情模型，仅包含订单ID+商品信息数据"""

    def __init__(self, data):
        """定义模型中的属性（成员变量），用来存储数据"""
        # 将传入的JSON字符串，转换成Python字典
        data_dict = json.loads(data)
        self.order_id = data_dict['orderID']        # 订单ID
        # 记录当前订单内，售卖的全部商品信息，每一条数据是一个SingleProductSoldModel的对象
        self.products_detail = []
        # 从字典中取出商品信息的list
        order_products_list = data_dict["product"]
        # for循环商品信息list，将每一个商品信息转换成SingleProductSoldModel对象，存入products_detail中
        for single_product in order_products_list:
            self.products_detail.append(SingleProductSoldModel(self.order_id, single_product))

    def generate_insert_sql(self):
        """
        生成插入MySQL的INSERT SQL语句
        可以完成一次性插入多条数据
        """
        sql = f"INSERT IGNORE INTO {conf.TARGET_ORDERS_DETAIL_TABLE_NAME}(" \
              f"order_id,barcode,name,count,price_per,retail_price,trade_price,category_id,unit_id) VALUES"
        # 当前这个SQL字符串是半成品，类似于：`INSERT IGNORE INTO table(id, name) VALUES`
        for model in self.products_detail:
            # model：SingleProductSoldModel的一个对象
            sql += "("
            sql += f"'{model.order_id}', " \
                   f"{str_util.check_str_null_and_transform_to_sql_null(model.barcode)}, " \
                   f"{str_util.check_str_null_and_transform_to_sql_null(model.name)}, " \
                   f"{model.count}, " \
                   f"{model.price_per}, " \
                   f"{model.retail_price}, " \
                   f"{model.trade_price}, " \
                   f"{model.category_id}, " \
                   f"{model.unit_id}"
            sql += "), "

        # 去除SQL结尾的逗号
        sql = sql[:-2]  # 为什么是-2，因为逗号后面还有一个空格

        return sql

    def to_csv(self, sep=","):
        csv_line = ""
        for model in self.products_detail:
            csv_line += model.to_csv()
            csv_line += '\n'
        return csv_line


class SingleProductSoldModel:
    """订单内售卖的单类商品信息"""
    def __init__(self, order_id, product_detail_dict):
        self.order_id = order_id                                    # 订单ID
        self.name = product_detail_dict["name"]                     # 商品名称
        self.count = product_detail_dict["count"]                   # 商品售卖数量
        self.unit_id = product_detail_dict["unitID"]                # 单位ID
        self.barcode = product_detail_dict["barcode"]               # 商品的条码
        self.price_per = product_detail_dict["pricePer"]            # 商品卖出的单价
        self.retail_price = product_detail_dict["retailPrice"]      # 商品建议零售价
        self.trade_price = product_detail_dict["tradePrice"]        # 商品建议成本价
        self.category_id = product_detail_dict["categoryID"]        # 商品类别ID

    def to_csv(self, sep=","):
        """生成一条csv数据，分隔符默认逗号"""
        csv_line = \
            f"{self.order_id}{sep}" \
            f"{self.barcode}{sep}" \
            f"{self.name}{sep}" \
            f"{self.count}{sep}" \
            f"{self.price_per}{sep}" \
            f"{self.retail_price}{sep}" \
            f"{self.trade_price}{sep}" \
            f"{self.category_id}{sep}" \
            f"{self.unit_id}"

        return csv_line


if __name__ == '__main__':
    json_str = '{"discountRate": 1, "storeShopNo": "None", "dayOrderSeq": 21, "storeDistrict": "芙蓉区", "isSigned": 0, "storeProvince": "湖南省", "origin": 0, "storeGPSLongitude": "113.00507336854932", "discount": 0, "storeID": 2179, "productCount": 2, "operatorName": "OperatorName", "operator": "NameStr", "storeStatus": "open", "storeOwnUserTel": 12345678910, "payType": "wechat", "discountType": 2, "storeName": "湖南平价特产总汇", "storeOwnUserName": "OwnUserNameStr", "dateTS": 1542458768000, "smallChange": 0, "storeGPSName": "None", "erase": 0, "product": [{"count": 3, "name": "伊利优酸乳草莓味250ml", "unitID": 3, "barcode": "6907992100012", "pricePer": 2.5, "retailPrice": 2.5, "tradePrice": 1.8, "categoryID": 11}, {"count": 3, "name": "巧克力面包", "unitID": 4, "barcode": "6971518660038", "pricePer": 3, "retailPrice": 3, "tradePrice": 1.5, "categoryID": 1}], "storeGPSAddress": "None", "orderID": "154245876623021796472", "moneyBeforeWholeDiscount": 16.5, "storeCategory": "normal", "receivable": 16.5, "faceID": "", "storeOwnUserId": 2127, "paymentChannel": 0, "paymentScenarios": "PASV", "storeAddress": "StoreAddress", "totalNoDiscount": 16.5, "payedTotal": 16.5, "storeGPSLatitude": "28.194364121754337", "storeCreateDateTS": 1541746839000, "storeCity": "长沙市", "memberID": "0"}'
    model = OrdersModel(json_str)
    print(model.to_csv())
    print(model.generate_insert_sql())


