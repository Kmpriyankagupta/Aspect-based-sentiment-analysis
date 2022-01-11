import xml.etree.ElementTree as ET
root = ET.parse('Laptop_Train_v2.xml').getroot()
from xml.dom import minidom
xmldoc = minidom.parse('aspectTerms.xml')
aspectTerms = xmldoc.getElementsByTagName('term')
print(len(aspectTerms))
# print(itemlist[0].attributes['name'].value)
# for s in itemlist:
#     print(s.attributes['name'].value)