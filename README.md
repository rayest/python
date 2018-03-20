## with Python2.7 and Python3.6 both
### Problem One 
* if
> OSError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/wtforms'
* try
> sudo pip install flask-wtf

### operate db
> from WebDemo import db
> db.create_all()

### 通过python3运行文件
> python3 word.py 

### run test
> 执行 unittest.main()
> 或者：python -m unittest test_mysql_orm.py

### 模块导入
> 如果包的命名不合适，会产生'导入错误'

> pip install -r requirements