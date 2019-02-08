cmake_minimum_required(VERSION 3.5)

set(PROJECT_NAME HAL)
project(${PROJECT_NAME} VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(NOT EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    # message(FATAL_ERROR "The file conanbuildinfo.cmake doesn't exist.\nPlease run 'conan install' first")
    execute_process(COMMAND conan install "${CMAKE_CURRENT_SOURCE_DIR}" WORKING_DIRECTORY ${CMAKE_BINARY_DIR})
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories(include)

if (${CMAKE_SYSTEM_NAME} STREQUAL Arduino)
    add_subdirectory(src/arduino)
elseif (UNIX)
    add_subdirectory(src/unix)
else ()
    message(FATAL_ERROR "unsupported platform")
endif()
