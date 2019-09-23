import numpy as np
import netCDF4
import cftime

def get_fill_type(dt):
  return{
  'float32' : 'f4',
  'float64' : 'f8',
  '|S1'     : '\x00',
  'int8'    : 'i1',
  'int16'   : 'i2',
  'int32'   : 'i4',
  'int64'   : 'i8',
   }[dt]

def mask_v(v):
  v = np.ma.masked_where(v == netCDF4.default_fillvals[get_fill_type(str(v.dtype))], v)
  return v

def num2date(x,u):
    return netCDF4.num2date(x,units=u,calendar='Julian')

def j2iso(date_time_julian):
    return ('%s-%s-%s' % (str(date_time_julian.year).zfill(4),str(date_time_julian.month).zfill(2),str(date_time_julian.day).zfill(2)))

def ja2siso(date_time_julian_array):
    iso_date_list=[]
    for d in date_time_julian_array:
        iso_date_list.append(JtoSISO(d))
    return np.array(iso_date_list)

def getSISO(x,u):
    return j2iso(num2date(x,u))
