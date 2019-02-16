cmake_minimum_required(VERSION 3.8)

set(PROJECT_NAME HAL)
project(${PROJECT_NAME} VERSION 1.0.0)
enable_testing()

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CONAN_BUILD_INFO_FILE ${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
if(NOT EXISTS ${CONAN_BUILD_INFO_FILE})
  message(
    WARNING
      "The file conanbuildinfo.cmake doesn't exist.\nRunning 'conan install' first..."
    )
  execute_process(COMMAND conan install "${CMAKE_CURRENT_SOURCE_DIR}"
                          -if="${CMAKE_CURRENT_BINARY_DIR}")
endif()

include(${CONAN_BUILD_INFO_FILE})
conan_basic_setup()

include_directories(include)

if(${CMAKE_SYSTEM_NAME} STREQUAL Arduino)
  add_subdirectory(src/arduino)
elseif(UNIX)
  add_subdirectory(src/unix)
  add_subdirectory(tests/unix)
else()
  message(FATAL_ERROR "unsupported platform")
endif()
