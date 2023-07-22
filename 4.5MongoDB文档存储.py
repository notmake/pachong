import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

student1 = {
    'id': '21561341745',
    'name': 'jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '21561341746',
    'name': 'Mike',
    'age': 18,
    'gender': 'male'
}
# result = collection.insert_many([student1,student2])
# print(result)
"""
# 查询 find_one find
chaxun = collection.find_one({'name': 'Mike'})
print(type(chaxun))
print(chaxun)
chaxuns = collection.find({'gender': 'male'})
for cha in chaxuns:
    print(cha)


# 更新
condition = {'name': 'jordan'}
stu = collection.find_one(condition)
stu['age'] = 24
genxin = collection.update_one(condition, {'$set': stu})
"""
# 删除
dele = collection.delete_one({'name':'jordan'})

