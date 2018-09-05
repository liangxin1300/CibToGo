import subprocess
import sys
import os
from lxml import etree, objectify


def file2cib_elem(f):
    cib_elem = None
    with open(f, 'r') as fd:
        try:
            cib_elem = etree.parse(fd).getroot()
        except Exception as err:
            print(err)
            return None

    # https://stackoverflow.com/questions/18159221/remove-namespace-and-prefix-from-xml-in-python-using-lxml
    if cib_elem is not None:
        for elem in cib_elem.getiterator():
            if not hasattr(elem.tag, 'find'):
                continue
            i = elem.tag.find('}')
            if i >= 0:
                elem.tag = elem.tag[i+1:]
        objectify.deannotate(cib_elem, cleanup_namespaces=True)
    return cib_elem


def gen_struct(f):
    cib_elem = file2cib_elem(f)
    if cib_elem is None:
        return -1
    print(cib_elem)
    #for c in cib_elem.iterchildren():
    #    print(c.tag)
    #for c in cib_elem.findall("define"):
    #    for i in c.findall("element"):
    #        print(i.tag)
    #for elem in cib_elem.getiterator():
    #    if not hasattr(elem.tag, 'find'):
    #        continue
    #    print(elem.tag)
    return 0


def run_cmd(cmd):
    try:
        proc = subprocess.Popen(cmd,
				shell=True,
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE)
        proc.communicate()
    except Exception as err:
        print(err)
    finally:
        return proc.returncode


if __name__ == "__main__":
    rc = run_cmd("which git")
    if rc != 0:
        print("Error: Please install git first")
        sys.exit(rc)

    if not os.path.exists("pacemaker/xml"):
        print("#### Downloading pacemaker")
        cmd = "git clone https://github.com/ClusterLabs/pacemaker.git --depth=1 --branch master"
        rc = run_cmd(cmd)
        if rc != 0:
            print("Error: Download pacemaker failed!")
            sys.exit(rc)
        print("#### Done\n")

    #for f in os.listdir("pacemaker/xml"):
    #    if f.endswith(".rng"):
    #        print(f)
    _file = "pacemaker/xml/nodes-3.0.rng"
    rc = gen_struct(_file)
    if rc != 0:
        print("Error: gen_struct for %s failed!" % _file)
        sys.exit(rc)
