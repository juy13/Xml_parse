import sys
import os
import time
import xml.etree.ElementTree as xml


def createXML(filename):
	"""
	Создаем XML файл.
	"""
	root = xml.Element("zAppointments")
	appt = xml.Element("appointment")
	root.append(appt)
	
	# создаем дочерний суб-элемент. 
	begin = xml.SubElement(appt, "begin")
	begin.text = "1181251680"
	
	uid = xml.SubElement(appt, "uid")
	uid.text = "040000008200E000"
	
	alarmTime = xml.SubElement(appt, "alarmTime")
	alarmTime.text = "1181572063"
	
	state = xml.SubElement(appt, "state")
	
	location = xml.SubElement(appt, "location")
	
	duration = xml.SubElement(appt, "duration")
	duration.text = "1800"
	
	subject = xml.SubElement(appt, "subject")
	
	#tree = xml.ElementTree(root)

	appt2 = xml.Element("appointment2")
	root.append(appt2)
	
	# создаем дочерний суб-элемент. 
	begin = xml.SubElement(appt2, "begin")
	begin.text = "1181251680"
	
	uid2 = xml.SubElement(appt2, "uid")
	uid2.text = "040000008200E000"
	
	alarmTime2 = xml.SubElement(appt2, "alarmTime")
	alarmTime2.text = "1181572063"
	
	state2 = xml.SubElement(appt2, "state")
	
	location2 = xml.SubElement(appt2, "location")
	
	duration2 = xml.SubElement(appt2, "duration")
	duration2.text = "1800"
	
	subject2 = xml.SubElement(appt2, "subject")
	
	tree = xml.ElementTree(root)

	with open(filename, "w") as fh:
	    tree.write(filename)


def editXML(filename):
	"""
	Редактируем XML файл.
	"""
	tree = xml.ElementTree(file=filename)
	root = tree.getroot()
	
	for begin_time in root.iter("begin"):
	    begin_time.text = time.ctime(int(begin_time.text))
	
	tree = xml.ElementTree(root)
	with open("updated.xml", "w") as f:
	    tree.write(filename)


if __name__ == "__main__":
	createXML("appt.xml")
	editXML("aq.xml")