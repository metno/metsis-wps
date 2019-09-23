# _*_ coding: utf-8 _*_
import sys
import netCDF4
from collections import defaultdict
import tsc as tsc
import csv

testInput={
  'url'           :'http://thredds.met.no/thredds/dodsC/cryoclim/met.no/ci-sie-nh/ci-sie-nh_osisaf_monthly_mean_sie.nc',
  'xvar'          :'time',
  'yvar'          :'sea_ice_extent',
  'everyNth'      : 200,
  'fileName'      : '1q2w3e4r5t.csv'
}
commentChar = '#'

def getDataMatrix(ds,varSNList,everyNth):
    columns=[]
    varSNListWUnits=[]
    title=''
    try:
        title = ds.title
    except:
        pass


    if everyNth >= tsc.getVarBySN(ds,varSNList[0]).size:
        everyNth = int(1)
    for var in varSNList:
        if var == 'time':
            vf = tsc.getVarBySN(ds,var)
            try:
                varSNListWUnits.append('%s [%s (raw units)]' % (var,vf.units))
            except:
                try:
                    varSNListWUnits.append('%s []' % (var))
                except:
                    pass
            vf = netCDF4.num2date(vf[0:-1:everyNth],units=vf.units)
            for idx,item in enumerate(vf):
                vf[idx] = item.isoformat()
                vs = vf
        else:
            try:
                varSNListWUnits.append('%s [%s]' % (var,tsc.getVarBySN(ds,var).units))
            except:
                try:
                    varSNListWUnits.append('%s []' % (var))
                except:
                    pass
            vf=tsc.getVarBySN(ds,var)[0:-1:everyNth]
            vs=[str(repr(i)) for i in vf]
        columns.append(vs)
    varSNListWUnits[0] = commentChar + str(varSNListWUnits[0])
    return varSNListWUnits,columns,title

def writeDataFile(title,varSNListWUnits,dataMatrix,outputFileName):
    with open(outputFileName, "w") as ofile:
        wr = csv.writer(ofile)
        wr.writerow([commentChar+'Title: '+title.encode('utf-8')])
        wr.writerow([''])
        wr.writerow(varSNListWUnits)
        for row in zip(*dataMatrix):
            wr.writerow(row)
    ofile.close()


if __name__ == "__main__":
    url,everyNth,outputFileName,varSNList = sys.argv[1],int(sys.argv[2]),sys.argv[3],sys.argv[4:]
    ds=tsc.getDataset(url)
    varSNListWUnits,dataMatrix = getDataMatrix(ds,varSNList,everyNth)
    writeDataFile(varSNListWUnits,dataMatrix,outputFileName)
    # d=defaultdict(list)
    # for k, v in ((k.lstrip('-'), v) for k,v in (a.split('=') for a in sys.argv[1:])):
    #     d[k].append(v)
    # print(dict(d))
