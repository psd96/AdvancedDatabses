from xml.dom.minidom import *

myDoc = parse('C:\\Users\\Happy\\Desktop\\test.xml')

report = myDoc.getElementsByTagName("Report")[0]

murder = report.getElementsByTagName("Murder")
graffiti = report.getElementsByTagName("Graffiti")
theft = report.getElementsByTagName("Theft")

print("Welcome to the report system, Crimes will be reported now")

for murd in murder:
    print("Murder: ")
    casename = murd.getElementsByTagName("Case_Name")[0].firstChild.data
    victimname = murd.getElementsByTagName("Victim_Name")[0].firstChild.data
    victimheight = murd.getElementsByTagName("Victim_Height")[0].firstChild.data
    victimweight = murd.getElementsByTagName("Victim_Weight")[0].firstChild.data
    offendername = murd.getElementsByTagName("Offender_Name")[0].firstChild.data
    offenderheight = murd.getElementsByTagName("Offender_Height")[0].firstChild.data
    offenderweight = murd.getElementsByTagName("Offender_Weight")[0].firstChild.data
    time = murd.getElementsByTagName("time")[0].firstChild.data
    weapon = murd.getElementsByTagName("Weapon")[0].firstChild.data
    weaponcolor = murd.getElementsByTagName("Weapon_color")[0].firstChild.data
    weaponsize = murd.getElementsByTagName("Weapon_size")[0].firstChild.data
    location = murd.getElementsByTagName("Location")[0].firstChild.data
    postcode = murd.getElementsByTagName("Postcode")[0].firstChild.data
    streetname = murd.getElementsByTagName("Street_Name")[0].firstChild.data
    county = murd.getElementsByTagName("County_Name")[0].firstChild.data
    witness = murd.getElementsByTagName("Witness")

    print("Case name: ", casename, "\nVictim Name: ", victimname, "\nVictim Weight: ", victimheight,
          "\nVictim Weight: ", victimweight, "\nOffender Name: ", offendername, "\nOffender Height: ", offenderheight,
          "\nOffender Weight: ", offenderweight, "\nTime: ", time, "\nWeapon: ", weapon, "\nWeapon Color: ",
          weaponcolor, "\nWeaoon Size: ", weaponsize)
    print("Location: ", location, "\nPostcode: ", postcode, "\nSteet Name: ", streetname, "\nCounty: ", county)

    for x in witness:
        witnessname = x.getElementsByTagName("Witness_Name")[0].firstChild.data
        witneslocation = x.getElementsByTagName("Witness_Location")[0].firstChild.data
        witnespostcode = x.getElementsByTagName("Witness_Postcode")[0].firstChild.data
        witnesstreetname = x.getElementsByTagName("Witness_Street_Name")[0].firstChild.data
        witnescounty = x.getElementsByTagName("Witness_County_Name")[0].firstChild.data
        print("Witness Name: ", witnessname, "\nWitness Location: ", witneslocation, "\nWitness Postcode: ",
              witnespostcode, "\nWitness Steet Name: ", witnesstreetname, "\nWitness County: ", witnescounty)

for graff in graffiti:
    print("Graffiti: ")
    printed = graff.getElementsByTagName("Printed")[0].firstChild.data
    found = county = graff.getElementsByTagName("Found")[0].firstChild.data
    importance = graff.getElementsByTagName("Importance")[0].firstChild.data
    residents_affected = graff.getElementsByTagName("Residents_affected")[0].firstChild.data
    easilyacc = graff.getElementsByTagName("Easilyacc")[0].firstChild.data
    offender = graff.getElementsByTagName("Offender")[0].firstChild.data
    previous = county = graff.getElementsByTagName("Previous_Conviction")[0].firstChild.data
    location = graff.getElementsByTagName("Location")[0].firstChild.data
    postcode = graff.getElementsByTagName("Postcode")[0].firstChild.data
    streetname = graff.getElementsByTagName("Street_Name")[0].firstChild.data
    county = graff.getElementsByTagName("County_Name")[0].firstChild.data

    print("What's Printed: ", printed, "\nWhen it was found: ", found, "\nHow important is it to remove: ", importance,
          "\nResidents affected: ", residents_affected, "\nHow easy is it to access: ", easilyacc,
          "\nWho is the offender: ", offender, "\nHave the been reported before: ", previous)
    print("Location: ", location, "\nPostcode: ", postcode, "\nSteet Name: ", streetname, "\nCounty: ", county)

    for x in graff:
        witnessname = x.getElementsByTagName("Witness_Name")[0].firstChild.data
        witneslocation = x.getElementsByTagName("Witness_Location")[0].firstChild.data
        witnespostcode = x.getElementsByTagName("Witness_Postcode")[0].firstChild.data
        witnesstreetname = x.getElementsByTagName("Witness_Street_Name")[0].firstChild.data
        witnescounty = x.getElementsByTagName("Witness_County_Name")[0].firstChild.data
        print("Witness Name: ", witnessname, "\nWitness Location: ", witneslocation, "\nWitness Postcode: ",
              witnespostcode, "\nWitness Steet Name: ", witnesstreetname, "\nWitness County: ", witnescounty)

for thef in theft:
    print("Theft: ")
    victimname = thef.getElementsByTagName("Victim_Name")[0].firstChild.data
    offendername = thef.getElementsByTagName("Offender_Name")[0].firstChild.data
    offenderheight = thef.getElementsByTagName("Offender_Height")[0].firstChild.data
    offenderweight = thef.getElementsByTagName("Offender_Weight")[0].firstChild.data
    items = thef.getElementsByTagName("Items")[0].firstChild.data
    value = thef.getElementsByTagName("Value")[0].firstChild.data
    room = thef.getElementsByTagName("Room")[0].firstChild.data
    insurance = thef.getElementsByTagName("Insurance")[0].firstChild.data
    safety = thef.getElementsByTagName("Safety")[0].firstChild.data

    location = thef.getElementsByTagName("Location")[0].firstChild.data
    postcode = thef.getElementsByTagName("Postcode")[0].firstChild.data
    streetname = thef.getElementsByTagName("Street_Name")[0].firstChild.data
    county = thef.getElementsByTagName("County_Name")[0].firstChild.data

    print("Victim Name: ", victimname, "\nOffender Name: ", offendername, "\nOffender Height: ", "\nOffender Height: ",
          offenderheight, "\nOffender Weight: ", offenderweight, "\nItems taken: ", items, "\nValue of items: ", value,
          "\nRooms where taken: ", room, "\nDo they have insurance: ", insurance, "\nDid they have safety features: ",
          safety)
    print("Location: ", location, "\nPostcode: ", postcode, "\nSteet Name: ", streetname, "\nCounty: ", county)

    for x in thef:
        witnessname = x.getElementsByTagName("Witness_Name")[0].firstChild.data
        witneslocation = x.getElementsByTagName("Witness_Location")[0].firstChild.data
        witnespostcode = x.getElementsByTagName("Witness_Postcode")[0].firstChild.data
        witnesstreetname = x.getElementsByTagName("Witness_Street_Name")[0].firstChild.data
        witnescounty = x.getElementsByTagName("Witness_County_Name")[0].firstChild.data
        print("Witness Name: ", witnessname, "\nWitness Location: ", witneslocation, "\nWitness Postcode: ",
              witnespostcode, "\nWitness Steet Name: ", witnesstreetname, "\nWitness County: ", witnescounty)
