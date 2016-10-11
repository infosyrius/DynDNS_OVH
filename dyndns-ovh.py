# -*- encoding: utf-8 -*-
import json
import ovh
from urllib2 import urlopen
import sys
# Variable statique a modifier pour ovh
application_key='XXXXXXXXXXXXXX'
application_secret='XXXXXXXXXXXXXXXXXXXXXX'
consumer_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Variable a modifier pour le dyndns
domain='mydomain.com'
subDomain='myserver' #Juste le sous domaine, pas le fqdn

'''
Fin de définition des variables
'''

# Definition de l'IP
ip=urlopen('http://ip.42.pl/raw').read()
client = ovh.Client(
    endpoint='ovh-eu',
    application_key=application_key,        # Application Key
    application_secret=application_secret,  # Application Secret
    consumer_key=consumer_key,              # Consumer Key
)

# On essaye de récuéprérer l'id de l'enregistrement DynDNS
result = client.get('/domain/zone/' + domain + '/dynHost/record', subDomain=subDomain)

if len(result) != 1:
    print "Erreur : Il n'existe pas d'enregistrement DynDNS OVH pour \"" + subDomain + "." + domain +"\" !"
    sys.exit(0)

idRecord = str(result[0])
# On modifie l'adresse IP du dyndns
result = client.put('/domain/zone/' + domain + '/dynHost/record/' + idRecord,ip=ip,subDomain=subDomain,)

# On rafraichit la zone dns
result = client.post('/domain/zone/' + domain + '/refresh')

print "MaJ OK ! Nouvelle IP : " + ip


