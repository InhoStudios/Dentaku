from action import Action 
from fbchat import Message
from fbchat import Mention

class ping(Action):

  def run(self):
    response_text = "@" + self.author.first_name + "Pong! Repl.it works for this!"
    mentions = [Mention(self.author_id, length = len(self.author.first_name) + 1)]

    self.client.send(
      Message(text = response_text, mentions = mentions),
      thread_id = self.thread_id,
      thread_type = self.thread_type
    )

  def define_documentation(self):
    self.documentation = {
      "parameteres": "None",
      "function": "Undefined"
    }