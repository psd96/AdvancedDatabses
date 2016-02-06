from xml.dom.minidom import *
from pip._vendor.distlib.compat import raw_input


def write_xml(doc, out):
    doc.writexml(out)
    out.flush()
    out.close()


def add_element(doc, node, name, identification):
    if identification == -1:
        node.appendChild(doc.createElement(name))
    else:
        element = doc.createElement(name)
        element.setAttribute('id', str(identification))
        element.setIdAttribute('id')
        node.appendChild(element)


def add_text(doc, node, text):
    text_node = doc.createTextNode(text)
    node.appendChild(text_node)


def element_input(doc, case_type, element_type, info_list, multiple, identification):
    # create a list of variables equal to the size of inputs
    variable_list = []
    for i in range(0, len(info_list)):
        variable_list.append(str)

    # a prompt for element count
    if multiple:
        count = int(raw_input("Number of " + element_type + "s: "))
    else:
        count = 1

    # loop for previously mentioned count
    for i in range(0, count):
        add_element(doc, doc.getElementsByTagName(case_type)[0], element_type, identification)
        identification += 1

        # take user input for murderer fields
        print(element_type + " number " + str(i + 1))

        for j in range(0, len(info_list)):
            variable_list[j] = raw_input("\t" + element_type + " " + info_list[j] + ": ")
            add_element(doc, doc.getElementsByTagName(element_type)[i], info_list[j], -1)
            add_text(doc, doc.getElementsByTagName(element_type)[i].getElementsByTagName(info_list[j])[0], variable_list[j])


def generate_murder_xml(doc):
    crime_type = "Murder"
    identification = 0
    add_element(doc, doc.childNodes[0], "Murder", -1)
    element_input(doc, crime_type, "Date", ["Day", "Month", "Year", "Time"], False, identification)
    element_input(doc, crime_type, "Murderer", ["Name", "Age", "Height"], True, identification)
    #element_input(doc, crime_type, "Victim", ["Name", "Age", "Height"], True, identification)
    #element_input(doc, crime_type, "Weapon", ["Type", "Weight", "Width", "Length", "Depth"], True, identification)
    #element_input(doc, "Murder", "Location", ["StreetNumber", "PostCode", "County", "Country"], False, identification)


def generate_theft_xml(doc):
    crime_type = "Theft"
    identification = 0
    add_element(doc, doc.childNodes[0], crime_type, -1)
    element_input(doc, crime_type, "Date", ["Day", "Month", "Year"], False, identification)
    element_input(doc, crime_type, "Thief", ["Name", "Age", "Height"], True, identification)
    element_input(doc, crime_type, "Victim", ["Name", "Age", "Height"], True, identification)
    element_input(doc, crime_type, "Object", ["Type", "Value", "Weight", "Width", "Length", "Depth"], True, identification)
    element_input(doc, "Murder", "Location", ["StreetNumber", "PostCode", "County", "Country"], False, identification)


def main():
    # define xml document
    doc = Document()

    # add the base element 'Crime'
    doc.appendChild(doc.createElement('Crime'))

    # fill xml with murder report
    generate_murder_xml(doc)

    # format
    doc = parseString(doc.toprettyxml())

    # write to file
    write_xml(doc, open('testOutput.xml', 'w'))


if __name__ == '__main__':
    main()
