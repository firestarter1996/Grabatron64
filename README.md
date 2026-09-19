# Grabatron64

**Grabatron 1.5.5** (Future Games of London, 2012) on a 64-bit-only Pixel 8 Pro.

Grabatron is © Future Games of London / Ubisoft; this is a fan compatibility build of the delisted 2012 Android release, not affiliated with or endorsed by them.

## Why it just works
The APK is pure Java (no `lib/` directory at all), so it is ABI-independent — nothing had to be recompiled. Android 14 only refuses it because of its ancient target SDK:

```
settings put global package_verifier_enable 0     # INSTALL_FAILED_VERIFICATION_FAILURE otherwise
pm install --bypass-low-target-sdk-block Grabatron-Unlimited-1.5.5.apk
settings put global package_verifier_enable 1
```

## Builds (see Releases)
- `Grabatron-1.5.5-original.apk` — untouched FGOL-signed APK (Internet Archive `com.fgol.grabatron`).
- `Grabatron-Unlimited-1.5.5.apk` — same package (`com.fgol.grabatron1`) and title, crystal total forced to 999,999 (`scripts/make_unlimited.py`), re-signed; the FGOL-signed original must be uninstalled first (different signature).

On first launch the game may open its (dead) Facebook dashboard — tap **Return to Game**.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=heyitsj0n/Grabatron64&type=Date)](https://star-history.com/#heyitsj0n/Grabatron64&Date)
