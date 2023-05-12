import os

# directory path of the .smali files
directory = "./"

with open("./trace.smali","r") as f:
    static_void_trace=f.read()

for root,dir_,filenames in os.walk(directory):
    for filename_ in filenames:
        filename=os.path.join(root, filename_)
        print(filename)
        package_name=""
        if filename.endswith(".smali"):
            filepath = os.path.join(directory, filename)

            with open(filepath, "r") as file:
                lines = file.readlines()

            with open(filepath, "w") as file:
                i = 0

                def l(i_):
                    return lines[i_].strip()

                def method_predicate(signature):
                    return not "abstract" in signature \
                        and not "native" in signature

                while i < len(lines):
                    l_i = l(i)
                    if l_i.startswith(".class"):
                        class_name=l_i.split()[-1][1:-1]
                        package_name = ".".join(class_name.split(".")[:-1])
                        print("CLASS: ",class_name,package_name)

                        file.write(lines[i])
                        i+=1
                        continue

                    if l_i.startswith(".source"):
                        file.write(l_i+static_void_trace)
                        i+=1
                        continue

                    if l_i.startswith(".locals") and method_predicate(l(i-1)):
                        locals_count = int(l_i.split()[1])
                        file.write(".locals {}\n".format(locals_count))
                        file.write(f"    invoke-static {{}}, L{class_name};->traceLastMethodCall()V\n")
                        i+=1
                        continue

                    file.write(lines[i])
                    i += 1
