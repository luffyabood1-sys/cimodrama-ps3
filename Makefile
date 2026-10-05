TITLE          := SimoDrama PS3
APPID          := SIMO00001
CONTENT_ID     := UP0001-SIMO00001_00-0000000000000000
TARGET         := SimoDrama
OBJS           := main.o

LIBS           := -lpsl1ght -lnet -lsysutil -lio

include $(PS3DEV)/spu/share/spu.mk
include $(PS3DEV)/psl1ght/share/psl1ght.mk
