import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import fitz

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
#@anvil.server.callable
#def add_contacts(name, email, help):
#  app_tables.page.add_row(name=name, email=email, help=help)

@anvil.server.callable
def add_contacts(name, email, help):
    # Basic validation to ensure no fields are empty
    if not name or not email or not help:
        raise ValueError("All fields must be filled in")

    try:
        # Add a new row to the Contacts table
        app_tables.contactable.add_row(name=name, email=email, help=help)
        return "Contact information submitted successfully!"
    
    except Exception as e:
        # Handle any errors that occur during the database operation
        raise RuntimeError(f"An error occurred while adding the contact: {e}")

@anvil.server.callable
def extract_text_from_pdf(file):
  pdf_document = fitz.open(stream=file.get_bytes(), filetype="pdf")
  text = ""
  for page in pdf_document:
    text+=page.get_text()
  return text