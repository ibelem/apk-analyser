# apk-analyser
Android APK Analyser especially for Crosswalk/Intel XDK Apps.

platform
========================================================
* Host OS: Linux 
* Bugs on Windows, will not fix them until there are users need it. 

environment:
========================================================
* Java JDK 1.5 or greater http://www.oracle.com/technetwork/java/javase/downloads/index.html
* Python 2.7 https://www.python.org/download/
* Android SDK installed http://developer.android.com
* Install and set environment for apktool: https://code.google.com/p/android-apktool/wiki/Install

# how to run:
========================================================
A:
	1. cd <pathto>/apk-analyser<br/>
	2. Put Android apks into "apks" folder
	3. python main.py

B. 
	1. cd <pathto>/apk-analyser
	2. python main.py -p <pathto>/xxx.apk

C. 
	python <pathto>/apk-analyser/main.py -p <pathto>/xxx.apk

# Review results:
========================================================
Get results in &lt;current dir&gt;/result folder.
If you run the third methods, please copy "apk-analyser/result/apk-analyser-result.xsl" to &lt;current dir&gt;/result folder.

