from xml.dom.minidom import *
from pip._vendor.distlib.compat import raw_input


def main():
    doc = Document()
    base = doc.createElement('Crime')
    doc.appendChild(base)
    while True:
        option = raw_input('What crime would you like to report? ')

        if option == 'Murder':
            murder = doc.createElement('Murder')
            base.appendChild(murder)
            criminal(doc, murder)
            victim(doc, murder)

        if option == 'Theft':
            theft = doc.createElement('Theft')
            base.appendChild(theft)
            criminal(doc, theft)
            victim(doc, theft)

        if option == 'Drugs':
            drugs = doc.createElement('Drugs')
            base.appendChild(drugs)
            criminal(doc, drugs)
            victim(doc, drugs)

        if option == 'Exit':
            break

    docstring = parseString(doc.toprettyxml())
    print(docstring)
    docstring.writexml(open('Crime.xml', 'w'))


def criminal(doc, crime):
    criminal = doc.createElement('Criminal')

    Name = doc.createElement('Name')
    Age = doc.createElement('Age')
    Height = doc.createElement('Height')

    name = raw_input("Enter criminals name: ")
    criminal_name = doc.createTextNode(name)
    age = raw_input("Enter criminals age: ")
    criminal_age = doc.createTextNode(age)
    height = raw_input("Enter criminals height: ")
    criminal_height = doc.createTextNode(height)

    Name.appendChild(criminal_name)
    Age.appendChild(criminal_age)
    Height.appendChild(criminal_height)

    crime.appendChild(criminal)
    criminal.appendChild(Name)
    criminal.appendChild(Age)
    criminal.appendChild(Height)


def victim(doc, crime):
    vict = doc.createElement('Victim')

    Name = doc.createElement('Name')
    Age = doc.createElement('Age')
    Height = doc.createElement('Height')

    name = raw_input("Enter Victims name: ")
    victim_name = doc.createTextNode(name)
    age = raw_input("Enter Victims age: ")
    victim_age = doc.createTextNode(age)
    height = raw_input("Enter Victims height: ")
    victim_height = doc.createTextNode(height)

    Name.appendChild(victim_name)
    Age.appendChild(victim_age)
    Height.appendChild(victim_height)

    crime.appendChild(vict)
    vict.appendChild(Name)
    vict.appendChild(Age)
    vict.appendChild(Height)


if __name__ == '__main__':
    main()