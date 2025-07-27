from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.toast.kivytoast.kivytoast import toast
import requests
import webbrowser
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image,AsyncImage,CoreImage
from kivymd.uix.textfield import MDTextField
from kivy.uix.videoplayer import VideoPlayer
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRaisedButton, MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDRoundFlatIconButton, MDRoundFlatButton, MDFloatingActionButton, MDIconButton
from kivy.metrics import dp
import requests
import time
import mimetypes
import random
from android.permissions import request_permissions, Permission
from kivy.animation import Animation
from kivy.utils import platform
from android.storage import primary_external_storage_path
from kivy.core.clipboard import Clipboard
import os
import re
import datetime
import time
import sqlite3
from kivy.clock import Clock
import io
import base64
import webbrowser
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from jnius import JavaException
import threading


kv='''
Manager:
    Fir:
    Sec:
<Fir>:
    name:'home'
    MDBottomNavigation:
        panel_color:(0.027, 0.369, 0.329, 1)
        text_color_active:1,0,0,1       
        pos_hint:{'bottom':1}         
        MDBottomNavigationItem:
            name:'ist'
            icon:'message'
            text:'chat'
            on_tab_press:app.tchange('PUBLIC MSG')   
            FitImage:
                source:'assets/aa1.png'
            MDTextFieldRect:
                id: lf1
                hint_text: 'ENTER MSG HERE'
                helper_text: 'Required'
                required: True
                multiline: True
                size_hint_y: None
                height: dp(60)
                pos_hint: {'center_y': 0.85}    
                fill_color: 0.93, 0.94, 0.94, 1  
              
              
              
                        
            MDFloatingActionButton:
                icon: "send"
                md_bg_color: 0.027, 0.369, 0.329, 1 
                icon_color: 1, 1, 1, 1
                elevation_normal: 20
                pos_hint:{'center_x':0.5,'center_y':0.77}
                on_press:app.send()
                   
            MDCard:
                orientation:'vertical'
                size_hint:None,None
                size:670,900
                pos_hint:{'center_x':0.5,'center_y':0.37}
                md_bg_color:0,0,0,0
                
                ScrollView:
                    id:s1
                    MDBoxLayout:
                        id:b1
                        orientation:'vertical'
                        adaptive_height:True
                        spacing:30
        	            padding:30
           
        MDBottomNavigationItem:
            name:'2nd'
            icon:'image'     
            text:'images'         
            on_tab_press:app.tchange('image')    
            FitImage:
                source:"assets/aa2.png"
            MDCard:           
                id:mdc1
                md_bg_color:0,0,0,0
                pos_hint:{'center_y':0.46}
                size_hint_y:0.9   
                FloatLayout:                                           
                    ScrollView:                                           
                        id:sv1
                        MDBoxLayout:
                            id:bl1
                            orientation:'vertical'    
                            spacing:dp(30)
                            padding:dp(10)   
                            adaptive_height:True
                                    
                    MDIconButton:
                        icon:'plus'            
                        pos_hint:{'center_x':0.9,'center_y':0.02}
                        on_press:app.file() 
                             





    MDTopAppBar:
        id:ta1
        title:'PUBLIC MSG'
        md_bg_color:(0.027, 0.369, 0.329, 1)
        pos_hint:{'top':1}


'''

class Manager(ScreenManager):
	pass




class Fir(Screen):
	pass		

class Sec(Screen):
	pass
	
