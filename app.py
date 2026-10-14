
from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3
from pathlib import Path
import os

app = Flask(__name__)


