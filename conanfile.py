from conans import ConanFile, CMake


class HalarduinoConan(ConanFile):
    name = "HAL"
    version = "develop"
    license = "Apache License, Version 2.0. https://www.apache.org/licenses/LICENSE-2.0"
    url = "https://github.com/Dr-QP/HALArduino"
    author = "Anton Matosov (anton.matosov@gmail.com)"
    description = """HAL layer.
 - Arduino implementation:\n
conan test_package -s compiler=gcc -s compiler.version=4.9 -s compiler.libcxx=libstdc++11 -s os="Arduino" -s arch=avr --build=missing"""
    
    options = {"shared": [True, False]}
    default_options = "shared=False", "Boost:shared=False"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    exports_sources = "include/*", "src/*", "!build/*", "!test_package/*", "CMakeLists.txt"

    def configure(self):
        self.options["Boost"].shared = self.options.shared

    def requirements(self):
        if self.settings.os != "Arduino":
            self.requires("boost/1.69.0@conan/stable")

    def build_requirements(self):
        if self.settings.os == "Arduino":
            self.build_requires("arduino-toolchain/[>1.8]@conan/testing")

    def imports(self):
        self.copy("*.dll", "", "bin")
        self.copy("*.dylib", "", "lib")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        if self.settings.os == "Arduino":
            self.copy("*.h", dst="include", src="src/arduino", keep_path=False)
        else:
            self.copy("*.h", dst="include", src="src/unix", keep_path=False)
        self.copy("*.h", dst="include", src="include")
        self.copy("*HAL*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.cppflags = ['-std=c++11']
        self.cpp_info.libs = ["HAL"]
