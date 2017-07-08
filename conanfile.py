from conans import ConanFile
import os


class HalConan(ConanFile):
    name = "HAL"
    version = "develop"
    license = "Apache License, Version 2.0. https://www.apache.org/licenses/LICENSE-2.0"
    url = "https://github.com/Dr-QP/HAL"
    author = "Anton Matosov (anton.matosov@gmail.com)"
    description = "HAL layer interfaces"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*", "!build/*", "!test_package/*"

    def package(self):
        self.copy("*.h", dst="include", src="include")

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.cppflags = ['-std=c++11']