class Msg(MDApp):
	def build(self):
		self.cu=f'https://myfirstapp-449eb-default-rtdb.firebaseio.com/msg.json'
		self.au='aUzUfyYhwIuPeWuSwwPo1IyhK0rBJt9ickXHxkV8'
		self.tu=f'{self.cu}?auth={self.au}'		
		self.h={}			
		self.li={}
		self.b=Builder.load_string(kv)
		self.ask_p()
		return self.b
	def on_start(self):
		try:		    
		    Clock.schedule_once(lambda x:threading.Thread(target=self.s,daemon=True).start(),2)
		    Clock.schedule_once(lambda x:threading.Thread(target=self.load_img,daemon=True).start(),2)		    		
		except Exception as e:
			toast(str(e))
				
	def s(self):
	    while True:
	        try:
	            data=requests.get(self.tu).json()
	            if data != self.h:	             
	                d={}
	                for k in data:
	                    if self.h.get(k) != data[k]:
	                        d[k]=data.get(k).get('msg')
	                Clock.schedule_once(lambda x:self.add(d)) 
	                self.h=data 
	                time.sleep(1)
	                       
		                                           
	                
	                
	               
	            else:
	                pass
	                
                
                            
	        except Exception as e:
	            Clock.schedule_once(lambda dt,t=e: toast('ERROR HAPPENED'))   				
	        time.sleep(1)        
	        
	def add(self,data):
	    try:
	        #self.b.get_screen('home').ids.b1.clear_widgets()
	        box=self.b.get_screen('home').ids.b1
	        if isinstance(data,dict):
	            for k,v in data.items():
	                c1=MDCard(adaptive_height=True,md_bg_color=(1, 0, 1, 0.5),radius=[0,0,0,0])
	                l1=MDLabel(text=str(v),adaptive_height=True,theme_text_color='Custom',text_color=(0.07, 0.07, 0.07, 1))
	                c1.add_widget(l1)
	                box.add_widget(c1)
	                Clock.schedule_once(lambda dt: self.b.get_screen('home').ids.s1.scroll_to(box.children[0]))
	                
	                
	        
	           
	    except Exception as e:
	        pass

	def send(self):
	    threading.Thread(target=self.sen,daemon=True).start()
	        
	def sen(self):
	    dat=self.b.get_screen('home').ids.lf1.text
	   
	    try:
	        if dat.strip()=='':
	            Clock.schedule_once(lambda x: toast('PLEASE ENTER VALUE FIRST'))
	        else:   
	            t={'msg':dat}
	            requests.post(self.cu,json=t)  
	        
	        
	    except Exception as e:
	        toast('sorry Not Send')	

	def tchange(self,t):
	    self.b.get_screen('home').ids.ta1.title=t
	def file(self):
	    path=primary_external_storage_path()
	    self.filemanager=MDFileManager(exit_manager=self.exit_manager,select_path=self.select_path,preview=True)
	    self.filemanager.show(os.path.join(path))	   
	def exit_manager(self,*a):
	    self.filemanager.close()	        	        
	def select_path(self,p):	   	  	      
	    self.exit_manager() 
	    threading.Thread(target=self.put_img,args=(p,),daemon=True).start()	     
	def put_img(self,p):
	    try:
	        cu=f'https://myfirstapp-449eb-default-rtdb.firebaseio.com/msgimg.json'
	        au=f'aUzUfyYhwIuPeWuSwwPo1IyhK0rBJt9ickXHxkV8'
	        tu=f'{cu}?auth={au}'
	        with open(p,'rb') as f:
	            data=f.read()
	        
	        encode=base64.b64encode(data).decode('utf-8')
	        d={'image':encode}
	        requests.post(cu,json=d)
	        Clock.schedule_once(lambda x:toast('SEND SUCCESFULLY'))
	    except Exception as e:
	        Clock.schedule_once(lambda x:toast('Error Happen'))
	    
	def load_img(self):
	    cu=f'https://myfirstapp-449eb-default-rtdb.firebaseio.com/msgimg.json'
	    au=f'aUzUfyYhwIuPeWuSwwPo1IyhK0rBJt9ickXHxkV8'
	    tu=f'{cu}?auth={au}'	    
	    while True:
	        try:
	            data=requests.get(tu).json()
	            if data !=self.li:
	                d={}
	                for k in data:
	                    if self.li.get(k) != data[k]:
	                        d[k]=data.get(k).get('image')
	                        
	                Clock.schedule_once(lambda x:self.lip(d))
	                self.li=data	               
	                
	            else:
	                pass
	                
	
	        	             	       
	        except Exception as e:
	            Clock.schedule_once(lambda x:toast('Error Happen'))
	            
	def lip(self,p):
	    try:
	        #self.b.get_screen('home').ids.bl1.clear_widgets()
	        if isinstance(p,dict):
	            for k,v in p.items():
	                i=v
	                d=base64.b64decode(i)
	                buf=io.BytesIO(d)
	                c=CoreImage(buf,ext='png').texture
	                img=Image(texture=c,allow_stretch=True,keep_ratio=False,size_hint_y=None,height=dp(500))
	                self.b.get_screen('home').ids.bl1.add_widget(img)
	            		            	             
	    except Exception as e:
	        toast(str(e))	            	             	             	             
	def ask_p(self):
         try:
             if platform == 'android':
                 request_permissions([
                    Permission.READ_EXTERNAL_STORAGE,
                    Permission.WRITE_EXTERNAL_STORAGE,
                    "android.permission.MANAGE_EXTERNAL_STORAGE"
                ])                                	    	    
                                	    	    
         except Exception as e:
             toast(str(e))  
             
                        	    
                
Msg().run()