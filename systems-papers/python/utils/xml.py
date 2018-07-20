import xml.etree.ElementTree as ET
import os

def parseXML(fn):
    try:
        tree = ET.parse(fn)
        root = tree.getroot()
        return root
    except Exception:
        return None

def getChildByTag(xml, tag, do_except=True):
    for child in xml.getchildren():
        if child.tag == tag:
            return child
    if do_except:
        raise Exception("couldn't find child of "+str(xml)+" with tag "+str(tag))

def getChildrenByTag(xml, tag):
    return [ child for child in xml.getchildren()
             if child.tag == tag ]

def getDescendantByTagPath(xml, tags, do_except=True):
    try:
        for tag in tags:
            xml = getChildrenByTag(xml, tag)
        return xml
    except Exception as e:
        if do_except: raise e