#!/usr/bin/env python3
"""Grabatron 1.5.5 -> "Unlimited" (999,999 crystals), same package name and title.
Usage: python3 make_unlimited.py grabatron.apk apktool.jar keystore.jks alias
Every smali store to FrontEnd.totalCrystals is preceded by `const vX, 0xf423f`, so the total is
always 999,999 (buy every ship / upgrade / unlock / extra life). Requires Java 21, apktool 2.10,
zipalign + apksigner (Android build-tools 34)."""
import glob, os, re, shutil, subprocess, sys
apk, apktool, ks, alias = sys.argv[1:5]
pw = os.environ.get("KS_PASS") or open(os.path.join(os.path.dirname(ks), "keystore.pass")).read().strip()
shutil.rmtree("gdec", ignore_errors=True)
subprocess.run(["java", "-jar", apktool, "d", "-o", "gdec", apk], check=True)
n = 0
for f in glob.glob("gdec/smali/**/*.smali", recursive=True):
    s = open(f, encoding="utf-8").read()
    if "Lcom/fgol/game/FrontEnd;->totalCrystals:I" not in s: continue
    s2, k = re.subn(r"    sput (v\d+|p\d+), Lcom/fgol/game/FrontEnd;->totalCrystals:I",
                    r"    const \1, 0xf423f\n    sput \1, Lcom/fgol/game/FrontEnd;->totalCrystals:I", s)
    if k: open(f, "w", encoding="utf-8").write(s2); n += k
print("patched", n, "crystal stores")
subprocess.run(["java", "-jar", apktool, "b", "gdec", "-o", "unl_unsigned.apk"], check=True)
bt = os.environ.get("BUILD_TOOLS", "")
subprocess.run([os.path.join(bt, "zipalign"), "-f", "-p", "4", "unl_unsigned.apk", "unl_aligned.apk"], check=True)
subprocess.run(["java", "-jar", os.path.join(bt, "lib", "apksigner.jar"), "sign", "--ks", ks, "--ks-key-alias", alias,
                "--ks-pass", "pass:" + pw, "--key-pass", "pass:" + pw, "--out", "Grabatron-Unlimited-1.5.5.apk", "unl_aligned.apk"], check=True)
print("done: Grabatron-Unlimited-1.5.5.apk")
