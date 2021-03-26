from wox import Wox
import os

class Main(Wox):

  def query(self, userInput):
    return [{
      'Title': 'Enter Artist / Album / Song name...',
      'SubTitle': 'Search for: ' + userInput,
      'IcoPath': 'Images/pic.png',
      'JsonRPCAction': {
        'method': 'action',
        'parameters': [userInput],
        'dontHideAfterAction': False
      }
    }]

  def action(self, query):
    # ToDo :: Search on YouTubeMusic
    url = 'https://music.youtube.com?q=' + query


if __name__ == '__main__':
  Main()
