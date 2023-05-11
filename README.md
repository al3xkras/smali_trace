### Smali trace injection

An improved implementation of the smali trace injection script

An alternative implementation of the smali trace: https://github.com/soulseekah/smalter - does not consider methods containing >= 16 registers, which complicates the injection of additional variables. 
The problem is corrected in this project (see ```smali_trace.py```), and tested independently by using ```adb logcat```


In the decompilation process of .smali source files, the following tools were used:
- ApkStudio: https://github.com/vaibhavpandeyvpz/apkstudio
- ApkTool (v 2.7.0): https://github.com/iBotPeaches/Apktool, 
- Jadx (v 17.0.5): https://github.com/skylot/jadx
- Uber APK Signer (1.3.0): https://github.com/patrickfav/uber-apk-signer
- ADB (v 1.0.41), 

#### The purpose of the project:
> Add method execution trace to all .smali classes in a package directory. (Injection of PrintStream calls 
> into each and every method.)

#### Capabilities:
- The script supports trace injection for all methods, only excluding methods which are defined as <b>abstract</b> or <b>native</b> (by definition, these methods can not be traced).

#### Additional notes:
- The 4-bit <b>.locals<b> (<b>.registers</b>) reference limit 
- System.out.println is used in favor of android.util.Log.i,
because it does not require the application context to be initialized). It is important to note, that some devices may not support System.out.println output in the ```adb logcat```.



Usage: smalter.py <classes dir> [classes dir] [classes dir] ...

smali 'em back up and watch the logs ;) shhh...