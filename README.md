## Smali trace injection


A tool that helps automatically track method calls in a decompiled Android project.
<br>
<br>

#### Features:
- The script supports tracing for all methods except methods defined as <b>abstract</b> or <b>native</b>.
  <br>
  <br>

#### Decompilation of the source code
The following tools (for which the script has been tested) are required to decompile the APK sources:
- ApkStudio: https://github.com/vaibhavpandeyvpz/apkstudio
- ApkTool (version 2.7.0): https://github.com/iBotPeaches/Apktool,
- Jadx (version 17.0.5): https://github.com/skylot/jadx
- Uber APK Signer (1.3.0): https://github.com/patrickfav/uber-apk-signer
- ADB (version 1.0.41)
<br>


#### Additional notes:
- Alternative implementation of smali tracing: https://github.com/soulseekah/smalter - does not consider methods containing >= 16 registers, making it difficult to introduce new registers and variables.
      
  The problem can be avoided in the [project](https://github.com/al3xkras/smali_trace) using StackTrace and static method calls (see ```smali_trace.py```)
  <br><br>
- ```System.out.println``` is used in favor of ```android.util.Log``` in order to avoid application context initialization exceptions.
  <br>
- ```System.out.println``` calls could be disabled by default for some Android devices (although, most modern AOSP-based ROMs support this feature).


<i>Any suggestions or contributions to the project would be appreciated.</i>