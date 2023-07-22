import pymysql
'''
# 创建数据库sqpiders
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4")
db.close()
# 创建表students （id name age)
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(100) NOT NULL, name VARCHAR(100) NOT NULL,age INT NOT NULL, PRIMARY KEY(id))'
cursor.execute(sql)
db.close()
'''
# 插入数据 加更新数据
"""
data = {
    'id': '1002',
    'name': 'Bob',
    'age': 20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = f'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ','.join(["{key} = %ss".format(key=key)for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
"""
"""
# 删除数据
table = 'students'
condition = 'age > 20'

sql = 'DELETE FROM {table] WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
"""
# 查询数据
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sqll = 'SELECT * FROM students WHERE age >=20'

try:
    cursor.execute(sqll)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    """
  # 从第二条数据开始的全部数据
    results = cursor.fetchall()
    print('Results:', results)  
    print('Results Type:', type(results))
    for row in results:
        print(row)"""
    while one:
        print('Row:', one)
        one = cursor.fetchone()
except:
    print('Error')
