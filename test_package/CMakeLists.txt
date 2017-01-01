find_package(LLVM REQUIRED CONFIG)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

llvm_map_components_to_libnames(llvm_libs core irreader support bitwriter executionengine native nativecodegen interpreter linker orcjit mcjit codegen )

add_executable(LLVMTest main.cpp)
target_link_libraries(LLVMTest ${llvm_libs})
target_include_directories(LLVMTest ${LLVM_INCLUDE_DIRS})


