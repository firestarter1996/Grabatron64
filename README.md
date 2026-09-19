# Grabatron64

**Grabatron 1.5.5** (Future Games of London, 2012) on a 64-bit-only Pixel 8 Pro.

**Tooling only — bring your own copy of the game.** Grabatron is © Future Games of London / Ubisoft. This repo contains the patch script and notes; no APKs are distributed here. You need your own Grabatron 1.5.5 APK.

## Why it just works
The APK is pure Java (no `lib/` directory at all), so it is ABI-independent — nothing had to be recompiled. Android 14 only refuses it because of its ancient target SDK:

```
settings put global package_verifier_enable 0     # INSTALL_FAILED_VERIFICATION_FAILURE otherwise
pm install --bypass-low-target-sdk-block Grabatron-Unlimited-1.5.5.apk
settings put global package_verifier_enable 1
```

## Builds
No APKs are published here (ours live in a private repo). `scripts/make_unlimited.py` turns your own APK into the 999,999-crystal build, same package (`com.fgol.grabatron1`) and title, re-signed with your key; the FGOL-signed original must be uninstalled first (different signature).

On first launch the game may open its (dead) Facebook dashboard — tap **Return to Game**.
