# Copyright 2016 Peppy Player peppy.player@gmail.com
# 
# This file is part of Peppy Player.
# 
# Peppy Player is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Peppy Player is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Peppy Player. If not, see <http://www.gnu.org/licenses/>.

class Screensaver():
    """ Parent class for all screensaver plug-ins """
    
    def __init__(self):
        """ Initializer. Sets the default update period - 1 second """                    
        self.update_period = 1
        
    def get_update_period(self):
        """ Return screensaver update period """              
        return self.update_period
    
    def set_image(self, image):
        """ Set station image. The method can be used by plug-ins which use station logo images 
        
        :param image: station logo image
        """
        pass
    
    def refresh(self):
        """ Refresh the screensaver. Used for animation """
        pass