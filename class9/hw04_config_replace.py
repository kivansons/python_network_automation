#!/usr/bin/env python
"""
4a. Add nxos1 to your my_devices.py file. Ensure that you include the necessary information to set the NX-API port to 8443.
This is done using 'optional_args' in NAPALM so you should have the following key-value pair defined:

​"optional_args": {"port": 8443}


4b. Create a new function named 'create_checkpoint'. Add this function into your my_functions.py file.
This function should take one argument, the NAPALM connection object. 
his function should use the NAPALM _get_checkpoint_file() method to retrieve a checkpoint from the NX-OS device. 
It should then write this checkpoint out to a file.

Recall that the NX-OS platform requires a 'checkpoint' file for configuration replace operations.
Using this new function, retrieve a checkpoint from nxos1 and write it to the local file system.

4c. Manually copy the saved checkpoint to a new file and add an additional loopback interface to the configuration.

4d. Create a Python script that stages a complete configuration replace operation
(using the checkpoint file that you just retrieved and modified). 
Once your candidate configuration is staged perform a compare_config (diff) on the configuration to see your pending changes.
After the compare_config is complete, then use the discard_config() method to eliminate the pending changes.
Next, perform an additional compare_config (diff) to verify that you have no pending configuration changes.
Do not actually perform the commit_config as part of this exercise.
"""
from my_functions import build_napalm_connection, create_checkpoint
from my_devices import net_devices


def main():
    nxos1 = net_devices["nxos1"]
    conn = build_napalm_connection(nxos1)

    create_checkpoint(conn)
    conn.close()
    
if __name__ == "__main__":
    main()


