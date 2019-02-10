cmake_minimum_required(VERSION 3.5)
project(PackageTest CXX)

generate_arduino_firmware(${PROJECT_NAME} SKETCH example.ino
                          # ARDLIBS StandardCplusplus
                          )
