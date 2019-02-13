set(TARGET_NAME test)

set(SOURCES TestOpenSerial.cpp)

add_executable(${TARGET_NAME} ${SOURCES})
target_link_libraries(${TARGET_NAME} ${PROJECT_NAME})

add_test(NAME ${TARGET_NAME}
         WORKING_DIRECTORY ${PROJECT_BINARY_DIR}/bin
         COMMAND ${TARGET_NAME})
