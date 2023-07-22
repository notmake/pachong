from lxml import etree
"""
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''


html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

"""
# 读取文本
html = etree.parse('./test.html', etree.HTMLParser())

# 修正 调用.tostring方法
result = etree.tostring(html)
print(result.decode('utf-8'))

# 利用Xpath规则选出节点
jiedian = html.xpath('//li')         # //开头 全部节点
print(jiedian)
print(jiedian[0])


# 节点轴选择

html1 = etree.parse('./节点轴选择.html', etree.HTMLParser())
result1 = html1.xpath('//li[1]/ancestor::*')  # 第一个li的节点的所有祖先节点
print(result1)
result1 = html1.xpath('//li[1]/ancestor::div')  # 加限定条件div
print(result1)
result1 = html1.xpath('//li[1]/attribute::*')  # 获取所有属性值
print(result1)
result1 = html1.xpath('//li[1]/child::a[@href="link1.html"]')  # 获取所有子节点 可加限定条件儿子得孙子
print(result1)
result1 = html1.xpath('//li[1]/descendant::span')  # 获取所有子孙节点
print(result1)
result1 = html1.xpath('//li[1]/following::*[2]')  # 获取之后的所有节点 加限定条件指定
print(result1)
result1 = html1.xpath('//li[1]/following-sibling::*')  # 获取之后的所有同级节点
print(result1)
