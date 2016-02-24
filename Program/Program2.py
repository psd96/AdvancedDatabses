from xml.dom.minidom import *

print("Welcome to the Crime Report Generator.")


def getCriminal(crime):
    criminal = crime.getElementsByTagName("Criminal")
    for x in criminal:
        crimName = x.getElementsByTagName('Name')[0].firstChild.data
        crimAge = x.getElementsByTagName('Age')[0].firstChild.data
        crimHeight = x.getElementsByTagName('Height')[0].firstChild.data
        print("\nCriminal Details:")
        print("\tName: ", crimName, "\n\tAge: ", crimAge, "\n\tHeight: ", crimHeight)


def getDateTime(crime):
    date = crime.getElementsByTagName("Date")
    time = crime.getElementsByTagName("Time")
    for x in date:
        day = x.getElementsByTagName('Day')[0].firstChild.data
        month = x.getElementsByTagName('Month')[0].firstChild.data
        year = x.getElementsByTagName('Year')[0].firstChild.data

    for x in time:
        hour = x.getElementsByTagName('Hour')[0].firstChild.data
        mins = x.getElementsByTagName('Minutes')[0].firstChild.data

    print("Crime took place on ",day,"/",month,"/",year," at ",hour,":",mins,".")


def getLocation(crime):
    location = crime.getElementsByTagName("Location")
    for x in location:
        streetNum = x.getElementsByTagName('StreetNum')[0].firstChild.data
        streetName = x.getElementsByTagName('StreetName')[0].firstChild.data
        county = x.getElementsByTagName('County')[0].firstChild.data
        postcode = x.getElementsByTagName('Postcode')[0].firstChild.data
        print("Crime took place at:")
        print("\t", streetNum, "", streetName)
        print("\t", county)
        print("\t", postcode)


def getVictim(crime):
    victim = crime.getElementsByTagName("Victim")
    for x in victim:
        victName = x.getElementsByTagName('Name')[0].firstChild.data
        victAge = x.getElementsByTagName('Age')[0].firstChild.data
        victHeight = x.getElementsByTagName('Height')[0].firstChild.data
        streetNum = x.getElementsByTagName('StreetNum')[0].firstChild.data
        streetName = x.getElementsByTagName('StreetName')[0].firstChild.data
        postcode = x.getElementsByTagName('Postcode')[0].firstChild.data
        print("\nVictim Details:")
        print("\tName: ", victName, "\n\tAge: ", victAge, "\n\tHeight: ", victHeight)
        print("\tHome address of Victim is:")
        print("\t\t", streetNum, "", streetName)
        print("\t\t", postcode)


def getWeapon(crime):
    weapon = crime.getElementsByTagName("Weapon")
    print("Weapons used where: ")
    for x in weapon:
        weap = crime.getElementsByTagName("Weapon")[0].firstChild.data
        print("\t", weap)


def getDrug(crime):
    drug = crime.getElementsByTagName("Drug")
    print("Drugs found on criminal: ")
    for x in drug:
        dru = x.getElementsByTagName("Substance")[0].firstChild.nodeValue
        amount = x.getElementsByTagName("Amount")[0].firstChild.nodeValue
        print("\t", amount, "g of ", dru)



def getStolenItems(crime):
    item = crime.getElementsByTagName("StolenItems")
    print("Stolen Items: ")
    for x in item:
        stolen = x.getElementsByTagName("Name")[0].firstChild.data
        value = x.getElementsByTagName("Value")[0].firstChild.data
        print("\tStolen item:", stolen, " Valued at:", value)


def getForced(crime):
    force = crime.getElementsByTagName("Forced")[0].firstChild.data
    print("Forced entry:", force)


def main():
    myDoc = parse('Crime.xml')
    report = myDoc.getElementsByTagName("Crime")[0]
    murder = report.getElementsByTagName("Murder")
    drugs = report.getElementsByTagName("Drugs")
    theft = report.getElementsByTagName("Theft")

    for murd in murder:
        print("\nMurder: ")
        getDateTime(murd)
        getCriminal(murd)
        getLocation(murd)
        getVictim(murd)
        getWeapon(murd)

    for dru in drugs:
        print("\nDrug crimes: ")
        getDateTime(dru)
        getCriminal(dru)
        getLocation(dru)
        getVictim(dru)
        getDrug(dru)

    for the in theft:
        print("\nTheft: ")
        getDateTime(the)
        getCriminal(the)
        getLocation(the)
        getVictim(the)
        getForced(the)
        getStolenItems(the)


if __name__ == '__main__':
    main()