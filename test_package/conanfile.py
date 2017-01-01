from conans import CMake, ConanFile
import os

channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "russelltg")

class LLVMTest(ConanFile):
    name = "llvmTest"
    requires = "llvm/3.9.0@{}/{}".format(username, channel)
    
    
    settings = "os", "arch", "compiler", "build_type"
    generators="cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run("cmake {} {}".format(self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . {}".format(cmake.build_config))
    
    def test(self):
        self.run("./LLVMTest")
    
