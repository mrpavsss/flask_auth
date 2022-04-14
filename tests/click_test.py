"""This file checks to see if logs directory was created in the click test"""

import os

from click.testing import CliRunner

from app import create_log_folder

runner = CliRunner()


def test_add():
    """THis checks logs folder creation"""
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../logs')
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) == False
