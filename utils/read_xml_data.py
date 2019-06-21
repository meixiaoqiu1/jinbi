# -*- coding:utf-8 -*-
#导入mindom模块
from xml.dom import minidom
class ReadXMLdata(object):
    def returnXmlDate(self,filename,firstNode,secondNode):
        #parse为打开。使用mindom打开数据文件，通过相对路径获取文件地址，该模块为通用模块，文件名不能写死，文件名用参数接收
        rootfile=minidom.parse("../data_pool/"+filename)
        #基于打开的数据文件，获取该文件的一级标签。这里如果一级标签有重名，需要一个num参数
        #OneNode一级标签。

        OneNode=rootfile.getElementsByTagName(firstNode)[0]
        #基于一级标签的基础上，获取二级标签的节点值
        TwoNode=OneNode.getElementsByTagName(secondNode)[0].childNodes[0].nodeValue
        return TwoNode