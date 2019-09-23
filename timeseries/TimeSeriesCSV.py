# _*_ coding: utf-8 _*_

import zoo
import sys
sys.path.append("./ts")
import tsc
import csvc

localConf = {
    'ekstra':{
    'tsFilesPath':'/var/www/html/files/ts/',
    'tsFilesURL':'http://adcwps.met.no/files/ts/',
    }
}

def TimeSeriesCSV(conf,inputs,outputs):
   # outputs["Result"]["value"]="this server/"+inputs["fileName"]["value"]+"."+inputs["fileFormat"]["value"]
   # outputs["test"]["value"]=conf['provider']['addressCountry']
   # outputs["test"]["value"]=conf['provider']['providerName']

   url        = inputs["odurl"]["value"]
   varSNList     = inputs["varSNList"]["value"]
#   yvar       = inputs["yvar"]["value"]
   everyNth   = int(inputs["everyNth"]["value"])
#   fileName   = '%s%s'  %  (localConf['ekstra']['tsFilesPath'],inputs["fileName"]["value"])
   fileName   = '%s%s'  %  (conf['ekstra']['tsFilesPath'],inputs["fileName"]["value"])
   fileFormat = inputs["fileFormat"]["value"]
   fileName = '%s.%s' % (fileName,fileFormat)
#   outputFileURL = '%s%s.%s' % (localConf['ekstra']['tsFilesURL'],inputs["fileName"]["value"],inputs["fileFormat"]["value"])
   outputFileURL = '%s%s.%s' % (conf['ekstra']['tsFilesURL'],inputs["fileName"]["value"],inputs["fileFormat"]["value"])
   outputs["Result"]["value"]=outputFileURL

   outputs["Debugtest"]["value"]=varSNList
   outputs["CSVOutputFileURL"]["value"]=outputFileURL
   ds=tsc.getDataset(url)
   varSNList = varSNList.split()
   varsWU,dataMatrix,title = csvc.getDataMatrix(ds,varSNList,everyNth)
   csvc.writeDataFile(title,varsWU,dataMatrix,fileName)

   return zoo.SERVICE_SUCCEEDED
