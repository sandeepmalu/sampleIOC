TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = sampleIOC
# sampleIOC.dbd will be created and installed
DBD += sampleIOC.dbd

# sampleIOC.dbd will be made up from these files:
sampleIOC_DBD += base.dbd

# Include dbd files from all support applications:
#sampleIOC_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#sampleIOC_LIBS += xxx

# sampleIOC_registerRecordDeviceDriver.cpp derives from sampleIOC.dbd
sampleIOC_SRCS += sampleIOC_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
sampleIOC_SRCS_DEFAULT += sampleIOCMain.cpp
sampleIOC_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#sampleIOC_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
sampleIOC_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

