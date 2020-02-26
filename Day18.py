files = [str(x)+'.csv.gz' for x in range(2010,2011)]
from ftplib import FTP
from datetime import datetime

start = datetime.now()
ftp = FTP('ftp.ncdc.noaa.gov')
ftp.login()
ftp.cwd("pub/data/ghcn/daily/by_year/")


# Get All Files
files = [str(x)+'.csv.gz' for x in range(2010,2011)]

# Print out the files
for file in files:
	print("Downloading..." + file)
	ftp.retrbinary("RETR " + file ,open(file, 'wb').write)

ftp.close()

end = datetime.now()
diff = end - start
print('All files downloaded for ' + str(diff.seconds) + 's')