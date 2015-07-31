
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import (ObjectProperty, ListProperty, StringProperty,
    NumericProperty)
from kivy.uix.modalview import ModalView
from kivy.factory import Factory
from kivy.uix.actionbar import ActionBar
#from kivy.core.image import Image
#from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader,Sound
from kivy.lib.gstplayer import GstPlayer,get_gst_version
from kivy.graphics import Canvas
from kivy.graphics.instructions import Callback,Canvas,CanvasBase
from os.path import realpath
import os




class herufi(ModalView):#class that holds all swahili alphabets
	xhint=NumericProperty(.15)
	yhint = NumericProperty(.15)
	switching_to_mainmenu = ObjectProperty()
	def view_switching_to_mainmenu(self):
		#self.switching_to_mainmenu = MainMenuForm()
		#self.switching_to_mainmenu.open()
		self.clear_widgets()
		self.add_widget(MainMenuForm())
		
class swahilivowels(ModalView):#class that holds the swahili vowels
	switching_to_mainmenu1 = ObjectProperty()
	xhint=NumericProperty(.15)
	yhint = NumericProperty(.15)
	def view_switching_to_mainmenu1(self):
		#self.switching_to_mainmenu = MainMenuForm()
		#self.switching_to_mainmenu.open()
		self.clear_widgets()
		self.add_widget(MainMenuForm())


class MainMenuForm(BoxLayout):#class that holds the button to go straight into the vowels
	pass	
class MainMenuRoot(BoxLayout):#root class that holds all items
	xhint=NumericProperty(.15)
	yhint = NumericProperty(.15)
	vowels={}
	vowels['a']=' A,a \nAngalia,Anga,Agana'
	vowels['e']='E,e \nEnda,Enea,Hepa'
	vowels['i']='I,i \nImba,Igiza,Ingia'
	vowels['o']='O,o \nOngea,Omba,Ongeza'
	vowels['u']='U,u \nUliza,Umba,Ujuzi'
	switching_to_swahilivowels = ObjectProperty()
	switching_to_herufi = ObjectProperty()
	switching_to_maneno = ObjectProperty()
	
	
	
	letters ={}
	letters['a'] = 'A,a \nAngalia,Anga,Agana'
	letters['b']='B,b \nBibi,bima,biu'
	letters['c'] = 'CH,ch \nChanganya,chemka,chafya'
	letters['d']='D,d \nDuma,Digo,'
	letters['e'] = 'E,e \nEnea,Eneza,Eneka'
	letters['f']='F,f \nFagia,Fuma,fua'
	letters['g'] = 'G,g \nGongwa,Gusa'
	letters['h']='H,h \n Harusi'
	letters['i'] = 'I,i \nImba,Igiza,Ingia'
	letters['j']='J,j \nJaribu'
	letters['k'] = 'K,k \nKeki'
	letters['l']='L,l \nLala,Lea,Lima,Loa,'
	letters['m'] = 'M,m \nMama,Mema,Mea'
	letters['n']='N,n \nNunua'
	letters['o'] = 'O,o \nOngea,Omba,Ongeza'
	letters['p']='P,p \nPapa,Pima,Poa'
	letters['r'] = 'R,r \nruka'
	letters['s']='S,s \nSimba'
	letters['t'] = 'T,t \nTaa'
	letters['u']='U,u \nUliza'
	letters['v'] = 'V,v \nVuka'
	letters['w']='W,w \nwewe'
	letters['y'] = 'Y,y \nYako'
	letters['z']='Z,z \nZima'

	
	def view_switching_to_herufi(self):#show herufi form where alphabets are kept
		self.switching_to_herufi = herufi()
		self.switching_to_herufi.open()
		
		
	def view_switching_to_swahilivowels(self):#makes form transits to vokali form
		self.switching_to_swahilivowels = swahilivowels()
		self.switching_to_swahilivowels.open()
		
	
	def view_switching_to_maneno(self):#form changes to maneno form
		self.switching_to_maneno = maneno()
		self.switching_to_maneno.open()
		
	def view_switching_to_video(self):#form changes to maneno form
		self.switching_to_video = maneno()
		self.switching_to_video.open()
	
	
	def popup_vowels(self,vowels):
		popup = Popup(title = self.vowels[vowels],
		
		content = Image(source="img/"+vowels+".png"),
		
		
		
		size_hint =(None,None),
		size=(Window.width-20,Window.height-50),
		auto_dismiss=(True),
		)
		
		#filename = 'video/'+vowels+'.mp4'
		filename = 'sounds/'+vowels+'.ogg'
		#filename = vowels+'.ogg'
		#if not os.path.exists(filename):
			#filename = 'sounds/default.ogg'
		sound = SoundLoader.load(filename)
		sound.play()
		popup.open()
		#print (filename)
		
		
	def popup_letters(self,letters):
		popup = Popup(title = self.letters[letters],
		content = Image(source="imgs/"+letters+".png"),
		
		
		
		size_hint =(None,None),
		size=(Window.width-40,Window.height-70),
		auto_dismiss=(True),
		
		)
		filename = 'sounds/'+ letters +'.ogg'
		#if not os.path.exists(filename):
		#	filename = 'snd/default.ogg'
		sound = SoundLoader.load(filename)
		sound.play()
		popup.open()
		
		
	
	
	words ={}
	words['a'] = 'A,a \nAngalia'
	words['b']='B,b \nBibi'
	words['c'] = 'CH,ch \nChafya'
	words['d']='D,d \nDuma'
	words['e'] = 'E,e \nEneza'
	words['f']='F,f \nFagia'
	words['g'] = 'G,g \nGongwa'
	words['h']='H,h \n Harusi'
	words['i'] = 'I,i \nImba'
	words['j']='J,j \nJaribu'
	words['k'] = 'K,k \nKeki'
	words['l']='L,l \nLala'
	words['m'] = 'M,m \nMama'
	words['n']='N,n \nNunua'
	words['o'] = 'O,o \nOngea'
	words['p']='P,p \nPapa'
	words['r'] = 'R,r \nRuka'
	words['s']='S,s \nSimba'
	words['t'] = 'T,t \nTaa'
	words['u']='U,u \nUliza'
	words['v'] = 'V,v \nVuka'
	words['w']='W,w \nwewe'
	words['y'] = 'Y,y \nYako'
	words['z']='Z,z \nZima'
		
	
	
	
	def popup_words(self,words):
		popup = Popup(title = self.words[words],
		content = Image(source="words/"+words+".png"),
		
		size_hint =(None,None),
		size=(Window.width-20,Window.height-50),
		auto_dismiss=(True),
		)
		filename = 'maneno/'+ words +'.ogg'
		sound = SoundLoader.load(filename)
		sound.play()
		popup.open()
		
		
class maneno(ModalView):#holds sample words of the swahili alphabet
	xhint=NumericProperty(.15)
	yhint = NumericProperty(.15)
	switching_to_mainmenu = ObjectProperty()
	def view_switching_to_mainmenu(self):
		self.clear_widgets()
		self.add_widget(MainMenuForm())
		

	
	
	
class Vokali(App):

	def build(self):
		self.title = 'Basic Educational App'
		use_kivy_settings = True
	# BEGIN PAUSE
	def on_pause(self):
		return True
	# END PAUSE
	

if __name__ == '__main__':
	
	Vokali().run()
