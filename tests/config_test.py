"""Configurations"""
# project/tests/test_config.py
#import os


def test_development_config(application):
    """developmental config"""
    application.config.from_object('app.config.DevelopmentConfig')
    assert application.config['DEBUG']
    assert not application.config['TESTING']
#    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:////home/myuser/database/db.sqlite'


def test_testing_config(application):
    """testing config"""
    application.config.from_object('app.config.TestingConfig')
    assert application.config['DEBUG']
    assert application.config['TESTING']
    assert not application.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///'

def test_production_config(application):
    """production config"""
    application.config.from_object('app.config.ProductionConfig')
    assert not application.config['DEBUG']
    assert not application.config['TESTING']
#    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:////home/myuser/database/db.sqlite'
