# -*- mode: python -*-
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, hookspath
from kivy.deps import sdl2, glew
block_cipher = None


a = Analysis(['2.0.py'],
	pathex=['C:\\Users\\sr38553\\Desktop\\projects\\work\\R56\\#app','C:\Users\sr38553\Documents\WinPython\x32\python-2.7.10\share\sdl2\bin'],
	binaries=[],
	datas=[],
	hookspath=hookspath(),
	runtime_hooks=[],
	win_no_prefer_redirects=False,
	win_private_assemblies=False,
	cipher=block_cipher,
	**get_deps_minimal(video=None, audio=None))

pyz = PYZ(a.pure, a.zipped_data,
	cipher=block_cipher)

exe = EXE(pyz,
	a.scripts,
	a.binaries,
	a.zipfiles,
	a.datas,
	name='gui',
	debug=False,
	strip=False,
	upx=True,
	console=True,
	icon='app.ico')

coll = COLLECT(exe,
	Tree('C:\\Users\\sr38553\\Documents\\WinPython\\x32\\python-2.7.10\\share\\glew\\bin\\'),
	Tree('C:\\Users\\sr38553\\Documents\\WinPython\\x32\\python-2.7.10\\share\\sdl2\\bin\\'),
	a.binaries,
	a.zipfiles,
	a.datas,
	strip=False,
	upx=True,
	name='gui')