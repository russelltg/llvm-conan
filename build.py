from conan.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager()
    
    if platform.system() == "Windows":
         for shared in [False]: # TODO: add shared
            for build_type in ["Debug", "Release"]:
                for vers in builder.visual_versions:
                    for runtimes in builder.visual_runtimes:
                        builder.add({"arch": "x86_64",
                                     "build_type": build_type,
                                     "compiler": "Visual Studio",
                                     "compiler.version": vers,
                                     "compiler.runtime": runtimes},
                                    {"llvm:shared": shared})
    else:
        builder.add_common_builds()
    
    builder.run()
