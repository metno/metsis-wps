# _*_ coding: utf-8 _*_

'''
conf = {
'main': {#'lang': 'en-UK',
         'language': 'en-USyyyy',
         'encoding': 'utf-8',
         'dataPath': '/var/www/tmp',
         'tmpPath': '/var/www/tmp',
         'version': '1.0.0',
         'mapserverAddress': 'http://localhost/cgi-bin/mapserv',
         'isSoap': 'false',
         'tmpUrl': 'http://localhost/tmp/',
         'serverAddress': 'http://localhost/zoo'
        },
'identification': {'keywords': 'WPS,GIS',
                   'abstract': 'WPS services for testing ZOO',
                   'fees': 'None',
                   'accessConstraints': 'none',
                   'title': 'testing services'
                  },
'lenv': {'status': '0',
         'soap': 'false',
         'cwd': '/usr/lib/cgi-bin',
         'sid': '24709'
        },
'env': {'DISPLAY': 'localhost:0'},
'provider': {'addressCountry': 'it',
             'positionName': 'Developer',
             'providerName': 'Name of provider',
             'addressAdministrativeArea': 'False',
             'phoneVoice': 'False',
             'addressCity': 'City',
             'providerSite': 'http://www.your.site',
             'addressPostalCode': '38122',
             'role': 'Developer',
             'addressDeliveryPoint': 'False',
             'phoneFacsimile': 'False',
             'addressElectronicMailAddress': 'your@email.com',
             'individualName': 'Your Name'
            }
}

inputs={
'variable_name': {'minOccurs': '1',
                  'DataType': 'string',
                  'value': 'this_is_the_value',
                  'maxOccurs': '1',
                  'inRequest': 'true'
                 }
}
outputs={
'result': {'DataType': 'string',
           'inRequest': 'true',
          }
}
'''

import zoo
import sys
sys.path.append("./ts")
import tsc

localConf = {
    'ekstra':{
    'tsFilesPath':'/var/www/html/files/ts/',
    'tsFilesURL':'http://157.249.176.137/files/ts/',
    }
}

def TimeSeries(conf,inputs,outputs):
   # outputs["Result"]["value"]="this server/"+inputs["fileName"]["value"]+"."+inputs["fileFormat"]["value"]
   # outputs["test"]["value"]=conf['provider']['addressCountry']
   # outputs["test"]["value"]=conf['provider']['providerName']

   url        = inputs["odurl"]["value"]
   xvar       = inputs["xvar"]["value"]
   yvar       = inputs["yvar"]["value"]
   everyNth   = int(inputs["everyNth"]["value"])
#   fileName   = '%s%s'  %  (localConf['ekstra']['tsFilesPath'],inputs["fileName"]["value"])
   fileName   = '%s%s'  %  (conf['ekstra']['tsFilesPath'],inputs["fileName"]["value"])
   fileFormat = inputs["fileFormat"]["value"]
#   outputFileURL = '%s%s.%s' % (localConf['ekstra']['tsFilesURL'],inputs["fileName"]["value"],inputs["fileFormat"]["value"])
   outputFileURL = '%s%s.%s' % (conf['ekstra']['tsFilesURL'],inputs["fileName"]["value"],inputs["fileFormat"]["value"])
   outputs["Result"]["value"]=outputFileURL


   X, Y, title, x, y = tsc.getPlotData(url,xvar,yvar)
   tsc.plot(X,Y,title,x,y,everyNth,fileName,fileFormat)
   # try:
   #   X, Y, title, x, y = tsc.getPlotData(url,xvar,yvar)
   #   tsc.plot(X,Y,title,x,y,10,fileName,fileFormat)
   # except:
   #     pass

   return zoo.SERVICE_SUCCEEDED
