cmake_minimum_required(VERSION 3.5)
set(PROJECT_NAME HAL)
project(${PROJECT_NAME} VERSION 1.0.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories(include)
add_subdirectory(src/arduino)