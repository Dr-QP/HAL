cmake_minimum_required(VERSION 3.5)

set(PROJECT_NAME HAL)
project(${PROJECT_NAME} VERSION 1.0.0)

if(NOT EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    # message(ERROR "The file conanbuildinfo.cmake doesn't exist.\nPlease run 'conan install' first")
    execute_process(COMMAND conan install "${CMAKE_CURRENT_SOURCE_DIR}" WORKING_DIRECTORY ${CMAKE_BINARY_DIR})
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories(include)

string(TOLOWER "src/${CMAKE_SYSTEM_NAME}" SOURCES_FOLDER)
add_subdirectory(${SOURCES_FOLDER})
