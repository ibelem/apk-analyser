# Apk Analyser
Android APK Analyser especially for Crosswalk/Intel XDK Apps.

# Platform
* Host OS: Linux Ubuntu

# Environment
* Java JDK 1.5 or greater http://www.oracle.com/technetwork/java/javase/downloads/index.html
* Python 2.7 https://www.python.org/download/
* Android SDK installed http://developer.android.com
* Install and set environment for apktool: https://code.google.com/p/android-apktool/wiki/Install

# How to Run
A.
  1. `cd <pathto>/apk-analyser`
  2. `Put Android apks into "apks" folder`
  3. `python main.py`

B.
  1. `cd <pathto>/apk-analyser`
  2.a. `python main.py -p <pathto>/xxx.apk`
  2.b. `python main.py -p <pathto>/<apk folder>`
	
C.
  a. `python <pathto>/apk-analyser/main.py -p <pathto>/xxx.apk`
  b. `python <pathto>/apk-analyser/main.py -p <pathto>/<apk folder>`
	
# Review Results
* Get results in `<pathto>/apk-analyser/result` folder.
* If run the third method, please copy "`apk-analyser/result/apk-analyser-result.xsl`" to `<current dir>/result` folder.
* Launch local `apk-analyser-result_<date>_<time>.xml` by Firefox or IE. For Google Chrome`[1]`, need to access `.xml` and `.xsl` via url on web server.

`[1]` Google Chrome is unable to perform an xsl transform on a local xml file due to a security concern that blocking XML files from accessing local XSLT files in the same directory.

