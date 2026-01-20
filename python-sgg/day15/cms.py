"""
    客户管理系统
"""
import time
from random import choice

from day15.customer import Customer


class CMS:
    def __init__(self):
        # 定义一个字典按照客户id存放客户信息   k:c_id   v:customer
        self.customer_id_dict = {}
        # 定义一个字典按照客户name存放客户信息   k:name   v:{k:c_id, v:customer}
        self.customer_name_dict = {}


    def delete_customer(self):
        """删除客户"""
        customer_id = input("请输入要删除的客户id:")
        # 校验
        if not Customer.check_id(customer_id):
            print("客户id必须为数字")
            return

        if customer_id not in self.customer_id_dict:
            print("要删除的客户不存在")
            return

        # 获取客户名称
        customer_name = self.customer_id_dict[customer_id].name
        #从id字典中删除客户
        del self.customer_id_dict[customer_id].delete()

    def display_customer(self):
        """显示所有客户"""
        if len(self.customer_id_dict) == 0:
            print("当前系统还没有客户")
            return
        else:
            for k in self.customer_id_dict.keys():
                print(self.customer_id_dict[k])

    def set_customer_email(self):
        """输入客户邮箱"""
        customer_email = input("请输入客户邮箱:")
        if Customer.check_email(customer_email):
            return customer_email
        else:
            print("输入的邮箱格式不合理，使用默认值")
            return "None"

    def set_customer_phone(self):
        """输入客户电话"""
        customer_phone = input("请输入客户电话:")
        if Customer.check_phone(customer_phone):
            return customer_phone
        else:
            print("输入的电话格式不合理，使用默认值")
            return "None"

    def set_customer_age(self):
        """输入客户年龄"""
        customer_age = input("请输入客户年龄:")
        if Customer.check_age(customer_age):
            return customer_age
        else:
            print("输入的年龄不合理，使用默认值")
            return "None"

    def set_customer_name(self):
        """输入客户名字"""
        customer_name = "None"
        for i in range(3):
            if i < 2:
                customer_name = input("请输入客户的名字:")
                if Customer.check_name(customer_name):
                    break
                else:
                    print("输入的名字必须为纯字母，请重新输入")
            else:
                customer_name = input("还剩最后一次机会，好好把握:")
                if Customer.check_name(customer_name):
                    break
                else:
                    print("3次机会耗尽，退出")
                    return False

        return customer_name


    def set_customer_id(self):
        """输入用户id"""
        customer_id = "None"
        for i in range(3):
            if i < 2:
                customer_id = input("请输入客户的id:")
                if Customer.check_id(customer_id):
                    break
                else:
                    print("输入的id必须为纯数字，请重新输入")
            else:
                customer_id = input("还剩最后一次机会，好好把握:")
                if Customer.check_id(customer_id):
                    break
                else:
                    print("3次机会耗尽，退出")
                    return False

        # 判断当前添加的客户id是否已经存在
        if customer_id in self.customer_id_dict:
            print("当前添加的用户已经存在")
            return False
        else:
            return customer_id

    def add_customer(self):
        """添加客户"""
        if not (customer_id := self.set_customer_id()):
            return

        if not (customer_name := self.set_customer_name()):
            return

        customer_age =  self.set_customer_age()

        customer_phone = self.set_customer_phone()

        customer_email = self.set_customer_email()

        customer = Customer(customer_id,customer_name,customer_age,customer_phone,customer_email)

        # 将新添加的客户放到字典中
        self.customer_id_dict[customer_id] = customer
        # k: name v: {k: c_id, v: customer}
        customer_inner_dict = self.customer_name_dict.get(customer_name)
        if customer_inner_dict is None:
            self.customer_name_dict[customer_name]= {customer_id:customer}
        else:
            customer_inner_dict[customer_id] = customer

        print("~~~添加用户成功~~~")

    def display_menu(self):
        """显示菜单"""
        print("""
                ~~~~~~~~~~~~~~~~~硅谷客户管理系统~~~~~~~~~~~~~~~~~~~~~~~
                                    1.添加客户
                                    2.删除客户
                                    3.修改客户
                                    4.查询客户
                                    5.显示所有客户
                                    6.退出系统
            """)
    def start(self):
        """启动客户管理系统，进入到菜单页面"""
        try:
            while True:
                # 显示菜单
                self.display_menu()
                choice = input("请输入您要进行的操作:")
                match choice:
                    case "1":
                        # 添加客户
                        print("添加客户")
                        self.add_customer()
                    case "2":
                        # 删除客户
                        print("删除客户")
                        self.delete_customer()
                    case "3":
                        # 修改客户
                        print("修改客户")
                        # self.update_customer()
                    case "4":
                        # 查询客户
                        print("查询客户")
                        # self.search_customer()
                    case "5":
                        # 显示所有客户
                        print("显示所有客户")
                        self.display_customer()
                    case "6":
                        # 退出系统
                        print("您已经成功退出系统")
                        break
                    case _:
                        print("输入有误，请重新输入")
                        time.sleep(1)
        except Exception as e:
            print("系统运行的过程中，发生了异常")



if __name__ == '__main__':
    cms = CMS()
    cms.start()