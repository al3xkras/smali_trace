import os

directory = "./"

ignored_packages = [
    "google", "android",
    "kotlin", "kotlinx",
    "java", "javax",
]

ignored_methods = set()

with open("./trace.smali", "r") as f:
    static_void_trace = f.read()

for root, dir_, filenames in os.walk(directory):
    if any(x in root for x in ignored_packages):
        print("package ignored:", root)
        continue
    for filename_ in filenames:
        if "trace" in filename_:
            continue
        filename = os.path.join(root, filename_)
        print(filename)
        package_name = ""
        if filename.endswith(".smali"):
            filepath = os.path.join(directory, filename)

            with open(filepath, "r") as file:
                lines = [x+"\n" for x in file.read().replace(static_void_trace, "\n").split("\n")]

            with open(filepath, "w") as file:
                i = 0


                def strip_line(i_):
                    return lines[i_].strip()


                def method_predicate(signature):
                    return not "abstract" in signature \
                        and not "native" in signature


                class_name = None
                trace_added = False
                method_name = None
                trace_line = "traceLastMethodCall"
                while i < len(lines):
                    l_i = strip_line(i)
                    if l_i.startswith(".class"):
                        class_name = l_i.split()[-1][1:-1]
                        package_name = ".".join(class_name.split(".")[:-1])
                        print("CLASS: ", class_name, package_name)

                        file.write(lines[i])
                        i += 1
                        continue

                    if l_i.startswith(".method"):
                        file.write(l_i)
                        i += 1
                        trace_added = True
                        try:
                            method_name = l_i.split()[-1].split("()")[0]
                        except IndexError:
                            pass
                        print("METHOD: ", method_name)
                        continue

                    if method_name not in ignored_methods \
                            and trace_line in lines[i]:
                        print("trace removed:", class_name, method_name)
                        i += 1
                    elif method_name in ignored_methods \
                            and trace_line in lines[i]:
                        print("method skipped:", class_name, method_name)

                    file.write(lines[i])
                    i += 1
