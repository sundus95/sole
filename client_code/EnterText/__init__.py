from ._anvil_designer import EnterTextTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class EnterText(EnterTextTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def get_clean_text_click(self, **event_args):
    """This method is called when the button is clicked"""
    file = self.file_loader_1.file
    if file:
      text = anvil. server.call('extract_text_from_pdf', file)
      self.clean_text.text = text
    else:
      alert("Please upload a pdf file.")
