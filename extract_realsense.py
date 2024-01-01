import pyrealsense2 as rs
import numpy as np
import os
import cv2

class Extract_Bag:

    def __init__(self, Bag_path,fps=0,extracting_frame_rate=0):
        self.pipeline=rs.pipeline()
        self.config=rs.config()

        self.bag_path=r'' + Bag_path 
        self.fps=fps
        self.extracting_frame_rate=extracting_frame_rate 




        if self.extracting_frame_rate>self.fps:

            print("Error : Extracting FrameRate should be less then or equal to  recording fps")


        if self.fps==0:
            stream = rs.stream.color 
            self.config.disable_all_streams()
            self.config.enable_stream(stream)
            self.config.enable_device_from_file(self.bag_path, repeat_playback=False)
            if not self.config.can_resolve(self.pipeline):
                print("Requested configuration cannot be resolved.")
                exit()

            profile = self.pipeline.start(self.config)
            playback = profile.get_device().as_playback()

            playback.resume()
            fr=0
            try:

                while True:  

                    frames = self.pipeline.wait_for_frames()

                    if frames.size() == 0:
                        break
                    
                    fr += 1



            except RuntimeError as e:
                if "Frame didn't arrive within" in str(e):
                    pass   


            self.pipeline.stop()            
            self.fps=fr


            print(f'{self.fps} frames recorded')
        
        if self.extracting_frame_rate==0:
            self.extracting_frame_rate=self.fps



    def extract_rgb_frames(self,dir='nill'):
        if dir=='nill':
            os.mkdir("color")
            dir="color"


        directory=r'' + dir  


        self.config.enable_device_from_file(self.bag_path,repeat_playback=False)
        self.pipeline.start(self.config)

        device = self.pipeline.get_active_profile().get_device()
        playback = device.as_playback()
        duration = playback.get_duration()
        print(duration.total_seconds())
        max_frames=self.fps*float(duration.total_seconds())
        index=0
        k=0
        playback.pause()

        

        extraced_frame_rate=int(self.fps/self.extracting_frame_rate)
        # print("rate ", extraced_frame_rate )s
        playback.resume()
        try:
            # while playback.current_status() == rs.playback_status.playing:
            while index<self.extracting_frame_rate*(duration.total_seconds()):
                frames = self.pipeline.wait_for_frames()



                # print(index,index%extraced_frame_rate )

                if k%extraced_frame_rate==0:
                    color_file=directory+"/"+"color_"+ str(index)+".jpg"
                    # depth_file="depth/"+ "depth_" +str(index)+".png"

                    frames = self.pipeline.wait_for_frames()

                    color=frames.get_color_frame()
                    rgb=np.asarray(color.get_data())


                    cv2.imwrite(color_file,cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR))

                    index=index+1

                k=k+1

        except RuntimeError as e:
            if "Frame didn't arrive within" in str(e):
                self.pipeline.stop()
                pass  # Ignore the timeout error, as it's expected at the end of playback

                # if playback.current_status==0:

            
                

        

        subdirectory_path = os.path.abspath(directory)
        print(f'{index } rgb frames extracted to {subdirectory_path}')


    def extract_depth_frames(self,dir='nill'):
        if dir=='nill':
            os.mkdir('depth')
            dir="depth"


        directory=r'' + dir 


        self.config.enable_device_from_file(self.bag_path,repeat_playback=False)
        self.pipeline.start(self.config)

        device = self.pipeline.get_active_profile().get_device()
        playback = device.as_playback()
        duration = playback.get_duration()
        max_frames=self.fps*float(duration.total_seconds())
        index=0
        k=0
        playback.pause()

        

        extraced_frame_rate=int(self.fps/self.extracting_frame_rate)
        # print("rate ", extraced_frame_rate )s
        playback.resume()
        try:
            while playback.current_status() == rs.playback_status.playing:
                # color_file=directory+"/"+"color_"+ str(index)+".jpg"
                if k%extraced_frame_rate==0:
                    depth_file=directory+"/"+ "depth_" +str(index)+".png"

                    frames = self.pipeline.wait_for_frames()

                    depth=frames.get_depth_frame()
                    dp=np.asarray(depth.get_data())


                    cv2.imwrite(depth_file,dp)

                    index=index+1
                k=k+1

        
        except RuntimeError as e:
            if "Frame didn't arrive within" in str(e):
                self.pipeline.stop()
                pass  # Ignore the timeout error, as it's expected at the end of playback



        subdirectory_path = os.path.abspath(directory)
        print(f'{index } depth frames extracted to {subdirectory_path}')



    def extract_rgb_and_depth_frames(self,dir_color='nill',dir_depth='nill'):
        if dir_color=='nill':
            os.mkdir('color')
            dir_color="color"


        if dir_depth=='nill':
            os.mkdir('depth')
            dir_depth="depth"


        directory_color=r'' + dir_color 
        directory_depth=r'' + dir_depth 



        self.config.enable_device_from_file(self.bag_path,repeat_playback=False)
        self.pipeline.start(self.config)

        device = self.pipeline.get_active_profile().get_device()
        playback = device.as_playback()
        duration = playback.get_duration()
        max_frames=self.fps*float(duration.total_seconds())
        index=0
        k=0
        playback.pause()

        

        extraced_frame_rate=int(self.fps/self.extracting_frame_rate)
        # print("rate ", extraced_frame_rate )s
        playback.resume()
        try:
            while playback.current_status() == rs.playback_status.playing:
                # color_file=directory+"/"+"color_"+ str(index)+".jpg"
                if k%extraced_frame_rate==0:
                    color_file=directory_color+"/"+ "color_" +str(index)+".jpg"
                    depth_file=directory_depth+"/"+ "depth_" +str(index)+".png"

                    frames = self.pipeline.wait_for_frames()

                    color=frames.get_color_frame()
                    depth=frames.get_depth_frame()
                    rgb=np.asarray(color.get_data())
                    dp=np.asarray(depth.get_data())


                    cv2.imwrite(color_file,cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR))
                    cv2.imwrite(depth_file,dp)

                    index=index+1
                k=k+1

        
        except RuntimeError as e:
            if "Frame didn't arrive within" in str(e):
                self.pipeline.stop()
                pass  # Ignore the timeout error, as it's expected at the end of playback

        
        subdirectory_path = os.path.abspath(directory_color)
        print(f'{index } color frames extracted to {subdirectory_path}')
        subdirectory_path = os.path.abspath(directory_depth)
        print(f'{index } depth frames extracted to {subdirectory_path}')




    


        



        









    
                    

