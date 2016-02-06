
from xml.dom.minidom import *

from pip._vendor.distlib.compat import raw_input


def main():
    doc = Document()
    base = doc.createElement('Crime')
    doc.appendChild(base)
    option = raw_input("Which crime to report")

    if option == 'murder':
        murder = doc.createElement('Murder')
        base.appendChild(murder)
        criminal(doc, murder)
        noofvic = raw_input("How many victims were there?")
        for x in range(1, noofvic):
            victim = doc.createElement('Victim')
            victim(doc, murder)
            murder.appendChild(victim)
            location =doc.createElement('location')
            location(doc, murder)
            victim.appendChild(location)
            location(doc, murder)
        weapon = doc.createElement('Weapon')
        weap = raw_input("Enter murder weapon")
        murder_weapon = doc.createTextNode(weap)
        weapon.appendChild(murder_weapon)
        murder.appendChild(weapon)

    if option == 'drugs':
        drugs = doc.createElement('Drugs')
        base.appendChild(drugs)
        criminal(doc, drugs)
        dtype = doc.createElement('Type')
        type = raw_input("Type of drugs")
        drug_type = doc.createTextNode(type)
        amount = raw_input("Amount of drugs")
        amount_drugs = doc.createTextNode(amount)
        dtype.appendChild(amount_drugs)
        dtype.appendChild(drug_type)
        drugs.appendChild(dtype)

    if option == 'theft':
        theft = doc.createElement('Theft')
        base.appendChild(theft)
        criminal(doc, theft)
        itemsstolen = doc.createElement('Stolen')
        victim(doc,theft)
        i = raw_input("How many items were stolen?: ")
        i = int(i)
        for x in range(0, i):
            items = raw_input("Enter Item name")
            stuff = doc.createTextNode(items)
            price = raw_input("Enter Items Value")
            cprice = doc.createTextNode(price)
            itemsstolen.appendChild(stuff)
            itemsstolen.appendChild(cprice)
        theft.appendChild(itemsstolen)
    docstring = parseString(doc.toprettyxml())
    print(docstring)
    docstring.writexml(open('Crime.xml', 'w'))

def criminal(doc, crime):
        criminal = doc.createElement('Criminal')

        cname = raw_input("Enter criminals name: ")
        criminal_name = doc.createTextNode(cname)
        cage = raw_input("Enter criminals age: ")
        criminal_age = doc.createTextNode(cage)
        cheight = raw_input("Enter criminals height: ")
        criminal_height = doc.createTextNode(cheight)
        cshoesize = raw_input("Enter criminals shoe size: ")
        criminal_shoesize = doc.createTextNode(cshoesize)

        criminal.appendChild(criminal_name)
        criminal.appendChild(criminal_age)
        criminal.appendChild(criminal_height)
        criminal.appendChild(criminal_shoesize)
        crime.appendChild(criminal)

def victim(doc, crime):
        vname = raw_input("Enter victims name: ")
        victim_name = doc.createTextNode(vname)
        vage = raw_input("Enter victims age: ")
        victim_age = doc.createTextNode(vage)
        victim.appendChild(victim_name)
        victim.appendChild(victim_age)

def location(doc, crime):
    lno = raw_input("Enter location name or number: ")
    loc_no = doc.createTextNode(lno)
    lstreet = raw_input("Enter street address: ")
    loc_street = doc.createTextNode(lstreet)
    loccity = raw_input("Enter city: ")
    loc_city = doc.createTextNode(loccity)
    locpostcode = raw_input("Enter Postcode: ")
    loc_postcode = doc.createTextNode(locpostcode)
    location.appendChild(loc_no)
    location.appendChild(loc_street)
    location.appendChild(loc_city)
    location.appendChild(loc_postcode)

if __name__ == '__main__':
    main()