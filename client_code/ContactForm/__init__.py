from ._anvil_designer import ContactFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ContactForm(ContactFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.confirmation_label.text = ""
    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name_box.text
    email = self.email_box.text
    help = self.help_box.text 
 
    # Basic validation to check if all fields are filled.
    if not name or not email or not help:
      self.confirmation_label.text = "Please fill in all fields."
      return
    
    try:
      # Server call to add contact information.
      response = anvil.server.call('add_contacts', name, email, help)
      # Display success message.
      self.confirmation_label.text = response
      
      # Clear the text boxes after submission.
      self.name_box.text = ""
      self.email_box.text = ""
      self.help_box.text = ""
    
    except Exception as e:
      # Display error message if server call fails.
      self.confirmation_label.text = f"Failed to submit contact information: {e}"