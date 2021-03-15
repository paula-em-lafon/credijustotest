from celery import shared_task
from .models import BdmExch, DofExch, FixerExch
from .helpers.bdmcrawler import parse_bdm
from .helpers.dofcrawler import parse_dof
from .helpers.fixercrawler import parse_fixer

@shared_task()
def read_bdm():
    attempts=0
    while attempts <3:
        try:
            result = parse_bdm()
            BdmExch.objects.create(time=result["date"],exch=result["exc"])
            return
        except:
            attempts += 1
            print("Parsing error on read_bdm")
    print("--------------- Parsing error on read_bdm -----------")
    return    

@shared_task()
def read_dof():
    attempts=0
    while attempts < 3:
        try:
            result = parse_dof()
            DofExch.objects.create(time=result["date"],exch=result["exc"])
            return
        except:
            attempts += 1
            print("Parsing error on read_dof")

    print("--------------- Parsing error on read_dof -----------")
    return

@shared_task()
def read_fixer():
    attempts=0
    while attempts < 3:
        try:
            result = parse_bdm()
            FixerExch.objects.create(time=result["date"],exch=result["exc"])
            return
        except:
            attempts += 1
            print("Parsing error on read_fixer")
    print("--------------- Parsing error on read_fixer -----------")
    return




