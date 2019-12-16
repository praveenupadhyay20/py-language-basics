import json

json_string = '''[{
    "id": 1,
    "first_name": "Angele",
    "last_name": "Wheatley",
    "email": "awheatley0@pinterest.com",
    "gender": "Female",
    "ip_address": "30.15.234.161"
}, {
    "id": 2,
    "first_name": "Alexis",
    "last_name": "Dellenbrok",
    "email": "adellenbrok1@sina.com.cn",
    "gender": "Female",
    "ip_address": "25.67.254.4"
}, {
    "id": 3,
    "first_name": "Licha",
    "last_name": "Grooby",
    "email": "lgrooby2@google.es",
    "gender": "Female",
    "ip_address": "158.100.200.239"
}, {
    "id": 4,
    "first_name": "Petronella",
    "last_name": "Rockingham",
    "email": "prockingham3@cargocollective.com",
    "gender": "Female",
    "ip_address": "137.212.101.188"
}, {
    "id": 5,
    "first_name": "Deeann",
    "last_name": "Scahill",
    "email": "dscahill4@over-blog.com",
    "gender": "Female",
    "ip_address": "214.230.227.119"
}, {
    "id": 6,
    "first_name": "Rabbi",
    "last_name": "Longstaffe",
    "email": "rlongstaffe5@theglobeandmail.com",
    "gender": "Male",
    "ip_address": "89.111.192.41"
}, {
    "id": 7,
    "first_name": "Winslow",
    "last_name": "Faill",
    "email": "wfaill6@yahoo.com",
    "gender": "Male",
    "ip_address": "142.195.42.187"
}, {
    "id": 8,
    "first_name": "Riannon",
    "last_name": "Haysham",
    "email": "rhaysham7@youku.com",
    "gender": "Female",
    "ip_address": "114.230.46.150"
}, {
    "id": 9,
    "first_name": "Alfy",
    "last_name": "O'Doohaine",
    "email": "aodoohaine8@irs.gov",
    "gender": "Female",
    "ip_address": "167.188.12.26"
}, {
    "id": 10,
    "first_name": "Andris",
    "last_name": "Cullinan",
    "email": "acullinan9@hibu.com",
    "gender": "Male",
    "ip_address": "28.134.140.206"
}]'''

# loads for parsing the json
json_data = json.loads(json_string)

for item in json_data:
    print(f'item: {json.dumps(item, indent=4, sort_keys = True)}')
    print('------------------')
