import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():

    scdb = []
    try:
        fH = open(dbfilename, 'rb')
        scdb = pickle.load(fH)
    except FileNotFoundError:
        print("New DB:", dbfilename)
        return []
    except:
        print("Empty DB:", dbfilename)
    else:
        print("Open DB:", dbfilename)

    fH.close()
    return scdb

def writeScoreDB(scdb):
    fH = open(dbfilename,"wb")
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
    while(True):
        inputstr = (input("ScoreDB> "))
        if inputstr == "" : continue
        parse=inputstr.split(" ")

        command = parse[0]

        if command == 'add':
            try:
                if len(parse)<5:
                    record={"Name": parse[1],"Age": int(parse[2]),"Score": int(parse[3])}
                    scdb +=[record]
                else:
                    print("Wrong input\nPlease enter in order\nEnter <add> <Name> <Age> <Score>")
            except IndexError:
                print("Wrong input\nPlease enter in order\nEnter <add> <Name> <Age> <Score>")
            except ValueError:
                print("Wrong input\nPlease enter in order\nEnter <add> <Name> <Age> <Score>")

        elif command=='del':
            try:
                if len(parse)<3:
                    for person in reversed(scdb):
                        if person['Name']==parse[1]:
                            scdb.remove(person)
                else:
                    print("Wrong input\nPlease enter in order\nEnter <del> <Name>")
            except IndexError:
                print("Wrong input\nEnter <del> <Name>")

        elif command == 'show':
            try:
                sortKey='Name' if len(parse)==1 else parse[1]
                showScoreDB(scdb,sortKey)
            except KeyError:
                print("Wrong input\nPlease enter show only")

        elif command == 'find':
            try:
                if len(parse)<2:
                    for person in scdb:
                        if person['Name']==parse[1]:
                            for k, v in person.items():
                                print("{}:{}".format(k,v),)
                            print('\n')
                else:
                    print("Wrong input\nPlease enter in order\nEnter <find> <Name>")
            except IndexError:
                print("Wrong input\nPlease enter in order\nEnter <find> <Name>")

        elif command == 'inc':
            try:
                if len(parse)<4:
                    for person in scdb:
                        if person['Name']==parse[1]:
                            try:
                                person['Score']+=int(parse[2])
                            except ValueError:
                                print("Enter Score")
                else:
                    print("Wrong input\nPlease enter in order\nEnter <inc> <Name> <Inc score>")
            except IndexError:
                print("Wrong input\nPlease enter in order\nEnter <inc> <Name> <Inc score>")

        elif command == 'quit':
            break

        else:
            print("Invalid command :"+command)

def showScoreDB(scdb,keyName):
    for p in sorted(scdb, key=lambda person: person[keyName]):
        for attr in sorted(p):
            print("{}={}".format(attr,p[attr]),end=' ')
        print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)