import re

a = r"MSG(app_id='smart_traffic', dev_id='paxcounter', hardware_serial='00DF713134272A39', port=1, counter=89, payload_raw='BgA=', payload_fields=MSG(wifi=6), metadata=MSG(time='2019-11-23T13:00:20.584910115Z', frequency=867.1, modulation='LORA', data_rate='SF7BW125', airtime=46336000, coding_rate='4/5', gateways=[MSG(gtw_id='eui-7276ff002ef47006', timestamp=2178280547, time='2019-11-23T13:00:20.558274Z', channel=0, rssi=0, snr=9.8, rf_chain=0, latitude=48.776657, longitude=11.459713, altitude=400, location_source='registry')]))"
b = re.split(r'[\s\,\=\(\)]', a)
print(b[14])
print(b[23])