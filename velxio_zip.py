# Packs diagram.json and the sketch sources into .pio/build/<env>/velxio.zip
# after each build, in the Wokwi zip layout that Velxio's "Import project" reads.
# Velxio's zip import does not carry firmware: load firmware.hex afterwards
# with "Upload firmware".
import os
import zipfile

Import("env")

CODE_EXTS = (".ino", ".h", ".hpp", ".cpp", ".cc", ".cxx", ".c")


def make_velxio_zip(source, target, env):
    project_dir = env.subst("$PROJECT_DIR")
    out = os.path.join(env.subst("$BUILD_DIR"), "velxio.zip")
    seen = set()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(project_dir, "diagram.json"), "diagram.json")
        for folder in ("src", "include"):
            for root, _, files in os.walk(os.path.join(project_dir, folder)):
                for name in sorted(files):
                    if not name.endswith(CODE_EXTS):
                        continue
                    if name in seen:  # Velxio flattens paths to basenames
                        print("velxio_zip: skipping duplicate %s" % name)
                        continue
                    seen.add(name)
                    z.write(os.path.join(root, name), name)
        libs = env.GetProjectOption("lib_deps", [])
        if libs:
            z.writestr("libraries.txt", "\n".join(libs) + "\n")
    print("Velxio project: %s" % os.path.relpath(out, project_dir))


env.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", make_velxio_zip)
