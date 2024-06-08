from flask import render_template, redirect, url_for, request
from web import app
from web.forms import *
from datetime import datetime

# Dashboard
@app.route('/')
def dashboard():
    clients = clientNumbers()
    jobNames = jobNameNumbers()
    return render_template('dashboard.html', clients=clients, jobNames=jobNames)

# Job Work
@app.route('/createJobCard', methods=['POST', 'GET'])
def createJobCard():
    if request.method == 'GET':
        now = datetime.now()
        dt_string = now.strftime("%Y%m%d%H%M%S")
        clients, paperTypes, jobNames, paperSuppliers, printingSuppliers, plateSuppliers, punchSuppliers, varnishSuppliers, laminationSuppliers, punchingSuppliers, pastingSuppliers, corrugationSuppliers = getAllMasters()

        return render_template('jobWorkCreate.html', id=dt_string, clientName=clients, paperTypes=paperTypes, jobNames=jobNames, paperSuppliers=paperSuppliers, printingSuppliers=printingSuppliers, corrugationSuppliers=corrugationSuppliers,
                               plateSuppliers=plateSuppliers, punchSuppliers=punchSuppliers, varnishSuppliers=varnishSuppliers, laminationSuppliers=laminationSuppliers, punchingSuppliers=punchingSuppliers, pastingSuppliers=pastingSuppliers)

    if request.method == 'POST':
        data = extractData(request)

        try :
            addJobWork(data)
            return redirect(url_for('dashboard'))
        except :
            return redirect(url_for("errorPage"))

@app.route('/duplicateJob', methods=['POST', 'GET'])
def duplicateJobCard():
    if request.method == 'GET':
        jobId = request.args.get("jobid")
        jobWork = getJobWork(jobId)
        now = datetime.now()
        dt_string = now.strftime("%Y%m%d%H%M%S")
        clients, paperTypes, jobNames, paperSuppliers, printingSuppliers, plateSuppliers, punchSuppliers, varnishSuppliers, laminationSuppliers, punchingSuppliers, pastingSuppliers, corrugationSuppliers = getAllMasters()
        jobDate = now.strftime("%Y-%m-%d")
        return render_template('duplicateJob.html', jobId=dt_string, jobDate=jobDate, job=jobWork, clients=clients, paperTypes=paperTypes, jobNames=jobNames, paperSuppliers=paperSuppliers, printingSuppliers=printingSuppliers, corrugationSuppliers=corrugationSuppliers,
                               plateSuppliers=plateSuppliers, punchSuppliers=punchSuppliers, varnishSuppliers=varnishSuppliers, laminationSuppliers=laminationSuppliers, punchingSuppliers=punchingSuppliers, pastingSuppliers=pastingSuppliers)


@app.route('/editJob', methods=['GET', 'POST'])
def editJobCard():

    if request.method == 'POST':
        try :
            data = extractData(request)
            updateJobWork(data['JobId'], data)
            return redirect(url_for('generateReport'))
        except :
            return redirect(url_for("errorPage"))

    if request.method == 'GET':
        jobId = request.args.get("jobid")
        jobWork = getJobWork(jobId)

        clients, paperTypes, jobNames, paperSuppliers, printingSuppliers, plateSuppliers, punchSuppliers, varnishSuppliers, laminationSuppliers, punchingSuppliers, pastingSuppliers, corrugationSuppliers = getAllMasters()

        return render_template('editJob.html', job=jobWork, clients=clients, paperTypes=paperTypes, jobNames=jobNames, paperSuppliers=paperSuppliers, printingSuppliers=printingSuppliers, corrugationSuppliers=corrugationSuppliers,
                               plateSuppliers=plateSuppliers, punchSuppliers=punchSuppliers, varnishSuppliers=varnishSuppliers, laminationSuppliers=laminationSuppliers, punchingSuppliers=punchingSuppliers, pastingSuppliers=pastingSuppliers)

@app.route('/delete')
def deleteJobCard():
    jobId = request.args.get("jobid")
    deleteJobWork(jobId)
    return redirect(url_for('generateReport'))

