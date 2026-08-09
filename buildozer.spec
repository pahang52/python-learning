[app]

title = Python Quest
package.name = pythonquest
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json,ogg,mp3,wav

version = 0.2.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.accept_sdk_license = True

android.api = 33
android.minapi = 21
android.ndk_api = 21

# این خط مهم را اضافه کن
android.build_tools_version = 33.0.2

android.archs = arm64-v8a
android.allow_backup = True
android.skip_update = True

log_level = 2
warn_on_root = 1

# برای رفع مشکل aidl
p4a.bootstrap = sdl2
