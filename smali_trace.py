import os

# directory path of the .smali files
directory = "./"

static_void_trace="""
.method public static traceLastMethodCall()V
    .locals 5

    .line 27
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Thread;->getStackTrace()[Ljava/lang/StackTraceElement;

    move-result-object v0

    const/4 v1, 0x3

    aget-object v0, v0, v1

    .line 28
    .local v0, "s":Ljava/lang/StackTraceElement;
    const-string v1, " "

    .line 29
    .local v1, "space":Ljava/lang/String;
    sget-object v2, Ljava/lang/System;->out:Ljava/io/PrintStream;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0}, Ljava/lang/StackTraceElement;->getFileName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v0}, Ljava/lang/StackTraceElement;->getClassName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v0}, Ljava/lang/StackTraceElement;->getMethodName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/io/PrintStream;->println(Ljava/lang/String;)V

    .line 30
    return-void
.end method
"""

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
