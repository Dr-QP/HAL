set(${PROJECT_NAME}_HDRS
    HALArduino.h
    ArduinoHardwareSerial.h
    ArduinoProgramMemory.h
    ArduinoTimeServices.h)

set(${PROJECT_NAME}_SRCS
    ArduinoHardwareSerial.cpp
    ArduinoProgramMemory.cpp
    ArduinoTimeServices.cpp)

generate_arduino_library(${PROJECT_NAME})

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
