from datetime import datetime
import pymongo
import dns.resolver

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ["8.8.8.8"]

myclient = pymongo.MongoClient(
    "mongodb+srv://test:test@cluster0.iczsyyp.mongodb.net/?retryWrites=true&w=majority"
)
mydb = myclient["inventory"]
mycol = mydb["inventory"]
clientsCollection = mydb["clients"]
jobNamesCollection = mydb["jobName"]
paperTypeCollection = mydb["paperTypes"]
paperSuppliersCollection = mydb["suppliers"]
printingSuppliersCollection = mydb["printingSuppliers"]
plateSuppliersCollection = mydb["plateSuppliers"]
punchSuppliersCollection = mydb["punchSuppliers"]
varnishSuppliersCollection = mydb["varnishSuppliers"]
laminationSuppliersCollection = mydb["laminationSuppliers"]
punchingSuppliersCollection = mydb["punchingSuppliers"]
pastingSuppliersCollection = mydb["pastingSuppliers"]
corrugationSuppliersCollection = mydb["corrugationSuppliers"]

def getAllJobWorks():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-01")
    allJobWork = list(mycol.find({"date": {"$gte": dt_string}}).sort("date", 1))
    return allJobWork

def clientNumbers():
    clients = mycol.find({}).sort("clientName", 1)
    dic = {}
    for row in clients:
        if row["clientName"] not in dic:
            dic[f'{row["clientName"]}'] = 1
        else:
            dic[f'{row["clientName"]}'] += 1
    ls = []
    for row in dic:
        ls.append([row, dic[row]])
    return ls

def jobNameNumbers():
    jobNames = mycol.find({}).sort("jobName", 1)
    dic = {}
    for row in jobNames:
        if row["jobName"] not in dic:
            dic[f'{row["jobName"]}'] = 1
        else:
            dic[f'{row["jobName"]}'] += 1
    ls = []
    for row in dic:
        ls.append([row, dic[row]])
    return ls

def getOnlyJob(jobName):
    onlyJob = list(mycol.find({"jobName": jobName}).sort("date", 1))
    return onlyJob

def getAllJobWork(
    startDate,
    endDate,
    clientName,
    jobName,
    paperSupplierName,
    paperType,
    printingSupplier,
    corrugationSupplier,
    plateSupplier,
    punchSupplier,
    varnishSupplier,
    laminationSupplier,
    punchingSupplier,
    pastingSupplier,
):

    myquery = {
        "clientName": clientName,
        "jobName": jobName,
        "paperSupplierName": paperSupplierName,
        "paperType": paperType,
        "printingSupplierName": printingSupplier,
        "corrugationSupplierName": corrugationSupplier,
        "plateSupplierName": plateSupplier,
        "punchSuppliers": punchSupplier,
        "varnishSuppliers": varnishSupplier,
        "laminationSuppliers": laminationSupplier,
        "punchingSuppliers": punchingSupplier,
        "pastingSuppliers": pastingSupplier,
    }

    print(myquery)

    if not startDate and not endDate:
        now = datetime.now()
        dt_string = now.strftime("%Y%m")
        print(dt_string)
        allJobWork = list(mycol.find(myquery).sort("date", 1))

    elif not endDate:
        myquery["date"] = {"$gte": startDate}
        allJobWork = list(mycol.find(myquery).sort("date", 1))

    elif not startDate:
        myquery["date"] = {"$lte": endDate}
        allJobWork = list(mycol.find(myquery).sort("date", 1))

    else:
        myquery["date"] = {"$lte": endDate, "$gte": startDate}
        allJobWork = list(mycol.find(myquery).sort("date", 1))

    return allJobWork

def getJobWork(jobId):
    myquery = {"JobId": f"{jobId}"}
    print(myquery)
    jobWork = mycol.find(myquery).collation({"locale": "en", "strength": 2})[0]
    return jobWork

def addJobWork(data):
    try:
        mycol.insert_one(data)
        return 1
    except:
        return 0

def updateJobWork(jobId, data):
    try:
        mycol.update_one({"JobId": jobId}, {"$set": data})
        return 1
    except:
        return 0

def deleteJobWork(jobId):
    try:
        mycol.delete_one({"JobId": jobId})
        return 1
    except:
        return 0