# Individual Job
@app.route('/onlyJob')
def onlyJob():
    job = request.args.get("job")
    data = getOnlyJob(job)
    return render_template('job_report.html', jobName=job, jobWorks=data)

# Master Pages
@app.route('/client_master')
def clientMaster():
    clients = getAllClients()
    return render_template('masters/client_master.html', clients=clients)

@app.route('/paper_types_master')
def paperTypeMaster():
    paperTypes = getAllPaperType()
    return render_template('masters/paper_types_master.html', paperTypes=paperTypes)

@app.route('/job_master')
def jobMaster():
    jobNames = getAllJobNames()
    return render_template('masters/job_master.html', jobNames=jobNames)

@app.route('/paper_suppliers_master')
def paperSupplierMaster():
    paperSuppliers = getAllPaperSuppliers()
    return render_template('masters/paper_suppliers_master.html', paperSuppliers=paperSuppliers)

@app.route('/printing_supplier_master')
def printingSupplierMaster():
    printingSuppliers = getAllPrintingSuppliers()
    return render_template('masters/printing_supplier_master.html', printingSuppliers=printingSuppliers)

@app.route('/corrugation_supplier_master')
def corrugationSupplierMaster():
    corrugationSuppliers = getAllCorrugationSuppliers()
    return render_template('masters/corrugation_supplier_master.html', corrugationSuppliers=corrugationSuppliers)

# Add Masters
@app.route('/addclientName', methods=['POST'])
def addClient():

    arg = {}
    for k, v in request.form.items():
        arg[k] = v

    try:
        addClientDb(**{k: v for k, v in arg.items()})
        return redirect(url_for('clientMaster'))
    except :
        return redirect(url_for("errorPage"))

@app.route('/addpaperType', methods=['POST'])
def addPapertype():
    paperType = request.form['paperType']
    try :
        addPaperTypeDb(paperType)
        return redirect(url_for('paperTypeMaster'))
    except :
            return redirect(url_for("errorPage"))

@app.route('/addjobName', methods=['POST'])
def addJobNames():
    jobNames = request.form['jobName']
    try :
        addJobNamesDb(jobNames)
        return redirect(url_for('jobMaster'))
    except :
        return redirect(url_for("errorPage"))

@app.route('/addpaperSupplierName', methods=['POST'])
def addPaperSupplier():

    arg = {}
    for k, v in request.form.items():
        arg[k] = v

    try :
        addPaperSupplierDb(**{k: v for k, v in arg.items()})
        return redirect(url_for('paperSupplierMaster'))
    except :
        return redirect(url_for("errorPage"))

@app.route('/addprintingSupplierName', methods=['POST'])
def addPrintingSupplier():

    arg = {}
    for k, v in request.form.items():
        arg[k] = v

    try : 
        addPrintingSupplierDb(**{k: v for k, v in arg.items()})
        return redirect(url_for('printingSupplierMaster'))
    except :
        return redirect(url_for("errorPage"))

@app.route('/addcorrugationSupplierName', methods=['POST'])
def addCorrugationSupplier():

    arg = {}
    for k, v in request.form.items():
        arg[k] = v

    try: 
        addCorrugationSupplierDb(**{k: v for k, v in arg.items()})
        return redirect(url_for('corrugationSupplierMaster'))
    except:
        return redirect(url_for("errorPage"))

# Delete Master
@app.route('/deletefield')
def deleteField():
    field = request.args.get("field")
    name = request.args.get("row")

    if field == 'clientName':
        deleteClientDb(name)
        return redirect(url_for('clientMaster'))
    elif field == 'paperTypeName':
        deletePaperTypeDb(name)
        return redirect(url_for('paperTypeMaster'))
    elif field == 'jobName':
        deleteJobNameDb(name)
        return redirect(url_for('jobMaster'))
    elif field == 'paperSupplierName':
        deletePaperSupplierDb(name)
        return redirect(url_for('paperSupplierMaster'))
    elif field == 'printingSupplierName':
        deletePrintingSupplierDb(name)
        return redirect(url_for('printingSupplierMaster'))
    elif field == 'corrugationSupplierName':
        deleteCorrugationSupplierDb(name)
        return redirect(url_for('corrugationSupplierMaster'))

    return redirect(url_for("errorPage"))

