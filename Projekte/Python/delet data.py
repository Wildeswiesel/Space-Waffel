import os

ordner_pfad = 'path/to/ordner'

video_dateiendungen = ['hier die dateiendungen']


for datei in os.listdir(ordner_pfad):
    datei_pfad = os.path.join(ordner_pfad, datei)
    

    if not any(datei.endswith(endung) for endung in video_dateiendungen):
        os.remove(datei_pfad)
        print(f'Datei gelöscht: {datei_pfad}')

print('Fertig!')
