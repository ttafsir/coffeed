#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coffeed_project.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coffeed.settings")
>>>>>>> a3cae2367010b0b071e5943437dc8e44353371cc

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
