import os
import time
from pathlib import Path
import yaml
from ddt import file_data


@file_data('../data/jxm_file.yaml')
def run():
    Mytime = time.strftime("%Y-%m-%d_%H-%M-%S")
    print("程序开始运行")
    os.system(
                "jmeter -n -t D:/apache-jmeter-5.1/jmx/jsfk-it-002.jmx -l D:/apache-jmeter-5.1/jtl/{}.jtl -e -o D:/apache-jmeter-5.1/report/{}"
                    .format(Mytime, Mytime))
    linkName = Path('D:/apache-jmeter-5.1/report/' + Mytime + '/index.html').as_uri()
    print("已生成测试报告，具体内容可点击超链接", linkName)
    print("程序已结束,即将关闭窗口")
    time.sleep(5)


if __name__ == '__main__':
    run()

