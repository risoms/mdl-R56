#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:52:04 2019

@author: mdl-admin
"""
# import
from pdb import set_trace as breakpoint
from pathlib import Path

class DisplayablePath():
	display_filename_prefix_middle = '├──'
	display_filename_prefix_last = '└──'
	display_parent_prefix_middle = '    '
	display_parent_prefix_last = '│   '

	def __init__(self, path, parent_path, is_last):
		self.path = Path(str(path))
		self.parent = parent_path
		self.is_last = is_last
		if self.parent:
			print(path)
			self.depth = self.parent.depth + 1
		else:
			self.depth = 0

	@classmethod
	def exclude(cls, child, exclude_extension=None, exclude_files=None, exclude_folders=None, exclude_all_files=False):
		# exclude_extension
		if exclude_extension is not None:
			# find file extensions
			if Path(child).suffix in exclude_extension:
				return None
		# exclude_files
		if exclude_files is not None:
			if str(child.name) in exclude_files:
				return None
				
		# exclude_folders
		if exclude_folders is not None:
			if str(child.name) in exclude_folders:
				return None
				
		# exclude_all_files
		if exclude_all_files is True:
			if not child.is_dir():
				return None
		
		return child

	@classmethod
	def make_tree(cls, root, parent=None, is_last=False, criteria=None, exclude_extension=None, exclude_files=None, exclude_folders=None, exclude_all_files=False):
		"""[summary]
		
		Parameters
		----------
		root : [type]
			[description]
		parent : [type], optional
			[description], by default None
		is_last : bool, optional
			[description], by default False
		criteria : [type], optional
			[description], by default None
		exclude_extension : [type], optional
			[description], by default None
		exclude_files : [type], optional
			[description], by default None
		exclude_folders : [type], optional
			[description], by default None
		exclude_all_files : [type], optional
			[description], by default False
		"""
		root = Path(str(root))
		criteria = criteria or cls._default_criteria

		displayable_root = cls(root, parent, is_last)
		yield displayable_root
		# get list of files
		children = sorted(list(path for path in root.iterdir() if criteria(path)), key=lambda s: str(s).lower())		
		count = 1
		for path in children:
			path = cls.exclude(child=path, exclude_extension=exclude_extension, exclude_files=exclude_files, 
					  exclude_folders=exclude_files, exclude_all_files=exclude_files)
			if path is None:
				continue
			is_last = count == len(children)
			if path.is_dir():
				yield from cls.make_tree(path, parent=displayable_root, is_last=is_last, criteria=criteria)
			else:
				yield cls(path, displayable_root, is_last)
			count += 1

	@classmethod
	def _default_criteria(cls, path):
		return True

	@property
	def displayname(self):
		if self.path.is_dir():
			#print(self.path.name)
			return self.path.name + '/'
		return self.path.name

	def displayable(self):
		if self.parent is None:
			return self.displayname

		_filename_prefix = (self.display_filename_prefix_last if self.is_last else self.display_filename_prefix_middle)
		parts = ['{!s} {!s}'.format(_filename_prefix, self.displayname)]

		parent = self.parent
		while parent and parent.parent is not None:
			parts.append(self.display_parent_prefix_middle if parent.is_last else self.display_parent_prefix_last)
			parent = parent.parent

		return ''.join(reversed(parts))

# parameters
doctreepath = Path('/Users/mdl-admin/Desktop/mdl-R56/')
outputpath = Path('/Users/mdl-admin/Desktop/mdl-R56/')
export = []
ex_extension = ['.csv','.pyc','.idx','.pack','.wav','.png','.pyd','.pyc','.dll']
ex_files = ['.git','.DS_Store','.gitignore','.git','.dll','.pyd']
ex_folders = ['DS_Store','.git','__pycache__','.gitignore','include','dist','build','backup','other','__pycache__','rename']
ex_all_files = False

# init
doctree = DisplayablePath.make_tree(root=doctreepath, exclude_extension=ex_extension, exclude_files=ex_files, exclude_folders=ex_folders, exclude_all_files=ex_all_files)
for branch_ in doctree:
	branch = branch_.displayable()
	export.append(branch)
	#print(branch)
## save
output = '\n'.join(export)
with open("%s/doctree.txt"%(outputpath), "w") as file_:
	file_.write(output)
