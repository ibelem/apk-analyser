# apk-analyser
Android APK Analyser especially for Crosswalk/Intel XDK Apps.

# platform
* Host OS: Linux 
* Bugs on Windows, will not fix them until there are users need it. 

# environment
* Java JDK 1.5 or greater http://www.oracle.com/technetwork/java/javase/downloads/index.html
* Python 2.7 https://www.python.org/download/
* Android SDK installed http://developer.android.com
* Install and set environment for apktool: https://code.google.com/p/android-apktool/wiki/Install

# how to run
A:<br/>
	`1. cd &lt;pathto&gt;/apk-analyser`<br/>
	`2. Put Android apks into "apks" folder`<br/>
	`3. python main.py`<br/>

B. <br/>
	`1. cd &lt;pathto&gt;/apk-analyser`<br/>
	`2. python main.py -p &lt;pathto&gt;/xxx.apk`<br/>

C. <br/>
	`python &lt;pathto&gt;/apk-analyser/main.py -p <pathto>/xxx.apk`<br/>

# Review results
* Get results in `&lt;pathto&gt;/apk-analyser/result` folder.<br/>
* If run the third method, please copy "`apk-analyser/result/apk-analyser-result.xsl`" to `&lt;current dir&gt;/result` folder.

