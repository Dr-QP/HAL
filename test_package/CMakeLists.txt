project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if (${CMAKE_SYSTEM_NAME} STREQUAL Arduino)
    add_subdirectory(arduino)
elseif (UNIX)
    add_subdirectory(unix)
else ()
    message(FATAL_ERROR "unsupported platform")
endif()


# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
