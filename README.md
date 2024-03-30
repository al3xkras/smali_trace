## Smali trace

A script that automatically injects adb-logcat [System.out.println] calls in an ApkTool-decompiled Android project.

- Supports any method calls, regardless of the number of used registries. (except those defined as <b>abstract</b> or <b>native</b>)

#### Decompilation of the source code
The script was tested for the following APK decompiler and its dependencies:
- ApkStudio: https://github.com/vaibhavpandeyvpz/apkstudio
- ApkTool (version 2.7.0): https://github.com/iBotPeaches/Apktool,
- Jadx (version 17.0.5): https://github.com/skylot/jadx
- Uber APK Signer (1.3.0): https://github.com/patrickfav/uber-apk-signer
- ADB (version 1.0.41)
<br>

Notes:
- [System.out.println] is not enabled in all Android devices by default.
