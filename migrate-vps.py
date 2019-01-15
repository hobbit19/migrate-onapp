#!/usr/bin/env python

import MySQLdb
import sys
import time 
import config 

#Read VPS list file

timestamp = time.strftime("%Y%m%d-%H%M%S")
vps_file = sys.argv[1]   
vds_list = open(vps_file, "r").readlines()

#Find the ID of hypervisor from the label

def get_hvid(label):

   conn = MySQLdb.connect(host= config.host,
                       user= config.user,
                       passwd= config.passwd,
                       db= config.db )

   cur = conn.cursor()

   cur.execute("select id from hypervisors where label = %s", [label])
   result = cur.fetchall()

   for row in result:
      return row[0]

   cur.close()
   conn.close()

def get_vds_id(source):

   conn = MySQLdb.connect(host= config.host,
                       user= config.user,
                       passwd= config.passwd,
                       db= config.db )
   
   cur = conn.cursor()
   cur.execute("select id from virtual_machines where hypervisor_id = %s", [source])
   result = cur.fetchall()
   
   return result

   cur.close()
   conn.close()

#Update hypervisor of the listed VPS

def update_hv(destiantion, vds_id):

    conn = MySQLdb.connect(host= config.host,
                       user= config.user,
                       passwd= config.passwd,
                       db= config.db )

    cur = conn.cursor()
    cur.execute("update virtual_machines set hypervisor_id = %s where id = %s", (destination, vds_id))
   
    conn.commit() 
    print "   Completed ... !!!  %s  ---->   %s" % ([vds_id], destination)
    print "\n"
    cur.close()
    conn.close()

def usage():

  print usage_doc


usage_doc = """

 Usage : migrate-vps.py <virtual_machine_list_file> <destination_hypervisor_label>

 Description : Script to migrate all virtual machines listed on the file to a hypervisor.

 NOTE : Onapp supports only migrating the virtual machines between hypervisors that has shared data stores exist. This script does not migrate the          data stores or underlying volume group, it either automatically switch over to the online hypervisor if the other goes down or you have to
       manually migrate the volume group holds the virtual machine data.
       
"""


if __name__ == "__main__":
   
    if (len(sys.argv)) != 3:
        usage()
        sys.exit()


    destination = get_hvid(sys.argv[2])

    if destination is None:
       print "\n   Destination Hypervisor Label is Invalid"
       usage()
    
    else:

      print " Migrating all virtual machines to Hypervisor %s ..... \n" % destination

#      vds_list = get_vds_id(source)
      if not vds_list: 
           print "\n    No Virtual Machine exists on the file  ......!!!!!" 
           usage()
           exit()
 
  
      for id in vds_list:
         update_hv(destination, id) 
      
