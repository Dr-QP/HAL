from conans import ConanFile, CMake, tools
import os


class HalConan(ConanFile):
    name = "HAL"
    version = "develop"
    license = "Apache License, Version 2.0. https://www.apache.org/licenses/LICENSE-2.0"
    url = "https://github.com/Dr-QP/HAL"
    author = "Anton Matosov (anton.matosov@gmail.com)"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def package(self):
        self.copy("*.h", dst="include", src=".")

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.cppflags = ['-std=c++11']
