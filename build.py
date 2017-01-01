from conan.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager()
    
    if platform.system() == "Windows":
        builder.add_common_builds()
    
    if platform.system() == "Linux":
        for shared in [True, False]:
            for build_type in ["Debug", "Release"]:
                for gccver in builder.gcc_versions:
                    builder.add({"arch": "x86_64",
                                "build_type": build_type,
                                "compiler": "gcc",
                                "compiler.version": gccver,
                                "compiler.libcxx": "libstdc++11"},
                                {"llvm:shared": shared})

    if platform.system() == "Darwin":
        for shared in [True, False]:
            for compiler_version in builder.apple_clang_versions:
                for build_type in ["Debug", "Release"]:
                    builder.add({"arch": "x86_64",
                                 "build_type": build_type,
                                 "compiler": "apple-clang",
                                 "compiler.version": compiler_version,
                                 "llvm:shared": shared})
