#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction

cities = []
coords = {}
roads = []
km = {}

for _line in """A Coruña:-334.340:-296.380
Aara:51.100:357.700
Abrantes:-346.020:70.080
Adanero:-71.540:-48.180
Aguilar de Campoó:-35.040:-232.140
Alacant:245.280:201.480
Albacete:137.240:132.860
Albocàsser:289.080:2.920
Albufeira:-360.620:297.840
Alcala de Henarés:23.360:-8.760
Alcance:183.960:108.040
Alcantarilla:188.340:236.520
Alcaraz:87.600:173.740
Alcañices:-191.260:-131.400
Alcañiz:261.340:-65.700
Alcolea del Pinar:87.600:-61.320
Alcoy:246.740:167.900
Almería:91.980:348.940
Alfaro:144.540:-175.200
Algeciras:-147.460:416.100
Almadrones:59.860:-51.100
Almadén:-89.060:154.760
Almansa:191.260:151.840
Almazán:93.440:-102.200
Almonte:-224.840:305.140
Almuñecar:-4.380:359.160
Alzira:242.360:119.720
Amposta:319.740:-33.580
Andújar:-32.120:230.680
Ansiao:-348.940:29.200
Antequera:-70.080:329.960
Aranda de Duero:0.000:-124.100
Aranjuez:8.760:33.580
Arenas de San Pedro:-96.360:16.060
Arganda del Rey:21.900:14.600
Armiñón:62.780:-229.220
Arzúa:-321.200:-252.580
Arévalo:-75.920:-67.160
Astorga:-176.660:-213.160
Aveiro:-363.540:-45.260
Avilés:-153.300:-306.600
Ayamonte:-293.460:300.760
Ayora:186.880:128.480
Baamonde:-289.080:-271.560
Badajoz:-251.120:147.460
Baena:-45.260:280.320
Bailén:-5.840:227.760
Barbastro:271.560:-166.440
Barcelona:433.620:-105.120
Barreiros:-254.040:-303.680
Basauri:64.240:-278.860
Baza:64.240:290.540
Becerrea:-252.580:-236.520
Beja:-327.040:216.080
Belmonte:70.080:83.220
Benabarre:303.680:-183.960
Benavente:-143.080:-157.680
Benicarló:305.140:-1.460
Benicàssim:289.080:23.360
Benidorm:284.700:169.360
Betanzos:-313.900:-284.700
Bicorp:210.240:121.180
Bilbao:56.940:-280.320
Boltaña:277.400:-211.700
Borriol:280.320:21.900
Braga:-343.100:-128.480
Bragança:-224.840:-146.000
Burgo de Osma:55.480:-108.040
Burgos:5.840:-192.720
Béjar:-148.920:-4.380
Calatayud:144.540:-94.900
Caldas da Rainha:-410.260:77.380
Callosa del Segura:214.620:217.540
Campillos:-97.820:328.500
Campomanes:-146.000:-259.880
Cangas de Onís:-93.440:-280.320
Carballo:-353.320:-284.700
Carboneras:138.700:325.580
Carregado:-402.960:115.340
Cartagena:208.780:274.480
Casa de Juan Gil:167.900:122.640
Casas Ibáñez:166.440:103.660
Cascais:-433.620:143.080
Caspe:267.180:-81.760
Castelldefels:417.560:-94.900
Castelló de la Plana:283.240:27.740
Castelo Branco:-284.700:42.340
Castro Urdiales:39.420:-286.160
Caudete:175.200:77.380
Cañete:159.140:35.040
Cerceda:17.520:-240.900
Cervera:363.540:-132.860
Chantada:-299.300:-224.840
Chiclana de la Frontera:-192.720:394.200
Chiva:219.000:83.220
Cieza:169.360:205.860
Cinctorres:267.180:-14.600
Cistierna:-99.280:-239.440
Ciudad Real:-13.140:135.780
Cocentaina:248.200:160.600
Coimbra:-346.020:-5.840
Collado Villalba:-23.360:-17.520
Coruche:-365.000:124.100
Covilha:-286.160:0.000
Cudillero:-164.980:-308.060
Cuenca:110.960:30.660
Cullera:261.340:119.720
Cáceres:-204.400:81.760
Cádiz:-208.780:379.600
Córdoba:-87.600:235.060
Daimiel:10.220:131.400
Daroca:169.360:-67.160
Donostia:124.100:-278.860
Dos Hermanas:-172.280:300.760
Durango:80.300:-268.640
Durcal:2.920:332.880
El Barco de Ávila:-138.700:8.760
El Burgo del Ebro:204.400:-108.040
Elda:221.920:183.960
Elvas:-268.640:132.860
Elx:230.680:202.940
Espiel:-108.040:210.240
Espinho:-357.700:-75.920
Estepa:-96.360:306.600
Estepona:-116.800:385.440
Estremoz:-305.140:138.700
Faro:-338.720:313.900
Feira:-353.320:-65.700
Ferrol:-315.360:-310.980
Figueira da Foz:-381.060:4.380
Figueres:489.100:-192.720
Fraga:296.380:-116.800
Fuengirola:-78.840:379.600
Gaia:-357.700:-84.680
Gandia:265.720:140.160
Gibraleón:-261.340:286.160
Gijón:-138.700:-305.140
Gimileo:71.540:-207.320
Girona:480.340:-162.060
Grado:-160.600:-292.000
Granada:2.920:312.440
Grao de Sagunt:262.800:71.540
Graus:287.620:-191.260
Grândula:-376.680:194.180
Guadalajara:37.960:-36.500
Guadiaro:-138.700:398.580
Guarda:-268.640:-26.280
Guardamar del Segura:235.060:221.920
Guntín:-292.000:-245.280
Hellín:156.220:186.880
Herrera del Duque:-108.040:116.800
Honrubia:106.580:77.380
Huelva:-255.500:299.300
Huesca:242.360:-170.820
Híjar:239.440:-78.840
Ibi:237.980:169.360
Igualada:398.580:-122.640
Izurzun:132.860:-239.440
Jabugo:-236.520:239.440
Jaca:224.840:-219.000
Jaén:-11.680:255.500
Jerez de la Frontera:-195.640:356.240
L'Alcora:270.100:17.520
L'Hospitalet de l'Infant:343.100:-62.780
La Albuera:-236.520:164.980
La Bañeza:-162.060:-188.340
La Espina:-182.500:-294.920
La Jonquera:484.720:-204.400
La Línea de la Concepción:-137.240:413.180
La Magdalena:-154.760:-237.980
La Roda:113.880:118.260
La Seu d'Urgell:379.600:-194.180
La Unión:217.540:270.100
Lagos:-397.120:296.380
Lalín:-318.280:-233.600
Laredo:21.900:-289.080
Leiria:-388.360:42.340
Lepe:-284.700:303.680
Lerma:5.840:-160.600
Les Borges Blanques:346.020:-121.180
León:-132.860:-226.300
Linares:10.220:221.920
Liria:227.760:67.160
Lisboa:-416.100:138.700
Llanes:-70.080:-290.540
Lleida:329.960:-131.400
Llerena:-176.660:202.940
Llivia:410.260:-210.240
Logroño:91.980:-200.020
Loja:-36.500:312.440
Lorca:162.060:264.260
Los Alcázares:221.920:256.960
Los Gallardos:135.780:309.520
Losa del Obispo:202.940:58.400
Luarca:-191.260:-308.060
Lucena:-61.320:292.000
Lugo:-281.780:-254.040
Macedo de Cavaleiros:-239.440:-125.560
Madrid:0.000:0.000
Madridejos:16.060:91.980
Manresa:408.800:-153.300
Mansilla de la Mulas:-122.640:-208.780
Manzanares:29.200:135.780
Maqueda:-51.100:30.660
Marbella:-91.980:379.600
Marín:-360.620:-202.940
Mataró:448.220:-118.260
Mazagón:-246.740:312.440
Medina del Campo:-93.440:-84.680
Medinaceli:94.900:-80.300
Mieres:-143.080:-277.400
Miranda del Ebro:48.180:-220.460
Mogadouro:-223.380:-102.200
Molina de Aragón:141.620:-48.180
Mombuey:-197.100:-162.060
Monforte de Lemos:-280.320:-211.700
Monreal del Campo:172.280:-40.880
Montalbán:204.400:-55.480
Montemor-o-Novo:-348.940:150.380
Montijo:-407.340:144.540
Montoro:-59.860:224.840
Monzón:280.320:-153.300
Monóvar:216.080:188.340
Morella:271.560:-24.820
Motril:14.600:356.240
Murcia:198.560:237.980
Murça:-275.940:-109.500
Málaga:-64.240:359.160
Mérida:-201.480:140.160
Navalmoral de la Mata:-137.240:48.180
Navia:-207.320:-308.060
Novelda:221.920:197.100
Nueno:243.820:-197.100
Nules:277.400:42.340
O Barco:-232.140:-201.480
Ocaña:21.900:42.340
Odemira:-385.440:251.120
Oitura:172.280:-124.100
Oliva:270.100:147.460
Olot:436.540:-181.040
Onda:268.640:32.120
Ontinyent:232.140:151.840
Osorno:-48.180:-201.480
Ourense:-294.920:-197.100
Ourique:-350.400:245.280
Oviedo:-146.000:-284.700
Padul:-1.460:325.580
Palencia:-61.320:-159.140
Pamplona:146.000:-230.680
Peniche:-426.320:78.840
Penyíscola:305.140:4.380
Peñafiel:-27.740:-118.260
Peñaranda de Bracamonte:-113.880:-45.260
Piedrabuena:-35.040:129.940
Pinoso:200.020:192.720
Plasenncia:-166.440:30.660
Pola de Siero:-128.480:-286.160
Ponferrada:-210.240:-211.700
Pont de Suert:319.740:-205.860
Ponte de Lima:-350.400:-151.840
Ponte do Sôr:-329.960:99.280
Pontedeume:-313.900:-292.000
Pontevedra:-350.400:-211.700
Portalegre:-287.620:94.900
Portbou:496.400:-207.320
Portman:220.460:275.940
Porto:-362.080:-94.900
Potes:-65.700:-267.180
Puerto Lumbreras:153.300:273.020
Puerto Real:-194.180:378.140
Puertollano:-29.200:159.140
Puigcerdà:402.960:-204.400
Quintana del Puente:-32.120:-162.060
Quintanilha:-210.240:-138.700
Reinosa:-24.820:-252.580
Requena:183.960:83.220
Reus:346.020:-80.300
Riaza:23.360:-84.680
Ribadavia:-322.660:-189.800
Ribadeo:-237.980:-306.600
Ribadesella:-87.600:-296.380
Ribeira de Pena:-297.840:-119.720
Rincón de la Victorio:-45.260:360.620
Ripoll:429.240:-185.420
Ronda:-116.800:356.240
Ruidera:59.860:137.240
Sabiñánigo:232.140:-213.160
Sacedón:71.540:-7.300
Sagunt:262.800:67.160
Salamanca:-151.840:-48.180
San Ciprián:-264.260:-324.120
San Esteban de Gormaz:42.340:-110.960
San Fernando:-201.480:386.900
San Rafael:-37.960:-27.740
Sant Joan d'Alacant:248.200:195.640
Santa Pola:242.360:210.240
Santander:-7.300:-293.460
Santarem:-381.060:90.520
Santiago de Compostela:-353.320:-254.040
Santo Domingo de la Calzada:58.400:-192.720
Segorbe:240.900:48.180
Segovia:-30.660:-58.400
Serpa:-306.600:224.840
Setubal:-386.900:164.980
Sevilla:-179.580:289.080
Silla:246.740:94.900
Sines:-395.660:211.700
Sintra:-432.160:128.480
Sitges:391.280:-83.220
Solares:0.000:-286.160
Soria:97.820:-131.400
Sueca:255.500:112.420
Tafalla:144.540:-204.400
Talavera de la Reina:-84.680:40.880
Tarancón:55.480:32.120
Tarazona:147.460:-137.240
Tarifa:-159.140:426.320
Tarragona:363.540:-75.920
Tavira:-310.980:300.760
Teruel:189.800:2.920
Toledo:-23.360:51.100
Tordesillas:-97.820:-108.040
Toro:-125.560:-108.040
Torreblanca:299.300:11.680
Torrelavega:-20.440:-284.700
Torremolinos:-67.160:367.920
Torres Novas:-370.840:70.080
Torres Vedras:-420.480:108.040
Torrevieja:229.220:235.060
Totana:169.360:252.580
Trujillo:-159.140:83.220
Tuj:-354.780:-176.660
Unquera:-54.020:-284.700
Utiel:170.820:70.080
Valdepeñas:27.740:157.680
Valencia de Alcántara:-268.640:87.600
Valladolid:-71.540:-124.100
Valongo:-351.860:-93.440
Valverde del Camino:-236.520:271.560
València:251.120:84.680
Vegadeo:-235.060:-299.300
Venta El Alto:-188.340:255.500
Venturada:1.460:-36.500
Vera:144.540:300.760
Verín:-273.020:-154.760
Viana do Castelo:-366.460:-144.540
Vic:436.540:-160.600
Vielha:325.580:-230.680
Vigo:-363.540:-186.880
Vila Flor:-249.660:-96.360
Vila Nova de Foz Côa:-255.500:-75.920
Vila Real:-293.460:-100.740
Vila-real:280.320:36.500
Vilafranca del Cid:265.720:0.000
Vilafranca del Penedés:397.120:-109.500
Vilagarcía de Arousa:-362.080:-224.840
Vilareal de Santo Antonio:-302.220:296.380
Villalón de Campos:-94.900:-162.060
Villarrobledo:77.380:110.960
Villena:216.080:166.440
Vinarós:309.520:-8.760
Viseu:-312.440:-40.880
Vitoria:73.000:-236.520
Vélez-Rubio:122.640:259.880
Xert:294.920:-14.600
Xinzo de Limia:-289.080:-173.740
Xàtiva:236.520:140.160
Yecla:192.720:170.820
Zafra:-205.860:189.800
Zamora:-156.220:-109.500
Zaragoza:192.720:-119.720
Zarauz:110.960:-278.860
Zuera:208.780:-144.540
Ágreda:132.860:-141.620
Ávila:-77.380:-13.140
Écija:-119.720:270.100
Évora:-327.040:160.600
Úbeda:35.040:229.220""".split('\n'):
    _city, _x, _y = _line.strip().split(':')
    cities.append(_city)
    coords[_city] = (float(_x), float(_y))

