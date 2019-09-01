# coding=utf-8
# @Time    : 2019/5/31 10:12
# @Author  : Mandy
import yaml
import conftest


class WriteUserConfig:
    def __init__(self):
        try:
            self.file_path = conftest.userconfig_dir
        except Exception as msg:
            print(u"文件不存在%s" % msg)

    """
    加载yaml数据
    """
    def read_data(self):
        with open(self.file_path, 'r') as fr:
            data = yaml.load(fr, Loader=yaml.Loader)
        return data

    """
    获取value值
    """
    def get_value(self, section, key):
        data = self.read_data()
        value = data[section][key]
        return value

    """
    写入yaml数据
    """
    def write_data(self, i, device, bp, port):
        data = self.join_data(i, device, bp, port)
        with open(self.file_path, 'a') as fr:
            yaml.dump(data, fr)

    """
    拼接数据
    """
    def join_data(self, i, device, bp, port):
        data = {
            "device"+str(i):
                {"deviceName": device,
                 "port": port,
                 "bp": bp
                 }
        }
        return data

    """
    清除yaml数据
    """
    def clear_data(self):
        with open(self.file_path, 'w') as fr:
            fr.truncate()
        fr.close()


# if __name__ == '__main__':
#     write_file = WriteUserConfig()
#     write_file.write_data("1111111", "4000", "4200")
#     device1 = write_file.get_value('deviceName')
#     port = write_file.get_value('port')
#     print(device1)
#     print(port)
#     write_file.clear_data()
