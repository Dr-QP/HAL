from conans import ConanFile, CMake
import os

class HalarduinoTestConan(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def test(self):
        os.chdir("bin")
        # Tests need to be uploaded to Arduino to run. So do nothing for now
        # self.run(".%sexample" % os.sep)
