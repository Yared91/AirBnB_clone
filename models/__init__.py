#!/usr/bin/python3`
""" __init__ creates a unique file storage instance"""
import models
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
