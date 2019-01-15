### Migrate virtaul machines across hyperviosrs

```
 Usage : ./migrate-hv.py <source_hypervisor_label> <destination_hypervisor_label> 
 
 Description : Script to migrate all virtual machines on a hypervisor to another
 
 NOTE : Onapp supports only migrating the virtual machines between hypervisors that has shared data stores exist. This script does not             migrate the data stores or underlying volume group, it either automatically switch over to the online hypervisor if the other goes         down or it need to be manually migrate the volume group holds the virtual machine data

```
