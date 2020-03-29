import pytest

from page.main import Main

# 机会录入测试用例，仅提供了必填项的用例，其他项之后补充
# 输入框为姓名，手机号，其他选择框当前默认选择第一个

customer_name = [
    ('aaba', '13299990000')
]

class TestCustomerInput:

    def setup(self):
        self.main = Main()

    @pytest.mark.parametrize('customername, contactPhone', customer_name)
    def test_customer_input(self, customername, contactPhone):
        self.main.customer_input().add_customer(customername, contactPhone)

    def teardown(self):
        self.main.close()