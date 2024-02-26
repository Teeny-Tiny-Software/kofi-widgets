import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <kofi-username>")
        sys.exit(1)
    
    name = sys.argv[1]
    
    print(f"""<script src='https://storage.ko-fi.com/cdn/scripts/overlay-widget.js'></script>\n
        <script>\n
          kofiWidgetOverlay.draw('{name}', {\n
            'type': 'floating-chat',\n
            'floating-chat.donateButton.text': 'Support me',\n
            'floating-chat.donateButton.background-color': '#323842',\n
            'floating-chat.donateButton.text-color': '#fff'\n
          });\n
        </script>""")