# Clients
def getAllClients():
    clients = clientsCollection.find({}).sort("name", 1)
    return clients

def getClient(name):
    client = clientsCollection.find_one({"name": name})
    return client

def addClientDb(
    clientName,
    mailingName,
    address,
    country,
    countryCode,
    state,
    city,
    pincode,
    mobile,
    email,
    website,
    gst,
):
    try:
        clientsCollection.insert_one(
            {
                "name": clientName,
                "mailingName": mailingName,
                "address": address,
                "country": country,
                "state": state,
                "city": city,
                "pincode": pincode,
                "mobile": mobile,
                "email": email,
                "webiste": website,
                "gst": gst,
            }
        )
        return 1
    except:
        return 0

def deleteClientDb(clientName):
    try:
        clientsCollection.delete_one({"name": clientName})
        return 1
    except:
        return 0

def editClientDb(clientName, data):
    try:
        clientsCollection.update_one(
            {"name": clientName},
            {
                "$set": {
                    "name": data["name"],
                    "mailingName": data["mailingName"],
                    "address": data["address"],
                    "country": data["country"],
                    "state": data["state"],
                    "city": data["city"],
                    "pincode": data["pincode"],
                    "mobile": data["mobile"],
                    "email": data["email"],
                    "webiste": data["website"],
                    "gst": data["gst"],
                }
            },
        )
        return 1
    except:
        return 0

# Paper Types
def getAllPaperType():
    paperTypes = paperTypeCollection.find({}).sort("name", 1)
    return paperTypes

def getpaperType(name):
    paperType = paperTypeCollection.find_one({"name": name})
    return paperType

def addPaperTypeDb(paperType):
    try:
        paperTypeCollection.insert_one({"name": paperType})
        return 1
    except:
        return 0

def deletePaperTypeDb(paperType):
    try:
        paperTypeCollection.delete_one({"name": paperType})
        return 1
    except:
        return 0

def editPaperTypeDb(paperType, data):
    try:
        paperTypeCollection.update_one({"name": paperType}, {"$set": {"name": data}})
        return 1
    except:
        return 0

# Job Names
def getAllJobNames():
    jobNames = jobNamesCollection.find({}).sort("name", 1)
    return jobNames

def getJob(name):
    jobName = jobNamesCollection.find_one({"name": name})
    return jobName

def addJobNamesDb(jobName):
    try:
        jobNamesCollection.insert_one({"name": jobName})
        return 1
    except:
        return 0

def deleteJobNameDb(jobName):
    try:
        jobNamesCollection.delete_one({"name": jobName})
        return 1
    except:
        return 0

def editJobNameDb(jobName, data):
    try:
        jobNamesCollection.update_one({"name": jobName}, {"$set": {"name": data}})
        return 1
    except:
        return 0

# Paper
def getAllPaperSuppliers():
    paperSuppliers = paperSuppliersCollection.find({}).sort("name", 1)
    return paperSuppliers

def getPaperSupplier(name):
    paperSupplier = paperSuppliersCollection.find_one({"name": name})
    return paperSupplier

def addPaperSupplierDb(
    paperSupplierName,
    mailingName,
    address,
    countryCode,
    country,
    state,
    city,
    pincode,
    mobile,
    email,
    website,
    gst,
):
    try:
        paperSuppliersCollection.insert_one(
            {
                "name": paperSupplierName,
                "mailingName": mailingName,
                "address": address,
                "country": country,
                "state": state,
                "city": city,
                "pincode": pincode,
                "mobile": mobile,
                "email": email,
                "webiste": website,
                "gst": gst,
            }
        )
        return 1
    except:
        return 0

def deletePaperSupplierDb(supplierName):
    try:
        paperSuppliersCollection.delete_one({"name": supplierName})
        return 1
    except:
        return 0

def editPaperSupplierDb(supplierName, data):
    try:
        paperSuppliersCollection.update_one(
            {"name": supplierName}, {"$set": {"name": data}}
        )
        return 1
    except:
        return 0

# Printing
def getAllPrintingSuppliers():
    printingSuppliers = printingSuppliersCollection.find({}).sort("name", 1)
    return printingSuppliers

