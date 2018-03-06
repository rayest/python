# coding=utf-8


# 创建类
class Employee:
    employeeCount = 0

    # 初始化方法 或 称之为构造方法。self 代表类的实例
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employeeCount += 1

    # 自定义方法, 类方法必须要传入 self 参数
    def display_count(self):
        print(Employee.employeeCount)


# 实例化对象
employee = Employee('Ray', 1000)

# 访问属性：调用对象方法
employee.display_count()

# 访问并输出对象属性值
print(employee.name)
print(employee.salary)
print(getattr(employee, 'name'))


# 继承
class MaleEmployee(Employee):
    def child_method(self):
        print('This is the child method')


maleEmployee = MaleEmployee()
maleEmployee.child_method()
