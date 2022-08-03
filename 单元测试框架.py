import unittest


# 创建一个类，继承于unittest.TestCase
class myUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('这是setupclass....')  # setupclass方法，只会在所有的用例执行之前，执行一次
        cls.name = '李四'  # 在setUpClass定义变量，cls.变量名  =变量值

    @classmethod
    def tearDownClass(cls):
        print('这是teardownClass.....')  # 等所有的用例执行完成之后，执行一次

    def setUp(self):
        print('在每一条测试用例执行之前，先执行')
        self.age = '19'  # 在setup中，定义变量，self.变量名 = 变量值

    def tearDown(self):
        print('在每一条测试用例执行之后，再执行')

    def test_aa(self):
        print(self.name)  # 在测试用例中，想要使用 setupclass中定义的变量，或者setup中定义的变量，都是通过self.变量名
        print(self.age)
        print('这是test_aa')  # 用例的执行顺序，按照0~9,A~Z,a~z # 断言，判断实际结果与预期结果是否一致
        self.assertIn('a', 'abc')  # 判断a是不是在abc中

    def test_AA(self):
        print('这是test_AA')
        self.assertEqual(3, 1 + 2)  # 判断3是不是和1+2 相等


if __name__ == '__main__':
    unittest.main()
