from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "dev")
username = os.getenv("CONAN_USERNAME", "anton-matosov")


class HalunixTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "HALUnix/develop@%s/%s" % (username, channel)
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
        self.run(".%sexample" % os.sep)
