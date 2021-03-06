from conans import ConanFile, CMake
import conans.tools as tools
import os
import platform
import multiprocessing

class LLVM(ConanFile):
    name = "llvm"
    version = "3.9.0"
    generators = "cmake"
    
    url = "https://github.com/russelltg/llvm-conan"
    license = "http://releases.llvm.org/{}/LICENSE.TXT".format(version)
    

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    
    folder_name = "llvm"
    
    # clone the source
    def source(self):
        self.run("git clone https://github.com/llvm-mirror/llvm -b release_39 --depth 1")
        
    def build(self):
        cmake = CMake(self.settings)
        
        sharedSetting = ""
        if(self.options.shared):
            sharedSetting = "ON"
        else:
            sharedSetting = "OFF"
            
        self.run('cmake {} {} -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS={} -DLLVM_TARGETS_TO_BUILD="X86"'.format(
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
        
    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
        self.env_info.LLVM_DIR = self.package_folder # for cmake finding
        
    
