import os

# directory path of the .smali files
directory = "./"

ignored_packages = [
    "google", "android",
    "kotlin", "kotlinx",
    "java", "javax",
]

ignored_methods = [
    "handleMessage",
    "executeGLThreadJobs",
    "isFinishing",
    "access$300"
]

with open("./trace.smali", "r") as f:
    static_void_trace = f.read()

for root, dir_, filenames in os.walk(directory):
    if any(x in root for x in ignored_packages):
        print("package ignored:", root)
        continue
    for filename_ in filenames:
        filename = os.path.join(root, filename_)
        if "trace" in filename:
            continue
        print(filename)
        package_name = ""
        if filename.endswith(".smali"):
            filepath = os.path.join(directory, filename)

            with open(filepath, "r") as file:
                lines = file.readlines()

            with open(filepath, "w") as file:
                i = 0

                def strip_line(i_):
                    return lines[i_].strip()

                def method_predicate(signature):
                    return not "abstract" in signature \
                        and not "native" in signature

                def is_ignored_method(signature):
                    return signature is None or \
                        any(x in signature for x in ignored_methods)

                class_name = None
                trace_added = False
                method_name = None
                while i < len(lines):
                    l_i = strip_line(i)
                    if l_i.startswith(".class"):
                        class_name = l_i.split()[-1][1:-1]
                        package_name = ".".join(class_name.split(".")[:-1])
                        print("CLASS: ", class_name, package_name)

                        file.write(lines[i])
                        i += 1
                        continue

                    if l_i.startswith(".method") and not trace_added:
                        if "traceLastMethodCall" not in l_i:
                            file.write("\n" + static_void_trace + "\n" + lines[i])
                        else:
                            file.write(lines[i])
                        i += 1
                        trace_added = True
                        continue
                    elif l_i.startswith(".method"):
                        try:
                            method_name = l_i.split()[-1].split("(")[0]
                        except IndexError:
                            pass

                    if l_i.startswith(".locals") and method_predicate(strip_line(i - 1)) and not is_ignored_method(method_name):

                        locals_count = int(l_i.split()[1])
                        file.write("\n    .locals {}\n".format(locals_count))
                        if class_name is not None:
                            file.write(f"    invoke-static {{}}, L{class_name};->traceLastMethodCall()V\n")
                        i += 1
                        continue

                    file.write(lines[i])
                    i += 1