# Edit Master
@app.route('/editfield', methods=['GET', 'POST'])
def editField():
    field = request.args.get("field")
    name = request.args.get("row")

    if request.method == 'GET':
        if field == 'clientName':
            data = getClient(name)
            return render_template('editFieldInput.html',  field=field, data=data)
        elif field == 'paperType':
            data = getpaperType(name)
            return render_template('editFieldInput.html',  field=field, data=data)
        elif field == 'jobName':
            data = getJob(name)
            return render_template('editFieldInput.html',  field=field, data=data)
        elif field == 'paperSupplierName':
            data = getPaperSupplier(name)
            return render_template('editFieldInput.html',  field=field, data=data)
        elif field == 'printingSupplierName':
            data = getPrintingSupplier(name)
            return render_template('editFieldInput.html',  field=field, data=data)
        elif field == 'corrugationSupplierName':
            data = getCorrugationSupplier(name)
            return render_template('editFieldInput.html',  field=field, data=data)

        return redirect(url_for("errorPage"))

    if request.method == 'POST':
        data = request.form
        if field == 'clientName':
            editClientDb(name, data)
            return redirect(url_for('clientMaster'))
        elif field == 'paperType':
            editPaperTypeDb(name, data)
            return redirect(url_for('paperTypeMaster'))
        elif field == 'jobName':
            editJobNameDb(name, data)
            return redirect(url_for('jobMaster'))
        elif field == 'paperSupplierName':
            editPaperSupplierDb(name, data)
            return redirect(url_for('paperSupplierMaster'))
        elif field == 'printingSupplierName':
            editPrintingSupplierDb(name, data)
            return redirect(url_for('printingSupplierMaster'))
        elif field == 'corrugationSupplierName':
            editCorrugationSupplierDb(name, data)
            return redirect(url_for('corrugationSupplierMaster'))

        return redirect(url_for('errorPage'))

# Reports
@app.route('/generateReport', methods=['GET', 'POST'])
def generateReport():
    clients, paperTypes, jobNames, paperSuppliers, printingSuppliers, plateSuppliers, punchSuppliers, varnishSuppliers, laminationSuppliers, punchingSuppliers, pastingSuppliers, corrugationSuppliers = getAllMasters()

    if request.method == 'GET':
        jobWorks = getAllJobWorks()
        return render_template('report_page.html', jobWorks=jobWorks, paperSuppliers=paperSuppliers, clientName=clients, jobName=jobNames,
                               paperTypes=paperTypes, printingSuppliers=printingSuppliers, plateSuppliers=plateSuppliers, punchSuppliers=punchSuppliers,
                               varnishSuppliers=varnishSuppliers, laminationSuppliers=laminationSuppliers, punchingSuppliers=punchingSuppliers,
                               pastingSuppliers=pastingSuppliers, corrugationSuppliers=corrugationSuppliers)

    if request.method == 'POST':
        default = {'$exists': 1}

        startDate = request.form['startDate']
        endDate = request.form['endDate']

        arg = {}

        for k, v in request.form.items():
            if k == 'startDate' or k == 'endDate':
                continue
            if v != "null":
                arg[k] = v
            else:
                arg[k] = default

        jobWorks = getAllJobWork(
            startDate, endDate, **{k: v for k, v in arg.items()})

        return render_template('report_page.html', jobWorks=jobWorks, paperSuppliers=paperSuppliers, clientName=clients, jobName=jobNames,
                               paperTypes=paperTypes, printingSuppliers=printingSuppliers, plateSuppliers=plateSuppliers, punchSuppliers=punchSuppliers,
                               varnishSuppliers=varnishSuppliers, laminationSuppliers=laminationSuppliers, punchingSuppliers=punchingSuppliers,
                               pastingSuppliers=pastingSuppliers, corrugationSuppliers=corrugationSuppliers)

@app.route('/job')
def showJob():
    jobId = request.args.get("jobid")
    jobWork = getJobWork(jobId)
    return render_template('job_card.html', job=jobWork)

# Error
@app.route('/error')
def errorPage():
    return render_template('error_page.html')