def getPrintingSupplier(name):
    printingSupplier = printingSuppliersCollection.find_one({"name": name})
    return printingSupplier

def addPrintingSupplierDb(
    printingSupplierName,
    mailingName,
    address,
    countryCode,
    country,
    state,
    city,
    pincode,
    mobile,
    email,
    website,
    gst,
):
    try:
        printingSuppliersCollection.insert_one(
            {
                "name": printingSupplierName,
                "mailingName": mailingName,
                "address": address,
                "country": country,
                "state": state,
                "city": city,
                "pincode": pincode,
                "mobile": mobile,
                "email": email,
                "webiste": website,
                "gst": gst,
            }
        )
        return 1
    except:
        return 0

def deletePrintingSupplierDb(supplierName):
    try:
        printingSuppliersCollection.delete_one({"name": supplierName})
        return 1
    except:
        return 0

def editPrintingSupplierDb(supplierName, data):
    try:
        printingSuppliersCollection.update_one(
            {"name": supplierName}, {"$set": {"name": data}}
        )
        return 1
    except:
        return 0

# Corrugation
def getAllCorrugationSuppliers():
    corrugationSuppliers = corrugationSuppliersCollection.find({}).sort("name", 1)
    return corrugationSuppliers

def getCorrugationSupplier(name):
    corrugationSupplier = corrugationSuppliersCollection.find_one({"name": name})
    return corrugationSupplier

def addCorrugationSupplierDb(
    corrugationSupplierName,
    mailingName,
    address,
    countryCode,
    country,
    state,
    city,
    pincode,
    mobile,
    email,
    website,
    gst,
):
    try:
        corrugationSuppliersCollection.insert_one(
            {
                "name": corrugationSupplierName,
                "mailingName": mailingName,
                "address": address,
                "countryCode": countryCode,
                "country": country,
                "state": state,
                "city": city,
                "pincode": pincode,
                "mobile": mobile,
                "email": email,
                "webiste": website,
                "gst": gst,
            }
        )
        return 1
    except:
        return 0

def deleteCorrugationSupplierDb(supplierName):
    try:
        corrugationSuppliersCollection.delete_one({"name": supplierName})
        return 1
    except:
        return 0

def editCorrugationSupplierDb(supplierName, data):
    try:
        corrugationSuppliersCollection.update_one(
            {"name": supplierName}, {"$set": {"name": data}}
        )
        return 1
    except:
        return 0

def getAllPlateSuppliers():
    plateSuppliers = plateSuppliersCollection.find({}).sort("name", 1)
    return plateSuppliers

def getAllPunchSuppliers():
    punchSuppliers = punchSuppliersCollection.find({}).sort("name", 1)
    return punchSuppliers

def getAllVarnishSuppliers():
    varnishSuppliers = varnishSuppliersCollection.find({}).sort("name", 1)
    return varnishSuppliers

def getAlllaminationSuppliers():
    laminationSuppliers = laminationSuppliersCollection.find({}).sort("name", 1)
    return laminationSuppliers

def getAllPunchingSuppliers():
    punchingSuppliers = punchingSuppliersCollection.find({}).sort("name", 1)
    return punchingSuppliers

def getAllPastingSuppliers():
    pastingSuppliers = pastingSuppliersCollection.find({}).sort("name", 1)
    return pastingSuppliers

def getAllMasters():
    clients = getAllClients()
    paperTypes = getAllPaperType()
    jobNames = getAllJobNames()
    paperSuppliers = getAllPaperSuppliers()
    printingSuppliers = getAllPrintingSuppliers()
    plateSuppliers = getAllPlateSuppliers()
    punchSuppliers = getAllPunchSuppliers()
    varnishSuppliers = getAllVarnishSuppliers()
    laminationSuppliers = getAlllaminationSuppliers()
    punchingSuppliers = getAllPunchingSuppliers()
    pastingSuppliers = getAllPastingSuppliers()
    corrugationSuppliers = getAllCorrugationSuppliers()

    return (
        clients,
        paperTypes,
        jobNames,
        paperSuppliers,
        printingSuppliers,
        plateSuppliers,
        punchSuppliers,
        varnishSuppliers,
        laminationSuppliers,
        punchingSuppliers,
        pastingSuppliers,
        corrugationSuppliers
    )
