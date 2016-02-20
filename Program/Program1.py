from xml.dom.minidom import *
from pip._vendor.distlib.compat import raw_input


def main():
    doc = Document()
    base = doc.createElement('Crime')
    doc.appendChild(base)
    while True:
        option = raw_input('\nWhat crime would you like to report? (Murder, Theft or Drugs. Exit to quit): ')

        if option == 'Murder' or option == 'murder':
            murder = doc.createElement('Murder')
            base.appendChild(murder)
            dateTime(doc,murder)
            criminal(doc, murder)
            #location(doc, murder)
            #victim(doc, murder)
            #weapon(doc, murder)

        if option == 'Theft' or option == 'theft':
            theft = doc.createElement('Theft')
            base.appendChild(theft)
            #dateTime(doc,theft)
            #criminal(doc, theft)
            #forced(doc, theft)
            #location(doc, theft)
            #victim(doc, theft)
            stolenItems(doc, theft)

        if option == 'Drugs' or option == 'drugs':
            drugs = doc.createElement('Drugs')
            base.appendChild(drugs)
            #dateTime(doc,drugs)
            #criminal(doc, drugs)
            drug(doc, drugs)
            #location(doc, drugs)

        if option == 'Exit':
            break

    docstring = parseString(doc.toprettyxml())
    print(docstring)
    docstring.writexml(open('Crime.xml', 'w'))


def dateTime(doc, crime):
    date = doc.createElement('Date')
    time = doc.createElement('Time')

    day = doc.createElement('Day')
    month = doc.createElement('Month')
    year = doc.createElement('Year')

    mins = doc.createElement('Minutes')
    hour = doc.createElement('Hour')

    print("\nWhat day did the crime take place?")
    dayIn = raw_input("\tDay: ")
    dayNode = doc.createTextNode(dayIn)
    monthIn = raw_input("\tMonth: ")
    monthNode = doc.createTextNode(monthIn)
    yearIn = raw_input("\tYear: ")
    yearNode = doc.createTextNode(yearIn)

    day.appendChild(dayNode)
    month.appendChild(monthNode)
    year.appendChild(yearNode)

    date.appendChild(day)
    date.appendChild(month)
    date.appendChild(year)

    print("What time did the crime take place?\n")
    hourIn = raw_input("\tHour: ")
    hourNode = doc.createTextNode(hourIn)
    minIn = raw_input("\tMinutes: ")
    minNode = doc.createTextNode(minIn)

    hour.appendChild(hourNode)
    mins.appendChild(minNode)

    time.appendChild(hour)
    time.appendChild(mins)

    crime.appendChild(date)
    crime.appendChild(time)


def criminal(doc, crime):

    crim_num = int(raw_input("\nHow many criminals where involved in the crime? "))
    for x in range(0, crim_num):
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
    vict_num = int(raw_input("\nHow many victims where involved in the crime? "))
    for x in range(0, vict_num):
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

    weapon_num = raw_input("\nHow many weapons where used in the murder? ")
    weapon_num = int(weapon_num)
    for x in range(0, weapon_num):
        item = raw_input("\tWhat weapon was used? ")
        weapon_item = doc.createTextNode(item)
        weapon.appendChild(weapon_item)

    crime.appendChild(weapon)


def forced(doc, crime):
    forc = doc.createElement('Forced')

    input = raw_input("\nWas there forced entry? ")
    force = doc.createTextNode(input)

    forc.appendChild(force);
    crime.appendChild(forc)


def stolenItems(doc, crime):
    input = raw_input("\nHow many items have been stolen? ")
    input = int(input)
    for x in range(0, input):
        stolen = doc.createElement('StolenItems')
        name = doc.createElement('Name')
        val = doc.createElement('Value')
        item = raw_input("\tWhat is the item? ")
        stolenItem = doc.createTextNode(item)
        value = raw_input("\tWhat is value of the item? ")
        stolenValue = doc.createTextNode(value)

        name.appendChild(stolenItem)
        val.appendChild(stolenValue)
        stolen.appendChild(name)
        stolen.appendChild(val)

        crime.appendChild(stolen)


def drug(doc, crime):

    num = raw_input("\nHow many drugs did they have on them? ")
    num = int(num)
    for x in range(0, num):
        drug = doc.createElement('Drug')
        subs = doc.createElement('Substance')
        amoun = doc.createElement('Amount')
        input = raw_input("\tWhat drug was on their possession? ")
        poss = doc.createTextNode(input)
        input = raw_input("\tHow much, in grams, did they have on them? ")
        amount = doc.createTextNode(input)

        subs.appendChild(poss)
        amoun.appendChild(amount)
        drug.appendChild(subs)
        drug.appendChild(amoun)

        crime.appendChild(drug)


if __name__ == '__main__':
    main()