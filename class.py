class ClassName:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary,str=''):
        self.name = name
        self.salary = salary
        self.str = str
        ClassName.empCount += 1

    def displayCount(self):
        print(ClassName.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary ,"缺省值"+self.str)



"创建 Employee 类的第一个对象"
emp1 = ClassName("Zara", 2000,'eee')
"创建 Employee 类的第二个对象"
emp2 = ClassName("Manni", 5000,'3333')
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % ClassName.empCount)

