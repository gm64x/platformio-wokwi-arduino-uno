# Include the AVR toolchain headers (avr-libc, libstdc++) in compile_commands.json
# so clangd can resolve <avr/io.h> and friends.
Import("env")

env.Replace(COMPILATIONDB_INCLUDE_TOOLCHAIN=True)
