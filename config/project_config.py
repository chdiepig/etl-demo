# 此文件存放项目中使用到的一些常量信息
from datetime import datetime

# 配置日志生成的名字
# 定义一个常量,记录日志文件保存的路径
LOG_FILE_PATH = '../logs/pyetl_log/'
# 定义一个常量,生成日志的名字
LOG_FILE_NAME = "pyetl_" + datetime.now().strftime("%Y%m%d%H") + ".log"

#  ===============MySQL相关配置===========================
MYSQL_CHARSET = 'utf8'

# 元数据库的配置
METADATA_HOST = '192.168.88.100'
METADATA_USER = 'root'
METADATA_PWD = 'hadoop'
METADATA_PORT = 3306
METADATA_DB_NAME = "metadata"
# 文件监控表名称，存储哪些文件被处理过
METADATA_FILE_MONITOR_TABLE_NAME = "file_monitor"
# 文件监控表，建表语句的列信息
METADATA_FILE_MONITOR_TABLE_CREATE_COLS = """
    id INT PRIMARY KEY AUTO_INCREMENT, 
    file_name VARCHAR(255) UNIQUE NOT NULL COMMENT '被处理的文件名称', 
    process_lines INT COMMENT '本文件中有多少条数据被处理', 
    process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '处理时间'
"""

# ======================目标数据库的相关配置=======================
TARGET_HOST = METADATA_HOST
TARGET_USER = METADATA_USER
TARGET_PASSWORD = METADATA_PWD
TARGET_PORT = METADATA_PORT
TARGET_DB_NAME = "retail"

# JSON数据采集后，写入MySQL，存储订单相关的表，表名是：
TARGET_ORDERS_TABLE_NAME = "orders"
# orders表的建表语句的列信息
TARGET_ORDERS_TABLE_CREATE_COLS = \
    f"order_id VARCHAR(255) PRIMARY KEY, " \
    f"store_id INT COMMENT '店铺ID', " \
    f"store_name VARCHAR(30) COMMENT '店铺名称', " \
    f"store_status VARCHAR(10) COMMENT '店铺状态(open,close)', " \
    f"store_own_user_id INT COMMENT '店主id', " \
    f"store_own_user_name VARCHAR(50) COMMENT '店主名称', " \
    f"store_own_user_tel VARCHAR(15) COMMENT '店主手机号', " \
    f"store_category VARCHAR(10) COMMENT '店铺类型(normal,test)', " \
    f"store_address VARCHAR(255) COMMENT '店铺地址', " \
    f"store_shop_no VARCHAR(255) COMMENT '店铺第三方支付id号', " \
    f"store_province VARCHAR(10) COMMENT '店铺所在省', " \
    f"store_city VARCHAR(10) COMMENT '店铺所在市', " \
    f"store_district VARCHAR(10) COMMENT '店铺所在行政区', " \
    f"store_gps_name VARCHAR(255) COMMENT '店铺gps名称', " \
    f"store_gps_address VARCHAR(255) COMMENT '店铺gps地址', " \
    f"store_gps_longitude VARCHAR(255) COMMENT '店铺gps经度', " \
    f"store_gps_latitude VARCHAR(255) COMMENT '店铺gps纬度', " \
    f"is_signed TINYINT COMMENT '是否第三方支付签约(0,1)', " \
    f"operator VARCHAR(10) COMMENT '操作员', " \
    f"operator_name VARCHAR(50) COMMENT '操作员名称', " \
    f"face_id VARCHAR(255) COMMENT '顾客面部识别ID', " \
    f"member_id VARCHAR(255) COMMENT '顾客会员ID', " \
    f"store_create_date_ts TIMESTAMP COMMENT '店铺创建时间', " \
    f"origin VARCHAR(255) COMMENT '原始信息(无用)', " \
    f"day_order_seq INT COMMENT '本订单是当日第几单', " \
    f"discount_rate DECIMAL(10, 5) COMMENT '折扣率', " \
    f"discount_type TINYINT COMMENT '折扣类型', " \
    f"discount DECIMAL(10, 5) COMMENT '折扣金额', " \
    f"money_before_whole_discount DECIMAL(10, 5) COMMENT '折扣前总金额', " \
    f"receivable DECIMAL(10, 5) COMMENT '应收金额', " \
    f"erase DECIMAL(10, 5) COMMENT '抹零金额', " \
    f"small_change DECIMAL(10, 5) COMMENT '找零金额', " \
    f"total_no_discount DECIMAL(10, 5) COMMENT '总价格(无折扣)', " \
    f"pay_total DECIMAL(10, 5) COMMENT '付款金额', " \
    f"pay_type VARCHAR(10) COMMENT '付款类型', " \
    f"payment_channel TINYINT COMMENT '付款通道', " \
    f"payment_scenarios VARCHAR(15) COMMENT '付款描述(无用)', " \
    f"product_count INT COMMENT '本单卖出多少商品', " \
    f"date_ts datetime COMMENT '订单时间', " \
    f"INDEX (receivable), INDEX (date_ts)"

