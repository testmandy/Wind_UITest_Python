# coding=utf-8
# @Time    : 2019/5/3 15:00
# @Author  : Mandy
import os


class DosCmd:
    def excute_cmd_result(self, command):
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == "\n":
                continue
            result_list.append(i.strip("\n"))
        return result_list

    def excute_cmd(self, command):
        os.system(command)


# if __name__ == '__main__':
#     dos = DosCmd()
#     print('result is：' + str(dos.excute_cmd_result("appium -p")))

