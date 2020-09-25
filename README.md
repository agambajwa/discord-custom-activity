# discord-custom-activity
Custom Activity for users on Discord

## Installation
1. Download or clone this repository.

2. Install all requirements 
   ```bash
   pip install -r requirements.txt
   ```
   
## Usage
This is how it will look - 

<img src = "images/Five.jpg">

1. Go to [Discord Developer's](https://discord.com/developers/applications) site to create a new application. 

2. Click on New Application. <br>
   <img src = "images/One.jpg">

3. Give a name for your activity. <br>
   <img src = "images/Two.jpg">
   
4. Copy the client ID <br>
   <img src = "images/Three.jpg">

5. Paste the client ID in ``config.ini`` file.
   ```
   [CLIENT]
   client_id=759023045418680320
   ```
      
6. You can upload image assets under Rich Presence -> Art Assets. <br>
   <img src = "images/Four.jpg">

7. Edit ``base_activity`` from ``app.py`` to your own custom text and images. Check Rich Presence -> Visualizer to see how the images work.
   ```python
   base_activity = {
      'details': 'Custom details',
      'state' : 'Custom state',
      'assets': {
          'large_image': 'image_name',
          'large_text': 'Image text',
          'small_image': 'small_image_name',
          'small_text': 'Small image text'
      },
      'party': {
          'size': [1, 5]
      }
   }
    ```
      
8. Run the program
   ```bash
   python app.py
   ```
