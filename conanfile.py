from conans import ConanFile, CMake
import conans.tools as tools
import tarfile
import os
import platform
import multiprocessing
import sys

class LLVM(ConanFile):
    name = "llvm"
    version = "3.9.1"
    generators = "cmake"
    
    url = "https://github.com/russelltg/llvm-conan"
    license = "http://releases.llvm.org/{}/LICENSE.TXT".format(version)
    

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    
    folder_name = "llvm-{}.src".format(version)
    
    def source(self):
        tarName = "{}.tar.xz".format(self.folder_name)
        tarUrl = "http://releases.llvm.org/{}/{}".format(self.version, tarName)
        tools.download(tarUrl, tarName)
        self.output.info("Using version {} of python".format(sys.version_info))
        with tarfile.open(tarName, "r:xz") as tar:
            tar.extractall()
        
    def build(self):
        cmake = CMake(self.settings)
        
        sharedSetting = ""
        if(self.options.shared):
            sharedSetting = "ON"
        else:
            sharedSetting = "OFF"
            
        self.run("cmake {} {} -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS={}".format(
            os.path.join(self.conanfile_directory, self.folder_name), 
            cmake.command_line, 
            os.path.join(self.conanfile_directory, "install"), 
            sharedSetting))
        
        if platform.system() != "Windows":
            self.run("make -j{}".format(multiprocessing.cpu_count()))
        else:
            self.run("cmake --build . --target install {}".format(cmake.build_config))

    def package(self):
        self.copy(pattern="*", dst="", src=os.path.join(self.conanfile_directory, "install"))
        
        
        
    
