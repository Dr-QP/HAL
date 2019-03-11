#pragma once 

#import <SerialProtocol.h>
#import <ProgramMemoryProtocol.h>
#import <TimeServices.h>

#ifdef ARDUINO
#   include <HALArduino.h>
#else
#   include <HALUnix.h>
#endif
