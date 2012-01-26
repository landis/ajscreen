import kivy
kivy.require('1.0.9') 

from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.uix.settings import Settings
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label

Config.set('graphics', 'fullscreen', 1)
#Config.set('graphics', 'width', 1024)
#Config.set('graphics', 'height', 768)
#Config.write()


class Picture(Scatter):

	source = StringProperty(None)
	

class AjScreenApp(App):

    def build(self):
        # the root is created in pictures.kv
        root = self.root
        
        # get any files into images directory
        curdir = dirname(__file__)
        for filename in glob(join(curdir, 'images', '*')):
            try:
                # load the image
                picture = Picture(source=filename, rotation=randint(-30,30))
                # add to the main field
                root.add_widget(picture)
            except Exception, e:
                Logger.exception('Pictures: Unable to load <%s>' % filename)

        return root

if __name__ in ('__main__', '__android__'):
    AjScreenApp().run()