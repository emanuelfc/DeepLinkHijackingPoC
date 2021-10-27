# DeepLinkHijackingPoC

Create PoC Android Apps for Deep Link Hijacking.
<br><br>

## Description

A script that automates the creation of an Android application which receives deep links of the specified URL, for the purpose of creating a Proof-of-Concept of Deep Link Hijacking for Android Security assessments (Android Penetration Tests).
<br><br>

## Requirements

Python3

adb (Android Debug Bridge) - Optional. Only required for the install option.
<br><br>

## Usage

```
usage: DeepLinkHijacker.py [-h] -l DEEPLINK [-o OUTPUT] [-i]

Deep Link Hijacking Proof-of-Concept Builder - Creates an application for testing Deep Link Hijacking.

optional arguments:
  -h, --help            show this help message and exit
  -l DEEPLINK, --link DEEPLINK
                        Deep Link to hijack using the application.
  -o OUTPUT, --output OUTPUT
                        Output location for application.
  -i, --install         Install application after build.
```

<br>

### Example:

Creates the PoC app receiving deep links for "testApp://test/".
```text
python3 DeepLinkHijacker.py -l "testApp://test/"
```

<br>

Creates the PoC app and copies the package to the directory - with the name 'DeepLinkHijackingPoCApp-release.apk', or with the specified name.
```text
python3 DeepLinkHijacker.py -l "testApp://test/" -o "./dir"

python3 DeepLinkHijacker.py -l "testApp://test/" -o "./dir/pocApp.apk"
```

<br>

Creates the PoC app and installs it via 'adb'.
```
python3 DeepLinkHijacker.py -l "testApp://test/" -i
```