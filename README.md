### Migrate virtaul machines across hyperviosrs

Update the config.py file with the MySQL login details andrun the migration scripts. 

# migrate-hv.py

Migrate all the virtual machines in a hypervisor to another. The script will save the list of VPS migrated
during the process as text file with timestamp, this file can used as a direct input to the migrate-vps.py 
script

```
 Usage : ./migrate-hv.py <source_hypervisor_label> <destination_hypervisor_label> 
 
 Description : Script to migrate all virtual machines on a hypervisor to another
 
 NOTE : Onapp supports only migrating the virtual machines between hypervisors that has shared data stores 
  exist. This script does not migrate the data stores or underlying volume group, it either automatically
  switch over to the online hypervisor if the other goes down or it need to be manually migrate the volume 
  group holds the virtual machine data

```
# migrate-vps.py

Migrate multiple VPS listed in the file to another hypervisor

```

Usage : ./migrate-vps.py <virtual_machine_list_file> <destination_hypervisor_label>

Description : Script to migrate all virtual machines listed on the file to a hypervisor.

NOTE : Onapp supports only migrating the virtual machines between hypervisors that has shared data stores 
 exist. This script does not migrate the data stores or underlying volume group, it either automatically
 switch over to the online hypervisor if the other goes down or it need to be manually migrate the volume 
 group holds the virtual machine data
 
 ```
