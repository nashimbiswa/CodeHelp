import wfdb
import pandas as pd
ds=['sel30','sel31','sel32','sel33','sel34','sel35','sel36','sel37','sel38','sel39','sel40','sel41','sel42','sel43','sel44','sel45', 'sel46','sel47','sel48','sel49','sel50','sel51','sel52','sel100','sel102', 'sel103','sel104','sel114','sel116','sel117','sel123','sel213','sel221','sel223','sel230','sel231','sel232','sel233','sel301','sel302','sel306','sel307','sel308','sel310','sel803','sel808','sel811','sel820','sel821','sel840','sel847','sel853','sel871',
     'sel872','sel873','sel883','sel891','sel14046','sel14157','sel14172','sel15814','sel16265','sel16272','sel16273',
     'sel16420','sel16483','sel16539','sel16773','sel16786','sel16795', 'sel17152','sel17453','sele0104','sele0107',
     'sele0110','sele0112','sele0114','sele0116','sele0121', 'sele0122','sele0124','sele0126','sele0129','sele0133',
     'sele0136','sele0166','sele0170','sele0203','sele0210','sele0211','sele0303','sele0405','sele0406','sele0409',
     'sele0411','sele0509','sele0603','sele0604', 'sele0607','sele0609','sele0612','sele0704']
for i in range(len(ds)):
    record = wfdb.rdsamp(ds[i])
    df = pd.DataFrame(record[0], columns=record[1]['sig_name'])
    df.to_csv((ds[i]+'.csv'), index=False)
