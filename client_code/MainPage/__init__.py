from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MainPage(MainPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('ContactForm')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('AboutForm')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('EnterText')
