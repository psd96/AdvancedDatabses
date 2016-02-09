from xml.dom.minidom import *
from pip._vendor.distlib.compat import raw_input


def main():
    doc = Document()
    base = doc.createElement('Crime')
    doc.appendChild(base)
    while True:
        option = raw_input('\nWhat crime would you like to report? (Murder, Theft or Drug. Exit to quit): ')

        if option == 'Murder':
            murder = doc.createElement('Murder')
            base.appendChild(murder)
            criminal(doc, murder)
            location(doc, murder)
            victim(doc, murder)
            weapon(doc, murder)

        if option == 'Theft':
            theft = doc.createElement('Theft')
            base.appendChild(theft)
            criminal(doc, theft)
            location(doc, theft)
            victim(doc, theft)

        if option == 'Drugs':
            drugs = doc.createElement('Drugs')
            base.appendChild(drugs)
            criminal(doc, drugs)
            location(doc, drugs)
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

    name = raw_input("\nDetails about Criminal: \n\tEnter criminals name: ")
    criminal_name = doc.createTextNode(name)
    age = raw_input("\tEnter criminals age: ")
    criminal_age = doc.createTextNode(age)
    height = raw_input("\tEnter criminals height: ")
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
    Num = doc.createElement('StreetNum')
    StreetName = doc.createElement('StreetName')
    Postcode = doc.createElement('Postcode')

    name = raw_input("\nVictims Details: \n\tEnter Victims name: ")
    victim_name = doc.createTextNode(name)
    age = raw_input("\tEnter Victims age: ")
    victim_age = doc.createTextNode(age)
    height = raw_input("\tEnter Victims height: ")
    victim_height = doc.createTextNode(height)
    num = raw_input("\tEnter Victims house number: ")
    victim_num = doc.createTextNode(num)
    street = raw_input("\tEnter street name: ")
    victim_street = doc.createTextNode(street)
    code = raw_input("\tEnter postcode: ")
    victim_postcode = doc.createTextNode(code)

    Name.appendChild(victim_name)
    Age.appendChild(victim_age)
    Height.appendChild(victim_height)
    Num.appendChild(victim_num)
    StreetName.appendChild(victim_street)
    Postcode.appendChild(victim_postcode)

    crime.appendChild(vict)
    vict.appendChild(Name)
    vict.appendChild(Age)
    vict.appendChild(Height)
    vict.appendChild(Num)
    vict.appendChild(StreetName)
    vict.appendChild(Postcode)


def location(doc, crime):
    location = doc.createElement('Location')

    streetNum = doc.createElement('StreetNum')
    streetName = doc.createElement('StreetName')
    county = doc.createElement('County')
    postcode = doc.createElement('Postcode')

    num = raw_input("\nLocation of where crime took place: \n\tEnter the street number of crime: ")
    loc_num = doc.createTextNode(num)
    name = raw_input("\tEnter the street name: ")
    loc_name = doc.createTextNode(name)
    conty = raw_input("\tEnter County: ")
    loc_county = doc.createTextNode(conty)
    code = raw_input("\tEnter Postcode: ")
    loc_code = doc.createTextNode(code)

    streetNum.appendChild(loc_num)
    streetName.appendChild(loc_name)
    county.appendChild(loc_county)
    postcode.appendChild(loc_code)

    crime.appendChild(location)
    location.appendChild(streetNum)
    location.appendChild(streetName)
    location.appendChild(county)
    location.appendChild(postcode)


def weapon(doc, crime):
    weapon = doc.createElement('Weapon')

    weapon_num = raw_input("\nHow many weapons where used in the murder?")
    weapon_num = int(weapon_num)
    for x in range(0, weapon_num):
        item = raw_input("\tWhat weapon was used? ")
        weapon_item = doc.createTextNode(item)
        weaponno = doc.createElement('Weapon' + str(x+1))
        weaponno.appendChild(weapon_item)
        weapon.appendChild(weaponno)

    crime.appendChild(weapon)


if __name__ == '__main__':
    main()