# JSON数据采集后，写入MySQL，存储订单详情（带商品信息的）相关的表，表名是：
TARGET_ORDERS_DETAIL_TABLE_NAME = "orders_detail"
# orders_detail表的建表语句的列信息
TARGET_ORDERS_DETAIL_TABLE_CREATE_COLS = \
    f"order_id VARCHAR(255) COMMENT '订单ID', " \
    f"barcode VARCHAR(255) COMMENT '商品条码', " \
    f"name VARCHAR(255) COMMENT '商品名称', " \
    f"count INT COMMENT '本单此商品卖出数量', " \
    f"price_per DECIMAL(10, 5) COMMENT '实际售卖单价', " \
    f"retail_price DECIMAL(10, 5) COMMENT '零售建议价', " \
    f"trade_price DECIMAL(10, 5) COMMENT '贸易价格(进货价)', " \
    f"category_id INT COMMENT '商品类别ID', " \
    f"unit_id INT COMMENT '商品单位ID(包、袋、箱、等)', " \
    f"PRIMARY KEY (order_id, barcode)"

# =======================文件写入配置=======================
# 写出CSV的根目录配置
retail_output_csv_root_path = "../output_csv/orders_and_detail_csv/"
# 写出订单模型，CSV的文件名字配置
retail_orders_output_csv_file_name = f'orders_{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'
print(retail_orders_output_csv_file_name)
# 写出订单详情（带商品信息）模型，CSV的文件名字配置
retail_orders_detail_output_csv_file_name = f'orders_detail_{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'
# 日志写入到csv文件路径
log_output_csv_root_path = "../output_csv/log_csv/"
log_output_csv_file_name = f'log_{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'

# ============日志数据保存的相关配置================
# 存储已经被处理过的日志文件的表名
metadata_backend_logs_tb_name = 'backend_logs_monitor'
# 建表的时候的字段
metadata_backend_logs_tb_create_cols = """
    id INT PRIMARY KEY AUTO_INCREMENT, 
    file_name VARCHAR(255) UNIQUE NOT NULL COMMENT '被处理的文件名称', 
    process_lines INT COMMENT '本文件中有多少条数据被处理', 
    process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '处理时间'
"""

# 日志文件数据写入mysql数据表的名字和建表的字段
target_log_table_name = 'backend_logs'
target_log_create_cols = \
        f"id int PRIMARY KEY AUTO_INCREMENT COMMENT '自增ID', " \
        f"log_time TIMESTAMP(6) COMMENT '日志时间,精确到6位毫秒值', " \
        f"log_level VARCHAR(10) COMMENT '日志级别', " \
        f"log_module VARCHAR(50) COMMENT '输出日志的功能模块名', " \
        f"response_time INT COMMENT '接口响应时间毫秒', " \
        f"province VARCHAR(30) COMMENT '访问者省份', " \
        f"city VARCHAR(30) COMMENT '访问者城市', " \
        f"log_text VARCHAR(255) COMMENT '日志正文', " \
        f"INDEX(log_time)"



# barcode业务，update_at字段的监控表的名称
metadata_barcode_table_name = "barcode_monitor"
# barcode业务，update_at字段的监控表的建表语句的列信息
metadata_barcode_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT COMMENT '自增ID', " \
                                             "time_record TIMESTAMP NOT NULL COMMENT '本次采集记录的最大时间', " \
                                             "gather_line_count INT NULL COMMENT '本次采集条数'"


# 采集barcode业务，写入MySQL的表名
target_barcode_table_name = "barcode"
target_barcode_table_create_cols = """
    `code` varchar(50) PRIMARY KEY COMMENT '商品条码',
    `name` varchar(200) DEFAULT '' COMMENT '商品名称',
    `spec` varchar(200) DEFAULT '' COMMENT '商品规格',
    `trademark` varchar(100) DEFAULT '' COMMENT '商品商标',
    `addr` varchar(200) DEFAULT '' COMMENT '商品产地',
    `units` varchar(50) DEFAULT '' COMMENT '商品单位(个、杯、箱、等)',
    `factory_name` varchar(200) DEFAULT '' COMMENT '生产厂家',
    `trade_price` DECIMAL(50, 5) DEFAULT 0.0 COMMENT '贸易价格(指导进价)',
    `retail_price` DECIMAL(50, 5) DEFAULT 0.0 COMMENT '零售价格(建议卖价)',
    `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    `wholeunit` varchar(50) DEFAULT NULL COMMENT '大包装单位',
    `wholenum` int(11) DEFAULT NULL COMMENT '大包装内装数量',
    `img` varchar(500) DEFAULT NULL COMMENT '商品图片',
    `src` varchar(20) DEFAULT NULL COMMENT '源信息', 
    INDEX (update_at)
"""
# 数据源数据库的配置
source_host = METADATA_HOST
source_user = METADATA_USER
source_password = METADATA_PWD
source_port = METADATA_PORT
source_db_name = "source_data"
source_barcode_data_table_name = "sys_barcode"


# 写出订单模型，CSV的文件名字配置
barcode_orders_output_csv_file_path = "../output_csv/barcode_csv/"
barcode_orders_output_csv_file_name = f'barcode-{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'
