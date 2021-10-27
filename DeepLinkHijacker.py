#!/usr/bin/env python3

from typing import NoReturn
import argparse
from lxml import etree
import urllib.parse
import platform
import os
import subprocess
import shutil

ANDROID_MANIFEST_PATH = "DeepLinkHijackingPoCApp/app/src/main/AndroidManifest.xml"

APK_LOCATION = "DeepLinkHijackingPoCApp/app/build/outputs/apk/release/DeepLinkHijackingPoCApp-release.apk"

def insertDeepLink(manifestFile: str, deepLink: str) -> None:

	xmlParser = etree.XMLParser()
	manifestTree = etree.parse(manifestFile, parser=xmlParser)
	manifestRoot = manifestTree.getroot()

	deepLinkIntent = manifestRoot.xpath("./application/activity/intent-filter/data[@android:scheme and @android:host]", namespaces=manifestRoot.nsmap)[0]

	baseAttribute = "{" + manifestRoot.nsmap["android"] + "}"

	parsedDeepLink = urllib.parse.urlparse(deepLink)

	deepLinkIntent.attrib[baseAttribute + "scheme"] = parsedDeepLink.scheme

	if not parsedDeepLink.netloc:
		deepLinkIntent.attrib[baseAttribute + "host"] = "*"
	else:
		deepLinkIntent.attrib[baseAttribute + "host"] = parsedDeepLink.netloc

	manifestTree.write(manifestFile, pretty_print=True, xml_declaration=True, encoding="utf-8")

def runCommand(command: list) -> NoReturn:
	result = subprocess.run(command)
	result.check_returncode()

def buildAPK() -> NoReturn:

	gradleExecutable = ""

	if platform.system() == "Linux":
		gradleExecutable = "gradlew"
	elif platform.system() == "Windows":
		gradleExecutable = "gradlew.bat"
	else:
		print("Script only supports Linux and Windows systems.")
		exit(1)

	runCommand([os.path.join("DeepLinkHijackingPoCApp", gradleExecutable), '-pDeepLinkHijackingPoCApp', 'assembleRelease'])

def main() -> NoReturn:

	parser = argparse.ArgumentParser(description = 'Deep Link Hijacking Proof-of-Concept Builder - Creates an application for testing Deep Link Hijacking.')

	parser.add_argument('-l', '--link', dest = 'deeplink', required = True, help = 'Deep Link to hijack using the application.')
	parser.add_argument('-o', '--output', dest = 'output', help = 'Output location for application.')
	parser.add_argument('-i', '--install', dest = 'install', action = "store_true", default = False, help = 'Install application after build.')

	args = parser.parse_args()

	insertDeepLink(ANDROID_MANIFEST_PATH, args.deeplink)
	buildAPK()

	if args.output:
		shutil.copy(APK_LOCATION, args.output)
	
	if args.install:
		runCommand(['adb', 'install', APK_LOCATION])

if __name__ == "__main__":
	main()

# References / Help
# https://stackoverflow.com/questions/57841507/navigation-components-deeplink-using-uri-depending-buildtype
# https://stackoverflow.com/questions/67487009/running-gradle-build-from-a-parent-folder