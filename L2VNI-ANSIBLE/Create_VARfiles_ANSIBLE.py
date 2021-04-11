import yaml
from user_login import user_login

user_login()

vlan_list = []
name_list = []
multi_list = []
tenant_list = []
ip_list = []
vn_list = []
vn_seg_name = []
while True:
    try:
        le_sp = input('Is configuration for Spine or Leaf : ')
        leaf_spine = le_sp.capitalize()
        if (leaf_spine == "Leaf") or (leaf_spine == "Spine"):
            print("You are configuring", leaf_spine)
            break
        print("Please retry again..... Please type leaf or spine")
    except Exception as e:
        print(e)
tenant = input('Please enter TENANT name: ')
tenant_list.append(tenant)
total = int(input('Please enter TOTAL VLAN in no : '))
for i in range(1, total):
    while len(vlan_list) < total:
        vlan = int(input('Please enter vlan %d no: ' % i))
        name_vlan = str(input('Please enter vlan %d name: ' % i))
        ip = str(input('Please enter %d ip address no:  ' % i))
        multi = str(input('Please enter %d multicast address no:  ' % i))
        vlan_list.append(vlan)
        name_list.append(name_vlan)
        ip_list.append(ip)
        multi_list.append(multi)
        i = i+1


def vn_seg(vlan_list):
    for i in vlan_list:
        a = str(i)
        k = len(a)
        if k == 1:
            vn_seg1 = str(10000) + a
        elif k == 2:
            vn_seg1 = str(1000) + a
        elif k == 3:
            vn_seg1 = str(100) + a
        elif k == 4:
            vn_seg1 = str(10) + a
        else:
            print("high")
            exit()
        vn_list.append(int(vn_seg1))
    return int(vn_seg1)
    vn_seg(vlan_list)
    return vlan_list, name_list


def vlan_vn_seg_name(vlan_list, multi_list, vn_list, name_list, tenant_list):
    n = len(vlan_list)
    for i in range(n):
        list = {'id': vlan_list[i], 'segment': vn_list[i],
                'name': name_list[i], 'multicast': multi_list[i], 'tenant':
                tenant_list[0], 'ip': ip_list[i]}
        vn_seg_name.append(list)
    return vn_seg_name


vn_seg(vlan_list)
config1 = dict()
config1 = vlan_vn_seg_name(vlan_list, multi_list, vn_list, name_list,
                           tenant_list)

final_list = {'L2VNI': config1}

if leaf_spine == "Leaf":
    with open(r'roles/leaf/vars/main.yml', 'w')as file:
        documents = yaml.dump(final_list, file, default_flow_style=False)
elif leaf_spine == "Spine":
    with open(r'roles/spine/vars/main.yml',
              'w')as file:
        documents = yaml.dump(final_list, file, default_flow_style=False)
