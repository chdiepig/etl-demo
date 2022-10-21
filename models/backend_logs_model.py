# coding:utf8
"""
后台日志采集的model模型
"""
from config import project_config as conf


class BackendLogsModel:
    def __init__(self, data: str, sep="\t"):
        arrs = data.split(sep)

        self.log_time = arrs[0]                                     # 日志时间
        self.log_level = arrs[1].replace("[", "").replace("]", "")  # 日志级别,处理方括号
        self.log_module = arrs[2]                                   # 日志模块
        self.response_time = int(arrs[3][:-2][5:])                  # 响应时间提取
        self.province = arrs[4]                                     # 省份
        self.city = arrs[5]                                         # 城市
        self.log_text = arrs[6]                                     # 日志正文

    def to_string(self):
        return f"log_time: {self.log_time}, " \
                f"log_level: {self.log_level}, " \
                f"log_module: {self.log_module}, " \
                f"response_time: {self.response_time}, " \
                f"province: {self.province}, " \
                f"city: {self.city}, " \
                f"log_text: {self.log_text}"

    def generate_insert_sql(self):
        # 注意，表名自行配置到配置文件中
        return f"INSERT INTO backend_logs(" \
                f"log_time, log_level, log_module, response_time, province, city, log_text) VALUES(" \
                f"'{self.log_time}', " \
                f"'{self.log_level}', " \
                f"'{self.log_module}', " \
                f"{self.response_time}, " \
                f"'{self.province}', " \
                f"'{self.city}', " \
                f"'{self.log_text}'" \
                f")"

    def to_csv(self, sep=","):
        return \
            f"{self.log_time}{sep}" \
            f"{self.log_level}{sep}" \
            f"{self.log_module}{sep}" \
            f"{self.response_time}{sep}" \
            f"{self.province}{sep}" \
            f"{self.city}{sep}" \
            f"{self.log_text}"
