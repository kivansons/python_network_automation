#!/usr/bin/env python
"""
3a. Open a connection to the srx2 device and acquire a configuration lock.
Validate that the configuration session is indeed locked by SSH'ing into the device and attempting to enter configuration mode ("configure").
Reuse, the 'srx2' device definition from the jnpr_devices.py file that you created in exercise2.

You should receive a prompt similar to the following:

pyclass@srx2> configure
Entering configuration mode
Users currently editing the configuration:
  pyclass (pid 30316) on since 2019-03-08 18:30:51 PST
      exclusive


Add code to attempt to lock the configuration again.
Gracefully handle the "LockError" exception (meaning the configuration is already locked).
"""
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2

def try_lock(device: Config) -> bool:
  """Try and lock device config: Returns outcome as bool"""
  print("Attempting to lock the device config")
  try:
    lock_result = device.lock()
  except LockError:
    lock_result = False
  print(f"Was config lock sucessfull?: {lock_result}")
  return lock_result

# Build connection to device
srx2_device = Device(**srx2)
srx2_device.open()

# Build device config obj from device connection
srx2_device_conf = Config(srx2_device)

# Lock device
try_lock(srx2_device_conf)
input("Enter to continue")

# Try and lock device config again
try_lock(srx2_device_conf)
input("Enter to continue")

"""3b. Use the "load" method to stage a configuration using a basic set command, for example, "set system host-name python4life"."""
print("Sending config to device:")
config_cmd = "set system host-name python4life"
srx2_device_conf.load(config_cmd, format=set, merge=True)

"""
3c. Print the diff of the current configuration with the staged configuration. Your output should look similar to the following:

[edit system]
-  host-name srx2;
+  host-name python4life;
"""
print("Config diff is:")
print(srx2_device_conf.diff())

"""
3d. Rollback the staged configuration. 
Once again, print out the diff of the staged and the current configuration (which at this point should be None).
"""
print("Rolling back config:")
srx2_device_conf.rollback()

print("Config diff is:")
print(srx2_device_conf.diff())