for _line in """A Coruña:Carballo:22.286
A Coruña:Pontedeume:20.904
Abrantes:Castelo Branco:67.303
Adanero:San Rafael:39.312
Aguilar de Campoó:Burgos:56.790
Aguilar de Campoó:Reinosa:22.853
Alacant:Santa Pola:9.234
Albacete:Almansa:57.257
Albacete:La Roda:27.547
Albacete:Ruidera:77.504
Albocàsser:Xert:18.468
Albocàsser:L'Alcora:23.946
Albufeira:Ourique:53.544
Alcala de Henarés:Guadalajara:31.348
Alcance:Ayora:20.648
Alcance:Casas Ibáñez:18.059
Alcance:Bicorp:29.382
Alcantarilla:Callosa del Segura:32.417
Alcantarilla:Cieza:36.059
Alcantarilla:Totana:24.863
Alcaraz:Albacete:64.306
Alcaraz:Úbeda:76.424
Alcañices:Mogadouro:43.409
Alcañiz:Híjar:25.540
Alcañiz:Reus:85.929
Alcolea del Pinar:Molina de Aragón:55.595
Alcoy:Sant Joan d'Alacant:27.778
Almería:Aara:41.808
Alfaro:Ágreda:35.553
Alfaro:Tafalla:29.200
Alfaro:Logroño:58.126
Algeciras:Guadiaro:19.588
Algeciras:Tarifa:15.520
Almadrones:Sacedón:45.331
Almadrones:Alcolea del Pinar:29.563
Almadén:Córdoba:80.313
Almansa:Yecla:19.036
Almazán:Medinaceli:21.949
Almonte:Sevilla:48.025
Alzira:Xàtiva:21.258
Alzira:Silla:25.204
Alzira:Gandia:31.040
Amposta:Vinarós:26.842
Andújar:Bailén:26.442
Andújar:Córdoba:55.653
Ansiao:Castelo Branco:65.570
Ansiao:Torres Novas:46.377
Ansiao:Coimbra:35.161
Ansiao:Leiria:41.552
Antequera:Málaga:29.778
Antequera:Lucena:38.958
Antequera:Estepa:35.161
Aranda de Duero:Riaza:45.822
Aranda de Duero:Segovia:72.502
Aranjuez:Ocaña:15.792
Aranjuez:Madrid:34.704
Arenas de San Pedro:Talavera de la Reina:27.431
Arganda del Rey:Tarancón:37.876
Armiñón:Vitoria:12.559
Armiñón:Miranda del Ebro:17.026
Arévalo:Adanero:19.479
Astorga:La Bañeza:28.796
Astorga:Ponferrada:33.612
Aveiro:Figueira da Foz:52.641
Avilés:Oviedo:23.085
Ayora:Almansa:23.767
Ayora:Casa de Juan Gil:19.858
Ayora:Xàtiva:50.996
Baamonde:Becerrea:50.597
Baamonde:Vegadeo:60.726
Baamonde:Arzúa:37.309
Baamonde:Betanzos:28.084
Badajoz:Mérida:50.174
Baena:Córdoba:61.977
Bailén:Jaén:28.348
Barbastro:Graus:29.563
Barcelona:Mataró:19.642
Barcelona:Vic:55.557
Barcelona:Manresa:54.197
Barcelona:Igualada:39.176
Barcelona:Vilafranca del Penedés:36.762
Barreiros:San Ciprián:22.853
Barreiros:Baamonde:47.534
Basauri:Vitoria:43.237
Basauri:Armiñón:49.661
Basauri:Bilbao:7.445
Baza:Granada:65.113
Becerrea:O Barco:40.566
Becerrea:Lugo:34.053
Beja:Grândula:54.256
Beja:Serpa:22.238
Belmonte:Daimiel:76.841
Benabarre:Lleida:58.764
Benavente:Villalón de Campos:48.379
Benavente:Mombuey:54.197
Benicarló:Vinarós:8.513
Benicàssim:Castelló de la Plana:7.300
Benicàssim:Torreblanca:15.520
Benidorm:Sant Joan d'Alacant:44.977
Betanzos:A Coruña:23.542
Betanzos:Carballo:39.420
Betanzos:Arzúa:32.939
Betanzos:Pontedeume:7.300
Bicorp:Xàtiva:32.417
Bilbao:Castro Urdiales:18.468
Boltaña:Sabiñánigo:45.284
Boltaña:Jaca:53.065
Borriol:L'Alcora:11.119
Braga:Porto:38.573
Braga:Valongo:36.118
Braga:Ribeira de Pena:46.100
Bragança:Quintanilha:16.323
Burgo de Osma:Soria:48.357
Burgos:Lerma:32.120
Burgos:Quintana del Puente:48.795
Burgos:Palencia:75.087
Béjar:Salamanca:43.897
Calatayud:Soria:59.288
Caldas da Rainha:Santarem:32.020
Campillos:Estepa:21.949
Campillos:Antequera:27.778
Campomanes:La Magdalena:23.587
Campomanes:Mieres:17.762
Cangas de Onís:Potes:30.695
Cangas de Onís:Pola de Siero:35.523
Carboneras:Vera:25.498
Carboneras:Almería:52.235
Carboneras:Aara:93.303
Carregado:Torres Vedras:18.980
Cartagena:La Unión:9.794
Cartagena:Murcia:37.904
Casa de Juan Gil:Albacete:32.318
Casas Ibáñez:Albacete:41.295
Cascais:Lisboa:18.059
Caspe:Fraga:45.612
Caspe:Alcañiz:17.089
Castelldefels:Barcelona:19.036
Castelldefels:Sitges:28.759
Castelló de la Plana:Borriol:6.529
Castelo Branco:Portalegre:52.641
Castelo Branco:Plasenncia:118.835
Castro Urdiales:Laredo:17.762
Caudete:Requena:10.528
Cañete:Utiel:36.935
Cañete:Cuenca:48.379
Cerceda:Burgos:49.576
Cerceda:Santander:58.126
Cervera:Lleida:33.612
Cervera:Manresa:49.661
Chantada:Ourense:28.084
Chiva:València:32.153
Chiva:Alzira:43.335
Chiva:Liria:18.294
Cieza:Hellín:23.085
Cinctorres:Vilafranca del Cid:14.673
Cinctorres:Morella:11.119
Cistierna:Potes:43.556
Cistierna:Cangas de Onís:41.295
Ciudad Real:Puertollano:28.348
Ciudad Real:Piedrabuena:22.665
Cocentaina:Alcoy:7.445
Coimbra:Aveiro:43.138
Coimbra:Leiria:64.140
Coimbra:Guarda:80.034
Coimbra:Castelo Branco:77.984
Collado Villalba:Madrid:29.200
Coruche:Santarem:37.223
Coruche:Ponte do Sôr:42.940
Covilha:Castelo Branco:42.365
Covilha:Coimbra:60.144
Cudillero:Avilés:11.771
Cuenca:Belmonte:66.586
Cuenca:Sacedón:54.726
Cullera:Gandia:20.904
Cáceres:Valencia de Alcántara:64.505
Cáceres:Trujillo:45.284
Cáceres:Plasenncia:63.657
Córdoba:Montoro:29.563
Córdoba:Espiel:32.153
Córdoba:Lucena:62.712
Córdoba:Écija:47.534
Daimiel:Madridejos:39.850
Daimiel:Ciudad Real:23.767
Daroca:Calatayud:37.223
Donostia:Zarauz:13.140
Dos Hermanas:Jerez de la Frontera:60.197
Durango:Basauri:19.036
Durcal:Motril:26.117
Durcal:Padul:8.513
El Barco de Ávila:Ávila:65.113
El Burgo del Ebro:Zaragoza:16.518
Elda:Novelda:13.140
Elvas:Estremoz:36.964
Elvas:Badajoz:22.806
Elx:Novelda:10.528
Elx:Callosa del Segura:21.704
Elx:Alacant:14.673
Espiel:Almadén:58.637
Espiel:Llerena:69.007
Espinho:Feira:11.119
Estepa:Sevilla:85.044
Estepona:Guadiaro:25.540
Estremoz:Évora:30.971
Faro:Albufeira:27.158
Faro:Tavira:30.695
Feira:Aveiro:22.853
Figueira da Foz:Coimbra:36.500
Figueres:Portbou:16.323
Figueres:La Jonquera:12.474
Figueres:Olot:53.842
Fraga:Lleida:36.617
Fraga:Zaragoza:103.701
Fuengirola:Marbella:13.140
Fuengirola:Torremolinos:16.518
Gaia:Espinho:8.760
Gandia:Oliva:8.513
Gandia:Xàtiva:29.200
Gibraleón:Sevilla:81.812
Gijón:Pola de Siero:21.557
Gijón:Avilés:14.673
Gimileo:Armiñón:23.587
Girona:Figueres:31.887
Girona:Vic:43.824
Granada:Loja:39.420
Granada:Baena:57.905
Grao de Sagunt:València:17.581
Graus:Benabarre:17.641
Grândula:Sines:25.830
Grândula:Ourique:57.462
Guadalajara:Venturada:36.500
Guadalajara:Almadrones:26.321
Guadiaro:La Línea de la Concepción:14.673
Guarda:Vila Real:78.488
Guarda:Covilha:31.585
Guarda:Salamanca:118.835
Guardamar del Segura:Torrevieja:14.379
Guntín:Chantada:21.704
Guntín:Lalín:28.759
Hellín:Albacete:57.257
Herrera del Duque:Almadén:42.441
Herrera del Duque:Piedrabuena:74.173
Honrubia:La Roda:41.527
Honrubia:Cuenca:46.925
Honrubia:Belmonte:36.964
Huelva:Mazagón:15.792
Huelva:Almonte:31.211
Huelva:Gibraleón:14.379
Huesca:Barbastro:29.527
Huesca:Nueno:26.321
Huesca:Fraga:76.396
Híjar:Montalbán:42.113
Híjar:El Burgo del Ebro:45.612
Ibi:Alcoy:8.881
Igualada:Cervera:36.500
Izurzun:Donostia:40.382
Jabugo:Valverde del Camino:32.120
Jabugo:Venta El Alto:50.786
Jaén:Granada:58.782
Jerez de la Frontera:Puerto Real:21.949
L'Alcora:Onda:14.673
L'Hospitalet de l'Infant:Amposta:37.394
La Albuera:Jabugo:74.460
La Albuera:Badajoz:22.806
La Bañeza:Benavente:36.059
La Espina:Grado:22.094
La Línea de la Concepción:Algeciras:10.629
La Magdalena:León:24.820
La Magdalena:Astorga:33.100
La Roda:Cuenca:87.649
La Seu d'Urgell:Pont de Suert:60.989
La Unión:Portman:6.529
La Unión:Murcia:37.309
Lagos:Albufeira:36.529
Lalín:Ourense:43.335
Lalín:Chantada:20.904
Lalín:Vilagarcía de Arousa:44.667
Laredo:Cerceda:48.379
Leiria:Figueira da Foz:38.656
Leiria:Caldas da Rainha:41.321
Leiria:Torres Novas:32.809
Lepe:Ayamonte:9.234
Lepe:Gibraleón:29.200
Lerma:Aranda de Duero:36.964
Lerma:Soria:96.504
Les Borges Blanques:Tarragona:48.533
León:Astorga:45.729
León:Benavente:69.377
León:Campomanes:36.059
Linares:Bailén:17.089
Liria:Segorbe:23.085
Liria:València:29.200
Lisboa:Sintra:19.036
Lisboa:Montijo:10.528
Llanes:Ribadesella:18.468
Lleida:Les Borges Blanques:19.036
Lleida:Monzón:54.256
Llerena:Zafra:32.020
Logroño:Santo Domingo de la Calzada:34.364
Logroño:Gimileo:21.704
Logroño:Soria:68.868
Loja:Antequera:37.876
Lorca:Puerto Lumbreras:12.389
Lorca:Vélez-Rubio:39.663
Los Alcázares:La Unión:13.851
Los Gallardos:Carboneras:16.323
Los Gallardos:Almería:58.927
Losa del Obispo:Liria:26.321
Losa del Obispo:Cañete:49.640
Losa del Obispo:Segorbe:39.312
Luarca:Cudillero:26.280
Lugo:Guntín:13.461
Lugo:Baamonde:18.980
Lugo:Vegadeo:65.048
Macedo de Cavaleiros:Bragança:25.119
Macedo de Cavaleiros:Murça:39.877
Madrid:Toledo:56.186
Madrid:Arganda del Rey:26.321
Madrid:Alcala de Henarés:24.948
Madrid:Venturada:36.529
Madridejos:Manzanares:45.729
Madridejos:Ocaña:49.982
Mansilla de la Mulas:León:20.283
Mansilla de la Mulas:Cistierna:38.545
Manzanares:Valdepeñas:21.949
Manzanares:Daimiel:19.479
Maqueda:Toledo:34.457
Maqueda:Madrid:59.592
Marbella:Estepona:25.498
Marín:Pontevedra:13.461
Mataró:Girona:54.315
Medina del Campo:Arévalo:24.777
Medinaceli:Alcolea del Pinar:20.335
Medinaceli:Calatayud:51.743
Mieres:Oviedo:7.862
Miranda del Ebro:Gimileo:26.802
Miranda del Ebro:Burgos:50.618
Miranda del Ebro:Cerceda:36.849
Mogadouro:Murça:53.065
Mogadouro:Guarda:88.387
Mombuey:Zamora:66.586
Mombuey:Verín:76.270
Monforte de Lemos:Ourense:20.648
Monreal del Campo:Teruel:47.174
Monreal del Campo:Daroca:26.442
Monreal del Campo:Molina de Aragón:31.517
Montalbán:Monreal del Campo:35.282
Montalbán:Alcañiz:57.850
Montemor-o-Novo:Coruche:30.799
Montijo:Carregado:29.527
Montijo:Setubal:28.907
Montoro:Andújar:28.348
Monzón:Barbastro:15.792
Monóvar:Elda:7.300
Morella:Alcañiz:42.138
Motril:Almuñecar:19.203
Motril:Aara:36.529
Murcia:Alcantarilla:10.324
Murça:Vila Flor:29.382
Málaga:Rincón de la Victorio:19.036
Mérida:Herrera del Duque:96.316
Mérida:Cáceres:58.473
Navalmoral de la Mata:Talavera de la Reina:53.065
Navia:Luarca:16.060
Navia:La Espina:28.084
Nueno:Sabiñánigo:19.858
Nules:Sagunt:28.796
Nules:Vila-real:6.529
O Barco:Monforte de Lemos:49.252
Ocaña:Villarrobledo:88.242
Odemira:Lagos:46.743
Oitura:Tarazona:28.084
Oliva:Benidorm:26.321
Olot:Ripoll:8.513
Onda:Segorbe:32.054
Onda:Castelló de la Plana:15.243
Onda:Vila-real:12.474
Ontinyent:Xàtiva:12.474
Osorno:Aguilar de Campoó:33.357
Ourense:Xinzo de Limia:24.079
Ourense:Ribadavia:28.684
Ourique:Beja:37.394
Ourique:Faro:69.607
Oviedo:Pola de Siero:17.581
Oviedo:Grado:16.323
Oviedo:Gijón:21.704
Padul:Granada:13.851
Palencia:Quintana del Puente:29.346
Palencia:Villalón de Campos:33.707
Palencia:Osorno:44.332
Pamplona:Izurzun:15.792
Pamplona:Jaca:79.700
Peniche:Caldas da Rainha:16.126
Penyíscola:Benicarló:5.840
Peñafiel:Aranda de Duero:28.348
Piedrabuena:Almadén:59.449
Pinoso:Alcantarilla:45.331
Pinoso:Monóvar:16.647
Plasenncia:El Barco de Ávila:35.343
Plasenncia:Béjar:39.176
Ponferrada:O Barco:24.167
Ponferrada:Becerrea:49.079
Pont de Suert:Vielha:25.498
Pont de Suert:Boltaña:42.741
Pont de Suert:Benabarre:27.158
Ponte de Lima:Viana do Castelo:17.641
Ponte de Lima:Braga:24.474
Ponte de Lima:Xinzo de Limia:65.113
Ponte do Sôr:Abrantes:33.325
Pontedeume:Ferrol:19.036
Pontevedra:Vigo:28.084
Pontevedra:Vilagarcía de Arousa:17.581
Pontevedra:Ourense:57.369
Portalegre:Ponte do Sôr:42.566
Portalegre:Estremoz:47.174
Portman:Cartagena:11.771
Potes:Unquera:21.056
Puerto Lumbreras:Vélez-Rubio:33.357
Puerto Lumbreras:Vera:29.090
Puerto Real:Cádiz:14.673
Puerto Real:Chiclana de la Frontera:16.126
Puertollano:Montoro:72.502
Puigcerdà:Llivia:9.349
Puigcerdà:La Seu d'Urgell:25.498
Quintana del Puente:Lerma:37.988
Quintanilha:Alcañices:20.335
Reinosa:Torrelavega:32.417
Requena:Chiva:35.040
Requena:Alcance:24.820
Requena:Casas Ibáñez:26.921
Requena:Liria:46.652
Requena:Losa del Obispo:31.245
Riaza:Venturada:52.924
Riaza:San Esteban de Gormaz:32.417
Ribadavia:Tuj:34.704
Ribadeo:Navia:30.695
Ribadeo:Vegadeo:7.862
Ribadeo:Barreiros:16.323
Ribadesella:Cangas de Onís:17.089
Ribadesella:Gijón:51.845
Ribeira de Pena:Vila Real:19.479
Ribeira de Pena:Murça:24.167
Rincón de la Victorio:Almuñecar:40.906
Ripoll:Puigcerdà:32.417
Ronda:Marbella:34.084
Ronda:Campillos:33.612
Ruidera:Manzanares:30.695
Sabiñánigo:Jaca:9.349
Sacedón:Guadalajara:44.500
Sagunt:Grao de Sagunt:4.380
Sagunt:Segorbe:28.980
Salamanca:Peñaranda de Bracamonte:38.072
Salamanca:Zamora:61.476
San Esteban de Gormaz:Aranda de Duero:44.332
San Esteban de Gormaz:Burgo de Osma:13.461
San Fernando:Cádiz:10.324
San Fernando:Chiclana de la Frontera:11.403
San Rafael:Collado Villalba:17.822
San Rafael:Segovia:31.517
Sant Joan d'Alacant:Alacant:6.529
Santa Pola:Guardamar del Segura:13.774
Santander:Solares:10.324
Santander:Burgos:101.593
Santarem:Carregado:33.100
Santiago de Compostela:Betanzos:49.940
Santiago de Compostela:Lalín:40.566
Santo Domingo de la Calzada:Burgos:52.560
Segorbe:Teruel:68.262
Segovia:Adanero:42.138
Segovia:Venturada:38.875
Serpa:Jabugo:71.585
Setubal:Carregado:52.173
Setubal:Sines:47.534
Setubal:Grândula:30.937
Setubal:Montemor-o-Novo:40.671
Sevilla:Dos Hermanas:13.774
Sevilla:Huelva:76.605
Silla:Sueca:19.588
Sines:Odemira:40.723
Sintra:Cascais:14.673
Sitges:Tarragona:28.684
Sitges:Vilafranca del Penedés:26.921
Solares:Laredo:22.094
Soria:Almazán:29.527
Sueca:Cullera:9.349
Tafalla:Pamplona:26.321
Talavera de la Reina:Maqueda:35.101
Talavera de la Reina:Herrera del Duque:79.433
Tarancón:Cuenca:55.499
Tarancón:Belmonte:53.145
Tarancón:Ocaña:35.101
Tarazona:Ágreda:15.243
Tarazona:Alfaro:38.072
Tarifa:Chiclana de la Frontera:46.468
Tarragona:Reus:18.059
Tarragona:L'Hospitalet de l'Infant:24.299
Tavira:Albufeira:49.726
Tavira:Vilareal de Santo Antonio:9.794
Teruel:Montalbán:60.197
Teruel:Cañete:44.404
Toledo:Aranjuez:36.587
Toledo:Ciudad Real:85.294
Tordesillas:Medina del Campo:23.767
Tordesillas:Valladolid:30.799
Tordesillas:Benavente:67.176
Toro:Tordesillas:27.740
Torreblanca:Penyíscola:9.349
Torreblanca:Albocàsser:13.461
Torrelavega:Santander:15.792
Torremolinos:Málaga:9.234
Torres Novas:Santarem:22.853
Torres Novas:Abrantes:24.820
Torres Vedras:Lisboa:30.971
Torres Vedras:Caldas da Rainha:32.318
Torrevieja:Los Alcázares:23.085
Totana:Lorca:13.774
Trujillo:Mérida:70.957
Trujillo:Navalmoral de la Mata:41.321
Tuj:Ponte de Lima:25.204
Unquera:Llanes:17.089
Unquera:Torrelavega:33.580
Utiel:Honrubia:64.653
Utiel:Caudete:8.513
Valdepeñas:Bailén:77.710
Valdepeñas:Linares:66.586
Valladolid:Adanero:75.920
Valladolid:Peñafiel:44.188
Valladolid:Palencia:36.500
Valongo:Porto:10.324
Valongo:Gaia:10.528
Valongo:Vila Real:58.854
Valverde del Camino:Huelva:33.612
València:Silla:11.119
València:Sagunt:21.056
Vegadeo:Navia:29.090
Venturada:Alcala de Henarés:35.343
Venturada:Aranda de Duero:87.612
Vera:Los Gallardos:12.389
Verín:Ribeira de Pena:42.940
Viana do Castelo:Vigo:42.441
Vic:Manresa:28.684
Vigo:Tuj:13.461
Vigo:Ribadavia:40.984
Vigo:Marín:16.323
Vila Flor:Mogadouro:26.921
Vila Flor:Vila Nova de Foz Côa:21.258
Vila Nova de Foz Côa:Guarda:51.350
Vila Real:Murça:19.588
Vila Real:Braga:56.865
Vila-real:Castelló de la Plana:9.234
Vilafranca del Cid:Albocàsser:23.542
Vilagarcía de Arousa:Santiago de Compostela:30.486
Vilareal de Santo Antonio:Ayamonte:9.794
Vilareal de Santo Antonio:Beja:84.048
Villalón de Campos:Valladolid:44.572
Villalón de Campos:Mansilla de la Mulas:54.335
Villarrobledo:Manzanares:54.197
Villarrobledo:La Roda:37.223
Villarrobledo:Belmonte:28.684
Villarrobledo:Honrubia:44.500
Villena:Elda:18.468
Villena:Ibi:22.094
Villena:Ontinyent:21.704
Viseu:Guarda:46.169
Viseu:Vila Real:62.797
Viseu:Aveiro:51.287
Viseu:Coimbra:48.533
Vitoria:Izurzun:59.931
Vélez-Rubio:Baza:65.959
Xert:Morella:25.498
Xert:Vinarós:15.725
Xinzo de Limia:Verín:24.863
Xàtiva:Almansa:46.743
Xàtiva:Cocentaina:23.542
Yecla:Villena:23.767
Yecla:Elda:32.020
Yecla:Cieza:42.113
Yecla:Pinoso:23.085
Zafra:La Albuera:39.447
Zamora:Toro:30.695
Zamora:Alcañices:41.321
Zaragoza:Daroca:57.517
Zaragoza:Zuera:29.563
Zaragoza:Oitura:20.904
Zaragoza:Alfaro:73.480
Zarauz:Durango:32.318
Zuera:Huesca:42.641
Ágreda:Soria:36.500
Ávila:Arenas de San Pedro:34.826
Ávila:Maqueda:51.079
Ávila:San Rafael:42.037
Ávila:Peñaranda de Bracamonte:48.620
Ávila:Adanero:35.523
Ávila:Arévalo:54.040
Écija:Lucena:62.371
Évora:Montemor-o-Novo:24.167
Évora:Beja:55.480
Évora:Grândula:59.931
Úbeda:Linares:25.871""".split('\n'):
    _cityA, _cityB, _aux = _line.strip().split(':')
    roads.append((_cityA, _cityB))
    km[_cityA, _cityB] = float(_aux)

iberia = UndirectedGraph(V=cities, E=roads)
km = WeightingFunction(km, symmetrical=True)
#> full