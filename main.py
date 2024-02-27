import sys

def kofi(username):
    return f"""
<script src='https://storage.ko-fi.com/cdn/scripts/overlay-widget.js'></script>
<script>
  kofiWidgetOverlay.draw('{username}', {{
    'type': 'floating-chat',
    'floating-chat.donateButton.text': 'Support me',
    'floating-chat.donateButton.background-color': '#323842',
    'floating-chat.donateButton.text-color': '#fff'
  }});
</script>
"""

test = False
u = "wolfthedev"

if __name__ == "__main__":
    if test:
      username = u
      print(kofi(username))
    elif len(sys.argv) > 1:
        username = sys.argv[1]
        print(kofi(username))
    else:
        print("Usage: python main.py username")
        sys.exit(1)
